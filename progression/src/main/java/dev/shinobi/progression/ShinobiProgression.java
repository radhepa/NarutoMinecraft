package dev.shinobi.progression;

import com.mojang.brigadier.arguments.StringArgumentType;
import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.Quests.Quest;
import dev.shinobi.village.ShinobiVillage;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.fabricmc.fabric.api.event.Event;
import net.fabricmc.fabric.api.event.player.UseEntityCallback;
import net.minecraft.commands.Commands;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
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
    /** Quests by id, read from every data pack's {@code quests/} folder when the server starts. */
    public static final Map<String, Quest> QUESTS = new HashMap<>();

    @Override
    public void onInitialize() {
        ServerLifecycleEvents.SERVER_STARTED.register(ShinobiProgression::load);
        ServerLifecycleEvents.END_DATA_PACK_RELOAD.register((server, resources, ok) -> load(server));
        ServerTickEvents.END_SERVER_TICK.register(s -> {
            if (s.getTickCount() % 10 == 0) for (var p : s.getPlayerList().getPlayers()) tick(p);
        });
        // Talking: using the resident a talk step names, once per click (the client sends the off hand too after a PASS).
        // In an early phase: VF's own resident listener returns SUCCESS and ends the event, so ours must run first and PASS.
        var early = Identifier.fromNamespaceAndPath(MOD_ID, "early");
        UseEntityCallback.EVENT.addPhaseOrdering(early, Event.DEFAULT_PHASE);
        UseEntityCallback.EVENT.register(early, (player, level, hand, entity, hit) -> {
            if (player instanceof ServerPlayer p && hand == InteractionHand.MAIN_HAND) talked(p, entity.getUUID().toString());
            return InteractionResult.PASS;
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
                var q = Quests.quest(raw);
                QUESTS.put(q.template().id(), q);
            } catch (IOException | RuntimeException e) {
                throw new IllegalStateException("Quest file " + file + ": " + e.getMessage(), e);
            }
        });
        LOG.info("Shinobi Progression: {} quests", QUESTS.size());
    }


    /** Takes the quest into the player's journal, cast on this map; false if it is already there or done, or the map lacks a slot or place. */
    public static boolean accept(ServerPlayer player, String id) {
        var quest = QUESTS.get(id);
        var journal = player.getAttachedOrCreate(JOURNAL);
        if (journal.knows(id)) return false;
        var level = player.level();
        Map<String, String> cast;
        try {
            cast = Quests.cast(quest.template(), level.getAttachedOrElse(ShinobiVillage.ROLES, Map.of()), level.getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()));
        } catch (IllegalArgumentException e) {
            LOG.warn("Quest {} cannot start: {}", id, e.getMessage());
            player.sendSystemMessage(Component.translatable("shinobi_progression.quest.cannot", Component.translatable(quest.title()), e.getMessage()));
            return false;
        }
        player.setAttached(JOURNAL, Quests.start(journal, quest, cast));
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
            if (step != null && "go".equals(step.type()) && near(player, Quests.resolve(Json.str(step.objective().get("place"), ""), journal.castOf(quest.template().id()))))
                complete(player, quest);
        }
    }

    /** Finishes the talk steps that name the resident {@code who} (its UUID). */
    static void talked(ServerPlayer player, String who) {
        var journal = player.getAttachedOrCreate(JOURNAL);
        for (var entry : journal.active().entrySet()) {
            var quest = QUESTS.get(entry.getKey());
            var step = quest == null ? null : quest.template().steps().get(entry.getValue());
            if (step != null && "talk".equals(step.type()) && who.equals(Quests.resolve(Json.str(step.objective().get("who"), ""), journal.castOf(quest.template().id()))))
                complete(player, quest);
        }
    }

    static void complete(ServerPlayer player, Quest quest) {
        var next = Quests.complete(player.getAttachedOrCreate(JOURNAL), quest);
        player.setAttached(JOURNAL, next);
        if (next.done().contains(quest.template().id()))
            player.sendSystemMessage(Component.translatable("shinobi_progression.quest.done", Component.translatable(quest.title())));
    }

    /** Whether the player stands within four blocks of the anchor; null (a slot the journal's cast lacks) is nowhere. */
    static boolean near(ServerPlayer player, String anchor) {
        if (anchor == null) return false;
        var at = player.level().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).get(anchor);
        return at != null && player.blockPosition().closerThan(at, 4);
    }
}
