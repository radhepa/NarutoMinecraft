package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.function.Predicate;

/**
 * Residents have lives of their own. Each week, the people the player knows may have something happen: a promotion,
 * an injury, a new pet, a baby in the family, a heartbreak, a step toward their dream or a setback. They tell the
 * player when the bond is deep enough for it (good news early, hard news only to close friends), and how the player
 * responds matters: congratulating, comforting, helping, or shrugging it off. Comforting a close friend through
 * something hard is a real moment for the gates. A close friend whose hard news goes unanswered for a week feels
 * overlooked. Later they tell you how it turned out ({@code life.<kind>.update}).
 */
public final class LifeEvents {
    public static final int WEEKLY_PERCENT_CAST = 35, WEEKLY_PERCENT = 20, PENDING = 3, UNANSWERED_DAYS = 7, MOMENT_LEVEL = 5;

    public enum Kind {
        PROMOTED(1, 1, 3, p -> p.shinobi() && p.rank() >= 1 && p.rank() < 4),
        PASSED_EXAM(1, 1, 3, p -> p.stage() == Person.Stage.CHILD || p.rank() == 1),
        PROUD_MOMENT(2, 1, 4, p -> true),
        NEW_PET(1, 1, 2, p -> true),
        NEW_BABY_IN_FAMILY(2, 1, 2, p -> !p.family().isEmpty()),
        NEW_HOBBY(2, 1, 3, p -> true),
        DREAM_STEP(4, 1, 3, p -> !p.personality().dream().isEmpty()),
        MOVING(2, 0, 1, p -> p.stage() == Person.Stage.ADULT),
        RIVAL_LOSS(3, -1, 2, Person::shinobi),
        INJURED(3, -1, 3, Person::shinobi),
        SICK(3, -1, 2, p -> true),
        SHOP_TROUBLE(3, -1, 2, p -> !p.shinobi() && p.circles().stream().anyMatch(c -> c.startsWith("work:"))),
        FRIEND_QUARREL(4, -1, 2, p -> true),
        DREAM_SETBACK(5, -1, 2, p -> !p.personality().dream().isEmpty()),
        FAMILY_LOSS(4, -1, 1, p -> !p.family().isEmpty()),
        HEARTBREAK(5, -1, 2, p -> p.stage() != Person.Stage.CHILD && p.romantic());

        /** The level at which they would tell the player; whether it is good (1), hard (-1) or neither (0); its weight. */
        public final int shareLevel, valence, weight;
        final Predicate<Person> fits;
        Kind(int shareLevel, int valence, int weight, Predicate<Person> fits) { this.shareLevel = shareLevel; this.valence = valence; this.weight = weight; this.fits = fits; }
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Kind of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
    }
    /** Something in someone's life: whether they told the player (and when), and how the player responded ("" not yet). */
    public record News(Kind kind, long day, boolean shared, long sharedDay, String response) {
        News told(long d) { return new News(kind, day, true, d, response); }
        News answered(String r) { return new News(kind, day, shared, sharedDay, r); }
    }

    /** Each person's weekly turn (spread over the week): the cast and the known may have something happen. */
    static void daily(BondWorld w) {
        long day = w.day;
        for (var b : List.copyOf(w.bonds.values())) {
            if (!b.to.equals(BondWorld.PLAYER) || !b.met() || Village.slot(b.from) != Math.floorMod(day, Village.WEEK)) continue;
            var p = w.person(b.from);
            if (b.news.stream().filter(n -> n.response().isEmpty()).count() < PENDING) {
                int percent = b.from.startsWith("role:") ? WEEKLY_PERCENT_CAST : WEEKLY_PERCENT;
                if (Seeds.roll(w.seed, "life", b.from, Long.toString(day)) * 100 < percent) {
                    var kind = pick(w, p, day);
                    if (kind != null) b.news.add(new News(kind, day, false, -1, ""));
                }
            }
            if (b.news.size() > 12) b.news.removeFirst();
        }
        // Hard news a close friend told you, left unanswered for a week.
        for (var b : List.copyOf(w.bonds.values())) {
            if (!b.to.equals(BondWorld.PLAYER)) continue;
            for (int i = 0; i < b.news.size(); i++) {
                var n = b.news.get(i);
                if (n.shared() && n.response().isEmpty() && n.kind().valence < 0 && day - n.sharedDay() >= UNANSWERED_DAYS && b.level >= MOMENT_LEVEL) {
                    b.news.set(i, n.answered("unanswered"));
                    w.npcFelt(b.from, Act.FELT_OVERLOOKED);
                }
            }
        }
    }
    static Kind pick(BondWorld w, Person p, long day) {
        var fits = new ArrayList<Kind>(); int total = 0;
        for (var k : Kind.values()) if (k.fits.test(p)) { fits.add(k); total += k.weight; }
        if (total == 0) return null;
        int roll = (int) (Seeds.roll(w.seed, "life_kind", p.id(), Long.toString(day)) * total);
        for (var k : fits) { roll -= k.weight; if (roll < 0) return k; }
        return fits.getLast();
    }

    /** What they tell the player next time they talk, if the bond is deep enough: {@code life.<kind>}, once. */
    public static java.util.Optional<String> tell(BondWorld w, String who) {
        var b = w.bond(who);
        int level = w.effectiveLevel(who);
        for (int i = 0; i < b.news.size(); i++) {
            var n = b.news.get(i);
            if (n.shared() || level < n.kind().shareLevel) continue;
            b.news.set(i, n.told(w.day));
            return java.util.Optional.of("life." + n.kind().id());
        }
        return java.util.Optional.empty();
    }
    /**
     * The player responds to the news they were told most recently: "congratulate", "comfort", "help" or "shrug".
     * Returns "" or why not (nothing to respond to, or a response that does not fit).
     */
    public static String respond(BondWorld w, String who, String response) {
        var b = w.bond(who);
        for (int i = b.news.size() - 1; i >= 0; i--) {
            var n = b.news.get(i);
            if (!n.shared() || !n.response().isEmpty()) continue;
            int v = n.kind().valence;
            switch (response) {
                case "congratulate" -> {
                    if (v < 0) { w.act(who, Act.RUDE); break; }
                    w.act(who, Act.CELEBRATED_WITH_THEM);
                }
                case "comfort" -> {
                    if (v > 0) { w.addFriendship(who, .5); break; }
                    w.act(who, Act.COMFORTED);
                    if (w.effectiveLevel(who) >= MOMENT_LEVEL && v < 0) w.moment(who, "life." + n.kind().id() + "@" + n.day());
                    b.followUps.add(new Together.FollowUp("life." + n.kind().id() + ".update", w.day + 7 + (int) (Seeds.roll(w.seed, "update", who) * 7), false));
                }
                case "help" -> {
                    w.act(who, v < 0 ? Act.STOOD_BY_THEM : Act.CELEBRATED_WITH_THEM);
                    b.followUps.add(new Together.FollowUp("life." + n.kind().id() + ".update", w.day + 7, false));
                }
                case "shrug" -> { if (v < 0) w.act(who, Act.FELT_OVERLOOKED); }
                default -> { return "unknown_response"; }
            }
            b.news.set(i, n.answered(response));
            return "";
        }
        return "nothing_to_respond_to";
    }

    private LifeEvents() {}
}
