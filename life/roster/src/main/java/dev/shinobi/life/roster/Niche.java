package dev.shinobi.life.roster;

/** What a shinobi is best at. In their niche a teammate fights as if {@link Roster#nicheEdge} levels higher. */
public enum Niche {
    NINJUTSU, TAIJUTSU, GENJUTSU, KENJUTSU, TRACKING, SENSING, MEDICAL, SEALING, TOOLS, SUPPORT;

    public String id() { return name().toLowerCase(java.util.Locale.ROOT); }
}
