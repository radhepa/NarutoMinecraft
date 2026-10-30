package dev.shinobi.core;

import com.mojang.serialization.Codec;
import com.mojang.serialization.DataResult;
import com.mojang.serialization.MapCodec;
import com.mojang.serialization.codecs.RecordCodecBuilder;

/**
 * The shared player record (ROADMAP.md, "Code by mod"), a Fabric attachment on the player. Rank, age stage and
 * difficulty are ids, not enums, because those enums live in higher mods; an empty clan is clanless.
 */
public record PlayerRecord(int version, String rank, int level, String ageStage, String clan, String difficulty) {
    public static final int VERSION = 1;
    /** A new beta player: a clanless child at the Academy, on the default difficulty. */
    public static final PlayerRecord NEW = new PlayerRecord(VERSION, "academy", 1, "child", "", "shinobi");

    /**
     * Reads damaged fields as their {@link #NEW} values, with a logged error. A record from a newer pack keeps the fields
     * this pack knows; the ones it does not know are lost at the next save (shortcut: no downgrade support, revisit if a
     * beta ever ships a schema change players might roll back).
     */
    public static final Codec<PlayerRecord> CODEC = Saved.forgiving("player record", codec(false),
            r -> r.version() <= VERSION ? DataResult.success(r)
                    : DataResult.error(() -> "record version " + r.version() + " is newer than this pack's " + VERSION),
            codec(true));

    private static Codec<PlayerRecord> codec(boolean lenient) {
        return RecordCodecBuilder.create(i -> i.group(
                field(Codec.INT, "version", NEW.version, lenient).forGetter(PlayerRecord::version),
                field(Codec.STRING, "rank", NEW.rank, lenient).forGetter(PlayerRecord::rank),
                field(Codec.INT, "level", NEW.level, lenient).forGetter(PlayerRecord::level),
                field(Codec.STRING, "age_stage", NEW.ageStage, lenient).forGetter(PlayerRecord::ageStage),
                field(Codec.STRING, "clan", NEW.clan, lenient).forGetter(PlayerRecord::clan),
                field(Codec.STRING, "difficulty", NEW.difficulty, lenient).forGetter(PlayerRecord::difficulty)
        ).apply(i, PlayerRecord::new));
    }

    /** This record at another rank (a promotion). */
    public PlayerRecord withRank(String rank) { return new PlayerRecord(version, rank, level, ageStage, clan, difficulty); }

    private static <T> MapCodec<T> field(Codec<T> codec, String name, T fallback, boolean lenient) {
        return lenient ? codec.lenientOptionalFieldOf(name, fallback) : codec.fieldOf(name);
    }
}
