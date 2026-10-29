package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Time together: hangouts, asked for and offered, kept and missed.
 *
 * <ul>
 * <li><b>Asking</b> ({@link #invite}): suggest an activity, a day and an hour to one or more people. Each answers yes,
 * or why not: busy (with the next time they are free), not close enough yet, not that kind of relationship, not
 * their thing, still cold after a quarrel, or not today. The chance grows with the level they act on and with how much
 * they like the activity, and shrinks if you keep asking after a no.</li>
 * <li><b>Being asked</b> ({@link #daily}): residents at level 3 or more invite the player themselves (about one
 * chance in fifty a day, more for closer, warmer, more open people, never twice within six days), the warm and
 * open more often, to what they like doing, when they are free. Turning them down three times running makes them feel
 * overlooked, and they stop asking for two weeks.</li>
 * <li><b>The hangout</b> ({@link #go}): if the player does not come, they were stood up. Otherwise it goes rough,
 * fine, good or great, from taste, chemistry, the village's mood, a ritual, the company (two people who dislike each
 * other spoil it) and a seeded roll. A great one leaves a highlight: a specific memory with a dialogue line, which they
 * bring up later ({@link BondDialogue#callback}). Hanging out introduces friends to each other.</li>
 * <li><b>Rituals:</b> the same activity with the same person three times within five weeks becomes theirs ("our
 * ramen"): it goes better, and they miss it when it lapses.</li>
 * <li><b>Follow-ups</b> ({@link #share}): tell someone what is coming up (an exam, a mission) and they ask how it went.</li>
 * </ul>
 */
public final class Together {
    public static final int RITUAL_TIMES = 3, RITUAL_WINDOW = 35, RITUAL_LAPSE = 28, MAX_HIGHLIGHTS = 24, PENDING_INVITES = 3, QUIET_DAYS = 14,
            DECLINES_TO_QUIET = 3, INVITE_GAP = 6;

    public record Highlight(String activity, long day, String key, List<String> with) {}
    /** Something to ask about later: {@code theyAsk} when they will ask the player, else the player can ask them. */
    public record FollowUp(String topic, long due, boolean theyAsk) {}
    public record Plan(String id, List<String> with, String activity, long day, int hour, String host) {}
    public record Invitation(String id, String from, String activity, long day, int hour, long expires) {}
    /** An answer per person ("" for yes) and the plan made with those who said yes, or null; a counter-proposal when busy. */
    public record Answer(Map<String, String> answers, Plan plan, long[] counter) {}
    public record Outcome(String band, Map<String, Double> quality, Highlight highlight, List<String> newRituals) {}

    // -- asking --------------------------------------------------------------------------------------

    public static Answer invite(BondWorld w, List<String> who, String activityId, long day, int hour) {
        var a = Activity.of(activityId);
        var answers = new LinkedHashMap<String, String>();
        var yes = new ArrayList<String>();
        long[] counter = null;
        if (who.size() > a.maxGroup()) return new Answer(Map.of("group", "too_many"), null, null);
        for (String id : who) {
            String why = answer(w, id, a, day, hour);
            if (why.equals("busy") && counter == null) counter = Schedule.nextFree(w.seed, List.of(w.person(id)), a, day, hour + 1, 3);
            answers.put(id, why);
            var b = w.bond(id);
            if (why.isEmpty()) { yes.add(id); b.declinedByThem = 0; } else if (!why.equals("busy") && !why.equals("closed")) b.declinedByThem++;
            b.lastAsked = w.day;
        }
        Plan plan = null;
        if (!yes.isEmpty()) { plan = new Plan("plan." + (++w.planSerial), List.copyOf(yes), a.id(), day, hour, BondWorld.PLAYER); w.plans.add(plan); }
        return new Answer(answers, plan, counter);
    }
    /** One person's answer to the player's invitation: "" for yes. */
    static String answer(BondWorld w, String who, Activity a, long day, int hour) {
        var p = w.person(who); var b = w.bond(who);
        if (a.romantic() && !b.romance.committed()) return "not_like_that";
        if (a.minStage().compareTo(w.playerStage) > 0 || a.minStage().compareTo(p.stage()) > 0) return "too_young";
        var state = b.conflict.state();
        if (state == Conflict.State.COLD_SHOULDER || state == Conflict.State.FALLING_OUT || state == Conflict.State.ARGUMENT) return "cold";
        int level = w.effectiveLevel(who);
        if (level < a.minLevel()) return "not_close_enough";
        if (!a.open(day, hour)) return "closed";
        if (!Schedule.free(w.seed, p, day, hour)) return "busy";
        double taste = Activity.taste(w.seed, p, a);
        double pester = b.lastAsked >= 0 && w.day - b.lastAsked <= 2 ? .15 * b.declinedByThem : 0;
        double cheer = w.village == null ? 0 : w.village.mood("village").cheer();
        double chance = Math.clamp(.25 + .08 * level + .3 * taste - pester + .1 * cheer, .02, .97);
        if (Seeds.roll(w.seed, "ask", who, a.id(), Long.toString(day), Long.toString(w.day)) < chance) return "";
        return taste < -.3 ? "not_their_thing" : "not_today";
    }

    // -- being asked ---------------------------------------------------------------------------------

    /** End of day: invitations residents send the player, missed plans, lapsed invitations and rituals. */
    static void daily(BondWorld w) {
        long day = w.day;
        for (var plan : List.copyOf(w.plans)) if (plan.day() < day) go(w, plan.id(), false);
        for (var inv : List.copyOf(w.invitations)) if (inv.expires() < day) answer(w, inv.id(), false);
        for (var b : List.copyOf(w.bonds.values())) {
            if (!b.to.equals(BondWorld.PLAYER) || !b.met()) continue;
            lapse(w, b);
            if (w.invitations.size() >= PENDING_INVITES || day < b.quietUntil || b.conflict.active() || b.conflict.broken()) continue;
            int level = w.effectiveLevel(b.from);
            if (level < 3 || w.invitedOn.getOrDefault(b.from, Long.MIN_VALUE / 2) > day - INVITE_GAP) continue;
            var pp = w.person(b.from).personality();
            double chance = .02 + .01 * (level - 3) + .02 * Math.max(0, pp.openness()) + .015 * Math.max(0, pp.warmth());
            if (Seeds.roll(w.seed, "invites_you", b.from, Long.toString(day)) >= chance) continue;
            var pick = choose(w, b.from, level);
            if (pick == null) continue;
            var slot = Schedule.nextFree(w.seed, List.of(w.person(b.from)), pick, day + 1, 8, 2);
            if (slot == null) continue;
            w.invitations.add(new Invitation("invite." + (++w.planSerial), b.from, pick.id(), slot[0], (int) slot[1], day + 1));
            w.invitedOn.put(b.from, day);
            w.events.add(new BondEvent(day, b.from, "invitation", pick.id()));
        }
    }
    /** What someone asks the player to do: their favorite when close enough for it, else what they like most that they may suggest. */
    static Activity choose(BondWorld w, String who, int level) {
        var p = w.person(who);
        Activity best = null; double top = -2;
        for (var a : Activity.CATALOG.values()) {
            if (a.minLevel() > level || a.romantic() && !w.bond(who).romance.committed() || a.minStage().compareTo(w.playerStage) > 0 || a.minStage().compareTo(p.stage()) > 0) continue;
            double t = Activity.taste(w.seed, p, a) + .05 * Seeds.roll(w.seed, "whim", who, a.id(), Long.toString(w.day));
            if (t > top) { top = t; best = a; }
        }
        return top > 0 ? best : null;
    }
    public static List<Invitation> invitations(BondWorld w) { return List.copyOf(w.invitations); }
    /** The player answers an invitation. Turning someone down three times running makes them feel overlooked. */
    public static Plan answer(BondWorld w, String invitationId, boolean accept) {
        var inv = w.invitations.stream().filter(i -> i.id().equals(invitationId)).findFirst().orElse(null);
        if (inv == null) return null;
        w.invitations.remove(inv);
        var b = w.bond(inv.from());
        if (accept) {
            b.declinedByYou = 0;
            var plan = new Plan("plan." + (++w.planSerial), List.of(inv.from()), inv.activity(), inv.day(), inv.hour(), inv.from());
            w.plans.add(plan);
            return plan;
        }
        if (++b.declinedByYou >= DECLINES_TO_QUIET) {
            w.npcFelt(inv.from(), Act.FELT_OVERLOOKED);
            b.quietUntil = w.day + QUIET_DAYS; b.declinedByYou = 0;
            w.events.add(new BondEvent(w.day, inv.from(), "stopped_asking", ""));
        }
        return null;
    }

    // -- the hangout ---------------------------------------------------------------------------------

    public static List<Plan> plans(BondWorld w) { return List.copyOf(w.plans); }
    /** The hangout happens (or the player did not come). Returns the outcome, or null for an unknown plan. */
    public static Outcome go(BondWorld w, String planId, boolean came) {
        var plan = w.plans.stream().filter(p -> p.id().equals(planId)).findFirst().orElse(null);
        if (plan == null) return null;
        w.plans.remove(plan);
        var a = Activity.of(plan.activity());
        if (!came) {
            for (String who : plan.with()) { w.act(who, Act.STOOD_UP); w.events.add(new BondEvent(w.day, who, "stood_up", a.id())); }
            return new Outcome("stood_up", Map.of(), null, List.of());
        }
        var quality = new LinkedHashMap<String, Double>();
        double cheer = w.village == null ? 0 : w.village.mood("village").cheer();
        for (String who : plan.with()) {
            var p = w.person(who); var b = w.bond(who);
            double q = .45 + .3 * Activity.taste(w.seed, p, a) + .1 * w.chemistry(who, BondWorld.PLAYER) + .1 * cheer
                    + (b.rituals.contains(a.id()) ? .15 : 0) + (Seeds.roll(w.seed, "hangout", plan.id(), who) - .5) * .4;
            for (String other : plan.with()) if (!other.equals(who) && dislike(w, who, other)) q -= .2;
            quality.put(who, Math.clamp(q, 0, 1));
        }
        double mean = quality.values().stream().mapToDouble(Double::doubleValue).average().orElse(.5);
        String band = mean < .3 ? "rough" : mean < .6 ? "fine" : mean < .85 ? "good" : "great";
        Highlight highlight = null;
        if (band.equals("great")) {
            int n = 1 + (int) (Seeds.roll(w.seed, "highlight", plan.id()) * a.highlights());
            highlight = new Highlight(a.id(), w.day, "hangout." + a.id() + ".highlight." + n, plan.with());
        }
        var rituals = new ArrayList<String>();
        for (String who : plan.with()) {
            var b = w.bond(who);
            w.together(who);
            double q = quality.get(who);
            if (q < .3) { w.act(who, Act.AWKWARD_HANGOUT); continue; }
            w.act(who, a.act());
            if (q >= .6) w.addFriendship(who, 1);
            if (highlight != null) {
                w.act(who, Act.HIGHLIGHT);
                b.highlights.add(highlight);
                if (b.highlights.size() > MAX_HIGHLIGHTS) b.highlights.removeFirst();
            }
            var days = b.hangouts.computeIfAbsent(a.id(), k -> new ArrayList<>());
            days.add(w.day);
            if (days.size() > 6) days.removeFirst();
            long recent = days.stream().filter(d -> w.day - d <= RITUAL_WINDOW).count();
            if (recent >= RITUAL_TIMES && b.rituals.add(a.id())) { rituals.add(who + ":" + a.id()); w.events.add(new BondEvent(w.day, who, "ritual", a.id())); }
            if (a.id().equals(Activity.favorite(w.seed, who)) && days.size() >= 2) b.facts.add("favorite_hangout");
        }
        // Friends of yours meet each other: a good time together starts a friendship of their own.
        if (!band.equals("rough")) for (String x : plan.with()) for (String y : plan.with()) if (x.compareTo(y) < 0) {
            w.npcAct(x, y, a.act()); w.npcAct(y, x, a.act());
            if (w.village != null && w.village.tie(x, y) == null && !band.equals("fine")) w.village.link(x, y, "friend");
        }
        return new Outcome(band, quality, highlight, rituals);
    }
    private static boolean dislike(BondWorld w, String a, String b) {
        var bond = w.bonds.get(BondWorld.key(a, b));
        if (bond != null && (bond.conflict.active() || bond.conflict.broken())) return true;
        return w.village != null && w.village.affinity(a, b) < -20;
    }
    /** A ritual that lapses: missed after four weeks (they mention it), let go after eight. */
    private static void lapse(BondWorld w, Bond b) {
        for (String r : List.copyOf(b.rituals)) {
            var days = b.hangouts.getOrDefault(r, List.of());
            long since = days.isEmpty() ? Long.MAX_VALUE : w.day - days.getLast();
            if (since == RITUAL_LAPSE) b.followUps.add(new FollowUp("ritual_missed." + r, w.day, true));
            if (since >= 2L * RITUAL_LAPSE) { b.rituals.remove(r); w.events.add(new BondEvent(w.day, b.from, "ritual_lapsed", r)); }
        }
    }

    // -- follow-ups ----------------------------------------------------------------------------------

    /** The player tells someone about something coming up ({@code topic}: "exam", "mission", "festival"...); they ask in {@code days}. */
    public static void share(BondWorld w, String who, String topic, int days) {
        var b = w.bond(who);
        b.contact(w.day);
        b.followUps.add(new FollowUp(topic, w.day + days, true));
        w.addFriendship(who, .5);
    }

    private Together() {}
}
