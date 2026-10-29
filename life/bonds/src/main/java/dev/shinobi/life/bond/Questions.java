package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * Questions and choices: residents ask the player things (an opinion, a dilemma, advice, a preference, about the
 * player's past and plans, or they confess something small and wait to see how the player takes it), and the answer
 * matters.
 *
 * <ul>
 * <li><b>Effects:</b> an answer's tags ({@link AnswerTag}) are resolved against the asker's personality and values,
 * weighted by the kind of question and its depth: meter changes both ways (a blunt answer raises trust and costs
 * warmth), their mood today ({@link #reaction}) and a remembered answer.</li>
 * <li><b>Memory:</b> every answer is kept in the bond's ledger. A week later they may bring it up
 * ({@link #callback}). Answering the opposite of something you said before on the same axis (to them, or to someone
 * they heard it from) is a contradiction they may notice: likelier the closer you are, if they value honesty, and if
 * they are disciplined. People change their minds, so answers older than a year do not count.</li>
 * <li><b>Growth:</b> an answer can set a flag quests read ({@code answered}) and nudge the asker's personality a
 * little (advice taken to heart).</li>
 * <li><b>Pacing:</b> questions open by level, deeper ones later; an answered question is never asked again, only
 * continued by its follow-ups; at most one question per person per day, one every four to eight days per person
 * (closer friends ask more), from level 2, one a day across everyone; an unanswered question waits three days.</li>
 * <li><b>Gossip:</b> an answer to a public question (about a clan, a person, the village) becomes something the
 * village knows the player said, travelling along ties like any small deed; an answer can also be a deed outright
 * (an insult to a clan).</li>
 * </ul>
 */
public final class Questions {
    public static final int DAILY_CAP = 1, MIN_LEVEL = 2, PENDING_DAYS = 3, CALLBACK_AFTER = 7, CALLBACK_GAP = 14, CHANGED_MIND = BondWorld.YEAR;
    public static final double NUDGE_LIMIT = .3;

    /** One answer in the ledger: the question, the answer, when, and where it stood on the question's axis. */
    public record Answered(String question, String answer, long day, String about, String stance, boolean recalled) {}
    /** What answering did: the change to their meters, their reaction, whether it contradicted something, the deed if it spread. */
    public record Outcome(Meters delta, String reaction, String lineKey, boolean contradiction, boolean noticed, int deedSerial) {
        /** What the dialogue should say next: {@code callback.contradict} when they caught it, else "". */
        public String say() { return noticed ? "callback.contradict" : ""; }
    }

    public static void load(BondWorld w, List<Question> bank) { w.questionBank.clear(); w.questionBank.addAll(bank); }
    public static Question question(BondWorld w, String id) {
        return w.questionBank.stream().filter(q -> q.id().equals(id)).findFirst().orElseThrow(() -> new IllegalArgumentException("no question " + id));
    }
    /** Days between questions from one person: closer friends ask more often. */
    public static int gap(int level) { return level >= 7 ? 4 : level >= 4 ? 6 : 8; }

    /** The question this person asks now, if any: within the budget, at their level, never one already answered. */
    public static Optional<Question> next(BondWorld w, String who) { return next(w, who, q -> true); }
    /**
     * The same with the dialogue glue's veto: {@code allowed} checks what the engine cannot (the question's Core
     * {@code when} condition, the dialogue's own talk budget and never-repeat ledger).
     */
    public static Optional<Question> next(BondWorld w, String who, java.util.function.Predicate<Question> allowed) {
        var b = w.bond(who); long day = w.day;
        if (w.questionsDay != day) { w.questionsDay = day; w.questionsToday = 0; }
        if (!b.pendingQuestion.isEmpty() && day - b.pendingSince <= PENDING_DAYS && allowed.test(question(w, b.pendingQuestion)))
            return Optional.of(question(w, b.pendingQuestion));
        b.pendingQuestion = "";
        int level = w.effectiveLevel(who);
        if (w.questionsToday >= DAILY_CAP || level < MIN_LEVEL || b.conflict.active() || b.conflict.broken()) return Optional.empty();
        if (b.lastQuestion >= 0 && day - b.lastQuestion < gap(level)) return Optional.empty();
        var p = w.person(who);
        var recentKinds = b.answers.stream().skip(Math.max(0, b.answers.size() - 2)).map(a -> question(w, a.question()).kind()).toList();
        var candidates = new ArrayList<Question>(); var weights = new ArrayList<Double>(); double total = 0;
        for (var q : w.questionBank) {
            if (q.level() > level || answered(b, q.id()) || !q.suits(p) || !allowed.test(q)) continue;
            if (!q.followUpOf().isEmpty()) {
                var prior = b.answers.stream().filter(a -> a.question().equals(q.followUpOf())).findFirst();
                if (prior.isEmpty() || day - prior.get().day() < q.minGapDays()) continue;
            }
            double weight = (q.followUpOf().isEmpty() ? 1 : 3) * (recentKinds.contains(q.kind()) ? 1 : 1.5) * (q.roles().isEmpty() ? 1 : 4) * (1 + .2 * (q.depth() - 1));
            candidates.add(q); weights.add(weight); total += weight;
        }
        if (candidates.isEmpty()) { w.questionsDry++; return Optional.empty(); }
        double roll = Seeds.roll(w.seed, "question", who, Long.toString(day)) * total;
        Question pick = candidates.getLast();
        for (int i = 0; i < candidates.size(); i++) { roll -= weights.get(i); if (roll < 0) { pick = candidates.get(i); break; } }
        b.pendingQuestion = pick.id(); b.pendingSince = day;
        w.questionsToday++;
        return Optional.of(pick);
    }
    /** Asks a particular question now (a quest or a story scene), outside the budget. */
    public static void ask(BondWorld w, String who, String questionId) {
        question(w, questionId);
        var b = w.bond(who); b.pendingQuestion = questionId; b.pendingSince = w.day;
    }
    static boolean answered(Bond b, String questionId) { return b.answers.stream().anyMatch(a -> a.question().equals(questionId)); }
    public static boolean answered(BondWorld w, String who, String questionId, String answerId) {
        return w.bond(who).answers.stream().anyMatch(a -> a.question().equals(questionId) && (answerId == null || answerId.isEmpty() || a.answer().equals(answerId)));
    }

    /** What an answer would do to how they feel, without answering. */
    public static Meters preview(BondWorld w, String who, Question q, String answerId) {
        var p = w.person(who).personality(); var a = q.answer(answerId);
        Meters sum = Meters.ZERO;
        for (var tag : a.tags()) sum = sum.plus(tag.react(p));
        // What the answer stands for, against what they live by.
        for (var e : a.stands().entrySet()) {
            boolean theirs = p.holds(e.getKey());
            if (e.getValue() > 0) sum = sum.plus(theirs ? Meters.of(1.5, 1.5, 0, 0) : Meters.of(.3, .3, 0, 0));
            else if (e.getValue() < 0 && theirs) sum = sum.plus(Meters.of(-2, -2.5, 0, 0));
        }
        return sum.times(q.kind().weight() * (1 + .25 * (q.depth() - 1)));
    }
    /** The player answers. Throws for an unknown question or answer. */
    public static Outcome answer(BondWorld w, String who, String questionId, String answerId) {
        var q = question(w, questionId); var a = q.answer(answerId); var b = w.bond(who); long day = w.day;
        var delta = preview(w, who, q, answerId);
        boolean contradiction = false, noticed = false;
        if (!q.about().isEmpty()) {
            String earlier = earlierStance(w, who, q.about());
            if (earlier != null && !earlier.isEmpty() && !a.stance().isEmpty() && !earlier.equals(a.stance())) {
                contradiction = true;
                var p = w.person(who).personality();
                double chance = .15 + .07 * w.effectiveLevel(who) + (p.holds(Personality.Value.HONESTY) ? .25 : 0) + .1 * Math.max(0, p.discipline());
                noticed = Seeds.roll(w.seed, "contradiction", who, questionId, Long.toString(day)) < chance;
            }
        }
        w.applyDelta(who, Act.ANSWERED, delta);
        if (noticed) w.act(who, Act.CAUGHT_CONTRADICTION);
        b.answers.add(new Answered(q.id(), a.id(), day, q.about(), a.stance(), false));
        b.pendingQuestion = ""; b.lastQuestion = day;
        if (!a.sets().isEmpty()) b.flags.add(a.sets());
        b.flags.add("answer:" + q.id() + "=" + a.id());
        if (a.nudgeTrait() != null && a.nudge() != 0) nudge(w, who, a.nudgeTrait(), a.nudge());
        int serial = -1;
        if (a.deed() != null || q.isPublic() && !q.about().isEmpty()) {
            var d = w.deed(a.deed() != null ? a.deed() : Act.STATED, who, List.of());
            d.note = q.about() + "=" + a.stance();
            serial = d.serial;
        }
        String reaction = noticed ? "noticed_contradiction" : reaction(delta, a);
        b.mood = reaction; b.moodDay = day;
        return new Outcome(delta, reaction, "answer." + q.id() + "." + a.id(), contradiction, noticed, serial);
    }
    /** Where the player last stood on an axis, as far as this person knows: told them, or heard it from someone. */
    static String earlierStance(BondWorld w, String who, String about) {
        long day = w.day;
        var own = w.bond(who).answers.reversed().stream().filter(a -> a.about().equals(about) && !a.stance().isEmpty() && day - a.day() <= CHANGED_MIND).findFirst();
        if (own.isPresent()) return own.get().stance();
        for (var d : w.deeds.reversed()) {
            if (d.note.isEmpty() || !d.note.startsWith(about + "=") || day - d.day > CHANGED_MIND || !d.knows(who)) continue;
            return d.note.substring(about.length() + 1);
        }
        return null;
    }
    /** How they take an answer: touched, pleased, amused, impressed, fine, stung_but_respects or hurt. */
    public static String reaction(Meters d, Question.Answer a) {
        if (d.affection() <= -1.5 && d.trust() >= 1.5) return "stung_but_respects";
        if (d.affection() <= -1.5) return "hurt";
        if (d.affection() >= 2.5 && d.trust() >= 1.5) return "touched";
        if (d.respect() >= 1.5 && d.respect() >= d.affection()) return "impressed";
        if (a.tags().contains(AnswerTag.PLAYFUL) && d.affection() > 0) return "amused";
        if (d.affection() + d.trust() >= 1.5) return "pleased";
        return "fine";
    }
    private static void nudge(BondWorld w, String who, Personality.Trait trait, double amount) {
        var b = w.bond(who);
        double before = b.nudges.getOrDefault(trait.name(), 0.0), after = Math.clamp(before + amount, -NUDGE_LIMIT, NUDGE_LIMIT);
        if (after == before) return;
        b.nudges.put(trait.name(), after);
        w.add(w.person(who).withPersonality(shifted(w.person(who).personality(), trait, after - before)));
    }
    static Personality shifted(Personality p, Personality.Trait t, double by) {
        return p.withTraits(p.warmth() + (t == Personality.Trait.WARMTH ? by : 0), p.boldness() + (t == Personality.Trait.BOLDNESS ? by : 0),
                p.pride() + (t == Personality.Trait.PRIDE ? by : 0), p.discipline() + (t == Personality.Trait.DISCIPLINE ? by : 0),
                p.openness() + (t == Personality.Trait.OPENNESS ? by : 0));
    }
    /** An answer from at least a week ago they bring up now ({@code callback.answer.<question>.<answer>}), once each, at most every two weeks. */
    public static Optional<String> callback(BondWorld w, String who) {
        var b = w.bond(who);
        if (b.flags.stream().anyMatch(f -> f.startsWith("answer_callback:") && w.day - Long.parseLong(f.substring(16)) < CALLBACK_GAP)) return Optional.empty();
        for (int i = b.answers.size() - 1; i >= 0; i--) {
            var a = b.answers.get(i);
            if (a.recalled() || w.day - a.day() < CALLBACK_AFTER) continue;
            b.answers.set(i, new Answered(a.question(), a.answer(), a.day(), a.about(), a.stance(), true));
            b.flags.removeIf(f -> f.startsWith("answer_callback:"));
            b.flags.add("answer_callback:" + w.day);
            return Optional.of("callback.answer." + a.question() + "." + a.answer());
        }
        return Optional.empty();
    }

    private Questions() {}
}
