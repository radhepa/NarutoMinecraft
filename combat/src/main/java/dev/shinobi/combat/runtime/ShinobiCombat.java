package dev.shinobi.combat.runtime;

import com.mojang.brigadier.arguments.StringArgumentType;
import dev.shinobi.combat.CombatData;
import dev.shinobi.combat.Json;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentSyncPredicate;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.fabricmc.fabric.api.entity.event.v1.ServerLivingEntityEvents;
import net.fabricmc.fabric.api.event.Event;
import net.fabricmc.fabric.api.event.EventFactory;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerEntityEvents;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.fabricmc.fabric.api.event.player.AttackEntityCallback;
import net.fabricmc.fabric.api.event.player.UseEntityCallback;
import net.fabricmc.fabric.api.networking.v1.PayloadTypeRegistry;
import net.fabricmc.fabric.api.networking.v1.ServerPlayConnectionEvents;
import net.fabricmc.fabric.api.networking.v1.ServerPlayNetworking;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.commands.Commands;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.Mob;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.SnowballItem;
import net.minecraft.world.level.block.Blocks;

import java.util.HashMap;
import java.util.Map;
import java.util.function.BiConsumer;
import java.util.function.Function;
import java.util.function.ToDoubleFunction;

/** Shinobi Combat's entrypoint: the combat data from data/combat, the practice spar, the Academy techniques and tools. */
public final class ShinobiCombat implements ModInitializer {
    public static final String MOD_ID = "shinobi_combat";
    public static CombatData data;
    /** Fired on the server thread after a technique is cast, with its id (quests listen for it). */
    @SuppressWarnings("unchecked")
    public static final Event<BiConsumer<ServerPlayer, String>> CAST = EventFactory.createArrayBacked(BiConsumer.class, all -> (player, id) -> {
        for (var l : all) l.accept(player, id);
    });
    /** Chakra, stamina and the techniques learned: saved with the player, kept through death and synced to its owner. */
    public static final AttachmentType<Fighter.State> STATE = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(MOD_ID, "state"),
            b -> b.persistent(Fighter.State.CODEC).copyOnDeath().initializer(() -> Fighter.State.NEW)
                    .syncWith(ByteBufCodecs.fromCodec(Fighter.State.CODEC), AttachmentSyncPredicate.targetOnly()));
    /** The weave or guard pose and the signs woven so far, synced to every client. */
    public static final AttachmentType<Fighter.Stance> STANCE = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(MOD_ID, "stance"),
            b -> b.syncWith(Fighter.Stance.CODEC, AttachmentSyncPredicate.all()));
    /** The practice tools, thrown like snowballs, and the damage each deals on a hit (weapons.json). */
    public static final Map<Item, Double> THROWN = new HashMap<>();
    /** Thrown like the practice tools; bursts where it lands (Tools.smoke). */
    public static Item SMOKE_BOMB;
    /** A multiplier on each player's chakra regen (fatigue, food); the daily-life mod fills it in. */
    public static ToDoubleFunction<ServerPlayer> regen = p -> 1;

    /** Teaches a technique from data/combat; false if it is unknown or already learned. */
    public static boolean teach(ServerPlayer player, String id) { return Fighter.of(player).teach(player, id); }

    public static boolean isTechnique(String id) { return data.techniques.containsKey(id); }

    public static boolean knows(ServerPlayer player, String id) { return player.getAttachedOrCreate(STATE).learned().contains(id); }

    private static Item item(String name, Function<Item.Properties, Item> make) {
        var id = Identifier.fromNamespaceAndPath(MOD_ID, name);
        return Registry.register(BuiltInRegistries.ITEM, id, make.apply(new Item.Properties().setId(ResourceKey.create(Registries.ITEM, id)).stacksTo(16)));
    }

    @Override
    public void onInitialize() {
        data = new CombatData(FabricLoader.getInstance().getModContainer(MOD_ID).orElseThrow().findPath("data/shinobi_combat/combat").orElseThrow());
        for (String name : new String[]{"practice_kunai", "practice_shuriken"})
            THROWN.put(item(name, SnowballItem::new), Json.num(data.weapons.get("item:" + name).thrown(), "damage", 1));
        SMOKE_BOMB = item("smoke_bomb", SnowballItem::new);
        item("ninja_wire", props -> new BlockItem(Blocks.TRIPWIRE, props));   // strung like string: a tripwire that trips mobs (Tools.trip)
        // The workbench's materials, bought at the Academy supply counter.
        // shortcut: smoke bombs and wire are crafted at the vanilla crafting table with no grade roll, until the workbench station exists.
        for (String name : new String[]{"smoke_powder", "washi_paper", "thread", "steel_wire"}) item(name, props -> new Item(props.stacksTo(64)));
        PayloadTypeRegistry.serverboundPlay().register(Fighter.Act.TYPE, Fighter.Act.CODEC);
        ServerPlayNetworking.registerGlobalReceiver(Fighter.Act.TYPE, (payload, context) -> Fighter.act(context.player(), payload));
        // The client fires this too, with no tags synced: it passes there and the attack reaches the server, which takes it over.
        AttackEntityCallback.EVENT.register((player, level, hand, entity, hit) -> {
            if (player instanceof ServerPlayer p) Jutsu.undisguise(p);
            if (!(player instanceof ServerPlayer p) || p.isSpectator() || !(entity instanceof Mob partner) || !entity.entityTags().contains(Spar.PARTNER)) return InteractionResult.PASS;
            Spar.attack(p, partner);
            return InteractionResult.SUCCESS;
        });
        // Crouching with an empty hand on a hurt ally tends them (Field First Aid) instead of the ally's own interaction; the client
        // takes it too, so the off hand is never used as well.
        UseEntityCallback.EVENT.register((player, level, hand, entity, hit) -> {
            if (hand != InteractionHand.MAIN_HAND || player.isSpectator()) return InteractionResult.PASS;
            boolean taken = player instanceof ServerPlayer p ? entity instanceof LivingEntity e && Fighter.aid(p, e) : Fighter.tends(player, entity);
            return taken ? InteractionResult.SUCCESS : InteractionResult.PASS;
        });
        ServerLivingEntityEvents.ALLOW_DAMAGE.register((entity, source, amount) -> Fighter.allow(entity, source));
        ServerLivingEntityEvents.AFTER_DEATH.register((entity, source) -> { if (entity instanceof ServerPlayer p) Fighter.died(p); });
        ServerEntityEvents.ENTITY_LOAD.register((entity, level) -> Jutsu.loaded(entity));
        ServerTickEvents.END_SERVER_TICK.register(Spar::tick);
        ServerTickEvents.END_SERVER_TICK.register(Fighter::tick);
        ServerTickEvents.END_SERVER_TICK.register(Jutsu::tick);
        ServerPlayConnectionEvents.DISCONNECT.register((handler, server) -> {
            Spar.end(handler.getPlayer());
            Jutsu.undisguise(handler.getPlayer());
            Fighter.end(handler.getPlayer());
        });
        ServerLifecycleEvents.SERVER_STOPPED.register(s -> { Fighter.clear(); Jutsu.clear(); });
        // `/shinobi teach <id>` teaches a technique (a test hook until mentors teach them).
        CommandRegistrationCallback.EVENT.register((dispatcher, registry, env) -> dispatcher.register(Commands.literal("shinobi")
                .then(Commands.literal("teach").requires(Commands.hasPermission(Commands.LEVEL_GAMEMASTERS))
                        .then(Commands.argument("id", StringArgumentType.greedyString()).executes(ctx -> {
                            String id = StringArgumentType.getString(ctx, "id");
                            if (!data.techniques.containsKey(id)) { ctx.getSource().sendFailure(Component.literal("No technique " + id)); return 0; }
                            return teach(ctx.getSource().getPlayerOrException(), id) ? 1 : 0;
                        })))));
    }
}
