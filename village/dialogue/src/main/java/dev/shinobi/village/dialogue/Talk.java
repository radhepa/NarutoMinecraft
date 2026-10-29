package dev.shinobi.village.dialogue;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Set;

/**
 * Chooses what a speaker says to the player (DIALOGUE.md). The rules, in order:
 *
 * <ol>
 *   <li><b>Never repeat.</b> A line the player has heard, from anyone, is not chosen again while a fresh line fits;
 *       a line whose content group is spent counts as heard.</li>
 *   <li><b>The most specific line wins.</b> A topic picks a facet by weight (greet: the time, the weather, their
 *       personality...), then the fresh line with the highest specificity among those whose tags and condition hold.
 *       Explicit pool lists (the bond engine's keys) are tried in order.</li>
 *   <li><b>A talk budget.</b> Each speaker gives a few fresh exchanges a day and, unless they are cast, a lifetime
 *       allowance that grows with the bond. The first greeting of the day is free; news, bond moments, quests,
 *       missions, barks and shop talk are exempt.</li>
 *   <li><b>Beyond the budget, they repeat.</b> Past it, or when nothing fresh fits, the first ask gets a
 *       "we already talked" line in their voice, the second a line they said before, and the third a polite close that
 *       ends the chat for today.</li>
 *   <li><b>Filler is capped</b> at a fifth of a speaker's fresh lines: past the cap a filler line is chosen only if
 *       nothing else fits.</li>
 * </ol>
 *
 * Barks and other {@link Line.Kind#CYCLE} pools skip the budget and deal every line once before any comes back.
 * Pure: the world is read into a {@link Context} by the glue, which also passes the in-game day.
 */
public final class Talk {
    /** What came of a request. */
    public enum Outcome { FRESH, AGAIN, REPEAT, CLOSE, NONE }
    /** Why a speaker fell back to repeating: their budget, or nothing fresh left that fits. */
    public enum Why { NONE, BUDGET, EXHAUSTED }

    /** A line said, its outcome, and the filled text (null for {@link Outcome#NONE}). */
    public record Said(Outcome outcome, Why why, Line line, String text) {
        public boolean fresh() { return outcome == Outcome.FRESH; }
        /** A close ends the conversation: only gifts, trades and quest talk remain today. */
        public boolean ended() { return outcome == Outcome.CLOSE; }
    }
    /** An overheard exchange with its turns filled. */
    public record Overheard(Line line, List<String> turns) {}
    /** The player's answer to a question: the reply, and the earlier question it contradicts (null if none). */
    public record Answered(Question question, Question.Answer answer, String reply, String contradicts) {}

    public static final Set<String> ARCHETYPES = Set.of("warmhearted", "thoughtful", "playful", "adventurous", "meticulous",
            "steadfast", "reserved", "imaginative", "pragmatic", "curious", "protective", "gentle", "proud", "fiery", "shy", "stern");

    private final Bank bank;
    private final Heard heard;
    private final Conditions conditions;
    private final Names names;
    private final Rules rules;

    public Talk(Bank bank, Heard heard, Conditions conditions, Names names) {
        this.bank = bank; this.heard = heard; this.conditions = conditions; this.names = names; this.rules = bank.rules();
    }

    public Heard heard() { return heard; }
    public Question question(String id) { return bank.question(id); }

    // -- conversation ------------------------------------------------------------------------------------------

    /** The opening line of a conversation: the first of the day is free of the budget. */
    public Said greet(String speaker, Context c, int day, Random r) { return topic(speaker, "greet", c, day, r); }
    /** "How's your day?": small talk across the chat facets. */
    public Said chat(String speaker, Context c, int day, Random r) { return topic(speaker, "chat", c, day, r); }

    /** A topic with facets in the rules (greet, chat), or a single pool such as {@code talk.food}. */
    public Said topic(String speaker, String topic, Context c, int day, Random r) {
        String t = rules.topicAlias().getOrDefault(topic, topic);
        var facets = rules.facets().get(t);
        if (facets == null) return say(speaker, List.of(t), c, day, r);
        var s = heard.speaker(speaker, rules.recall());
        s.roll(day);
        boolean free = t.equals("greet") && s.greetDay != day;
        if (!free && !allowed(s, c)) return over(s, c, r, Why.BUDGET);
        var open = new ArrayList<Rules.Facet>();
        for (var f : facets) if (f.applies(c) && bank.has(f.pool())) open.add(f);
        while (!open.isEmpty()) {
            var f = weighted(open, r);
            var line = best(bank.pool(f.pool()), s, c, r);
            if (line != null) return fresh(s, line, c, day, free, t.equals("greet"));
            open.remove(f);
        }
        return over(s, c, r, Why.EXHAUSTED);
    }

