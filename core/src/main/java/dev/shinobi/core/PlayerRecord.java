package dev.shinobi.core;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;

/**
 * The shared player record (ROADMAP.md, "Code by mod"), a Fabric attachment on the player. Rank, age stage and
 * difficulty are ids, not enums, because those enums live in higher mods; an empty clan is clanless.
 */
public record PlayerRecord(int version, String rank, int level, String ageStage, String clan, String difficulty) {
    public static final int VERSION = 1;
    /** A new beta player: a clanless child at the Academy, on the default difficulty. */
    public static final PlayerRecord NEW = new PlayerRecord(VERSION, "academy", 1, "child", "", "shinobi");

    public static final Codec<PlayerRecord> CODEC = RecordCodecBuilder.create(i -> i.group(
            Codec.INT.fieldOf("version").forGetter(PlayerRecord::version),
            Codec.STRING.fieldOf("rank").forGetter(PlayerRecord::rank),
            Codec.INT.fieldOf("level").forGetter(PlayerRecord::level),
            Codec.STRING.fieldOf("age_stage").forGetter(PlayerRecord::ageStage),
            Codec.STRING.fieldOf("clan").forGetter(PlayerRecord::clan),
            Codec.STRING.fieldOf("difficulty").forGetter(PlayerRecord::difficulty)
    ).apply(i, PlayerRecord::new));
}
