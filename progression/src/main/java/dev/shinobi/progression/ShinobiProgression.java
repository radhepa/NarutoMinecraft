package dev.shinobi.progression;

import com.mojang.brigadier.arguments.StringArgumentType;
import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.mission.Template;
import dev.shinobi.village.ShinobiVillage;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.minecraft.commands.Commands;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerPlayer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

/** Shinobi Progression's entrypoint: quests from data packs, the player's journal and the quest commands. */
public final class ShinobiProgression implements ModInitializer {
    public static final String MOD_ID = "shinobi_progression";
    public static final Logger LOG = LoggerFactory.getLogger("Shinobi Progression");
    /** The player's journal, saved with the player and kept through death. */
    public static final AttachmentType<Journal> JOURNAL = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(MOD_ID, "journal"),
            b -> b.persistent(Journal.CODEC).copyOnDeath().initializer(() -> Journal.EMPTY));
    /** A quest's step graph and its title key. */
    public record Quest(Template template, String title) {}
    /** Quests by id, read from every data pack's {@code quests/} folder when the server starts. */
    public static final Map<String, Quest> QUESTS = new HashMap<>();

    @Override
    public void onInitialize() {
        ServerLifecycleEvents.SERVER_STARTED.register(ShinobiProgression::load);
        ServerLifecycleEvents.END_DATA_PACK_RELOAD.register((server, resources, ok) -> load(server));
        ServerTickEvents.END_SERVER_TICK.register(s -> {
            if (s.getTickCount() % 10 == 0) for (var p : s.getPlayerList().getPlayers()) tick(p);
        });
        // `/shinobi quest accept <id>` takes a quest (a test hook until givers offer them); `/shinobi journal` lists them.
        CommandRegistrationCallback.EVENT.register((dispatcher, registry, env) -> dispatcher.register(
                Commands.literal("shinobi").requires(Commands.hasPermission(Commands.LEVEL_GAMEMASTERS))
                        .then(Commands.literal("quest").then(Commands.literal("accept").then(Commands.argument("id", StringArgumentType.string())
                                .executes(ctx -> {
                                    var player = ctx.getSource().getPlayerOrException();
                                    String id = StringArgumentType.getString(ctx, "id");
                                    if (!QUESTS.containsKey(id)) { ctx.getSource().sendFailure(Component.literal("No quest " + id)); return 0; }
                                    return accept(player, id) ? 1 : 0;
                                }))))
                        .then(Commands.literal("journal").executes(ctx -> {
                            var journal = ctx.getSource().getPlayerOrException().getAttachedOrCreate(JOURNAL);
                            ctx.getSource().sendSuccess(() -> Component.literal("Under way: " + journal.active() + "; done: " + journal.done()), false);
                            return journal.active().size();
                        }))));
    }

    /** Reads every {@code data/<namespace>/quests/*.json}; a broken quest file stops the load, naming the file. */
    static void load(MinecraftServer server) {
        QUESTS.clear();
        server.getResourceManager().listResources("quests", id -> id.getPath().endsWith(".json")).forEach((file, resource) -> {
            try (var in = resource.open()) {
                Map<String, Object> raw = Json.object(new String(in.readAllBytes(), StandardCharsets.UTF_8));
                var t = Quests.check(raw);
                QUESTS.put(t.id(), new Quest(t, Json.str(raw.get("title"), "quest." + t.id() + ".title")));
            } catch (IOException | RuntimeException e) {
                throw new IllegalStateException("Quest file " + file + ": " + e.getMessage(), e);
            }
        });
        LOG.info("Shinobi Progression: {} quests", QUESTS.size());
    }


    /** Takes the quest into the player's journal; false if it is already there or done. */
    public static boolean accept(ServerPlayer player, String id) {
        var quest = QUESTS.get(id);
        var journal = player.getAttachedOrCreate(JOURNAL);
        if (journal.knows(id)) return false;
        player.setAttached(JOURNAL, journal.accept(quest.template()));
        player.sendSystemMessage(Component.translatable("shinobi_progression.quest.accepted", Component.translatable(quest.title())));
        return true;
    }

    /** Finishes the steps whose objective the player now meets. */
    static void tick(ServerPlayer player) {
        var journal = player.getAttachedOrCreate(JOURNAL);
        for (var entry : journal.active().entrySet()) {
            // shortcut: a quest or step since removed from the data stays put in the journal, until P04-6's failure handling.
            var quest = QUESTS.get(entry.getKey());
            var step = quest == null ? null : quest.template().steps().get(entry.getValue());
            if (step == null || !met(player, step.objective())) continue;
            var next = player.getAttachedOrCreate(JOURNAL).advance(quest.template());
            player.setAttached(JOURNAL, next);
            if (next.done().contains(entry.getKey()))
                player.sendSystemMessage(Component.translatable("shinobi_progression.quest.done", Component.translatable(quest.title())));
        }
    }

    /** Whether the player meets an objective now; types other than {@code go} wait for later increments. */
    static boolean met(ServerPlayer player, Map<String, Object> objective) {
        if (!"go".equals(objective.get("type"))) return false;
        var at = player.level().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).get(Json.str(objective.get("place"), ""));
        return at != null && player.blockPosition().closerThan(at, 4);
    }
}
