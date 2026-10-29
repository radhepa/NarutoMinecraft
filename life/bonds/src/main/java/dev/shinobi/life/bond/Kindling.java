package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;
import java.util.Set;

/**
 * Kindling Bond: power that flows outward through the people you are bonded to and grows with the whole web of them.
 * The bond engine owns who can be kindled and how strongly; Shinobi Combat owns what the powers do (it reads
 * {@link Flame} and {@link Bonfire}).
 *
 * <ul>
 * <li><b>Spark</b> (level 6): Thread Sight ({@link #threadSight}: people bonded at level 6 or more, a flicker when one
 * hides something, never what; threads between two of them; strangers stay unreadable) and small kindles. Someone
 * below 6 burns only if they freely offered their flame ({@code offered_flame}).</li>
 * <li><b>Flame</b> (level 8): Kindle (an ally's own technique pushed past its limits) and Ember Link (the squad as
 * one flame).</li>
 * <li><b>Blaze</b> (level 10, or a spouse): Ember Mark (travel to or call a deeply bonded ally) and unison techniques
 * for the pair.</li>
 * <li><b>Bonfire</b>: the ultimate, scaling with the whole web ({@link #bonfire}).</li>
 * </ul>
 *
 * Each bonded person has a <b>flame strength</b> (0 to 1): how deep the bond is within its tier, dimmed by a quarrel
 * (an argument halves it, a cold shoulder quarters it, making up leaves 60%, a quarrel left unmended for a month 20%),
 * snuffed out by a falling-out, and a little brighter after fighting side by side this week. The tier reads the level
 * they act on, so a quarrel can also drop a tier. <b>Resonance</b>: fighting beside someone at Spark or above (a
 * mission, a spar, training, defending the village, a kindle) counts once a day; at {@link #TRIAL_RESONANCE} their
 * trial can teach the player their nature. Story flags decide when the gift awakens ({@link #UNLOCK_FLAG}) and when
 * the Bonfire can be lit ({@link #BONFIRE_FLAG}).
 */
public final class Kindling {
    public static final String UNLOCK_FLAG = "story.kindling.awakened", BONFIRE_FLAG = "story.kindling.bonfire";
    public static final int TRIAL_RESONANCE = 30, UNMENDED_DAYS = 28;

    public enum Power {
        THREAD_SIGHT, SMALL_KINDLE, KINDLE, EMBER_LINK, EMBER_MARK, UNISON;
        public String id() { return name().toLowerCase(Locale.ROOT); }
    }
    public enum Tier {
        NONE(Set.of()), SPARK(Set.of(Power.THREAD_SIGHT, Power.SMALL_KINDLE)),
        FLAME(Set.of(Power.THREAD_SIGHT, Power.SMALL_KINDLE, Power.KINDLE, Power.EMBER_LINK)),
        BLAZE(Set.of(Power.values()));
        public final Set<Power> powers;
        Tier(Set<Power> powers) { this.powers = powers; }
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Tier of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
        /** What one person at this tier adds to the Bonfire, at full strength. */
        public double weight() { return switch (this) { case NONE -> 0; case SPARK -> 1; case FLAME -> 2; case BLAZE -> 4; }; }
    }
    /** One bonded person's flame, as combat reads it. */
    public record Flame(String who, Tier tier, double strength, boolean dimmed, int resonance, boolean natureTrialReady, int kindled) {
        public Set<Power> powers() { return tier.powers; }
    }
    /** The whole web as one fire: its strength, its form, how many burn in it, how many communities it reaches, and whether it can be lit. */
    public record Bonfire(double strength, String form, int bonds, int reach, boolean lit) {}
    public static final List<String> FORMS = List.of("candle", "campfire", "bonfire", "inferno");

    public static boolean unlocked(BondWorld w) { return w.flag(UNLOCK_FLAG); }

    public static Tier tier(boolean unlocked, int effectiveLevel, boolean spouse, Conflict conflict) {
        if (!unlocked || conflict.broken()) return Tier.NONE;
        if (effectiveLevel >= Levels.KINDLE_FULL || spouse && effectiveLevel >= Levels.KINDLE_NATURE) return Tier.BLAZE;
        if (effectiveLevel >= Levels.KINDLE_TECHNIQUE) return Tier.FLAME;
        if (effectiveLevel >= Levels.KINDLE_NATURE) return Tier.SPARK;
        return Tier.NONE;
    }
    /** Their tier: by level, or Spark for someone below it who freely offered their flame ({@code offered_flame}). */
    public static Tier tier(BondWorld w, String who) {
        var b = w.bond(who);
        var t = tier(unlocked(w), w.effectiveLevel(who), who.equals(w.spouse()), b.conflict());
        return t == Tier.NONE && unlocked(w) && !b.conflict().broken() && b.remembers(Act.OFFERED_FLAME) ? Tier.SPARK : t;
    }
    /** Their tier, at least {@code floor}: a scripted gift beat counts its target as that tier for the scene only. */
    public static Tier tier(BondWorld w, String who, Tier floor) {
        var t = tier(w, who);
        return t.compareTo(floor) >= 0 ? t : floor;
    }
    /** How brightly someone's flame burns, 0 to 1 (0 when there is no flame). */
    public static double strength(BondWorld w, String who) { return strength(w, who, Tier.NONE); }
    static double strength(BondWorld w, String who, Tier floor) {
        if (tier(w, who, floor) == Tier.NONE) return 0;
        var b = w.bond(who); var c = b.conflict();
        double s = Math.clamp((Levels.feeling(w.meters(who)) - 45) / 50, .1, 1);
        s *= switch (c.state()) {
            case ARGUMENT -> .5;
            case COLD_SHOULDER -> .25;
            case MAKING_UP -> w.day() - c.until() > UNMENDED_DAYS ? .2 : .6;
            default -> 1;
        };
        if (foughtTogether(b, w.day(), 7)) s += .1;
        return Math.clamp(s, 0, 1);
    }
    static boolean foughtTogether(Bond b, long day, int days) {
        return b.memories.stream().anyMatch(m -> m.source() == Reaction.Source.SELF && day - m.day() <= days && FIGHTING.contains(m.act()));
    }
    static final Set<Act> FIGHTING = Set.of(Act.MISSION_TOGETHER, Act.SPAR_WON, Act.SPAR_LOST, Act.TRAINED_TOGETHER, Act.DEFENDED_VILLAGE, Act.PROTECTED_THEM);

