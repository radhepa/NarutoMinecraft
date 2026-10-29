package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 * How one person feels about another: {@code from} toward {@code to}. The player's bonds are residents' feelings
 * toward the player ({@code to} is {@link BondWorld#PLAYER}); squadmates also have bonds with each other.
 *
 * <p>Only history is stored, as in VF's {@code Society}: contact days, warmth from talks and gifts, days spent side by
 * side, memories, shared experiences and moments, the quarrel and the courtship. The meters are computed from them
 * ({@link BondWorld#meters}):
 *
 * <pre>
 * affection = (5 + 15 chemistry) x (1 - e^(-contact days / 20))    familiarity
 *           + warmth                                                talks, gifts, favors (diminishing, at most 15)
 *           + 0.15 x days together (at most 60)                     side by side
 *           + memories (fading) + the quarrel's weight
 * trust     = 10 + 10 warmth trait + 5 openness + 0.2 x contact days (at most 15) + memories + quarrel
 * respect   = 10 + 6 x your seniority - 4 x how far they outrank you (0..60) + memories
 * rivalry   = for peers: 15 x pride + 5 x boldness (when positive) + memories
 * romance   = Courtship.meter (teen and up only)
 * </pre>
 *
 * Family start where VF's families do: affection and trust at least 55.
 */
public final class Bond {
    public static final double WARMTH_CAP = 15, WARMTH_FLOOR = -15, TOGETHER_RATE = .15;
    public static final int TOGETHER_CAP = 60, MEMORY_CAP = 64, NEGLECT_DAYS = 7;
    public static final double NEGLECT_FADE = .99;

    final String from, to;
    long met = -1, lastContact = -1, lastTogether = -1, talkDay = -1, giftDay = -1, romanceSince = -1, teenSince = -1;
    int contactDays, together, giftsToday, level, floor, lowDays, kindled;
    double warmth;
    String lastGift = "";
    final List<Memory> memories = new ArrayList<>();
    final EnumMap<Act.Experience, Integer> experiences = new EnumMap<>(Act.Experience.class);
    final Set<String> moments = new TreeSet<>(), facts = new TreeSet<>(), flags = new TreeSet<>();
    Conflict conflict = Conflict.NONE;
    /** Time together: the days of past hangouts by activity (the last few), the rituals they became, the highlights. */
    final java.util.Map<String, List<Long>> hangouts = new TreeMap<>();
    final Set<String> rituals = new TreeSet<>();
    final List<Together.Highlight> highlights = new ArrayList<>();
    /** Asking and being asked: when the player last asked, how many asks in a row they turned down, and the same the other way. */
    long lastAsked = -1, quietUntil = -1;
    int declinedByThem, declinedByYou;
    /** What is going on in their life, and what either of you means to ask about later. */
    final List<LifeEvents.News> news = new ArrayList<>();
    final List<Together.FollowUp> followUps = new ArrayList<>();
    /** Questions: what they asked and what the player answered, the question waiting for an answer, and how answers shaped them. */
    final List<Questions.Answered> answers = new ArrayList<>();
    String pendingQuestion = "";
    long pendingSince = -1, lastQuestion = -1;
    final java.util.Map<String, Double> nudges = new TreeMap<>();
    String mood = "";
    long moodDay = -1;
    /** Conversation topics already raised today. */
    final Set<String> topicsToday = new TreeSet<>();
    long topicsDay = -1;
    Courtship.Stage romance = Courtship.Stage.NONE;

    Bond(String from, String to) { this.from = from; this.to = to; }

    public String from() { return from; }
    public String to() { return to; }
    public boolean met() { return met >= 0; }
    public long metOn() { return met; }
    public int contactDays() { return contactDays; }
    public int together() { return together; }
    public double warmth() { return warmth; }
    public int level() { return level; }
    /** A level kept for good: one earned in Village Friends before Shinobi Life arrived. */
    public int floor() { return floor; }
    /** How many times Kindling Bond has borrowed from them (a master's trial can make a borrowed nature yours). */
    public int kindled() { return kindled; }
    public Conflict conflict() { return conflict; }
    public Courtship.Stage romance() { return romance; }
    public List<Memory> memories() { return List.copyOf(memories); }
    public int experiences() { return experiences.values().stream().mapToInt(Integer::intValue).sum(); }
    public int experienceKinds() { return (int) experiences.values().stream().filter(n -> n > 0).count(); }
    public int experiences(Act.Experience e) { return experiences.getOrDefault(e, 0); }
    public Map<Act.Experience, Integer> experienceCounts() { return new TreeMap<>(experiences); }
    public Set<String> moments() { return Set.copyOf(moments); }
    public Set<String> facts() { return Set.copyOf(facts); }
    public boolean has(String flag) { return flags.contains(flag); }
    public Set<String> flags() { return Set.copyOf(flags); }
    public boolean remembers(Act act) { return memories.stream().anyMatch(m -> m.act() == act); }
    public Set<String> rituals() { return Set.copyOf(rituals); }
    public List<Together.Highlight> highlights() { return List.copyOf(highlights); }
    public int hangoutCount(String activity) { return hangouts.getOrDefault(activity, List.of()).size(); }
    public List<LifeEvents.News> news() { return List.copyOf(news); }
    public List<Together.FollowUp> followUps() { return List.copyOf(followUps); }
    public int declinedByThem() { return declinedByThem; }
    public int declinedByYou() { return declinedByYou; }
    /** Whether the player talked with them today. */
    public boolean talkDayIsToday(long day) { return talkDay == day; }
    public List<Questions.Answered> answers() { return List.copyOf(answers); }
    public java.util.Map<String, Double> nudges() { return java.util.Map.copyOf(nudges); }
    /** Their mood from the last answer, today only: touched, pleased, amused, impressed, fine, stung_but_respects, hurt, noticed_contradiction. */
    public String mood(long day) { return moodDay == day ? mood : ""; }

    void meet(long day) { if (met < 0) met = day; }
    /** A day with any contact at all (a talk, a lesson, a mission). */
    void contact(long day) {
        meet(day);
        if (lastContact != day) { contactDays++; lastContact = day; }
    }
    /** A day spent side by side (VF's Tie): counts once a day, at most {@link #TOGETHER_CAP} days. */
    void together(long day) {
        contact(day);
        if (lastTogether != day) { together = Math.min(TOGETHER_CAP, together + 1); lastTogether = day; }
    }
    /** Warmth from small kindnesses, with diminishing returns: each gain shrinks as warmth nears its cap. */
    double warm(double amount, double let) {
        double gain = amount > 0 ? amount * let * (1 - warmth / WARMTH_CAP) : amount;
        warmth = Math.clamp(warmth + gain, WARMTH_FLOOR, WARMTH_CAP);
        return gain;
    }
    /** Remembers an act (or folds it into a recent memory of the same small act). */
    Memory remember(Act act, Meters delta, Reaction.Source how, String about, long day) {
        if (act.experience != null && how == Reaction.Source.SELF) experiences.merge(act.experience, 1, Integer::sum);
        if (!act.remembered() || delta.isZero()) return null;
        for (int i = memories.size() - 1; i >= 0; i--) {
            var m = memories.get(i);
            if (m.merges(act, how, about, day)) { var merged = m.merged(delta, day, about); memories.set(i, merged); return merged; }
        }
        var memory = new Memory(act, day, delta, how, about, 1);
        memories.add(memory);
        if (memories.size() > MEMORY_CAP) prune(day);
        return memory;
    }
    Meters memoryWeight(long day) {
        Meters sum = Meters.ZERO;
        for (var m : memories) sum = sum.plus(m.now(day));
        return sum;
    }
    double romanticMemories(long day) {
        double sum = 0;
        for (var m : memories) sum += m.now(day).romance();
        return sum;
    }
    /** Lets faded memories go; past the cap, the weakest fading memory goes first. Big memories always stay. */
    void prune(long day) {
        memories.removeIf(m -> m.forgotten(day));
        while (memories.size() > MEMORY_CAP) {
            var weakest = memories.stream().filter(m -> !m.permanent())
                    .min(Comparator.comparingDouble((Memory m) -> m.now(day).sumOfGains() - m.now(day).sumOfLosses()));
            if (weakest.isEmpty()) break;
            memories.remove(weakest.get());
        }
    }
    /** Warmth cools a little each day nobody has been in touch for over a week. */
    void neglect(long day) {
        if (lastContact >= 0 && day - lastContact > NEGLECT_DAYS && warmth > 0) warmth *= NEGLECT_FADE;
    }
}
