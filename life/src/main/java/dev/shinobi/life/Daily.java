package dev.shinobi.life;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import dev.shinobi.life.economy.Json;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.entity.event.v1.EntitySleepEvents;
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
import net.minecraft.world.level.Level;

import java.util.List;
import java.util.function.BiPredicate;
import java.util.function.Consumer;

/**
 * The ordinary day (P05): the calendar, the orphan's stipend each morning and fatigue (ROADMAP.md, "The daily cycle").
 * Each night stayed up past 01:00 adds a stage: Tired (movement -10%, chakra regen -25%), then Exhausted (-20%, -50%);
 * a third collapses the player, who wakes at home rested. Any bed clears fatigue; a whole night in your own bed, lain
 * down before midnight, gives Well Rested (chakra regen +10% until noon, the bare flat's tier in docs/HOME.md).
 * shortcut: a stage a night rather than the clock thresholds by difficulty, no Exhausted damage penalty or darkened edge,
 * the collapse keeps the clock (no noon) and Well Rested ignores the home's comfort, until difficulty, a combat damage
 * hook and comfort scoring (life/home Rest) are wired.
 */
public final class Daily {
    /** The owner's week; day 1 is a Moonday. */
    public static final List<String> WEEK = List.of("Moonday", "Fireday", "Waterday", "Woodday", "Metalday", "Earthday", "Sunday");
    /** 01:00, when a player still awake has stayed up another night; midnight and noon (day ticks count from 06:00). */
    static final long TIRED_AT = 19000, MIDNIGHT = 18000, NOON = 6000;
    static final double WELL_RESTED = .10;
    public static final Identifier FATIGUE = Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "fatigue");
    /** The last day the player was greeted (and paid) on; 0 before their first day. */
    public static final AttachmentType<Integer> SEEN = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "seen"),
            b -> b.persistent(Codec.INT).copyOnDeath().initializer(() -> 0));
    /**
     * A player's rest, in clock ticks: nights stayed up (1 Tired, 2 Exhausted), the last day whose night counted, tea's
     * delay tonight, when they lay down (-1: not in bed) and when Well Rested ends.
     */
    public record Rest(int nights, int counted, int tea, long bed, long rested) {
        static final Codec<Rest> CODEC = RecordCodecBuilder.create(i -> i.group(Codec.INT.fieldOf("nights").forGetter(Rest::nights),
                Codec.INT.fieldOf("counted").forGetter(Rest::counted), Codec.INT.fieldOf("tea").forGetter(Rest::tea),
                Codec.LONG.fieldOf("bed").forGetter(Rest::bed), Codec.LONG.fieldOf("rested").forGetter(Rest::rested)).apply(i, Rest::new));
    }
    /** Not kept through death, since waking clears it. */
    public static final AttachmentType<Rest> REST = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "rest"),
            b -> b.persistent(Rest.CODEC).initializer(() -> new Rest(0, 0, 0, -1, 0)));
    /** Whether a bed is the player's own; Shinobi Progression names the flat's. */
    public static BiPredicate<Level, BlockPos> ownBed = (level, bed) -> true;
    /** Wakes a collapsed player at home; Shinobi Progression puts them in the flat. */
    public static Consumer<ServerPlayer> home = p -> {};
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
        return (1 - .25 * rest(p).nights()) * (1 + (wellRested(p) ? WELL_RESTED : 0) + Dishes.regen(p));
    }

    /** Tea: tonight's fatigue comes an hour later. */
    static void tea(ServerPlayer p) {
        var r = rest(p);
        p.setAttached(REST, new Rest(r.nights(), r.counted(), Dishes.HOUR, r.bed(), r.rested()));
    }

    /** Notes when a player lies down, and gives Well Rested for a whole night in their own bed lain down before midnight. */
    static void register() {
        EntitySleepEvents.START_SLEEPING.register((e, bed) -> {
            if (e instanceof ServerPlayer p) {
                var r = rest(p);
                p.setAttached(REST, new Rest(r.nights(), r.counted(), r.tea(), p.level().getOverworldClockTime(), r.rested()));
            }
        });
        EntitySleepEvents.STOP_SLEEPING.register((e, bed) -> {
            if (!(e instanceof ServerPlayer p)) return;
            var r = rest(p);
            long now = p.level().getOverworldClockTime();
            boolean rested = r.bed() >= 0 && now / 24000 > r.bed() / 24000 && r.bed() % 24000 < MIDNIGHT && ownBed.test(p.level(), bed);
            p.setAttached(REST, new Rest(r.nights(), r.counted(), r.tea(), -1, rested ? now / 24000 * 24000 + NOON : r.rested()));
            if (rested) p.sendSystemMessage(Component.translatable("shinobi_life.well_rested"));
        });
    }

    /**
     * Once a second: a new day shows its name and pays the stipend; a player awake at 01:00 has stayed up another night,
     * and sleeping clears it. The welcome purse (the wallet's first 100 ryo) is the player's first day's stipend (ITEMS.md, kit:start;
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
            if (p.isSleeping()) {
                if (r.nights() > 0 || r.tea() > 0) p.setAttached(REST, new Rest(0, r.counted(), 0, r.bed(), r.rested()));
            } else if (day > r.counted() && p.level().getOverworldClockTime() % 24000 >= TIRED_AT + r.tea()) {
                if (r.nights() >= 2) {
                    p.setAttached(REST, new Rest(0, day, 0, -1, r.rested()));
                    p.sendSystemMessage(Component.translatable("shinobi_life.collapse"));
                    home.accept(p);
                } else {
                    p.setAttached(REST, new Rest(r.nights() + 1, day, 0, r.bed(), r.rested()));
                    p.sendSystemMessage(Component.translatable(r.nights() == 0 ? "shinobi_life.tired" : "shinobi_life.exhausted"));
                }
            }
            // An endless Slowness is what Tired gave before the stages; a meal halves the stages' slowdown.
            if (p.getEffect(MobEffects.SLOWNESS) instanceof MobEffectInstance e && e.isInfiniteDuration() && e.isAmbient()) p.removeEffect(MobEffects.SLOWNESS);
            int nights = rest(p).nights();
            var speed = p.getAttribute(Attributes.MOVEMENT_SPEED);
            if (nights == 0) speed.removeModifier(FATIGUE);
            else speed.addOrUpdateTransientModifier(new AttributeModifier(FATIGUE, -.1 * nights * (Dishes.meal(p) ? .5 : 1), AttributeModifier.Operation.ADD_MULTIPLIED_TOTAL));
        }
    }
}
