package dev.shinobi.life;

import com.mojang.serialization.Codec;
import dev.shinobi.life.economy.Catalogue;
import dev.shinobi.life.economy.Prices;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.entity.event.v1.ServerPlayerEvents;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.util.Prediction;
import net.minecraft.world.entity.EntitySpawnReason;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.entity.TamableAnimal;
import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.component.Consumables;

import java.util.List;
import java.util.Map;

/** Shinobi Life's entrypoint: the player's wallet, and the shops' stock and prices from the item data. */
public final class ShinobiLife implements ModInitializer {
    public static final String MOD_ID = "shinobi_life";
    /** The player's ryo, kept through death; 100 on the first day (ITEMS.md), then the stipend each morning ({@link Daily}). */
    public static final AttachmentType<Integer> WALLET = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(MOD_ID, "wallet"),
            b -> b.persistent(Codec.INT).copyOnDeath().initializer(() -> 100));
    /** The pets the adoption services hand over, young and tamed (shops.json services). */
    static final Map<String, EntityType<? extends TamableAnimal>> PETS = Map.of("service.adoption.cat", EntityTypes.CAT, "service.adoption.pup", EntityTypes.WOLF);
    public static Catalogue catalogue;
    static Prices prices;

    /**
     * shortcut: green tea is the only dish registered, with no buff; the Leaf dishes' buffs (items.json stats.buff) come
     * with their items, until P05's food items are registered from the item data.
     */
    @Override
    public void onInitialize() {
        var tea = Identifier.fromNamespaceAndPath(MOD_ID, "green_tea");
        Registry.register(BuiltInRegistries.ITEM, tea, new Item(new Item.Properties().setId(ResourceKey.create(Registries.ITEM, tea))
                .food(new FoodProperties.Builder().nutrition(2).saturationModifier(.3F).alwaysEdible().build(), Consumables.DEFAULT_DRINK)));
        catalogue = Catalogue.load(FabricLoader.getInstance().getModContainer(MOD_ID).orElseThrow().findPath("data/shinobi_life/items").orElseThrow());
        prices = new Prices(catalogue);
        ServerTickEvents.END_SERVER_TICK.register(Daily::tick);
        ServerPlayerEvents.AFTER_RESPAWN.register((old, now, alive) -> { if (!alive) Daily.woke(now); });
    }

    public static int ryo(ServerPlayer player) { return player.getAttachedOrCreate(WALLET); }

    public static void earn(ServerPlayer player, int ryo) {
        player.setAttached(WALLET, ryo(player) + ryo);
        player.sendSystemMessage(Component.translatable("shinobi_life.ryo.earned", ryo, ryo(player)));
    }

    /**
     * The Beta 1 lines of a shop this pack can hand over, with no variant.
     * shortcut: unlimited stock with no opening hours, until P05's weekly stock and calendar.
     */
    public static List<Catalogue.Line> stock(String shop) {
        var s = catalogue.shops.get(shop);
        return s == null ? List.of() : s.stock().stream().filter(l -> l.variant().isEmpty() && !"beta2".equals(l.slice()) && item(l.item()) != Items.AIR).toList();
    }

    /**
     * The price of {@code item} at {@code shop} for a newcomer.
     * shortcut: every player is a newcomer at keeper level 0, until P05 hands in the player's title and the keeper's bond.
     */
    public static int price(String shop, String item) { return prices.buy(item, catalogue.shops.get(shop), null, "newcomer", 0); }

    /** The Beta 1 adoption services {@code shop} offers. */
    public static List<Catalogue.Service> services(String shop) {
        return catalogue.services.values().stream().filter(s -> s.provider().equals(shop) && "beta1".equals(s.slice()) && PETS.containsKey(s.id())).toList();
    }

    /**
     * Pays for one {@code item} from {@code shop} and hands it over, or for an adoption service and its pet, which
     * follows the player; false, saying why, if the shop lacks it or the wallet is short.
     */
    public static boolean buy(ServerPlayer player, String shop, String item) {
        var service = services(shop).stream().filter(s -> s.id().equals(item)).findFirst();
        if (service.isPresent()) {
            var pet = PETS.get(item).create(player.level(), EntitySpawnReason.MOB_SUMMONED);
            if (!pay(player, pet.getType().getDescription(), service.get().price())) return false;
            pet.setBaby(true);
            pet.tame(player);
            pet.snapTo(player.getX(), player.getY(), player.getZ(), player.getYRot(), 0);
            player.level().addFreshEntity(pet);
            return true;
        }
        if (stock(shop).stream().noneMatch(l -> l.item().equals(item))) {
            player.sendSystemMessage(Component.translatable("shinobi_life.shop.lacks"));
            return false;
        }
        var stack = new ItemStack(item(item));
        if (!pay(player, stack.getHoverName(), price(shop, item))) return false;
        player.getInventory().placeItemBackInInventory(stack, Prediction.SERVER_ONLY);
        return true;
    }

    private static boolean pay(ServerPlayer player, Component what, int price) {
        int have = ryo(player);
        if (price > have) {
            player.sendSystemMessage(Component.translatable("shinobi_life.ryo.short", what, price, have));
            return false;
        }
        player.setAttached(WALLET, have - price);
        player.sendSystemMessage(Component.translatable("shinobi_life.ryo.paid", what, price, have - price));
        return true;
    }

    /**
     * The registered item for a catalogue id, or air.
     * shortcut: this mod's own id, then the Konoha block of the same name, until the item data's registry field is read.
     */
    public static Item item(String id) {
        for (String ns : new String[]{MOD_ID, "narutominecraft"}) {
            var found = BuiltInRegistries.ITEM.getOptional(Identifier.fromNamespaceAndPath(ns, id));
            if (found.isPresent()) return found.get();
        }
        return Items.AIR;
    }
}
