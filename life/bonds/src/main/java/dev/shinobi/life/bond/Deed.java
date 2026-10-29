package dev.shinobi.life.bond;

import java.util.Map;
import java.util.TreeMap;

/**
 * Something the player did that people talk about, after VF's {@code deed/Deed}: the act, the day, who it was about
 * ({@code ""} for the whole village) and who knows, how and from whom. Good deeds are news for
 * {@link #GOOD_WINDOW} days and bad ones for {@link #BAD_WINDOW}; after that word stops spreading, but those who know
 * keep knowing.
 */
public final class Deed {
    public static final int GOOD_WINDOW = 14, BAD_WINDOW = 28;
    /**
     * How one person knows: {@code from} is who told them ("news" for village news, "" when they saw or lived it);
     * {@code slant} (-0.6 to 0.6) is how the retelling bent it, for the player (positive) or against them.
     */
    public record Know(Reaction.Source how, long day, String from, double slant) {
        public Know(Reaction.Source how, long day, String from) { this(how, day, from, 0); }
    }

    final int serial;
    final Act act;
    final long day;
    final String about;
    /** What was said, for a {@link Act#STATED} deed: {@code <axis>=<stance>} (see {@link Questions}). */
    String note = "";
    final Map<String, Know> knowers = new TreeMap<>();
    /** Days in a row nobody new heard it: after {@link Gossip#DIES_DOWN} the news has died down and stops spreading. */
    int quiet;
    /** A bad deed the village let go of (after {@link Act#SAVED_THE_VILLAGE}): remembered, but no longer weighing on standing. */
    boolean forgiven;

    Deed(int serial, Act act, long day, String about) { this.serial = serial; this.act = act; this.day = day; this.about = about == null ? "" : about; }

    public int serial() { return serial; }
    public Act act() { return act; }
    public long day() { return day; }
    public String about() { return about; }
    public String note() { return note; }
    public boolean forgiven() { return forgiven; }
    public boolean knows(String id) { return knowers.containsKey(id); }
    public Know know(String id) { return knowers.get(id); }
    public Map<String, Know> knowers() { return Map.copyOf(knowers); }
    public boolean good() { return act.worth > 0 || act.worth == 0 && act.base.sumOfLosses() == 0; }
    public boolean fresh(long today) { return today - day <= (good() ? GOOD_WINDOW : BAD_WINDOW); }
    /** How much it still weighs on standing: good deeds never fade; bad deeds fade by half every 28 days. */
    public double fade(long today) { return good() ? 1 : forgiven ? 0 : Math.pow(.5, Math.max(0, today - day) / (double) BAD_WINDOW); }
}
