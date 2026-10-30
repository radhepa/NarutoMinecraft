package dev.shinobi.progression;

import com.mojang.brigadier.arguments.StringArgumentType;
import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.Quests.Quest;
import dev.shinobi.life.ShinobiLife;
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
import net.minecraft.ChatFormatting;
import net.minecraft.network.chat.ClickEvent;
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
import java.util.List;
import java.util.Map;
import java.util.UUID;

/** Shinobi Progression's entrypoint: quests from data packs, the player's journal and the quest commands. */
public final class ShinobiProgression implements ModInitializer {
    public static final String MOD_ID = "shinobi_progression";
    public static final Logger LOG = LoggerFactory.getLogger("Shinobi Progression");
    /** The player's journal, saved with the player and kept through death. */
    public static final AttachmentType<Journal> JOURNAL = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(MOD_ID, "journal"),
            b -> b.persistent(Journal.CODEC).copyOnDeath().initializer(() -> Journal.EMPTY));
    /** Quests by id, read from every data pack's {@code quests/} folder when the server starts. */
    public static final Map<String, Quest> QUESTS = new HashMap<>();
    /**
     * The shops each bound resident keeps, by role or job key.
     * shortcut: the test street's tea house keeper also sells the furniture shop's lines, until the map has a furniture shop.
     */
    static final Map<String, List<String>> SHOPS = Map.of("job:tea_house", List.of("tea_house", "furniture_shop"),
            "role:shop.tea_house.owner", List.of("tea_house"), "role:shop.furniture.keeper", List.of("furniture_shop"));

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
            if (player instanceof ServerPlayer p && hand == InteractionHand.MAIN_HAND) {
                talked(p, entity.getUUID().toString());
                offer(p, entity.getUUID());
            }
            return InteractionResult.PASS;
        });
        // `/shinobi quest accept <id>` takes a quest (a test hook until givers offer them); `/shinobi journal` lists them.
        // `/shinobi buy <shop> <item>` is what a shop's chat line runs, so it needs no permission.
        CommandRegistrationCallback.EVENT.register((dispatcher, registry, env) -> dispatcher.register(
                Commands.literal("shinobi")
                        .then(Commands.literal("buy").then(Commands.argument("shop", StringArgumentType.string()).then(Commands.argument("item", StringArgumentType.string())
                                .executes(ctx -> buy(ctx.getSource().getPlayerOrException(), StringArgumentType.getString(ctx, "shop"), StringArgumentType.getString(ctx, "item")) ? 1 : 0))))
                        .then(Commands.literal("quest").requires(Commands.hasPermission(Commands.LEVEL_GAMEMASTERS)).then(Commands.literal("accept").then(Commands.argument("id", StringArgumentType.string())
                                .executes(ctx -> {
                                    var player = ctx.getSource().getPlayerOrException();
                                    String id = StringArgumentType.getString(ctx, "id");
                                    if (!QUESTS.containsKey(id)) { ctx.getSource().sendFailure(Component.literal("No quest " + id)); return 0; }
                                    return accept(player, id) ? 1 : 0;
                                }))))
                        .then(Commands.literal("journal").requires(Commands.hasPermission(Commands.LEVEL_GAMEMASTERS)).executes(ctx -> {
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
        player.sendSystemMessage(Component.translatable("shinobi_progression.quest.accepted", Component.translatable(quest.title())));
        apply(player, Quests.start(journal, quest, cast));
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
        if (next.journal().done().contains(quest.template().id()))
            player.sendSystemMessage(Component.translatable("shinobi_progression.quest.done", Component.translatable(quest.title())));
        apply(player, next);
    }

    /** Saves the journal and pays the ryo together, in one tick, so a reload never pays a step twice. */
    static void apply(ServerPlayer player, Quests.Outcome o) {
        player.setAttached(JOURNAL, o.journal());
        if (o.ryo() > 0) ShinobiLife.earn(player, o.ryo());
    }

    /** The shops the resident keeps, from the level's bound roles. */
    static List<String> shopsOf(ServerPlayer player, UUID resident) {
        return player.level().getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).entrySet().stream()
                .filter(e -> e.getValue().equals(resident)).flatMap(e -> SHOPS.getOrDefault(e.getKey(), List.of()).stream()).toList();
    }

    /** Lists a shopkeeper's stock in chat, each line a click to buy. shortcut: one chat line per stock line, until P05's shop screen. */
    static void offer(ServerPlayer player, UUID resident) {
        var shops = shopsOf(player, resident);
        if (shops.isEmpty()) return;
        player.sendSystemMessage(Component.translatable("shinobi_progression.shop.header", ShinobiLife.ryo(player)));
        for (String shop : shops)
            for (var line : ShinobiLife.stock(shop)) {
                String cmd = "/shinobi buy " + shop + " " + line.item();
                player.sendSystemMessage(Component.translatable("shinobi_progression.shop.line", ShinobiLife.item(line.item()).getDefaultInstance().getHoverName(), ShinobiLife.price(shop, line.item()))
                        .withStyle(s -> s.withColor(ChatFormatting.GREEN).withClickEvent(new ClickEvent.RunCommand(cmd))));
            }
    }

    /** Buys from a shop whose keeper stands within six blocks; false, saying why, otherwise. */
    static boolean buy(ServerPlayer player, String shop, String item) {
        var level = player.level();
        boolean near = level.getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).entrySet().stream()
                .filter(e -> SHOPS.getOrDefault(e.getKey(), List.of()).contains(shop))
                .map(e -> level.getEntity(e.getValue())).anyMatch(k -> k != null && k.closerThan(player, 6));
        if (!near) {
            player.sendSystemMessage(Component.translatable("shinobi_progression.shop.away"));
            return false;
        }
        return ShinobiLife.buy(player, shop, item);
    }

    /** Whether the player stands within four blocks of the anchor; null (a slot the journal's cast lacks) is nowhere. */
    static boolean near(ServerPlayer player, String anchor) {
        if (anchor == null) return false;
        var at = player.level().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).get(anchor);
        return at != null && player.blockPosition().closerThan(at, 4);
    }
}
