package dev.shinobi.life;

import com.mojang.serialization.Codec;
import dev.shinobi.life.economy.Json;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.minecraft.network.chat.Component;
import net.minecraft.network.protocol.game.ClientboundSetTitleTextPacket;
import net.minecraft.resources.Identifier;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.effect.MobEffects;

import java.util.List;

/**
 * The ordinary day (P05): the calendar, the orphan's stipend each morning and fatigue after a night awake (ROADMAP.md,
 * "The daily cycle"); Shinobi Progression wakes a defeated player at home.
 * shortcut: one fatigue stage, Tired (Slowness I, chakra regen -25%), cleared by any bed; no Exhausted, Collapse or
 * Well Rested, until the difficulty thresholds and the home bed's bonus are wired.
 */
public final class Daily {
    /** The owner's week; day 1 is a Moonday. */
    public static final List<String> WEEK = List.of("Moonday", "Fireday", "Waterday", "Woodday", "Metalday", "Earthday", "Sunday");
    /** 01:00, when a player still awake turns tired (day ticks count from 06:00). */
    static final long TIRED_AT = 19000;
    /** The last day the player was greeted (and paid) on; 0 before their first day. */
    public static final AttachmentType<Integer> SEEN = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "seen"),
            b -> b.persistent(Codec.INT).copyOnDeath().initializer(() -> 0));
    /** Whether the player stayed up through the night; not kept through death, since waking clears it. */
    public static final AttachmentType<Boolean> TIRED = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "tired"),
            b -> b.persistent(Codec.BOOL).initializer(() -> false));
    private Daily() {}

    /** The day number, 1 on the world's first day. */
    public static int day(ServerLevel level) { return (int) (level.getOverworldClockTime() / 24000) + 1; }

    public static String weekday(ServerLevel level) { return WEEK.get((day(level) - 1) % WEEK.size()); }

    public static boolean tired(ServerPlayer player) { return player.getAttachedOrCreate(TIRED); }

    /**
     * Once a second: a new day shows its name and pays the stipend; a player awake at 01:00 turns tired, and sleeping
     * clears it. The welcome purse (the wallet's first 100 ryo) is the player's first day's stipend (ITEMS.md, kit:start;
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
            if (p.isSleeping()) {
                if (tired(p)) rested(p);
            } else if (!tired(p) && p.level().getOverworldClockTime() % 24000 >= TIRED_AT) {
                p.setAttached(TIRED, true);
                p.sendSystemMessage(Component.translatable("shinobi_life.tired"));
            }
            if (tired(p) && !p.hasEffect(MobEffects.SLOWNESS)) p.addEffect(new MobEffectInstance(MobEffects.SLOWNESS, MobEffectInstance.INFINITE_DURATION, 0, true, false, true));
        }
    }

    static void rested(ServerPlayer p) {
        p.setAttached(TIRED, false);
        p.removeEffect(MobEffects.SLOWNESS);
    }
}
