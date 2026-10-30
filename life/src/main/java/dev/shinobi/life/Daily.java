package dev.shinobi.life;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import dev.shinobi.life.economy.Json;
import dev.shinobi.life.home.Catalog;
import dev.shinobi.life.home.Comfort;
import dev.shinobi.life.home.Flat;
import dev.shinobi.life.home.Home;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.entity.event.v1.EntitySleepEvents;
import net.fabricmc.fabric.api.entity.event.v1.ServerPlayerEvents;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.network.protocol.game.ClientboundSetTitleTextPacket;
import net.minecraft.resources.Identifier;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.entity.ai.attributes.AttributeModifier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.clock.WorldClocks;
import net.minecraft.world.level.Level;

import java.util.List;
import java.util.function.BiPredicate;
import java.util.function.Function;
import java.util.function.Predicate;

/**
 * The ordinary day (P05): the calendar, the orphan's stipend each morning and fatigue (ROADMAP.md, "The daily cycle").
 * A player still awake at 01:00 is Tired (movement -10%, chakra regen -25%), at 03:00 Exhausted (-20%, -50%, damage
 * -20%, a darkened screen), and at 06:00 collapses, to wake at home at noon. A whole night in any bed clears fatigue; one
 * in your own bed gives Well Rested by the home's comfort (life/home Rest: +10% until noon in a bare flat).
 * shortcut: the Story thresholds only, a Darkness pulse for the darkened edge, no short chakra jumps, until difficulty,
 * a client vignette and chakra jumps exist.
 */