    /**
     * A line from explicit pools, most specific first (the bond engine's keys: {@code bond.greet.argument.fiery},
     * {@code bond.greet.argument}...). A trailing personality is the {@code personality} tag of a line in the pool.
     */
    public Said say(String speaker, List<String> pools, Context c, int day, Random r) {
        var s = heard.speaker(speaker, rules.recall());
        s.roll(day);
        var keys = new ArrayList<String>();
        for (String p : pools) {
            String k = normalize(p);
            if (!keys.contains(k)) keys.add(k);
        }
        boolean exempt = keys.stream().allMatch(rules::exempt);
        if (!exempt && !allowed(s, c)) return over(s, c, r, Why.BUDGET);
        for (String k : keys) {
            var line = best(bank.pool(k), s, c, r);
            if (line != null) return fresh(s, line, c, day, rules.exempt(k), false);
        }
        return over(s, c, r, Why.EXHAUSTED);
    }

    /** Whether a speaker has fresh exchanges left for the player today and over their lifetime. */
    public boolean allowed(String speaker, Context c, int day) {
        var s = heard.speaker(speaker, rules.recall());
        s.roll(day);
        return allowed(s, c);
    }
    private boolean allowed(Heard.Speaker s, Context c) {
        var tier = rules.tier(c.get("tier"));
        if (s.today >= tier.daily()) return false;
        Integer life = tier.lifetime(c.level(), slices(c));
        return life == null || s.lifetime < life;
    }
    private static int slices(Context c) {
        String slice = c.get("slice");
        return slice == null ? 1 : Math.max(1, slice.charAt(slice.length() - 1) - '0');
    }

    private Said fresh(Heard.Speaker s, Line line, Context c, int day, boolean free, boolean greeting) {
        heard.mark(line);
        s.said(line.id());
        s.fresh++;
        if (line.filler()) s.filler++;
        if (greeting) s.greetDay = day;
        if (!free) { s.today++; s.lifetime++; }
        return new Said(Outcome.FRESH, Why.NONE, line, Tokens.fill(line.text(), c, names));
    }

    /** Past the budget or out of fresh lines: "we already talked", then a line they said before, then a close. */
    private Said over(Heard.Speaker s, Context c, Random r, Why why) {
        int n = s.over++;
        if (n == 1) {
            var again = recalled(s, c, r);
            if (again != null) return new Said(Outcome.REPEAT, why, again, Tokens.fill(again.text(), c, names));
        }
        if (n >= 2) {
            var close = repeatable("close", c, r);
            if (close != null) return new Said(Outcome.CLOSE, why, close, Tokens.fill(close.text(), c, names));
            return new Said(Outcome.CLOSE, why, null, null);
        }
        var again = repeatable("again", c, r);
        if (again != null) return new Said(Outcome.AGAIN, why, again, Tokens.fill(again.text(), c, names));
        var said = recalled(s, c, r);
        if (said != null) return new Said(Outcome.REPEAT, why, said, Tokens.fill(said.text(), c, names));
        return new Said(Outcome.NONE, why, null, null);
    }
    private Line recalled(Heard.Speaker s, Context c, Random r) {
        var options = new ArrayList<Line>();
        for (int id : s.recall) {
            if (id == 0) continue;
            var l = byId(id);
            if (l != null && l.kind() == Line.Kind.LINE && l.text() != null && Tokens.fill(l.text(), c, names) != null) options.add(l);
        }
        return options.isEmpty() ? null : options.get(r.nextInt(options.size()));
    }
    private Line repeatable(String pool, Context c, Random r) {
        var fit = new ArrayList<Line>();
        int top = -1;
        for (var l : bank.pool(pool)) {
            if (!l.tags().matches(c) || !conditions.test(l.when(), c) || Tokens.fill(l.text(), c, names) == null) continue;
            if (l.spec() > top) { top = l.spec(); fit.clear(); }
            if (l.spec() == top) fit.add(l);
        }
        return fit.isEmpty() ? null : fit.get(r.nextInt(fit.size()));
    }

