package dev.shinobi.life.bond;

import dev.shinobi.life.bond.Reaction.Source;
import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 * One player's bonds with the Leaf: the people, every bond, the squad, the deeds the village talks about and the
 * story flags the bond engine reads. Everything is a pure function of the save seed and what happens, so a save
 * replays the same way (ROADMAP.md: "Reproducible Varied saves"). The world glue calls the verbs below when things
 * happen and {@link #endDay()} once a day; quests reach it through {@link BondConditions} and {@link BondEffects}.
 */
public final class BondWorld {
    public static final String PLAYER = "player";
    /** VF's calendar: four seasons of 28 days. */
    public static final int YEAR = 112, DAILY_GIFTS = 3;
    /** A clan-born player is one of their own to their clan: a head start. */
    public static final double KIN_AFFECTION = 8, KIN_TRUST = 6;

    final long seed;
    long day;
    final Map<String, Person> people = new TreeMap<>();
    final Map<String, Bond> bonds = new TreeMap<>();
    final List<Deed> deeds = new ArrayList<>();
    int nextSerial = 1;
    final Set<String> flags = new TreeSet<>();
    Squad squad;
    Person.Stage playerStage = Person.Stage.CHILD;
    int playerRank = 0;
    String playerGender = "NON_BINARY", playerClan = "";
    final List<BondEvent> events = new ArrayList<>();
    private Map<String, Map<String, Double>> contacts;
    /** The village-scale society, when one is settled ({@link Village#settle}); without it gossip runs on circles. */
    Village village;
    /** Time together: hangouts planned, invitations residents sent the player, and when each last invited them. */
    final List<Together.Plan> plans = new ArrayList<>();
    final List<Together.Invitation> invitations = new ArrayList<>();
    final Map<String, Long> invitedOn = new TreeMap<>();
    int planSerial;
    /** Questions asked across everyone today (the daily budget). */
    int questionsToday, questionsDry;
    long questionsDay = -1;
    /** The questions residents can ask (content, loaded by the glue from the dialogue data; not saved). */
    final List<Question> questionBank = new ArrayList<>();

    public BondWorld(long seed, long day) { this.seed = seed; this.day = day; }

    // -- people and the player ---------------------------------------------------------------------

    public long seed() { return seed; }
    public Village village() { return village; }
    public long day() { return day; }
    public void add(Person p) { people.put(p.id(), p); contacts = null; }
    public Person person(String id) { return people.get(id); }
    public Collection<Person> people() { return List.copyOf(people.values()); }
    private Person need(String id) {
        var p = people.get(id);
        if (p == null) throw new IllegalArgumentException("nobody called " + id);
        return p;
    }
    public Person.Stage playerStage() { return playerStage; }
    public int playerRank() { return playerRank; }
    public String playerClan() { return playerClan; }
    public void player(String gender, String clan) { playerGender = gender; playerClan = clan == null ? "" : clan; }
    public void setPlayerStage(Person.Stage stage) { playerStage = stage; }
    /** Someone grows up (residents and cast grow alongside the player). */
    public void grow(String id, Person.Stage stage) { add(need(id).withStage(stage)); }
    public void setRank(String id, int rank) { add(need(id).withRank(rank)); }
    public boolean flag(String f) { return flags.contains(f); }
    public void setFlag(String f, boolean on) { if (on) flags.add(f); else flags.remove(f); }
    public Set<String> flags() { return Set.copyOf(flags); }
    public List<BondEvent> drainEvents() { var out = List.copyOf(events); events.clear(); return out; }
    private void event(String who, String kind, String detail) { events.add(new BondEvent(day, who, kind, detail)); }

    // -- reading bonds -----------------------------------------------------------------------------

    static String key(String from, String to) { return from + ">" + to; }
    public Bond bond(String who) { return bond(who, PLAYER); }
    public Bond bond(String from, String to) {
        need(from);
        if (!to.equals(PLAYER)) need(to);
        return bonds.computeIfAbsent(key(from, to), k -> new Bond(from, to));
    }
    public Collection<Bond> bonds() { return List.copyOf(bonds.values()); }
    public boolean knows(String who) { var b = bonds.get(key(who, PLAYER)); return b != null && b.met(); }

    /** How naturally {@code from} and {@code to} click, from -1 to 1 (the spark is the pair's, either way round). */
    public double chemistry(String from, String to) {
        String pair = from.compareTo(to) < 0 ? from + "|" + to : to + "|" + from;
        double spark = Seeds.roll(seed, "chemistry", pair) * 2 - 1;
        var q = to.equals(PLAYER) ? null : need(to).personality();
        return Personality.chemistry(spark, need(from).personality(), q);
    }
    public Meters meters(String who) { return meters(who, PLAYER); }
    /** The meters, computed from the bond's history (see {@link Bond}). */
    public Meters meters(String from, String to) {
        var b = bond(from, to); var p = need(from); var pp = p.personality();
        double chem = chemistry(from, to);
        double affection = (5 + 15 * chem) * (1 - Math.exp(-b.contactDays / 20.0)) + b.warmth + Bond.TOGETHER_RATE * b.together;
        double trust = 10 + 10 * pp.warmth() + 5 * pp.openness() + Math.min(15, .2 * b.contactDays);
        int theirRank = to.equals(PLAYER) ? playerRank : need(to).rank();
        int mine = Person.seniority(p.rank()), yours = Person.seniority(theirRank);
        double respect = Math.clamp(10 + 6 * yours - 4 * Math.max(0, mine - yours), 0, 60);
        boolean peers = p.shinobi() && (to.equals(PLAYER) || need(to).shinobi()) && mine == yours;
        double rivalry = peers ? 15 * Math.max(0, pp.pride()) + 5 * Math.max(0, pp.boldness()) : 0;
        if (p.family().containsKey(to)) { affection = Math.max(affection, 55); trust = Math.max(trust, 55); }
        if (to.equals(PLAYER) && !playerClan.isEmpty() && p.clan().equals(playerClan)) { affection += KIN_AFFECTION; trust += KIN_TRUST; }
        var m = new Meters(affection, trust, respect, rivalry, 0).plus(b.memoryWeight(day)).plus(b.conflict.weight());
        double romance = to.equals(PLAYER) && romanceOpen(from)
                ? Courtship.meter(Courtship.spark(seed, from, chem), b.teenSince < 0 ? 0 : day - b.teenSince, b.romanticMemories(day), m.clamped().affection()) : 0;
        return m.with(Meter.ROMANCE, romance).clamped();
    }
    public double closeness(String who) { return Levels.closeness(meters(who)); }
    public int level(String who) { var b = bonds.get(key(who, PLAYER)); return b == null ? 0 : b.level; }
    /** The level they act on: their level, lowered while a quarrel lasts. */
    public int effectiveLevel(String who) { return effectiveLevel(who, PLAYER); }
    public int effectiveLevel(String from, String to) { var b = bonds.get(key(from, to)); return b == null ? 0 : b.conflict.cap(b.level); }
    /** Which story gate holds this bond back ("experience", "moment", "time") or "". */
    public String gate(String who) {
        var b = bond(who);
        if (Levels.byPoints(closeness(who)) <= b.level) return "";
        return Levels.gate(b.experiences(), b.moments.size(), b.contactDays, b.level);
    }
    public boolean romanceOpen(String who) {
        var p = need(who); var b = bond(who);
        return Courtship.eligible(p, playerStage, playerGender, p.family().containsKey(PLAYER), b.conflict);
    }

    // -- what the player does ----------------------------------------------------------------------

    /** A conversation: warmth once a day. Returns false when they already talked today. */
    public boolean talk(String who) {
        var b = bond(who);
        if (b.talkDay == day) return false;
        b.talkDay = day; b.contact(day);
        b.warm(Act.TALK.warmth, b.conflict.warmthLet());
        favor(who, 1);
        rise(b);
        return true;
    }
    /** A gift: "loved", "liked", "plain", "disliked", "hated", or "limit" after three today. */
    public String gift(String who, String item) {
        var b = bond(who); var p = need(who);
        if (b.giftDay != day) { b.giftDay = day; b.giftsToday = 0; }
        if (b.giftsToday >= DAILY_GIFTS) return "limit";
        b.giftsToday++;
        String taste = p.personality().taste(item);
        Act act = switch (taste) { case "loved" -> Act.GIFT_LOVED; case "liked" -> Act.GIFT_LIKED; case "disliked" -> Act.GIFT_DISLIKED; case "hated" -> Act.GIFT_HATED; default -> Act.GIFT_PLAIN; };
        double variety = !b.lastGift.isEmpty() && !b.lastGift.equals(item) && act.warmth > 0 ? .5 : 0;
        b.lastGift = item; b.contact(day);
        b.warm(act.warmth + variety, b.conflict.warmthLet());
        if (act.remembered()) apply(who, act, Source.SELF, "", null, List.of(), false);
        favor(who, 2);
        rise(b);
        return taste;
    }
    /** {@code add_friendship}: warmth points, as a quest reward. */
    public void addFriendship(String who, double points) { var b = bond(who); b.contact(day); b.warm(points, b.conflict.warmthLet()); rise(b); }
    /** Attention for favoritism: picking someone as your partner, praising them, a meal for two. */
    public void favor(String who, double amount) { if (squad != null) squad.favor(who, amount); }
    /** A day spent side by side with someone (lessons, a shift, a mission). */
    public void together(String who) { bond(who).together(day); }

    public Meters act(String who, Act act) { return apply(who, act, Source.SELF, "", null, List.of(), true); }
    /** An act the people in {@code witnesses} saw: a deed spreads from them; a private act they only remember. */
    public Meters act(String who, Act act, Collection<String> witnesses) { return apply(who, act, Source.SELF, "", null, witnesses, true); }
    /** A bond quest's heart scene: a moment the gates count, under the quest's id. */
    public void moment(String who, String id) {
        if (bond(who).moments.contains(id)) return;
        apply(who, Act.BOND_MOMENT, Source.SELF, "", id, List.of(), true);
    }
    /** The player with a group: a mission, a camp night, a lesson. Squadmates also grow toward each other. */
    public void experience(Act act, Collection<String> group) {
        var list = List.copyOf(group);
        for (String who : list) { together(who); act(who, act); }
        for (String a : list) for (String b : list) if (!a.equals(b)) { bond(a, b).together(day); npcAct(a, b, act); }
        if (squad != null && act == Act.MISSION_TOGETHER && list.stream().anyMatch(squad::has)) squad.missions++;
    }
    /** How one resident's feelings toward another move (squadmates, family). */
    public Meters npcAct(String from, String to, Act act) {
        var b = bond(from, to); var p = need(from);
        b.contact(day);
        var delta = Reaction.react(p.personality(), act).with(Meter.ROMANCE, 0);
        b.remember(act, delta, Source.SELF, "", day);
        if (act.moment) b.moments.add(act.id() + "@" + day);
        hurt(b, p, act, delta, from + ">" + to);
        rise(b);
        return delta;
    }
    public void reveal(String who, String fact) { bond(who).facts.add(fact); }
    /** Kindling Bond was used with someone: what was granted (nothing if the tier is none), and the use counted for the master's trial. */
    public Kindling.Grant kindle(String who) {
        var tier = Kindling.tier(this, who);
        if (tier == Kindling.Tier.NONE) return Kindling.grant(tier);
        bond(who).kindled++;
        return Kindling.grant(tier, who.equals(spouse()));
    }
    public void setBondFlag(String who, String f) { bond(who).flags.add(f); }

    /** A change worked out elsewhere (an answer to a question), remembered as {@code act}: contact, memory, a possible quarrel, a level-up. */
    Meters applyDelta(String who, Act act, Meters delta) {
        var p = need(who); var b = bond(who);
        b.contact(day);
        var d = romanceOpen(who) ? delta : delta.with(Meter.ROMANCE, 0);
        b.remember(act, d, Source.SELF, "", day);
        hurt(b, p, act, d, who);
        rise(b);
        return d;
    }
    /** Times the engine had a question budget for someone but nothing left to ask them (the bank is too small). */
    public int questionsDry() { return questionsDry; }

    /** Something they feel about the player without the player being there (overlooked, let down). */
    void npcFelt(String who, Act act) { apply(who, act, Source.SELF, "", null, List.of(), false); }

    private Meters apply(String who, Act act, Source how, String about, String momentId, Collection<String> witnesses, boolean contact) {
        var p = need(who); var b = bond(who);
        if (act.romantic && !romanceOpen(who)) return Meters.ZERO;
        if (contact) b.contact(day); else b.meet(day);
        var delta = Reaction.react(p.personality(), act);
        if (!romanceOpen(who)) delta = delta.with(Meter.ROMANCE, 0);
        b.remember(act, delta, how, about, day);
        if (act.moment) b.moments.add(momentId != null ? momentId : act.id() + "@" + day);
        hurt(b, p, act, delta, who);
        if (act.spreads) deed(act, who, witnesses);
        rise(b);
        return delta;
    }
    /** A level earned shows at once (a level-up in the middle of a conversation); falling waits for the end of the day. */
    private void rise(Bond b) {
        int cap = Levels.cap(b.experiences(), b.moments.size(), b.contactDays);
        int next = Math.min(Levels.byPoints(Levels.closeness(meters(b.from, b.to))), cap);
        if (next > b.level) { b.level = next; event(b.to.equals(PLAYER) ? b.from : b.from + ">" + b.to, "level_up", Integer.toString(next)); }
    }
    private void hurt(Bond b, Person p, Act act, Meters delta, String who) {
        if (delta.sumOfLosses() >= 0 || !Conflict.triggers(act, delta, p.personality())) return;
        var before = b.conflict.state();
        b.conflict = b.conflict.hurt(act, Conflict.severity(delta, p.personality()), p.personality(), day);
        if (b.conflict.state() != before) event(who, "conflict", b.conflict.state().id() + " (" + act.id() + ")");
    }

    // -- quarrels ----------------------------------------------------------------------------------

    /** Says sorry. True when they accept (trust 40 or more, or three days have passed); it halves the cold shoulder. */
    public boolean apologize(String who) {
        var b = bond(who);
        if (!b.conflict.apologyAccepted(meters(who).trust(), day)) { event(who, "apology", "cool"); return false; }
        b.conflict = b.conflict.apologized(day);
        act(who, Act.APOLOGIZED);
        event(who, "apology", "accepted");
        return true;
    }
    /** The reconciliation quest's end: only once they are ready to make up. */
    public boolean reconcile(String who) {
        var b = bond(who);
        if (!b.conflict.canReconcile()) return false;
        b.conflict = Conflict.NONE;
        act(who, Act.RECONCILED);
        event(who, "reconciled", "");
        return true;
    }
    /** The story mends even a falling-out ({@code mend} effect). */
    public void mend(String who) {
        var b = bond(who);
        if (b.conflict.state() == Conflict.State.NONE) return;
        b.conflict = Conflict.NONE;
        act(who, Act.RECONCILED);
        event(who, "reconciled", "mended");
    }
    public void quarrel(String who, Act cause) { act(who, cause == null ? Act.QUARREL : cause); }

    // -- romance -----------------------------------------------------------------------------------

    /** The player's move in a courtship ({@link Courtship#refuse}). "" when it worked, otherwise the reason. */
    public String court(String who, String move) {
        var b = bond(who);
        if (!romanceOpen(who)) return "not_eligible";
        boolean elsewhere = bonds.values().stream().anyMatch(o -> o.to.equals(PLAYER) && !o.from.equals(who) && o.romance.committed());
        String why = Courtship.refuse(move, b.romance, meters(who).romance(), effectiveLevel(who), playerStage, b.romanceSince < 0 ? 0 : day - b.romanceSince, elsewhere);
        if (!why.isEmpty()) return why;
        b.romance = Courtship.after(move); b.romanceSince = day;
        act(who, switch (move) { case "ask_out" -> Act.DATE; case "confess" -> Act.CONFESSION_ACCEPTED; case "propose" -> Act.PROPOSAL_ACCEPTED; default -> Act.WEDDING; });
        event(who, "romance", b.romance.id());
        return "";
    }
    public String spouse() {
        return bonds.values().stream().filter(b -> b.to.equals(PLAYER) && b.romance == Courtship.Stage.MARRIED).map(b -> b.from).findFirst().orElse("");
    }

    // -- birthdays ---------------------------------------------------------------------------------

    public static int dayOfYear(long day) { return (int) Math.floorMod(day, YEAR); }
    public boolean birthday(String who) { return need(who).birthday() == dayOfYear(day); }
    /** Wishing them a happy birthday (on the day). */
    public boolean celebrate(String who) {
        var b = bond(who);
        String f = "birthday:" + day / YEAR;
        if (!birthday(who) || b.flags.contains(f)) return false;
        b.flags.add(f);
        act(who, Act.BIRTHDAY_REMEMBERED);
        return true;
    }

    // -- deeds and gossip --------------------------------------------------------------------------

    public List<Deed> deeds() { return List.copyOf(deeds); }
    public Deed deedOf(int serial) { return deeds.stream().filter(d -> d.serial == serial).findFirst().orElse(null); }
    /** A deed: whoever it was about lived it, the witnesses saw it, and from them word spreads. */
    public Deed deed(Act act, String about, Collection<String> witnesses) {
        var d = new Deed(nextSerial++, act, day, about);
        deeds.add(d);
        if (village != null) village.onDeed(d);
        if (about != null && !about.isEmpty() && people.containsKey(about)) d.knowers.put(about, new Deed.Know(Source.SELF, day, ""));
        for (String w : witnesses) if (!d.knows(w) && people.containsKey(w)) { d.knowers.put(w, new Deed.Know(Source.SEEN, day, "")); absorb(w, d); }
        return d;
    }
    /** The player tells someone about a deed. False when they had already heard (word got there first). */
    public boolean tell(String who, int serial) {
        var d = deedOf(serial);
        if (d == null || d.knows(who)) { event(who, "heard", "already"); return false; }
        d.knowers.put(who, new Deed.Know(Source.TOLD, day, PLAYER));
        absorb(who, d);
        bond(who).contact(day);
        return true;
    }
    /** What learning of a deed does to how someone feels about the player. */
    private void absorb(String listener, Deed d) {
        if (listener.equals(d.about) || listener.equals(PLAYER)) return;
        var k = d.know(listener); var p = need(listener);
        double close = d.about.isEmpty() ? .3 : p.family().containsKey(d.about) ? 1 : effectiveLevel(listener, d.about) / 10.0;
        var delta = Reaction.secondhand(p.personality(), d.act, k.how(), close);
        if (k.how() == Source.TOLD && !d.good()) delta = delta.losses(.6).plus(Meter.TRUST, 2);
        if (k.slant() != 0) delta = Gossip.slanted(delta, k.slant());
        var b = bond(listener);
        b.meet(day);
        b.remember(d.act, delta, k.how(), d.about, day);
        if (close >= .6) hurt(b, p, d.act, delta, listener);
    }
    /** Who each person talks to, and how closely: shared circles, clan, district and family. */
    Map<String, Double> contacts(String id) {
        if (village != null) return village.contacts(id);
        if (contacts == null) {
            var circles = new TreeMap<String, List<String>>();
            for (var p : people.values()) for (String c : circlesOf(p)) circles.computeIfAbsent(c, k -> new ArrayList<>()).add(p.id());
            contacts = new TreeMap<>();
            for (var p : people.values()) {
                var mine = new TreeMap<String, Double>();
                for (String c : circlesOf(p)) {
                    var members = circles.get(c);
                    for (String other : members)
                        if (!other.equals(p.id()) && Gossip.talks(seed, c, p.id(), other, members.size())) mine.merge(other, Gossip.closeness(c), Math::max);
                }
                for (String kin : p.family().keySet()) if (people.containsKey(kin)) mine.merge(kin, Gossip.closeness("family"), Math::max);
                contacts.put(p.id(), mine);
            }
        }
        return contacts.getOrDefault(id, Map.of());
    }
    private static List<String> circlesOf(Person p) {
        var list = new ArrayList<>(p.circles());
        if (!p.clan().isEmpty()) list.add("clan:" + p.clan());
        if (!p.district().isEmpty()) list.add("district:" + p.district());
        return list;
    }
    public double standing(String community) { return Standing.score(this, community); }
    public Standing.Title title(String community) { return Standing.title(this, community); }
    /** A promotion: everyone who saw it respects it, and word spreads. */
    public void promote(int rank, Collection<String> witnesses) {
        if (rank <= playerRank) return;
        playerRank = rank;
        deed(Act.RANK_UP, "", witnesses);
    }

    // -- the squad ---------------------------------------------------------------------------------

    public Squad squad() { return squad; }
    public Squad formSquad(String id, String sensei, List<String> teammates, List<String> bench) {
        squad = new Squad(id, sensei, teammates, bench, day);
        return squad;
    }
    public double cohesion() {
        if (squad == null) return 0;
        var members = squad.members();
        double trust = 0, affection = 0; int n = 0, quarrels = 0;
        for (String m : members) {
            var targets = new ArrayList<String>(); targets.add(PLAYER);
            for (String o : members) if (!o.equals(m)) targets.add(o);
            for (String t : targets) {
                var meters = meters(m, t); trust += meters.trust(); affection += meters.affection(); n++;
                if (bond(m, t).conflict.active()) quarrels++;
            }
        }
        double jealousy = squad.teammates.stream().mapToDouble(squad::jealousy).average().orElse(0);
        return Squad.cohesion(n == 0 ? 0 : trust / n, n == 0 ? 0 : affection / n, squad.missions, jealousy, quarrels);
    }
    /** {@code remove_from_squad}: the story, a failed exam or a falling-out takes a teammate away. */
    public String leaveSquad(String who, String reason) {
        if (squad == null) return "";
        String replacement = squad.leave(who, reason, day);
        event(who, "left_squad", reason + (replacement.isEmpty() ? "" : ", replaced by " + replacement));
        return replacement;
    }
    /** Whether a teammate who left can come back: their bond is at level 4 again, with no quarrel. Story departures come back only by the story. */
    public boolean canReturn(String who) {
        if (squad == null) return false;
        var d = squad.departed.get(who);
        return d != null && !d.reason().equals("story") && effectiveLevel(who) >= Squad.RETURN_LEVEL && !bond(who).conflict.active() && !bond(who).conflict.broken();
    }
    /** {@code return_to_squad}. */
    public boolean returnToSquad(String who) {
        if (squad == null || !squad.rejoin(who)) return false;
        bond(who).lowDays = 0;
        event(who, "rejoined", "");
        return true;
    }

    // -- time --------------------------------------------------------------------------------------

    /** The end of a day: birthdays, gossip, the squad, then every bond's quarrel, courtship and level. */
    public void endDay() {
        birthdays();
        for (var d : List.copyOf(deeds)) for (String heard : Gossip.spread(this, d, day)) absorb(heard, d);
        squadDay();
        boolean weekly = Math.floorMod(day, Village.WEEK) == Village.WEEK - 1;
        for (var b : List.copyOf(bonds.values())) {
            // Someone who has only heard of you is a background bond: looked at once a week.
            if (!b.met() && !weekly && b.conflict.state() == Conflict.State.NONE) continue;
            b.neglect(day); b.prune(day);
            var before = b.conflict.state();
            b.conflict = b.conflict.tick(day);
            if (b.conflict.state() != before) event(b.from + (b.to.equals(PLAYER) ? "" : ">" + b.to), "conflict", b.conflict.state().id());
            if (b.to.equals(PLAYER)) courtship(b);
            updateLevel(b, 1);
        }
        Together.daily(this);
        LifeEvents.daily(this);
        if (village != null) village.endDay();
        day++;
    }
    public void advance(int days) { for (int i = 0; i < days; i++) endDay(); }

    private void birthdays() {
        int today = dayOfYear(day);
        for (var b : List.copyOf(bonds.values())) {
            if (!b.to.equals(PLAYER) || !b.met()) continue;
            var p = people.get(b.from);
            String f = "birthday:" + day / YEAR;
            if (p.birthday() != today || b.flags.contains(f) || effectiveLevel(b.from) < Levels.FRIEND) continue;
            b.flags.add(f);
            apply(b.from, Act.MISSED_BIRTHDAY, Source.SELF, "", null, List.of(), false);
            event(b.from, "birthday_missed", "");
        }
    }
    private void courtship(Bond b) {
        if (!romanceOpen(b.from)) { if (!b.romance.committed()) b.romance = Courtship.Stage.NONE; return; }
        if (b.teenSince < 0) b.teenSince = day;
        var next = Courtship.drift(b.romance, meters(b.from).romance(), b.level);
        if (next != b.romance) { b.romance = next; b.romanceSince = day; event(b.from, "romance", next.id()); }
    }
    private void updateLevel(Bond b, int maxSteps) {
        for (int step = 0; step < maxSteps; step++) {
            double c = Levels.closeness(meters(b.from, b.to));
            int cap = Levels.cap(b.experiences(), b.moments.size(), b.contactDays);
            int next = Math.max(b.floor, Levels.next(b.level, c, cap));
            String who = b.to.equals(PLAYER) ? b.from : b.from + ">" + b.to;
            if (next > b.level) event(who, "level_up", Integer.toString(next));
            else if (next < b.level) event(who, "level_down", Integer.toString(next));
            else {
                if (Levels.byPoints(c) > b.level && b.to.equals(PLAYER) && b.flags.add("gated:" + b.level))
                    event(who, "gated", Levels.gate(b.experiences(), b.moments.size(), b.contactDays, b.level));
                return;
            }
            b.level = next;
        }
    }
    private void squadDay() {
        if (squad == null) return;
        var team = squad.teammates;
        double total = 0;
        for (String t : team) total += squad.attention(t);
        String favorite = squad.favorite();
        for (String t : List.copyOf(team)) {
            double j = squad.jealousy(t);
            j = total >= Squad.MIN_ATTENTION && team.size() > 1
                    ? Squad.jealousy(j, squad.attention(t) / total, team.size(), need(t).personality().pride()) : j * .85;
            if (j >= Squad.JEALOUS && !squad.overlooked.getOrDefault(t, false)) {
                squad.overlooked.put(t, true);
                apply(t, Act.FELT_OVERLOOKED, Source.SELF, "", null, List.of(), false);
                if (!favorite.isEmpty() && !favorite.equals(t)) npcAct(t, favorite, Act.FELT_OVERLOOKED);
                event(t, "jealous", favorite);
            }
            if (j < Squad.JEALOUS / 2) squad.overlooked.put(t, false);
            if (j >= Squad.BOILS && !bond(t).conflict.active()) { apply(t, Act.QUARREL, Source.SELF, "", null, List.of(), false); j = Squad.JEALOUS - 5; }
            squad.jealousy.put(t, j);
        }
        for (String t : team) squad.attention.put(t, Squad.fadeAttention(squad.attention(t)));
        if (day - squad.formed < Squad.GRACE_DAYS) return;
        boolean recent = squad.departed.values().stream().anyMatch(d -> day - d.day() < Squad.LOW_DAYS);
        for (String t : List.copyOf(team)) {
            var b = bond(t);
            boolean low = effectiveLevel(t) <= Squad.LOW_LEVEL || meters(t).trust() < Squad.LOW_TRUST || b.conflict.broken();
            int days = low ? squad.lowDays.merge(t, 1, Integer::sum) : 0;
            if (!low) squad.lowDays.put(t, 0);
            if (days >= Squad.LOW_DAYS && !recent && !squad.bench.isEmpty()) { leaveSquad(t, "low_bond"); recent = true; }
        }
    }

    /**
     * A time skip of {@code days}: memories age and quarrels run their course; {@code companions} (the squad, a
     * spouse) were together all along, and everyone else the player was friendly with crossed paths now and then.
     * Levels then settle, falling at most one level for every four weeks skipped.
     */
    public void timeSkip(int days, Collection<String> companions) {
        var with = new TreeSet<>(companions);
        for (int i = 0; i < days; i++) {
            for (var b : bonds.values()) {
                if (!with.contains(b.from)) b.neglect(day);
                b.conflict = b.conflict.tick(day);
            }
            day++;
        }
        for (var b : List.copyOf(bonds.values())) {
            if (!b.met()) continue;
            if (with.contains(b.from) && (b.to.equals(PLAYER) || with.contains(b.to))) {
                b.contactDays += days / 4; b.together = Math.min(Bond.TOGETHER_CAP, b.together + days / 4); b.lastContact = day; b.lastTogether = day;
                if (b.to.equals(PLAYER) && days >= 100) apply(b.from, Act.YEARS_TOGETHER, Source.SELF, "", null, List.of(), false);
            } else if (b.to.equals(PLAYER) && b.level >= Levels.NEWS) {
                b.contactDays += days / 28; b.lastContact = day;
            }
            b.prune(day);
        }
        for (var b : List.copyOf(bonds.values())) {
            if (b.to.equals(PLAYER)) courtship(b);
            int down = Math.max(1, days / 28);
            int before = b.level;
            updateLevel(b, Levels.MAX);
            if (b.level < before - down) b.level = Math.max(b.floor, before - down);
        }
    }

    /** Everyone in a role group, for quest data: {@code role:squad} (teammates and sensei), {@code role:teammates}, or one id. */
    public List<String> resolve(String ref) {
        if (ref.equals("role:squad")) return squad == null ? List.of() : squad.members();
        if (ref.equals("role:teammates")) return squad == null ? List.of() : squad.teammates();
        if (ref.equals("role:sensei")) return squad != null && squad.sensei != null ? List.of(squad.sensei) : people.containsKey(ref) ? List.of(ref) : List.of();
        return people.containsKey(ref) ? List.of(ref) : List.of();
    }
    /** The bonded people, highest level first (the bond book's index). */
    public List<String> bonded() {
        var order = new LinkedHashMap<String, Integer>();
        bonds.values().stream().filter(b -> b.to.equals(PLAYER) && b.met())
                .sorted((x, y) -> x.level != y.level ? Integer.compare(y.level, x.level) : x.from.compareTo(y.from))
                .forEach(b -> order.put(b.from, b.level));
        return List.copyOf(order.keySet());
    }
}
