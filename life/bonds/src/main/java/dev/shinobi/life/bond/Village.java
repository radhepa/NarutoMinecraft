package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 * The Leaf at village scale: about 300 residents, 25 clans and the civilian districts, where VF's every-pair meters
 * (some 45,000 pairs) would not work. Instead:
 *
 * <ul>
 * <li><b>A sparse social graph.</b> Each resident has a bounded set of real {@link SocialTie}s (family, household,
 * squad, class, coworkers, a few clanmates and neighbors, friends, rivals, a sweetheart or spouse); at most
 * {@link #CHOSEN_TIES} chosen ones. Everyone else is derived on demand ({@link #affinity}) from their clans'
 * relation, their district and their chemistry.</li>
 * <li><b>Clans as structures</b> ({@link House}): a head, elders, an heir, a main and branch house where the clan has
 * one, households in the quarter; {@link ClanProfile} values and customs shape members; {@link ClanRelations} is the
 * inter-clan matrix that drifts with events.</li>
 * <li><b>Simulation tiers</b> ({@link Tier}): the bound cast and the residents the player knows are updated every day;
 * background residents once a week, coarsely. Meeting someone promotes them to known.</li>
 * <li><b>Village-scale dynamics:</b> moods per community ({@link Mood}), quarrels, friendships, crushes and
 * marriages forming (with each clan's pressure to marry in), clan incidents, and the {@link SocietyHook}s they
 * raise for side quests.</li>
 * </ul>
 */
public final class Village {
    public enum Tier { CAST, KNOWN, BACKGROUND }
    /** A clan's structure: head, heir, elders, the branch house (where there is one) and the households in the quarter. */
    public record House(String clan, String head, String heir, List<String> elders, Set<String> branch, Map<String, List<String>> households) {}

    public static final int CHOSEN_TIES = 8, CLANMATES = 2, NEIGHBORS = 3, WEEK = 7, OPEN_HOOKS = 16, HOOKS_PER_TYPE = 4;
    public static final double FRIEND_CHANCE = .15, QUARREL_CHANCE = .006, INCIDENT_CHANCE = .3, CRUSH_AFFINITY = 40, SWEETHEART_AFFINITY = 55,
            MARRY_AFFINITY = 65;
    public static final int COURTSHIP_DAYS = 56;

    final BondWorld w;
    final Map<String, SocialTie> ties = new TreeMap<>();
    final Map<String, Set<String>> adjacency = new TreeMap<>();
    final Map<String, House> clans = new TreeMap<>();
    final ClanRelations relations = new ClanRelations();
    final Map<String, Mood> moods = new TreeMap<>();
    final List<SocietyHook> hooks = new ArrayList<>();
    final Map<String, Integer> raised = new TreeMap<>(), resolved = new TreeMap<>();
    int hookSerial;
    /** Work done: resident and tie updates, for the performance report. */
    long updates;

    private Village(BondWorld w) { this.w = w; }

    /** Builds the village's structure and first ties from the people in the world, and attaches it. */
    public static Village settle(BondWorld w) {
        var v = new Village(w);
        v.buildClans();
        v.buildTies();
        w.village = v;
        return v;
    }

    // -- reading -----------------------------------------------------------------------------------

    public ClanRelations relations() { return relations; }
    public House house(String clan) { return clans.get(clan); }
    public Collection<House> houses() { return List.copyOf(clans.values()); }
    public SocialTie tie(String a, String b) { return ties.get(ClanRelations.pair(a, b)); }
    public Set<String> tiesOf(String id) { return Set.copyOf(adjacency.getOrDefault(id, Set.of())); }
    public int tieCount() { return ties.size(); }
    public Map<String, Integer> tieKinds() {
        var m = new TreeMap<String, Integer>();
        for (var t : ties.values()) m.merge(t.kind(), 1, Integer::sum);
        return m;
    }
    public long updates() { return updates; }
    public Tier tier(String id) { return id.startsWith("role:") ? Tier.CAST : w.knows(id) ? Tier.KNOWN : Tier.BACKGROUND; }
    public Mood mood(String community) { return moods.getOrDefault(community, Mood.CALM); }
    public List<SocietyHook> hooks() { return List.copyOf(hooks); }
    public Map<String, Integer> raisedByType() { return Map.copyOf(raised); }
    public int raisedTotal() { return raised.values().stream().mapToInt(Integer::intValue).sum(); }
    String groupOf(String id) { return ClanRelations.groupOf(w.person(id)); }

    /** How {@code a} feels about {@code b}: from their tie (VF's formula) or, with none, from clans, district and chemistry. */
    public double affinity(String a, String b) {
        if (a.equals(b)) return 100;
        var pa = w.person(a); var pb = w.person(b);
        double chem = w.chemistry(a, b), rel = relations.get(groupOf(a), groupOf(b));
        var t = tie(a, b);
        if (t == null) return Math.clamp(rel * .3 + chem * 10 + (pa.district().equals(pb.district()) ? 5 : 0), -60, 60);
        double target = switch (t.kind()) {
            case "spouse" -> 88;
            case "sweetheart" -> 80;
            case "family", "household" -> 60 + chem * 15;
            default -> Math.clamp(14 + chem * 50 + (groupOf(a).equals(groupOf(b)) ? 0 : rel * .15), -45, 80);
        };
        boolean close = t.kind().equals("family") || t.kind().equals("household") || t.kind().equals("spouse");
        double start = close ? target : 3, growth = 1 - Math.exp(-Math.max(0, w.day - t.since()) / 40.0);
        double penalty = t.quarrel() >= 0 && w.day >= t.quarrel() ? Math.max(0, 30 - (w.day - t.quarrel())) : 0;
        return Math.clamp(start + (target - start) * growth + t.together() * .5 - penalty, -100, 100);
    }
    /** Who someone passes news to, and how readily: their ties, slower across clans that dislike each other. */
    Map<String, Double> contacts(String id) {
        if (contactsDay != w.day) { contactCache.clear(); contactsDay = w.day; }
        return contactCache.computeIfAbsent(id, this::computeContacts);
    }
    private final Map<String, Map<String, Double>> contactCache = new java.util.HashMap<>();
    private long contactsDay = Long.MIN_VALUE;
    private Map<String, Double> computeContacts(String id) {
        var out = new TreeMap<String, Double>();
        String g = groupOf(id);
        for (String other : adjacency.getOrDefault(id, Set.of())) {
            var t = tie(id, other);
            String h = groupOf(other);
            double across = g.equals(h) ? 1 : 1 + relations.get(g, h) / 200;
            out.put(other, t.closeness() * across);
        }
        return out;
    }

    // -- building ----------------------------------------------------------------------------------

    private void buildClans() {
        var byClan = new TreeMap<String, List<Person>>();
        for (var p : w.people.values()) if (!p.clan().isEmpty() && ClanProfile.known(p.clan())) byClan.computeIfAbsent(p.clan(), k -> new ArrayList<>()).add(p);
        for (var e : byClan.entrySet()) {
            var profile = ClanProfile.of(e.getKey());
            var adults = e.getValue().stream().filter(p -> p.stage() == Person.Stage.ADULT)
                    .sorted((x, y) -> x.rank() != y.rank() ? Integer.compare(y.rank(), x.rank())
                            : Double.compare(Seeds.roll(w.seed, "clan_order", x.id()), Seeds.roll(w.seed, "clan_order", y.id()))).toList();
            if (adults.isEmpty()) continue;
            String head = adults.getFirst().id();
            var elders = adults.stream().skip(1).limit(profile.elders()).map(Person::id).toList();
            String heir = adults.getFirst().family().entrySet().stream().filter(k -> k.getValue().equals("child") && w.people.containsKey(k.getKey()))
                    .map(Map.Entry::getKey).sorted().findFirst()
                    .orElse(e.getValue().stream().map(Person::id).filter(id -> !id.equals(head) && !elders.contains(id)).reduce((a, b) -> b).orElse(""));
            var branch = new TreeSet<String>();
            if (profile.branchHouse()) for (var p : e.getValue())
                if (!p.id().equals(head) && !p.id().equals(heir) && !elders.contains(p.id()) && Seeds.roll(w.seed, "branch", p.id()) < .6) branch.add(p.id());
            clans.put(e.getKey(), new House(e.getKey(), head, heir, elders, branch, households(e.getValue())));
        }
    }
    /** Households: people joined by family or a shared household circle, named by their first member. */
    private Map<String, List<String>> households(List<Person> members) {
        var parent = new TreeMap<String, String>();
        for (var p : members) parent.put(p.id(), p.id());
        for (var p : members) {
            for (String kin : p.family().keySet()) if (parent.containsKey(kin)) union(parent, p.id(), kin);
            for (var q : members) if (p.circles().stream().anyMatch(c -> c.startsWith("household:") && q.circles().contains(c))) union(parent, p.id(), q.id());
        }
        var out = new TreeMap<String, List<String>>();
        for (var p : members) out.computeIfAbsent(find(parent, p.id()), k -> new ArrayList<>()).add(p.id());
        return out;
    }
    private static String find(Map<String, String> parent, String x) { while (!parent.get(x).equals(x)) x = parent.get(x); return x; }
    private static void union(Map<String, String> parent, String a, String b) {
        String ra = find(parent, a), rb = find(parent, b);
        if (!ra.equals(rb)) parent.put(ra.compareTo(rb) < 0 ? rb : ra, ra.compareTo(rb) < 0 ? ra : rb);
    }
    private void buildTies() {
        var circles = new TreeMap<String, List<String>>(); var districts = new TreeMap<String, List<String>>();
        for (var p : w.people.values()) {
            for (var kin : p.family().entrySet()) if (w.people.containsKey(kin.getKey())) link(p.id(), kin.getKey(), kin.getValue().equals("spouse") ? "spouse" : "family");
            for (String c : p.circles()) if (c.contains(":")) circles.computeIfAbsent(c, k -> new ArrayList<>()).add(p.id());
            if (!p.district().isEmpty()) districts.computeIfAbsent(p.district(), k -> new ArrayList<>()).add(p.id());
        }
        for (var e : circles.entrySet()) {
            String kind = e.getKey().substring(0, e.getKey().indexOf(':'));
            if (!List.of("household", "squad", "class", "work").contains(kind)) continue;
            var members = e.getValue();
            for (int i = 0; i < members.size(); i++) for (int j = i + 1; j < members.size(); j++)
                if (members.size() <= 8 || Gossip.talks(w.seed, e.getKey(), members.get(i), members.get(j), members.size())) link(members.get(i), members.get(j), kind);
        }
        for (var house : clans.values()) {
            var members = w.people.values().stream().filter(p -> p.clan().equals(house.clan())).map(Person::id).toList();
            for (String m : members) {
                if (!m.equals(house.head())) link(m, house.head(), "clan");
                for (String o : members) if (m.compareTo(o) < 0 && Seeds.roll(w.seed, "clanmates", m, o) < (double) CLANMATES / Math.max(1, members.size() - 1)) link(m, o, "clan");
            }
        }
        for (var e : districts.entrySet()) {
            var members = e.getValue();
            for (int i = 0; i < members.size(); i++) for (int j = i + 1; j < members.size(); j++)
                if (Seeds.roll(w.seed, "neighbors", members.get(i), members.get(j)) < (double) NEIGHBORS / Math.max(1, members.size() - 1)
                        && chosen(members.get(i)) < CHOSEN_TIES && chosen(members.get(j)) < CHOSEN_TIES) link(members.get(i), members.get(j), "neighbor");
        }
    }
    /** Adds a tie (or upgrades its kind toward the closer one) and returns it. Known since a while back. */
    SocialTie link(String a, String b, String kind) {
        if (a.equals(b)) return null;
        String key = ClanRelations.pair(a, b);
        var old = ties.get(key);
        long since = w.day - 30 - (long) (Seeds.roll(w.seed, "known", key) * 400);
        var t = old == null ? SocialTie.of(kind, since) : SocialTie.rank(kind) < SocialTie.rank(old.kind()) ? old.kind(kind, w.day) : old;
        ties.put(key, t);
        contactCache.remove(a); contactCache.remove(b);
        adjacency.computeIfAbsent(a, k -> new TreeSet<>()).add(b);
        adjacency.computeIfAbsent(b, k -> new TreeSet<>()).add(a);
        return t;
    }
    private int chosen(String id) {
        int n = 0;
        for (String o : adjacency.getOrDefault(id, Set.of())) if (tie(id, o).chosen()) n++;
        return n;
    }

    // -- events from the bond engine ---------------------------------------------------------------

    /** A deed moves moods: big good news cheers the village, harm makes its district and clan uneasy. */
    void onDeed(Deed d) {
        if (d.act.worth >= 10) push("village", .2 * d.act.worth / 10, 0);
        if (d.act.worth < 0 && !d.about.isEmpty() && w.people.containsKey(d.about)) {
            var p = w.person(d.about);
            push("district:" + p.district(), -.1, .2);
            if (!p.clan().isEmpty()) push("clan:" + p.clan(), -.1, .2);
        }
    }
    public void push(String community, double cheer, double tension) { moods.put(community, mood(community).push(cheer, tension)); }
    /** The player meets someone: they are known from now on and their ties update daily. */
    public void meet(String id) { w.bond(id).contact(w.day); }

    // -- time --------------------------------------------------------------------------------------

    /** Called from {@link BondWorld#endDay()}: daily for the cast and the known, weekly (coarsely) for everyone else. */
    void endDay() {
        long day = w.day;
        for (var e : List.copyOf(ties.entrySet())) {
            var t = e.getValue();
            if (!SocialTie.DAILY.contains(t.kind())) continue;
            String[] ab = e.getKey().split("\\|");
            if (tier(ab[0]) == Tier.BACKGROUND && tier(ab[1]) == Tier.BACKGROUND) continue;
            ties.put(e.getKey(), t.together(day)); updates++;
        }
        for (var e : List.copyOf(moods.entrySet())) { var m = e.getValue().eased(); if (m.settled()) moods.remove(e.getKey()); else moods.put(e.getKey(), m); }
        hooks.removeIf(h -> !h.open(day) || h.type().equals("quarrel_to_mediate") && healed(h));
        week(Math.floorMod(day, WEEK));
        if (Math.floorMod(day, WEEK) == WEEK - 1) { clanIncidents(day); needs(day); relations.week(); }
    }
    /** Which day of the week a tie or a resident has its weekly turn: spread so no one day carries the whole village. */
    static int slot(String key) { return (int) Math.floorMod(Seeds.hash(key), (long) WEEK); }
    private boolean healed(SocietyHook h) {
        var t = tie(h.roles().get("a"), h.roles().get("b"));
        return t == null || t.quarrel() < 0 || w.day - t.quarrel() > 30;
    }

    /**
     * Each tie's and each resident's weekly turn (a seventh of the village a day): quarrels, rivalries, romance and
     * new friendships. Clan incidents, needs and the relations' drift run once a week.
     */
    void week(int slot) {
        long day = w.day;
        for (var e : List.copyOf(ties.entrySet())) {
            if (slot(e.getKey()) != slot) continue;
            var t = e.getValue(); String[] ab = e.getKey().split("\\|"); String a = ab[0], b = ab[1];
            updates++;
            if (SocialTie.DAILY.contains(t.kind()) && tier(a) == Tier.BACKGROUND && tier(b) == Tier.BACKGROUND) t = t.together(day, 5);
            else if (t.kind().equals("friend") || t.kind().equals("sweetheart")) t = t.together(day, 2); // friends meet up
            boolean kin = t.kind().equals("family") || t.kind().equals("household") || t.kind().equals("spouse");
            double tension = Math.max(mood("district:" + w.person(a).district()).tension(), mood("village").tension());
            double pride = (Math.max(0, w.person(a).personality().pride()) + Math.max(0, w.person(b).personality().pride())) / 2;
            if (!kin && t.quarrel() < 0 && roll("quarrel", e.getKey(), day) < QUARREL_CHANCE * (1 + 2 * tension) * (1 + pride)) {
                t = t.quarrel(day);
                if (affinity(a, b) > 15 && (tier(a) != Tier.BACKGROUND || tier(b) != Tier.BACKGROUND))
                    raise("quarrel_to_mediate", Map.of("a", a, "b", b), "district:" + w.person(a).district(), 21, .4, List.of(friendWithEither(a, b)), Map.of("tie", e.getKey()));
            }
            ties.put(e.getKey(), t);
            double aff = affinity(a, b);
            if (!kin && t.chosen() && aff < -20 && !t.kind().equals("rival")) {
                ties.put(e.getKey(), t = t.kind("rival", day));
                var pa = w.person(a); var pb = w.person(b);
                if (pa.shinobi() && pb.shinobi() && Person.seniority(pa.rank()) == Person.seniority(pb.rank()) && roll("rivalry", e.getKey(), day) < .5)
                    raise("rivalry_heating", Map.of("a", a, "b", b), "rank:" + Person.RANKS.get(pa.rank()), 14, .5, List.of(friendWithEither(a, b)), Map.of("tie", e.getKey()));
            }
            romance(a, b, t, aff, day);
        }
        friendships(day, slot);
    }
    private static Map<String, Object> friendWithEither(String a, String b) {
        return Map.of("any", List.of(Map.of("friendship", List.of(a, 3)), Map.of("friendship", List.of(b, 3))));
    }

    /** New friendships: someone with room for one befriends a friend of a friend they click with. */
    private void friendships(long day, int slot) {
        for (var p : List.copyOf(w.people.values())) {
            String id = p.id();
            if (slot(id) != slot) continue;
            if (chosen(id) >= CHOSEN_TIES) continue;
            var mine = adjacency.getOrDefault(id, Set.of());
            if (mine.isEmpty()) continue;
            var via = List.copyOf(mine).get((int) (roll("via", id, day) * mine.size()));
            var theirs = List.copyOf(adjacency.getOrDefault(via, Set.of()));
            if (theirs.isEmpty()) continue;
            String other = theirs.get((int) (roll("fof", id, day) * theirs.size()));
            if (other.equals(id) || mine.contains(other) || chosen(other) >= CHOSEN_TIES) continue;
            updates++;
            if (roll("friend", ClanRelations.pair(id, other), day) < FRIEND_CHANCE * (1 + w.chemistry(id, other))) link(id, other, "friend");
        }
    }
    /** Crushes, sweethearts and marriages between adults, with each clan's pressure to marry within. */
    private void romance(String a, String b, SocialTie t, double aff, long day) {
        var pa = w.person(a); var pb = w.person(b);
        if (pa.stage() != Person.Stage.ADULT || pb.stage() != Person.Stage.ADULT || t.kind().equals("family") || t.kind().equals("household")) return;
        boolean compatible = pa.romantic() && pb.romantic() && pa.attractedTo(pb.gender()) && pb.attractedTo(pa.gender())
                && !pa.family().containsKey(b) && !pb.family().containsKey(a);
        if (!compatible) return;
        String key = ClanRelations.pair(a, b);
        if (!t.crush() && t.chosen() && aff >= CRUSH_AFFINITY && single(a) && single(b) && roll("crush", key, day) < .2) {
            ties.put(key, t = t.crush(true));
            if (w.playerStage() != Person.Stage.CHILD && (tier(a) != Tier.BACKGROUND || tier(b) != Tier.BACKGROUND))
                raise("secret_crush", Map.of("admirer", a, "beloved", b), "district:" + pa.district(), 28, .3,
                        List.of(Map.of("friendship", List.of(a, 6)), Map.of("age_stage", "teen")), Map.of("tie", key));
        }
        if (t.crush() && t.chosen() && aff >= SWEETHEART_AFFINITY && single(a) && single(b)) ties.put(key, t = t.kind("sweetheart", day));
        if (t.kind().equals("sweetheart") && day - t.since() >= COURTSHIP_DAYS && aff >= MARRY_AFFINITY) {
            String ga = groupOf(a), gb = groupOf(b);
            double pressure = marriageChance(ga, gb);
            if (roll("marry", key, day) < pressure) {
                ties.put(key, t.kind("spouse", day));
                relations.married(ga, gb, day);
                push("village", .05, 0);
            } else if (!ga.equals(gb) && roll("forbidden", key, day) < .5)
                raise("forbidden_match", Map.of("a", a, "b", b, "clan_a", ga, "clan_b", gb), "village", 28, .6,
                        List.of(Map.of("age_stage", "teen"), friendWithEither(a, b)), Map.of("relation", List.of(ga, gb, -5)));
        }
    }
    private boolean single(String id) {
        for (String o : adjacency.getOrDefault(id, Set.of())) { var k = tie(id, o).kind(); if (k.equals("spouse") || k.equals("sweetheart")) return false; }
        return true;
    }
    /** How likely a couple's families let them marry: 1 within a clan, less the stricter either clan is about marrying in. */
    public static double marriageChance(String a, String b) { return a.equals(b) ? 1 : (1 - strictness(a)) * (1 - strictness(b)); }
    private static double strictness(String group) { return ClanProfile.known(group) ? ClanProfile.of(group).strictness() : 0; }

    /** Clans on bad terms have incidents; allies share good days. */
    private void clanIncidents(long day) {
        var groups = new TreeSet<String>(clans.keySet());
        groups.add(ClanProfile.CIVILIAN); groups.add(ClanProfile.CLANLESS);
        for (String a : groups) for (String b : groups) {
            if (a.compareTo(b) >= 0) continue;
            double r = relations.get(a, b);
            String key = a + "|" + b;
            if (r < -15 && roll("incident", key, day) < INCIDENT_CHANCE * (1 + mood("clan:" + a).tension() + mood("clan:" + b).tension())) {
                relations.event(a, b, -(3 + 4 * roll("incident_size", key, day)), "incident", day);
                push("clan:" + a, 0, .15); push("clan:" + b, 0, .15);
                String ma = member(a, day), mb = member(b, day);
                if (!ma.isEmpty() && !mb.isEmpty())
                    raise("clan_feud", Map.of("clan_a", a, "clan_b", b, "a", ma, "b", mb), "village", 14, Math.min(1, -r / 60),
                            List.of(Map.of("rank_at_least", "genin")), Map.of("relation", List.of(a, b, 10)));
            } else if (r > 40 && roll("good_day", key, day) < .1) relations.event(a, b, 2, "shared festival", day);
        }
    }
    private String member(String group, long day) {
        var all = w.people.values().stream().filter(p -> ClanRelations.groupOf(p).equals(group) && p.stage() == Person.Stage.ADULT).map(Person::id).toList();
        return all.isEmpty() ? "" : all.get((int) (roll("member", group, day) * all.size()));
    }
    /** Everyday needs of the people the player knows or lives among, and the elders' requests. */
    private void needs(long day) {
        for (var p : w.people.values()) {
            if (p.id().startsWith("role:") || tier(p.id()) == Tier.BACKGROUND && !p.district().equals(playerDistrict())) continue;
            double r = roll("need", p.id(), day);
            if (r < .025) raise("favor_needed", Map.of("client", p.id()), "district:" + p.district(), 7, .3, List.of(), Map.of("standing", "district:" + p.district()));
            else if (r < .035) raise("lost_item", Map.of("owner", p.id()), "district:" + p.district(), 5, .2, List.of(), Map.of("standing", "district:" + p.district()));
        }
        for (var house : clans.values()) {
            String community = "clan:" + house.clan();
            boolean welcome = house.clan().equals(w.playerClan()) || w.title(community).compareTo(Standing.Title.HELPING_HAND) >= 0;
            if (!welcome || house.elders().isEmpty() || roll("elder", house.clan(), day) >= .15) continue;
            String elder = house.elders().get((int) (roll("which_elder", house.clan(), day) * house.elders().size()));
            raise("elder_request", Map.of("elder", elder, "clan", community), community, 14, .5,
                    List.of(Map.of("any", List.of(Map.of("clan", house.clan()), Map.of("standing", List.of(community, "helping_hand"))))), Map.of("standing", community));
        }
    }
    String playerDistrict() { return w.flags.stream().filter(f -> f.startsWith("player.district:")).map(f -> f.substring(16)).findFirst().orElse("residential"); }

    /** A newcomer settles in the village: their household and neighbors, and a hook to befriend them. */
    public void arrive(Person p) {
        w.add(p);
        if (!p.district().isEmpty()) {
            var near = w.people.values().stream().filter(o -> o.district().equals(p.district()) && !o.id().equals(p.id())).map(Person::id).toList();
            for (int i = 0; i < Math.min(2, near.size()); i++) link(p.id(), near.get((int) (roll("newcomer", p.id() + i, w.day) * near.size())), "neighbor");
        }
        raise("newcomer", Map.of("newcomer", p.id()), "district:" + p.district(), 21, .3, List.of(), Map.of("standing", "district:" + p.district()));
    }

    // -- hooks -------------------------------------------------------------------------------------

    SocietyHook raise(String type, Map<String, String> roles, String place, int days, double urgency, List<Map<String, Object>> requires, Map<String, Object> stakes) {
        long open = hooks.stream().filter(h -> h.type().equals(type)).count();
        boolean duplicate = hooks.stream().anyMatch(h -> h.type().equals(type) && h.roles().equals(roles));
        if (duplicate || open >= HOOKS_PER_TYPE || hooks.size() >= OPEN_HOOKS) return null;
        var h = new SocietyHook("hook." + type + "." + (++hookSerial), type, roles, place, w.day, w.day + days, urgency, requires, stakes);
        hooks.add(h);
        raised.merge(type, 1, Integer::sum);
        return h;
    }
    public SocietyHook hook(String id) { return hooks.stream().filter(h -> h.id().equals(id)).findFirst().orElse(null); }
    /** Whether the player would come across a hook: someone in it is known, or it is in their district or clan. */
    public boolean visible(SocietyHook h) {
        for (String who : h.roles().values()) if (w.people.containsKey(who) && w.knows(who)) return true;
        return h.place().equals("district:" + playerDistrict()) || !w.playerClan().isEmpty() && h.roles().containsValue("clan:" + w.playerClan())
                || h.roles().containsValue(w.playerClan());
    }
    public List<SocietyHook> visibleHooks() { return hooks.stream().filter(this::visible).toList(); }

    /** A quest resolved a hook. Returns "" or why not. Outcomes per type: {@link SocietyHook#OUTCOMES}. */
    public String resolve(String id, String outcome) {
        var h = hook(id);
        if (h == null) return "no_hook";
        if (!SocietyHook.OUTCOMES.get(h.type()).contains(outcome)) return "unknown_outcome";
        var r = h.roles();
        switch (h.type() + ":" + outcome) {
            case "clan_feud:mediated" -> { relations.event(r.get("clan_a"), r.get("clan_b"), 10, "mediated", w.day); for (String p : List.of(r.get("a"), r.get("b"))) w.act(p, Act.MEDIATED); }
            case "clan_feud:sided_a", "clan_feud:sided_b" -> {
                boolean forA = outcome.endsWith("_a");
                relations.event(r.get("clan_a"), r.get("clan_b"), -6, "the player took a side", w.day);
                w.act(r.get(forA ? "a" : "b"), Act.STOOD_BY_THEM); w.act(r.get(forA ? "b" : "a"), Act.SIDED_AGAINST);
            }
            case "quarrel_to_mediate:mediated" -> {
                String key = ClanRelations.pair(r.get("a"), r.get("b"));
                var t = ties.get(key); if (t != null) ties.put(key, t.reconciled());
                w.act(r.get("a"), Act.MEDIATED); w.act(r.get("b"), Act.MEDIATED);
            }
            case "favor_needed:done" -> w.act(r.get("client"), Act.HELPED_RESIDENT, List.copyOf(tiesOf(r.get("client"))));
            case "lost_item:returned" -> w.act(r.get("owner"), Act.HELPED_RESIDENT, List.copyOf(tiesOf(r.get("owner"))));
            case "lost_item:kept" -> w.act(r.get("owner"), Act.HURT_RESIDENT);
            case "newcomer:befriended" -> w.experience(Act.MEAL_TOGETHER, List.of(r.get("newcomer")));
            case "elder_request:done" -> {
                String clan = r.get("clan").substring(5);
                var members = w.people.values().stream().filter(p -> p.clan().equals(clan)).map(Person::id).toList();
                w.deed(Act.HONORED_CUSTOM, r.get("elder"), members);
            }
            case "secret_crush:helped" -> {
                String key = ClanRelations.pair(r.get("admirer"), r.get("beloved"));
                var t = ties.get(key); if (t != null && single(r.get("admirer")) && single(r.get("beloved"))) ties.put(key, t.kind("sweetheart", w.day));
                w.act(r.get("admirer"), Act.HEART_TO_HEART);
            }
            case "secret_crush:kept_quiet" -> w.act(r.get("admirer"), Act.KEPT_PROMISE);
            case "secret_crush:told" -> w.act(r.get("admirer"), Act.BROKE_PROMISE);
            case "rivalry_heating:cooled" -> {
                String key = ClanRelations.pair(r.get("a"), r.get("b"));
                var t = ties.get(key); if (t != null) ties.put(key, t.reconciled().kind("friend", w.day));
                w.act(r.get("a"), Act.MEDIATED); w.act(r.get("b"), Act.MEDIATED);
            }
            case "rivalry_heating:fanned" -> {
                String key = ClanRelations.pair(r.get("a"), r.get("b"));
                var t = ties.get(key); if (t != null) ties.put(key, t.quarrel(w.day));
            }
            case "forbidden_match:supported" -> {
                String key = ClanRelations.pair(r.get("a"), r.get("b"));
                var t = ties.get(key); if (t != null) ties.put(key, t.kind("spouse", w.day));
                relations.married(r.get("clan_a"), r.get("clan_b"), w.day);
                relations.event(r.get("clan_a"), r.get("clan_b"), -5, "a match the elders opposed", w.day);
                w.act(r.get("a"), Act.STOOD_BY_THEM); w.act(r.get("b"), Act.STOOD_BY_THEM);
            }
            default -> {}
        }
        hooks.remove(h);
        resolved.merge(h.type(), 1, Integer::sum);
        return "";
    }

    private double roll(String what, String key, long day) { return Seeds.roll(w.seed, "society", what, key, Long.toString(day)); }

    // -- save --------------------------------------------------------------------------------------

    /** The village's state, a world attachment ({@code shinobi_life:village}); structure is rebuilt from the people. */
    public Map<String, Object> write() {
        var out = new LinkedHashMap<String, Object>();
        out.put("format", 1);
        var t = new LinkedHashMap<String, Object>();
        ties.forEach((k, v) -> t.put(k, List.of(v.kind(), v.since(), v.together(), v.lastTogether(), v.quarrel(), v.crush())));
        out.put("ties", t);
        out.put("relations", relations.moved()); out.put("relation_bonus", relations.bonuses());
        var m = new LinkedHashMap<String, Object>();
        moods.forEach((k, v) -> m.put(k, List.of(v.cheer(), v.tension())));
        out.put("moods", m);
        out.put("hooks", hooks.stream().map(SocietyHook::toMap).toList());
        out.put("hook_serial", hookSerial);
        return out;
    }
    @SuppressWarnings("unchecked")
    public static Village read(BondWorld w, Map<String, Object> saved) {
        var v = new Village(w);
        v.buildClans();
        for (var e : ((Map<String, Object>) saved.get("ties")).entrySet()) {
            var l = (List<Object>) e.getValue(); String[] ab = e.getKey().split("\\|");
            if (!w.people.containsKey(ab[0]) || !w.people.containsKey(ab[1])) continue;
            v.ties.put(e.getKey(), new SocialTie((String) l.get(0), SaveFormat.lng(l.get(1)), (int) SaveFormat.lng(l.get(2)), SaveFormat.lng(l.get(3)),
                    SaveFormat.lng(l.get(4)), (Boolean) l.get(5)));
            v.adjacency.computeIfAbsent(ab[0], k -> new TreeSet<>()).add(ab[1]);
            v.adjacency.computeIfAbsent(ab[1], k -> new TreeSet<>()).add(ab[0]);
        }
        var moved = new TreeMap<String, Double>(); var bonus = new TreeMap<String, Double>();
        ((Map<String, Object>) saved.getOrDefault("relations", Map.of())).forEach((k, x) -> moved.put(k, SaveFormat.dbl(x)));
        ((Map<String, Object>) saved.getOrDefault("relation_bonus", Map.of())).forEach((k, x) -> bonus.put(k, SaveFormat.dbl(x)));
        v.relations.restore(moved, bonus);
        ((Map<String, Object>) saved.getOrDefault("moods", Map.of())).forEach((k, x) -> {
            var l = (List<Object>) x; v.moods.put(k, new Mood(SaveFormat.dbl(l.get(0)), SaveFormat.dbl(l.get(1))));
        });
        for (Object o : (List<Object>) saved.getOrDefault("hooks", List.of())) {
            var h = (Map<String, Object>) o;
            var req = (Map<String, Object>) h.getOrDefault("requires", Map.of());
            v.hooks.add(new SocietyHook((String) h.get("id"), (String) h.get("type"), (Map<String, String>) h.get("roles"), (String) h.get("place"),
                    SaveFormat.lng(h.get("raised")), SaveFormat.lng(h.get("expires")), SaveFormat.dbl(h.get("urgency")),
                    (List<Map<String, Object>>) req.getOrDefault("all", List.of()), (Map<String, Object>) h.getOrDefault("stakes", Map.of())));
        }
        v.hookSerial = (int) SaveFormat.lng(saved.getOrDefault("hook_serial", 0));
        w.village = v;
        return v;
    }
}
