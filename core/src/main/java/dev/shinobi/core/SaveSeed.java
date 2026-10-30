package dev.shinobi.core;

import com.mojang.serialization.Codec;
import com.mojang.serialization.DataResult;
import com.mojang.serialization.codecs.RecordCodecBuilder;

import java.util.Set;

/** The save seed and world mode (ROADMAP.md, "World creation: Classic or Varied"), a Fabric attachment on the overworld. */
public record SaveSeed(long seed, String mode) {
    public static final Set<String> MODES = Set.of("classic", "varied");

    /**
     * A damaged or unknown mode reads as Classic, with a logged error. The seed has no safe default here: an unreadable
     * one drops the attachment, and the server start sets it from the world seed again in Classic, as for a new save.
     */
    public static final Codec<SaveSeed> CODEC = Saved.forgiving("save seed", codec(false),
            s -> MODES.contains(s.mode()) ? DataResult.success(s) : DataResult.error(() -> "unknown mode " + s.mode()),
            codec(true));

    private static Codec<SaveSeed> codec(boolean lenient) {
        return RecordCodecBuilder.create(i -> i.group(
                Codec.LONG.fieldOf("seed").forGetter(SaveSeed::seed),
                (lenient ? Codec.STRING.lenientOptionalFieldOf("mode", "classic") : Codec.STRING.fieldOf("mode")).forGetter(SaveSeed::mode)
        ).apply(i, (seed, mode) -> new SaveSeed(seed, lenient && !MODES.contains(mode) ? "classic" : mode)));
    }

    /** This save's stream for one system ({@code domain}) and one thing in it ({@code key}). */
    public Seeds.Rng stream(String domain, String key) {
        return Seeds.stream(seed, domain, key);
    }
}
