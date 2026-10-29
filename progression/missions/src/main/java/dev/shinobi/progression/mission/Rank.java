package dev.shinobi.progression.mission;

import java.util.Locale;

/** Mission ranks, D to S (ROADMAP.md, "Board missions"; MISSIONS.md section 3). Not to be confused with {@link Grade}. */
public enum Rank {
    D, C, B, A, S;

    public String id() { return name().toLowerCase(Locale.ROOT); }
    public static Rank of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
}