public final class Daily {
    /** The owner's week; day 1 is a Moonday. */
    public static final List<String> WEEK = List.of("Moonday", "Fireday", "Waterday", "Woodday", "Metalday", "Earthday", "Sunday");
    /** Tired at 01:00, Exhausted at 03:00, the evening's 18:00, midnight and noon (day ticks count from 06:00). */
    static final long TIRED_AT = 19000, EXHAUSTED_AT = 21000, EVENING = 12000, MIDNIGHT = 18000, NOON = 6000;
    public static final Identifier FATIGUE = Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "fatigue");
    /** The last day the player was greeted (and paid) on; 0 before their first day. */
    public static final AttachmentType<Integer> SEEN = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "seen"),
            b -> b.persistent(Codec.INT).copyOnDeath().initializer(() -> 0));
    /**
     * A player's rest, in clock ticks: the stage (1 Tired, 2 Exhausted), the day it was reached on (with stage 0, a
     * night already spent), tea's delay tonight, when they lay down (-1: not in bed), when Well Rested ends and its bonus.
     */
    public record Rest(int nights, int counted, int tea, long bed, long rested, double well) {
        static final Codec<Rest> CODEC = RecordCodecBuilder.create(i -> i.group(Codec.INT.fieldOf("nights").forGetter(Rest::nights),
                Codec.INT.fieldOf("counted").forGetter(Rest::counted), Codec.INT.fieldOf("tea").forGetter(Rest::tea),
                Codec.LONG.fieldOf("bed").forGetter(Rest::bed), Codec.LONG.fieldOf("rested").forGetter(Rest::rested),
                Codec.DOUBLE.optionalFieldOf("well", .10).forGetter(Rest::well)).apply(i, Rest::new));
    }
    /** Through death it comes back cleared (ROADMAP.md, Death), by {@link #register()}. */
    public static final AttachmentType<Rest> REST = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "rest"),
            b -> b.persistent(Rest.CODEC).initializer(() -> new Rest(0, 0, 0, -1, 0, 0)));
    /** Whether a bed is the player's own; Shinobi Progression names the flat's. */
    public static BiPredicate<Level, BlockPos> ownBed = (level, bed) -> true;
    /** Wakes a collapsed player at home, false when it cannot; Shinobi Progression puts them in the flat. */
    public static Predicate<ServerPlayer> home = p -> false;
    /** The home's furniture by piece id; Shinobi Progression reads the flat's placed blocks. */
    public static Function<ServerPlayer, List<String>> furnished = p -> List.of();
    private Daily() {}

    /** The day number, 1 on the world's first day. */
    public static int day(ServerLevel level) { return (int) (level.getOverworldClockTime() / 24000) + 1; }

    public static String weekday(ServerLevel level) { return WEEK.get((day(level) - 1) % WEEK.size()); }

    public static Rest rest(ServerPlayer player) { return player.getAttachedOrCreate(REST); }

    public static boolean tired(ServerPlayer player) { return rest(player).nights() > 0; }

    public static boolean exhausted(ServerPlayer player) { return rest(player).nights() > 1; }

    public static boolean wellRested(ServerPlayer player) { return player.level().getOverworldClockTime() < rest(player).rested(); }

    /** Chakra regen: fatigue's slowdown on Well Rested's and the last dish's bonuses. */
    public static double regen(ServerPlayer p) {
        var r = rest(p);
        return (1 - .25 * r.nights()) * (1 + (wellRested(p) ? r.well() : 0) + Dishes.regen(p));
    }

    /** Tea: tonight's fatigue comes an hour later. */
    static void tea(ServerPlayer p) {
        var r = rest(p);
        p.setAttached(REST, new Rest(r.nights(), r.counted(), Dishes.HOUR, r.bed(), r.rested(), r.well()));
    }

    /** The home's comfort from its furniture. shortcut: no season, mess, plant or pet, until the home keeps them at runtime. */
    static Comfort.Score comfort(ServerPlayer p) {
        var home = new Home(p.getStringUUID(), Flat.CLASSIC);
        for (String id : furnished.apply(p)) if (Catalog.PIECES.containsKey(id)) home.place(id);
        return Comfort.of(home, day(p.level()), 0, "");
    }

    /**
     * Notes when a player lies down; a whole night slept clears fatigue, and in their own bed from the evening gives
     * Well Rested by the home's comfort. A defeated player wakes with fatigue cleared, and a defeat after midnight spends the night.
     */
    static void register() {
        EntitySleepEvents.START_SLEEPING.register((e, bed) -> {
            if (e instanceof ServerPlayer p) {
                var r = rest(p);
                p.setAttached(REST, new Rest(r.nights(), r.counted(), r.tea(), p.level().getOverworldClockTime(), r.rested(), r.well()));
            }
        });
        EntitySleepEvents.STOP_SLEEPING.register((e, bed) -> {
            if (!(e instanceof ServerPlayer p)) return;
            var r = rest(p);
            long now = p.level().getOverworldClockTime(), at = r.bed() % 24000;
            if (r.bed() < 0 || now / 24000 <= r.bed() / 24000) {
                p.setAttached(REST, new Rest(r.nights(), r.counted(), r.tea(), -1, r.rested(), r.well()));
                return;
            }
            // Lain down from 18:00 (a daytime storm nap gives nothing); the hour is 18 to 23, or 0 to 5 after midnight.
            var well = at >= EVENING ? dev.shinobi.life.home.Rest.sleep(comfort(p), (int) (at / 1000 + 6) % 24, ownBed.test(p.level(), bed))
                    : dev.shinobi.life.home.Rest.Rested.NONE;
            long morning = now / 24000 * 24000;
            p.setAttached(REST, well.any() ? new Rest(0, r.counted(), well.fatigueDelay() * Dishes.HOUR, -1, morning + (well.until() - 6) * 1000L, well.regen())
                    : new Rest(0, r.counted(), 0, -1, r.rested(), r.well()));
            if (well.any()) p.sendSystemMessage(Component.translatable("shinobi_life.well_rested", Math.round(well.regen() * 100), well.until()));
        });
        // Not copyOnDeath: Fabric copies those after the other respawn listeners, over this.
        ServerPlayerEvents.COPY_FROM.register((old, p, alive) -> {
            if (alive) return;
            var r = rest(old);
            p.setAttached(REST, new Rest(0, p.level().getOverworldClockTime() % 24000 >= MIDNIGHT ? day(p.level()) : 0, 0, -1, r.rested(), r.well()));
        });
    }

    /**
     * Once a second: a new day shows its name and pays the stipend, and a player awake late reaches fatigue's stages by
     * the clock (tea puts them off an hour). The welcome purse (the wallet's first 100 ryo) is the player's first day's stipend (ITEMS.md, kit:start;
     * economy.json, stipend.from_day), so a player's first day pays nothing more and each later day pays 30: one envelope
     * for each day since the last one seen, so a clock jumped forward pays every skipped morning and one moved back none.
     */
    static void tick(MinecraftServer server) {
        if (server.getTickCount() % 20 != 0) return;
        var stipend = ShinobiLife.catalogue.tuning("stipend");
        for (var p : server.getPlayerList().getPlayers()) {
            int day = day(p.level()), seen = p.getAttachedOrCreate(SEEN);
            if (day > seen) {
                p.setAttached(SEEN, day);
                p.connection.send(new ClientboundSetTitleTextPacket(Component.translatable("shinobi_life.day", day, weekday(p.level()))));
                int from = Json.integer(stipend.get("from_day"), 2);
                if (seen > 0 && day >= from) {
                    int ryo = Json.integer(stipend.get("amount"), 30) * (day - Math.max(seen, from - 1));
                    p.setAttached(ShinobiLife.WALLET, ShinobiLife.ryo(p) + ryo);
                    p.sendSystemMessage(Component.translatable("shinobi_life.stipend", ryo, ShinobiLife.ryo(p)));
                }
            }
            var r = rest(p);
            long t = p.level().getOverworldClockTime() % 24000 - r.tea();
            int stage = t >= EXHAUSTED_AT ? 2 : t >= TIRED_AT ? 1 : 0;
            if (p.isSleeping()) {
                // Asleep, the stages wait; waking after the night clears them.
            } else if (r.nights() == 2 && day != r.counted() && t >= 0) {
                // 06:00 still awake: the player passes out and wakes at noon, at home or where they fell.
                p.setAttached(REST, new Rest(0, 0, 0, -1, r.rested(), r.well()));
                p.sendSystemMessage(Component.translatable("shinobi_life.collapse"));
                server.clockManager().setTotalTicks(server.registryAccess().get(WorldClocks.OVERWORLD).orElseThrow(), (day - 1) * 24000L + NOON);
                if (!home.test(p)) p.sendSystemMessage(Component.translatable("shinobi_life.woke"));
            } else if (stage > r.nights() && (r.nights() > 0 || day != r.counted())) {
                p.setAttached(REST, new Rest(stage, day, 0, r.bed(), r.rested(), r.well()));
                p.sendSystemMessage(Component.translatable(stage == 1 ? "shinobi_life.tired" : "shinobi_life.exhausted"));
            }
            // An endless Slowness is what Tired gave before the stages; a meal halves the stages' slowdown.
            if (p.getEffect(MobEffects.SLOWNESS) instanceof MobEffectInstance e && e.isInfiniteDuration() && e.isAmbient()) p.removeEffect(MobEffects.SLOWNESS);
            int nights = rest(p).nights();
            var speed = p.getAttribute(Attributes.MOVEMENT_SPEED);
            var damage = p.getAttribute(Attributes.ATTACK_DAMAGE);
            if (nights == 0) speed.removeModifier(FATIGUE);
            else speed.addOrUpdateTransientModifier(new AttributeModifier(FATIGUE, -.1 * nights * (Dishes.meal(p) ? .5 : 1), AttributeModifier.Operation.ADD_MULTIPLIED_TOTAL));
            if (nights < 2) damage.removeModifier(FATIGUE);
            else damage.addOrUpdateTransientModifier(new AttributeModifier(FATIGUE, -.2, AttributeModifier.Operation.ADD_MULTIPLIED_TOTAL));
            if (nights == 2 && server.getTickCount() % 600 == 0) p.addEffect(new MobEffectInstance(MobEffects.DARKNESS, 60, 0, true, false, false));
        }
    }
}
