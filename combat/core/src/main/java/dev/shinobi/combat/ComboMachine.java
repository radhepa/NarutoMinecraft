package dev.shinobi.combat;

import java.util.ArrayList;
import java.util.List;

/**
 * The server's combo state machine for one fighter. Inputs arrive with their tick; a move started inside the
 * previous move's window chains along the tree (inside a chain vanilla's attack cooldown does not apply), an input up
 * to {@link #BUFFER} ticks early is held and plays when the window opens, and an input outside every window waits
 * for the recovery to end and starts a new string from the root. Gating: style tier, momentum and open gates.
 */
public final class ComboMachine {
    public static final int BUFFER = 2;

    /** The fighter's state when an input arrives: the style tier, momentum, gates open and the path prefix it starts from. */
    public record Context(int tier, double momentum, int gates, String prefix) {
        public static Context ground(int tier, double momentum) { return new Context(tier, momentum, 0, ""); }
    }
    /** A move begun at a tick: it lands on {@code start + startup} and its window (if any) follows its active frames. */
    public record Started(Move move, long start, boolean chained) {
        public long hit() { return start + move.startup(); }
        public long activeEnd() { return start + move.startup() + move.active(); }
        public long end() { return activeEnd() + move.recovery(); }
        public long windowOpen() { return activeEnd() + move.windowOpen(); }
        public long windowClose() { return activeEnd() + move.windowClose(); }
    }

    private final Style style;
    private final List<String> path = new ArrayList<>();
    private Started current;

    public ComboMachine(Style style) { this.style = style; }

    public Started current() { return current; }
    public List<String> path() { return List.copyOf(path); }
    public boolean busy(long now) { return current != null && now < current.end(); }

    /** Breaks the chain (a stagger, a dodge, being hit hard). */
    public void reset() { path.clear(); current = null; }

    /** Press an input at {@code now}. Returns the move started (possibly scheduled a tick or two ahead), or null. */
    public Started press(String input, long now, Context ctx) {
        if (current != null && !current.move().ender()) {
            long open = current.windowOpen(), close = current.windowClose();
            if (now >= open - BUFFER && now <= close) {
                var next = new ArrayList<>(path);
                next.add(input);
                var m = style.find(next, ctx.tier(), ctx.momentum(), ctx.gates());
                if (m != null) {
                    path.add(input);
                    current = new Started(m, Math.max(now, open), true);
                    return current;
                }
            }
        }
        if (busy(now)) return null;
        path.clear();
        if (!ctx.prefix().isEmpty()) path.add(ctx.prefix());
        path.add(input);
        var m = style.find(path, ctx.tier(), ctx.momentum(), ctx.gates());
        if (m == null) { path.clear(); current = null; return null; }
        current = new Started(m, now, false);
        return current;
    }
}
