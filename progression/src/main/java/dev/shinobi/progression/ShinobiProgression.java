package dev.shinobi.progression;

import net.minecraft.server.TickTask;
import java.util.stream.Collectors;
import java.util.function.Supplier;
import java.util.function.Predicate;
import java.util.Set;
import net.minecraft.world.item.context.BlockPlaceContext;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.BlockItem;
import net.fabricmc.fabric.api.event.player.UseBlockCallback;
import com.google.common.base.Suppliers;
import dev.shinobi.progression.mission.Template;
import dev.shinobi.village.StreetGuard;
import dev.shinobi.village.TestStreet;
import dev.shinobi.village.PlayerLooks;
import dev.shinobi.combat.runtime.Spar;
import com.mojang.brigadier.arguments.StringArgumentType;
import dev.shinobi.progression.mission.Json;
import dev.shinobi.progression.Quests.Quest;
import dev.shinobi.life.Daily;
import dev.shinobi.life.Dishes;
import dev.shinobi.combat.runtime.Fighter;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import dev.shinobi.life.ShinobiLife;
import dev.shinobi.life.ShopMenu;
import net.minecraft.world.entity.Entity;
import dev.shinobi.combat.runtime.ShinobiCombat;
import net.fabricmc.fabric.api.entity.event.v1.ServerPlayerEvents;
import net.minecraft.world.item.ItemStack;
import net.minecraft.util.Prediction;
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
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.phys.Vec3;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.HashSet;
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
    /** Players the training quest could not be cast for on this map; tried again after a reload. */
    static final Set<UUID> UNCAST = new HashSet<>();
    /** Each blocked step already warned about, as player, quest, step and what is missing; cleared on a reload. */
    static final Set<String> WARNED = new HashSet<>();
    /** The noncanonical training fixture of the M2 play session (ROADMAP.md 13.4). */
    static final String TRAINING = "training.test.first_day";
    /** The furniture shop's blocks, once the registries are complete. */
    static final Supplier<Set<Item>> FURNITURE = Suppliers.memoize(() -> ShinobiLife.stock("furniture_shop").stream()
            .map(l -> ShinobiLife.item(l.item())).collect(Collectors.toSet()));
    /**
     * The shops each bound resident keeps, by role or job key, their own first.
     * shortcut: the test street's tea house keeper also keeps the furniture shop, Ichiraku, the dango stand, the grocer,
     * the fish stall, the Haruno store, the Market Day stalls (each at its own hours) and the clinic's and shelter's
     * adoptions, so every Beta 1 dish on a shelf has a seller, until the map has those shops and their keepers.
     */
    static final Map<String, List<String>> SHOPS = Map.of("job:tea_house", List.of("tea_house", "furniture_shop", "ichiraku", "dango_stand", "grocer",
                    "fishmonger", "haruno_store", "market_day_stalls", "inuzuka_clinic", "cat_shelter"),
            "role:shop.tea_house.owner", List.of("tea_house"), "role:shop.furniture.keeper", List.of("furniture_shop"));

    @Override
    public void onInitialize() {
        ServerLifecycleEvents.SERVER_STARTED.register(ShinobiProgression::load);
        ServerLifecycleEvents.END_DATA_PACK_RELOAD.register((server, resources, ok) -> load(server));
        ServerTickEvents.END_SERVER_TICK.register(s -> {
            if (s.getTickCount() % 10 == 0) for (var p : s.getPlayerList().getPlayers()) tick(p);
        });
        // Read at first use: Fabric does not promise Shinobi Life loads its catalogue before this entrypoint runs.
        StreetGuard.furnishing = item -> FURNITURE.get().contains(item);
        // Fatigue, Well Rested and the last dish set chakra regen (ROADMAP.md, "The daily cycle"); the flat's bed is the player's own.
        ShinobiCombat.regen = Daily::regen;
        Daily.ownBed = TestStreet::inPlayerRoom;
        Daily.home = ShinobiProgression::wakeAtHome;
        Dishes.chakra = Fighter::restore;
        // The flat's furniture, by the pieces' ids, for Well Rested's comfort.
        Daily.furnished = p -> p.level().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).get(TestStreet.PLAYER_FLAT) instanceof BlockPos at
                ? BlockPos.betweenClosedStream(at, at.offset(TestStreet.ROOM_SIZE)).map(pos -> p.level().getBlockState(pos).getBlock().asItem())
                        .filter(FURNITURE.get()::contains).map(item -> BuiltInRegistries.ITEM.getKey(item).getPath()).toList()
                : List.of();
        // The death penalty: the thrown tools carried are lost (ROADMAP.md, Death); the Leaf map keeps the rest of the pack.
        // A defeated player wakes in the flat beside the bed when the map has one and the spot is free, else at the vanilla respawn.
        // shortcut: no level lost, and the flat not the hospital, until P07's levels and a hospital on the map.
        ServerPlayerEvents.AFTER_RESPAWN.register((old, now, alive) -> {
            if (alive) return;
            var inv = now.getInventory();
            for (int i = 0; i < inv.getContainerSize(); i++) if (ShinobiCombat.THROWN.containsKey(inv.getItem(i).getItem())) inv.setItem(i, ItemStack.EMPTY);
            wakeAtHome(now);
        });
        Spar.WON.register(player -> stepDone(player, "spar", step -> true));
        // A lost bout leaves the quest at its spar step, its reward unpaid; the next hit is the retry.
        Spar.LOST.register(player -> player.getAttachedOrCreate(JOURNAL).active().forEach((id, at) -> {
            var quest = QUESTS.get(id);
            if (quest != null && quest.template().steps().get(at) instanceof Template.Step s && "spar".equals(s.type()))
                player.sendSystemMessage(Component.translatable("shinobi_progression.quest.retry", Component.translatable(quest.title())).withStyle(ChatFormatting.YELLOW));
        }));
        // Furnishing: a block from the furniture shop placed in the player's room, checked in a task after the placement.
        UseBlockCallback.EVENT.register((player, level, hand, hit) -> {
            if (player instanceof ServerPlayer p && p.getItemInHand(hand).getItem() instanceof BlockItem item && FURNITURE.get().contains(item)) {
                var at = new BlockPlaceContext(p, hand, p.getItemInHand(hand), hit).getClickedPos();
                if (TestStreet.inPlayerRoom(level, at) && !level.getBlockState(at).is(item.getBlock()))
                    p.level().getServer().schedule(new TickTask(p.level().getServer().getTickCount(), () -> {
                        if (level.getBlockState(at).is(item.getBlock())) stepDone(p, "furnish", step -> true);
                    }));
            }
            return InteractionResult.PASS;
        });
        // Talking: using the resident a talk step names, once per click (the client sends the off hand too after a PASS).
        // In an early phase: VF's own resident listener returns SUCCESS and ends the event, so ours must run first.
        // A keeper with a shop open opens the shop screen instead of VF's talk window; a shut shop's keeper talks as usual.
        // shortcut: no talk window for a keeper while a shop is open, until the shop counter block opens the screen.
        var early = Identifier.fromNamespaceAndPath(MOD_ID, "early");
        UseEntityCallback.EVENT.addPhaseOrdering(early, Event.DEFAULT_PHASE);
        UseEntityCallback.EVENT.register(early, (player, level, hand, entity, hit) -> {
            if (player instanceof ServerPlayer p && hand == InteractionHand.MAIN_HAND) {
                talked(p, entity.getUUID().toString());
                if (offer(p, entity)) return InteractionResult.SUCCESS_SERVER;
            }
            return InteractionResult.PASS;
        });
        // `/shinobi quest accept <id>` takes a quest (a test hook until givers offer them); `/shinobi journal` lists them.
        // `/shinobi buy <shop> <item>` buys as the shop screen does, by the keeper, so it needs no permission.
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
                            var player = ctx.getSource().getPlayerOrException();
                            var journal = player.getAttachedOrCreate(JOURNAL);
                            String under = journal.active().entrySet().stream().map(e -> e.getKey() + " at " + e.getValue()
                                    + (blocked(player, e.getKey()) instanceof String b ? " (blocked: no " + b + ")" : "")).collect(Collectors.joining(", "));
                            ctx.getSource().sendSuccess(() -> Component.literal("Under way: " + under + "; done: " + journal.done()), false);
                            return journal.active().size();
                        }))));
    }

    /** Puts the player beside the flat's bed when the map has one and the spot is free; false otherwise. */
    static boolean wakeAtHome(ServerPlayer player) {
        var bed = player.level().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).get(TestStreet.PLAYER_FLAT);
        if (bed == null) return false;
        var at = Vec3.atBottomCenterOf(bed.offset(1, 1, 1));
        if (!player.level().noCollision(player, player.getBoundingBox().move(at.subtract(player.position())))) return false;
        player.teleportTo(at.x, at.y, at.z);
        player.sendSystemMessage(Component.translatable("shinobi_life.woke"));
        return true;
    }

    /** Reads every {@code data/<namespace>/quests/*.json}; a broken quest file stops the load, naming the file. */
    static void load(MinecraftServer server) {
        QUESTS.clear();
        UNCAST.clear();
        WARNED.clear();
        server.getResourceManager().listResources("quests", id -> id.getPath().endsWith(".json")).forEach((file, resource) -> {
            try (var in = resource.open()) {
                Map<String, Object> raw = Json.object(new String(in.readAllBytes(), StandardCharsets.UTF_8));
                var q = Quests.quest(raw);
                knownItems(raw);
                QUESTS.put(q.template().id(), q);
            } catch (IOException | RuntimeException e) {
                throw new IllegalStateException("Quest file " + file + ": " + e.getMessage(), e);
            }
        });
        LOG.info("Shinobi Progression: {} quests", QUESTS.size());
    }


    /** Refuses a give_item naming no registered item or a teach_technique naming no technique, so a typo stops the load instead of handing over nothing. */
    private static void knownItems(Object o) {
        if (o instanceof Map<?, ?> m) {
            if (m.get("give_item") instanceof String id && ShinobiLife.item(id) == net.minecraft.world.item.Items.AIR)
                throw new IllegalArgumentException("give_item names no item: " + id);
            if (m.get("teach_technique") instanceof String id && !ShinobiCombat.isTechnique(id))
                throw new IllegalArgumentException("teach_technique names no technique: " + id);
            m.values().forEach(ShinobiProgression::knownItems);
        } else if (o instanceof List<?> l) l.forEach(ShinobiProgression::knownItems);
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

    /**
     * Starts the training quest for a player who has made a character, once the map has its training yard; finishes
     * go and sleep steps, and puts the spar partner in place for a spar step the player has reached.
     * shortcut: the noncanonical training fixture starts itself, until P07's opening hands out the first quests.
     */
    static void tick(ServerPlayer player) {
        var journal = player.getAttachedOrCreate(JOURNAL);
        if (player.hasAttached(PlayerLooks.LOOK) && QUESTS.containsKey(TRAINING) && !journal.knows(TRAINING)
                && player.level().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).keySet().containsAll(List.of("anchor:training", TestStreet.PLAYER_FLAT))
                && !UNCAST.contains(player.getUUID())) {
            if (!accept(player, TRAINING)) UNCAST.add(player.getUUID());
            journal = player.getAttachedOrCreate(JOURNAL);
        }
        for (var entry : journal.active().entrySet()) {
            // A cast saved before the quest declared a slot is cast again; while the map cannot cast it, the step stays blocked.
            var q = QUESTS.get(entry.getKey());
            if (q != null && !journal.castOf(entry.getKey()).keySet().containsAll(q.template().slots().keySet())) {
                try {
                    journal = journal.recast(entry.getKey(), Quests.cast(q.template(), player.level().getAttachedOrElse(ShinobiVillage.ROLES, Map.of()),
                            player.level().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of())));
                    player.setAttached(JOURNAL, journal);
                } catch (IllegalArgumentException ignored) {}
            }
            // A step whose quest, step, place or person is gone waits, blocked, with one warning; it goes on once that is back.
            String missing = blocked(player, entry.getKey());
            if (missing != null) {
                if (WARNED.add(player.getUUID() + " " + entry + " " + missing)) {
                    LOG.warn("Quest {} step {} is blocked for {}: no {} on this map or in the data", entry.getKey(), entry.getValue(), player.getName().getString(), missing);
                    player.sendSystemMessage(Component.translatable("shinobi_progression.quest.blocked", Component.translatable(QUESTS.containsKey(entry.getKey()) ? QUESTS.get(entry.getKey()).title() : entry.getKey()), missing)
                            .withStyle(ChatFormatting.RED));
                }
                continue;
            }
            var quest = QUESTS.get(entry.getKey());
            var step = quest.template().steps().get(entry.getValue());
            String place = Quests.resolve(Json.str(step.objective().get("place"), ""), journal.castOf(quest.template().id()));
            if ("go".equals(step.type()) && near(player, place) || "sleep".equals(step.type()) && player.getSleepingPos().filter(bed -> TestStreet.inPlayerRoom(player.level(), bed)).isPresent()) complete(player, quest);
            else if ("spar".equals(step.type()) && near(player, place))
                Spar.partnerAt(player.level(), player.level().getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).get(place));
        }
    }

    /**
     * What the player's current step of the quest needs and lacks: the quest or step in the data, the anchor of a go
     * or spar step, the resident a talk step names, bound in the map's roles; null if nothing (or the quest is not under way).
     * shortcut: a bound resident that has died still counts as present, until roles are rebound when a resident dies (P03).
     */
    static String blocked(ServerPlayer player, String id) {
        var journal = player.getAttachedOrCreate(JOURNAL);
        String at = journal.active().get(id);
        if (at == null) return null;
        var quest = QUESTS.get(id);
        if (quest == null) return "quest " + id;
        var step = quest.template().steps().get(at);
        if (step == null) return "step " + at;
        var level = player.level();
        var cast = journal.castOf(id);
        String field = Quests.field(step.type());
        if (field == null) return null;
        String ref = Json.str(step.objective().get(field), ""), key = Quests.resolve(ref, cast);
        boolean there = key != null && ("who".equals(field)
                ? level.getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).values().stream().anyMatch(u -> u.toString().equals(key))
                : level.getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).containsKey(key));
        if (there) return null;
        var slot = ref.startsWith("slot:") ? quest.template().slots().get(ref.substring(5)) : null;
        return ("who".equals(field) ? "resident " : "anchor ") + (slot == null ? ref : ref + " (" + Quests.key(Json.str(slot.get("pick"), ""), slot) + ")");
    }

    /** Finishes the player's active steps of {@code type} that {@code ok} accepts. */
    static void stepDone(ServerPlayer player, String type, Predicate<Template.Step> ok) {
        var journal = player.getAttachedOrCreate(JOURNAL);
        for (var entry : journal.active().entrySet()) {
            var quest = QUESTS.get(entry.getKey());
            var step = quest == null ? null : quest.template().steps().get(entry.getValue());
            if (step != null && type.equals(step.type()) && ok.test(step)) complete(player, quest);
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

    /** Saves the journal and pays the ryo, items and techniques together, in one tick, so a reload never pays a step twice; names each new step. */
    static void apply(ServerPlayer player, Quests.Outcome o) {
        var before = player.getAttachedOrCreate(JOURNAL).active();
        player.setAttached(JOURNAL, o.journal());
        o.journal().active().forEach((id, step) -> {
            if (!step.equals(before.get(id)))
                player.sendSystemMessage(Component.translatable("shinobi_progression.quest.next", Component.translatable("quest." + id + ".step." + step)).withStyle(ChatFormatting.YELLOW));
        });
        if (o.ryo() > 0) ShinobiLife.earn(player, o.ryo());
        // A full pack drops the item at the player's feet.
        for (String item : o.items()) player.getInventory().placeItemBackInInventory(new ItemStack(ShinobiLife.item(item)), Prediction.SERVER_ONLY);
        for (String technique : o.taught()) ShinobiCombat.teach(player, technique);
    }

    /** The shops the resident keeps, from the level's bound roles. */
    static List<String> shopsOf(ServerPlayer player, UUID resident) {
        return player.level().getAttachedOrElse(ShinobiVillage.ROLES, Map.<String, UUID>of()).entrySet().stream()
                .filter(e -> e.getValue().equals(resident)).flatMap(e -> SHOPS.getOrDefault(e.getKey(), List.of()).stream()).toList();
    }

    /** Opens a shopkeeper's shop screen on their open shops; false (with a polite line if all are shut) for anyone else. */
    static boolean offer(ServerPlayer player, Entity keeper) {
        var shops = shopsOf(player, keeper.getUUID());
        return !shops.isEmpty() && ShopMenu.open(player, keeper, shops);
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
