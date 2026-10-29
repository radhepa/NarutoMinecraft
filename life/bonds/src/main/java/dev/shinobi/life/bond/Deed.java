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
    /** How one person knows: {@code from} is who told them ("news" for village news, "" when they saw or lived it). */
    public record Know(Reaction.Source how, long day, String from) {}

    final int serial;
    final Act act;
    final long day;
    final String about;
    final Map<String, Know> knowers = new TreeMap<>();

    Deed(int serial, Act act, long day, String about) { this.serial = serial; this.act = act; this.day = day; this.about = about == null ? "" : about; }

    public int serial() { return serial; }
    public Act act() { return act; }
    public long day() { return day; }
    public String about() { return about; }
    public boolean knows(String id) { return knowers.containsKey(id); }
    public Know know(String id) { return knowers.get(id); }
    public Map<String, Know> knowers() { return Map.copyOf(knowers); }
    public boolean good() { return act.worth > 0 || act.worth == 0 && act.base.sumOfLosses() == 0; }
    public boolean fresh(long today) { return today - day <= (good() ? GOOD_WINDOW : BAD_WINDOW); }
    /** How much it still weighs on standing: good deeds never fade; bad deeds fade by half every 28 days. */
    public double fade(long today) { return good() ? 1 : Math.pow(.5, Math.max(0, today - day) / (double) BAD_WINDOW); }
}
