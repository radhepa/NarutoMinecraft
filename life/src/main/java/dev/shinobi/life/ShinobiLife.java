package dev.shinobi.life;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import dev.shinobi.core.SaveSeed;
import dev.shinobi.core.ShinobiCore;
import dev.shinobi.life.economy.Catalogue;
import dev.shinobi.life.economy.Prices;
import dev.shinobi.life.economy.Stock;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.EntitySpawnReason;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.entity.TamableAnimal;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/** Shinobi Life's entrypoint: the player's wallet, and the shops' stock, hours and prices from the item data. */
public final class ShinobiLife implements ModInitializer {
    public static final String MOD_ID = "shinobi_life";
    /** The player's ryo, kept through death; 100 on the first day (ITEMS.md), then the stipend each morning ({@link Daily}). */
    public static final AttachmentType<Integer> WALLET = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(MOD_ID, "wallet"),
            b -> b.persistent(Codec.INT).copyOnDeath().initializer(() -> 100));
    /** The pets the adoption services hand over, young and tamed (shops.json services). */
    static final Map<String, EntityType<? extends TamableAnimal>> PETS = Map.of("service.adoption.cat", EntityTypes.CAT, "service.adoption.pup", EntityTypes.WOLF);
    /** What a shop has sold of one line since its last restock: the VF day of the last sale and how many. */
    public record Sold(long day, int count) {
        static final Codec<Sold> CODEC = RecordCodecBuilder.create(i -> i.group(Codec.LONG.fieldOf("day").forGetter(Sold::day),
                Codec.INT.fieldOf("count").forGetter(Sold::count)).apply(i, Sold::new));
    }
    /** The shops' sales by {@code shop|item}, on the overworld: one shelf for the whole world. */
    public static final AttachmentType<Map<String, Sold>> SOLD = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(MOD_ID, "sold"),
            b -> b.persistent(Codec.unboundedMap(Codec.STRING, Sold.CODEC)).initializer(Map::of));
    public static Catalogue catalogue;
    static Prices prices;

    @Override
    public void onInitialize() {
        catalogue = Catalogue.load(FabricLoader.getInstance().getModContainer(MOD_ID).orElseThrow().findPath("data/shinobi_life/items").orElseThrow());
        prices = new Prices(catalogue);
        Dishes.register(catalogue);
        ServerTickEvents.END_SERVER_TICK.register(Daily::tick);
        Daily.register();
    }

    public static int ryo(ServerPlayer player) { return player.getAttachedOrCreate(WALLET); }

    public static void earn(ServerPlayer player, int ryo) {
        player.setAttached(WALLET, ryo(player) + ryo);
        player.sendSystemMessage(Component.translatable("shinobi_life.ryo.earned", ryo, ryo(player)));
    }

    /** Every Beta 1 line of a shop this pack can hand over, with no variant, on the shelf this week or not. */
    public static List<Catalogue.Line> stock(String shop) {
        var s = catalogue.shops.get(shop);
        return s == null ? List.of() : s.stock().stream().filter(l -> l.variant().isEmpty() && !"beta2".equals(l.slice()) && item(l.item()) != Items.AIR).toList();
    }

    /** The lines on a shop's shelf this week for the player's rank (life/economy Stock), that this pack can hand over. */
    public static List<Catalogue.Line> shelf(ServerPlayer player, String shop) {
        var s = catalogue.shops.get(shop);
        if (s == null) return List.of();
        var save = SaveSeed.of(player.level().getServer());
        return Stock.shelf(s, vfDay(player.level()) / 7, "varied".equals(save.mode()) ? Stock.Mode.VARIED : Stock.Mode.CLASSIC, save.seed(),
                player.getAttachedOrCreate(ShinobiCore.PLAYER).rank(), "beta1").stream().filter(l -> l.variant().isEmpty() && item(l.item()) != Items.AIR).toList();
    }

    /** VF's day number (0 on the world's first day), which the shelf's weeks and restocks count in. */
    static long vfDay(ServerLevel level) { return Daily.day(level) - 1; }

    /** How many of a shelf line the shop has left today (Integer.MAX_VALUE: unlimited). */
    public static int left(ServerLevel level, String shop, Catalogue.Line line) {
        var sold = level.getServer().overworld().getAttachedOrElse(SOLD, Map.of()).get(shop + "|" + line.item());
        return Stock.left(line, vfDay(level), sold == null ? 0 : sold.day(), sold == null ? 0 : sold.count());
    }

    /** Whether a shop of the catalogue is open now. */
    public static boolean open(ServerLevel level, String shop) { return catalogue.shops.containsKey(shop) && shut(level, shop) == null; }

    /**
     * The polite line of a catalogue shop shut now, or null while it is open: its closed day first (Market Day only,
     * a weekday, or Market Day), then its hours.
     * shortcut: event closings (festival, exams) never close a shop, until the calendar has events.
     */
    public static Component shut(ServerLevel level, String shop) {
        var s = catalogue.shops.get(shop);
        boolean market = Daily.marketDay(level);
        if (s.closed().equals("not_market_day") && !market) return Component.translatable("shinobi_life.shop.market_only", s.name());
        if (s.closed().equals(Daily.weekday(level)) || s.closed().equals("Market Day") && market)
            return Component.translatable("shinobi_life.shop.closed_day", s.name(), s.closed());
        long t = level.getOverworldClockTime() % 24000;
        int now = (int) ((t / 1000 + 6) % 24 * 60 + t % 1000 * 60 / 1000);
        return minutes(s.opens()) <= now && now < minutes(s.closes()) ? null : Component.translatable("shinobi_life.shop.closed", s.name(), s.opens(), s.closes());
    }
    private static int minutes(String hhmm) { return Integer.parseInt(hhmm.substring(0, 2)) * 60 + Integer.parseInt(hhmm.substring(3)); }

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
     * follows the player; false, saying why, if the shop is shut, lacks it this week or has sold out, the pack is full
     * or the wallet is short.
     */
    public static boolean buy(ServerPlayer player, String shop, String item) {
        var level = player.level();
        if (catalogue.shops.containsKey(shop) && !open(level, shop)) {
            player.sendSystemMessage(shut(level, shop));
            return false;
        }
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
        var line = shelf(player, shop).stream().filter(l -> l.item().equals(item)).findFirst().orElse(null);
        if (line == null) {
            player.sendSystemMessage(Component.translatable("shinobi_life.shop.lacks"));
            return false;
        }
        var stack = new ItemStack(item(item));
        int left = left(level, shop, line);
        if (left <= 0) {
            player.sendSystemMessage(Component.translatable("shinobi_life.shop.sold_out", stack.getHoverName()));
            return false;
        }
        var inv = player.getInventory();
        if (inv.getSlotWithRemainingSpace(stack) < 0 && inv.getFreeSlot() < 0) {
            player.sendSystemMessage(Component.translatable("shinobi_life.shop.full"));
            return false;
        }
        if (!pay(player, stack.getHoverName(), price(shop, item))) return false;
        if (line.qty() > 0) {
            var sold = new HashMap<>(level.getServer().overworld().getAttachedOrElse(SOLD, Map.of()));
            sold.put(shop + "|" + item, new Sold(vfDay(level), line.qty() - left + 1));
            level.getServer().overworld().setAttached(SOLD, Map.copyOf(sold));
        }
        inv.add(stack);
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
