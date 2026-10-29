package dev.shinobi.combat;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * Weaving hand signs in time. Hold Weave, enter signs (typed or radial), release to cast. Each sign plays for a
 * few ticks (4, or 3 at control 80, less with ninjutsu rank); a sign pressed while the last is still playing is
 * kept if it comes in its final {@link #BUFFER} ticks, otherwise it is dropped. A wrong sequence fizzles and an
 * interrupted weave is lost; the caller charges their share of the cost ({@link #FIZZLE_COST}, {@link #INTERRUPT_COST}).
 */
public final class Weaver {
    public static final int BUFFER = 2;
    public static final double FIZZLE_COST = 0.25, INTERRUPT_COST = 0.5;

    public enum Outcome { CAST, FIZZLE, INTERRUPTED, EMPTY }
    public record Result(Outcome outcome, Optional<String> technique, int ticks, List<HandSign> signs) {}

    private final SignBook book;
    private final int ticksPerSign;
    private final List<HandSign> woven = new ArrayList<>();
    private long busyUntil = Long.MIN_VALUE, started;
    private HandSign buffered;
    private boolean weaving, interrupted;

    public Weaver(SignBook book, int ticksPerSign) { this.book = book; this.ticksPerSign = ticksPerSign; }

    /** Ticks a sign takes for a caster with this control and ninjutsu rank (never below 2). */
    public static int ticksPerSign(int control, int ninjutsuRank) {
        int t = control >= 80 ? 3 : 4;
        if (ninjutsuRank >= 5) t--;
        if (ninjutsuRank >= 10) t--;
        return Math.max(2, t);
    }

    public void begin(long now) { woven.clear(); buffered = null; weaving = true; interrupted = false; started = now; busyUntil = now; }
    public boolean weaving() { return weaving; }

    /** A sign input at tick {@code now}: true if it was taken (played or buffered). */
    public boolean input(HandSign s, long now) {
        if (!weaving) return false;
        flush(now);
        if (now >= busyUntil) { play(s, now); return true; }
        if (busyUntil - now <= BUFFER && buffered == null) { buffered = s; return true; }
        return false;
    }
    private void play(HandSign s, long now) { woven.add(s); busyUntil = Math.max(now, busyUntil) + ticksPerSign; }
    private void flush(long now) { if (buffered != null && now >= busyUntil) { var b = buffered; buffered = null; play(b, busyUntil); } }

    /** The prefix hint for the HUD. */
    public List<String> hint() { return book.candidates(woven); }
    public List<HandSign> woven() { return List.copyOf(woven); }

    public void interrupt() { if (weaving) interrupted = true; }

    /** Release Weave: the technique cast, or why not, and how many ticks the weave took. */
    public Result release(long now) {
        flush(Math.max(now, busyUntil));
        weaving = false;
        int ticks = (int) (Math.max(now, busyUntil) - started);
        var signs = List.copyOf(woven);
        if (interrupted) return new Result(Outcome.INTERRUPTED, Optional.empty(), ticks, signs);
        if (signs.isEmpty()) return new Result(Outcome.EMPTY, Optional.empty(), 0, signs);
        var t = book.match(signs);
        return new Result(t.isPresent() ? Outcome.CAST : Outcome.FIZZLE, t, ticks, signs);
    }
}