    public static Flame flame(BondWorld w, String who) { return flame(w, who, Tier.NONE); }
    public static Flame flame(BondWorld w, String who, Tier floor) {
        var b = w.bond(who);
        return new Flame(who, tier(w, who, floor), strength(w, who, floor), b.conflict().active(), b.resonance, b.resonance >= TRIAL_RESONANCE, b.kindled);
    }

    /** Someone Thread Sight reads: {@code flicker} when they are hiding something (never what). */
    public record Read(String who, boolean flicker) {}
    /** A thread between two people the player can read: how close they are to each other, and whether they are at odds. */
    public record Thread(String a, String b, int level, boolean strained) {}
    public record Sight(List<Read> people, List<Thread> threads) {}
    /** A bond flag the story sets while someone hides something from the player ({@code hides:<what>}); Thread Sight shows only that it is there. */
    public static final String HIDING = "hides:";
    /**
     * Thread Sight (Spark): only people bonded to the player at level 6 or more can be read, each with a flicker when
     * they hide something; a thread between two others shows only when both are readable. Strangers stay unreadable.
     */
    public static Sight threadSight(BondWorld w) {
        if (!unlocked(w)) return new Sight(List.of(), List.of());
        var people = new ArrayList<Read>();
        for (String who : w.bonded()) {
            var b = w.bond(who);
            if (w.effectiveLevel(who) < Levels.KINDLE_NATURE || b.conflict().broken()) continue;
            people.add(new Read(who, b.flags.stream().anyMatch(f -> f.startsWith(HIDING))));
        }
        people.sort(Comparator.comparing(Read::who));
        var threads = new ArrayList<Thread>();
        for (int i = 0; i < people.size(); i++) for (int j = i + 1; j < people.size(); j++) {
            String a = people.get(i).who(), c = people.get(j).who();
            int level = Math.max(w.effectiveLevel(a, c), w.effectiveLevel(c, a));
            if (level == 0) continue;
            var ab = w.bonds.get(BondWorld.key(a, c)); var ba = w.bonds.get(BondWorld.key(c, a));
            boolean strained = ab != null && (ab.conflict.active() || ab.conflict.broken()) || ba != null && (ba.conflict.active() || ba.conflict.broken());
            threads.add(new Thread(a, c, level, strained));
        }
        return new Sight(List.copyOf(people), List.copyOf(threads));
    }
    /** Everyone whose flame burns, brightest first. */
    public static List<Flame> flames(BondWorld w) {
        var out = new ArrayList<Flame>();
        for (String who : w.bonded()) { var f = flame(w, who); if (f.tier() != Tier.NONE) out.add(f); }
        out.sort(Comparator.comparingDouble(Flame::strength).reversed().thenComparing(Flame::who));
        return out;
    }
    /** The squad members an Ember Link can join: in the squad, at Flame or above. */
    public static List<String> emberLink(BondWorld w) {
        if (w.squad() == null) return List.of();
        return w.squad().members().stream().filter(m -> tier(w, m).compareTo(Tier.FLAME) >= 0).toList();
    }
    /**
     * The Bonfire: every flame weighted by its tier and strength, plus half a point for each community the web reaches
     * (a clan, a district, a rank). Under 5 a candle, under 12 a campfire, under 21 a bonfire, past that an inferno.
     */
    public static Bonfire bonfire(BondWorld w) {
        double sum = 0; var reach = new java.util.TreeSet<String>(); int n = 0;
        for (var f : flames(w)) {
            sum += f.tier().weight() * f.strength(); n++;
            for (String c : w.person(f.who()).communities()) if (!c.equals("village")) reach.add(c);
        }
        double strength = sum + .5 * reach.size();
        String form = strength < 5 ? "candle" : strength < 12 ? "campfire" : strength < 21 ? "bonfire" : "inferno";
        return new Bonfire(strength, form, n, reach.size(), w.flag(BONFIRE_FLAG) && unlocked(w));
    }
    /** Fighting beside someone today (once a day) builds resonance toward their nature, at Spark or above. */
    static void resonate(BondWorld w, Bond b) { resonate(w, b, Tier.NONE); }
    static void resonate(BondWorld w, Bond b, Tier floor) {
        if (!b.to.equals(BondWorld.PLAYER) || b.resonanceDay == w.day || tier(w, b.from, floor).compareTo(Tier.SPARK) < 0) return;
        b.resonance++; b.resonanceDay = w.day;
    }

    private Kindling() {}
}
