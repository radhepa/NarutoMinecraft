package dev.shinobi.combat;

import java.util.HashMap;
import java.util.Map;

/** Cooldowns by id, against a tick clock: a technique, a dodge, a substitution, a pill. */
public final class Cooldowns {
    private final Map<String, Long> readyAt = new HashMap<>();

    public boolean ready(String id, long now) { return readyAt.getOrDefault(id, Long.MIN_VALUE) <= now; }
    public void start(String id, long now, int ticks) { readyAt.put(id, now + ticks); }
    public long remaining(String id, long now) { return Math.max(0, readyAt.getOrDefault(id, Long.MIN_VALUE) - now); }
    /** Uses it if ready; false (and nothing changes) otherwise. */
    public boolean use(String id, long now, int ticks) {
        if (!ready(id, now)) return false;
        start(id, now, ticks);
        return true;
    }
    public void reset(String id) { readyAt.remove(id); }
}