    /** The most specific fresh line in a pool that fits, respecting the speaker's filler cap; null if none. */
    private Line best(List<Line> pool, Heard.Speaker s, Context c, Random r) {
        var top = new ArrayList<Line>();
        var topFiller = new ArrayList<Line>();
        int spec = -1, specFiller = -1;
        for (var l : pool) {
            if (l.kind() != Line.Kind.LINE || heard.heard(l.id()) || heard.spent(l.group())) continue;
            if (!l.tags().matches(c) || !conditions.test(l.when(), c) || Tokens.fill(l.text(), c, names) == null) continue;
            if (l.filler()) {
                if (l.spec() > specFiller) { specFiller = l.spec(); topFiller.clear(); }
                if (l.spec() == specFiller) topFiller.add(l);
            } else {
                if (l.spec() > spec) { spec = l.spec(); top.clear(); }
                if (l.spec() == spec) top.add(l);
            }
        }
        boolean fillerOk = (s.filler + 1) <= rules.fillerCap() * (s.fresh + 1);
        if (fillerOk && !topFiller.isEmpty() && (top.isEmpty() || specFiller >= spec)) {
            if (top.isEmpty() || specFiller > spec) return topFiller.get(r.nextInt(topFiller.size()));
            var both = new ArrayList<>(top);
            both.addAll(topFiller);
            return both.get(r.nextInt(both.size()));
        }
        if (!top.isEmpty()) return top.get(r.nextInt(top.size()));
        return topFiller.isEmpty() ? null : topFiller.get(r.nextInt(topFiller.size()));
    }

    // -- barks and overheard talk --------------------------------------------------------------------------------

    /** A bark from a cycling pool ({@code combat.fight_start.bandit}): every line once before any returns; null: silence. */
    public String bark(String pool, Context c, Random r) {
        var l = cycle(bank.pool(normalize(pool)), c, r);
        return l == null ? null : Tokens.fill(l.text(), c, names);
    }
    /** An exchange two residents are having, from the first of the pools that has one that fits. */
    public Overheard overhear(List<String> pools, Context c, Random r) {
        for (String p : pools) {
            var l = cycle(bank.pool(p), c, r);
            if (l == null) continue;
            var turns = new ArrayList<String>();
            for (var t : l.turns()) turns.add(Tokens.fill(t.text(), c, names));
            return new Overheard(l, List.copyOf(turns));
        }
        return null;
    }
    private Line cycle(List<Line> pool, Context c, Random r) {
        var fit = new ArrayList<Line>();
        for (var l : pool) {
            if (!l.tags().matches(c) || !conditions.test(l.when(), c)) continue;
            if (l.exchange() ? l.turns().stream().anyMatch(t -> Tokens.fill(t.text(), c, names) == null) : Tokens.fill(l.text(), c, names) == null) continue;
            fit.add(l);
        }
        if (fit.isEmpty()) return null;
        var fresh = new ArrayList<Line>();
        int spec = -1;
        for (var l : fit) {
            if (heard.heard(l.id())) continue;
            if (l.spec() > spec) { spec = l.spec(); fresh.clear(); }
            if (l.spec() == spec) fresh.add(l);
        }
        if (fresh.isEmpty()) {
            for (var l : fit) heard.unmark(l); // The whole pool has been heard here: deal it again.
            return cycle(pool, c, r);
        }
        var l = fresh.get(r.nextInt(fresh.size()));
        if (l.kind() != Line.Kind.REPEAT) heard.mark(l);
        return l;
    }

    // -- questions ----------------------------------------------------------------------------------------------

