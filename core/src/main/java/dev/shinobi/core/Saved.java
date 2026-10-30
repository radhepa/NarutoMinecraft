package dev.shinobi.core;

import com.mojang.datafixers.util.Pair;
import com.mojang.serialization.Codec;
import com.mojang.serialization.DataResult;
import com.mojang.serialization.Decoder;
import com.mojang.serialization.DynamicOps;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.function.Function;

/**
 * Reading saved attachments without dropping them. Fabric drops an attachment it cannot decode, and the next save then
 * overwrites it with a fresh one; so a record that fails its strict codec or its {@code check} is read again leniently,
 * keeping every readable field and defaulting the rest, and the problem is logged. Writing always uses the strict codec,
 * so the check never blocks a save.
 */
final class Saved {
    static final Logger LOG = LoggerFactory.getLogger("Shinobi Core");

    static <A> Codec<A> forgiving(String what, Codec<A> strict, Function<A, DataResult<A>> check, Codec<A> lenient) {
        return Codec.of(strict, new Decoder<>() {
            @Override
            public <T> DataResult<Pair<A, T>> decode(DynamicOps<T> ops, T input) {
                DataResult<Pair<A, T>> read = strict.decode(ops, input)
                        .flatMap(p -> check.apply(p.getFirst()).map(a -> Pair.of(a, p.getSecond())));
                if (read.isSuccess()) return read;
                LOG.error("Could not fully read the {} in this save ({}); kept the readable fields and defaulted the rest",
                        what, read.error().orElseThrow().message());
                return lenient.decode(ops, input);
            }
        });
    }

    private Saved() {}
}
