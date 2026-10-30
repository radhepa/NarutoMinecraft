package dev.shinobi.core;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;

/** The save seed and world mode (ROADMAP.md, "World creation: Classic or Varied"), a Fabric attachment on the overworld. */
public record SaveSeed(long seed, String mode) {
    public static final Codec<SaveSeed> CODEC = RecordCodecBuilder.create(i -> i.group(
            Codec.LONG.fieldOf("seed").forGetter(SaveSeed::seed),
            Codec.STRING.fieldOf("mode").forGetter(SaveSeed::mode)
    ).apply(i, SaveSeed::new));

    /** This save's stream for one system ({@code domain}) and one thing in it ({@code key}). */
    public Seeds.Rng stream(String domain, String key) {
        return Seeds.stream(seed, domain, key);
    }
}