    /**
     * A question this speaker could ask now, paced as the bond engine paces them (from level 2, one a day across
     * everyone, days between one speaker's questions by level): the first {@link #askable} one, deeper follow-ups
     * first. For the standalone engine and the simulation; in the game the bond engine's {@code Questions.next} chooses
     * and calls {@link #askable} as its veto. Null if none.
     */
    public Question ask(String speaker, Context c, int day, Random r) {
        var p = rules.pacing();
        var s = heard.speaker(speaker, rules.recall());
        s.roll(day);
        if (heard.askDay != day) { heard.askDay = day; heard.asksToday = 0; }
        if (c.level() < p.minLevel() || heard.asksToday >= p.perDay() || day - s.askDay < p.gap(c.level())) return null;
        var fit = new ArrayList<Question>();
        int depth = 0;
        for (var q : bank.questions()) {
            if (!askable(speaker, q, c, day)) continue;
            if (q.depth() > depth) { depth = q.depth(); fit.clear(); }
            if (q.depth() == depth) fit.add(q);
        }
        if (fit.isEmpty()) return null;
        s.askDay = day;
        heard.asksToday++;
        return fit.get(r.nextInt(fit.size()));
    }
    /**
     * Whether this speaker may ask this question now: never answered (by anyone), within the bond level, its tags and
     * condition holding, the question it follows answered, its first phrasing fillable, and a fresh exchange left in
     * the speaker's budget. The bond engine's veto.
     */
    public boolean askable(String speaker, Question q, Context c, int day) {
        if (heard.heard(q.num()) || q.level() > c.level() || !q.tags().matches(c) || !conditions.test(q.when(), c)) return false;
        if (q.follows() != null && heard.answer(q.follows()) == null) return false;
        if (Tokens.fill(q.asks().getFirst(), c, names) == null) return false;
        var s = heard.speaker(speaker, rules.recall());
        s.roll(day);
        return allowed(s, c);
    }
    /** The phrasing of a question to show (one of its asks), filled. */
    public String phrase(Question q, Context c, Random r) {
        var options = new ArrayList<String>();
        for (var a : q.asks()) { String f = Tokens.fill(a, c, names); if (f != null) options.add(f); }
        return options.isEmpty() ? null : options.get(r.nextInt(options.size()));
    }
    /**
     * The player answers: the question is spent for good, the answer remembered, and an answer on the same axis with
     * the opposite pole as an earlier one is a contradiction (the bond engine decides what it costs).
     */
    public Answered answer(String speaker, Question q, String answerId, Context c, int day) {
        var a = q.answer(answerId);
        var s = heard.speaker(speaker, rules.recall());
        s.roll(day);
        heard.lines.set(q.num());
        heard.answers.put(q.id(), a.id());
        s.today++; s.lifetime++; s.fresh++;
        String contradicts = null;
        if (q.axis() != null && a.pole() != 0) {
            String before = heard.axes.get(q.axis());
            if (before != null) {
                int colon = before.indexOf(':');
                int pole = Integer.parseInt(before.substring(0, colon));
                if (pole != a.pole()) contradicts = before.substring(colon + 1);
            }
            heard.axes.put(q.axis(), a.pole() + ":" + q.id());
        }
        return new Answered(q, a, Tokens.fill(a.reply(), c, names), contradicts);
    }

    // -- helpers ------------------------------------------------------------------------------------------------

    /** A bond key's trailing personality is a tag in the compiled bank: {@code talk.food.fiery} is pool {@code talk.food}. */
    public static String normalize(String key) {
        int dot = key.lastIndexOf('.');
        if (dot <= 0 || !ARCHETYPES.contains(key.substring(dot + 1))) return key;
        String head = key.substring(0, dot);
        for (String p : SUFFIXED) if (head.startsWith(p)) return head;
        return key;
    }
    /** Families whose keys may end in a personality; elsewhere ({@code village.mood.proud}) the last word is part of the key. */
    static final List<String> SUFFIXED = List.of("home.", "bond.greet", "bond.levelup", "bond.jealous", "bond.birthday", "bond.romance", "talk.", "life.", "hangout.",
            "gift.", "reaction", "callback.contradict", "again", "close", "followup.", "combat.");
    private Line byId(int id) {
        if (index == null) {
            index = new java.util.HashMap<>();
            for (String k : bank.poolKeys()) for (var l : bank.pool(k)) index.put(l.id(), l);
        }
        return index.get(id);
    }
    private java.util.Map<Integer, Line> index;

    private static Rules.Facet weighted(List<Rules.Facet> facets, Random r) {
        int total = 0;
        for (var f : facets) total += f.weight();
        int roll = r.nextInt(Math.max(1, total));
        for (var f : facets) { roll -= f.weight(); if (roll < 0) return f; }
        return facets.getFirst();
    }
}
