package dev.shinobi.life.bond.sim;

import dev.shinobi.life.bond.Act;
import dev.shinobi.life.bond.BondWorld;
import dev.shinobi.life.bond.ClanProfile;
import dev.shinobi.life.bond.ClanRelations;
import dev.shinobi.life.bond.Leaf;
import dev.shinobi.life.bond.Person;
import dev.shinobi.life.bond.Personality;
import dev.shinobi.life.bond.Seeds;
import dev.shinobi.life.bond.SocietyHook;
import dev.shinobi.life.bond.Village;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.regex.Pattern;

/**
 * The village at scale: about 300 residents drawn by the real population weights ({@code tools/wardrobe/population.json}),
 * in households, clan quarters, streets and workplaces, around the Classic cast, lived through for a number of days
 * while a player meets people and takes up some of the hooks the society raises. Reports the cost per day, the ties
 * that form, how the clans' relations drift and how many hooks the player would see a week.
 *
 * <p>Run it with {@code ./gradlew :life:bonds:simulateVillage} ({@code -Pseed=N}).
 */
public final class VillageSim {
    public record Report(int residents, int days, double msPerDay, double maxMsPerDay, long updatesPerDay, int ties, Map<String, Integer> tieKinds,
            double chosenPerResident, int maxChosen, Map<String, Integer> raised, double raisedPerWeek, double visiblePerWeek, int resolvedByPlayer,
            List<String> drift, int marriages, int newMarriages, int crossClanMarriages, Map<String, String> moods, List<String> moodLog, int known,
            BondWorld world) {}

    static final String[] ARCHETYPES = {"warmhearted", "thoughtful", "playful", "adventurous", "meticulous", "steadfast", "reserved", "imaginative",
            "pragmatic", "curious", "protective", "gentle"};
    static final List<String> CIVIL_DISTRICTS = List.of("market", "residential", "riverside"), SHINOBI_DISTRICTS = List.of("residential", "academy", "gate");

    /** The weights per thousand from population.json: civilian, clanless and each clan. */
    public static Map<String, Integer> weights() {
        var out = new LinkedHashMap<String, Integer>();
        String json;
        try { json = Files.readString(Path.of("../../tools/wardrobe/population.json")); }
        catch (IOException e) { throw new IllegalStateException("population.json not found from " + Path.of("").toAbsolutePath(), e); }
        var m = Pattern.compile("\"(civilian|clanless)\"\\s*:\\s*(\\d+)").matcher(json);
        while (m.find()) out.put(m.group(1), Integer.parseInt(m.group(2)));
        String clans = json.substring(json.indexOf("\"clans\""), json.indexOf('}', json.indexOf("\"clans\"")));
        var c = Pattern.compile("\"(\\w+)\"\\s*:\\s*(\\d+)").matcher(clans);
        while (c.find()) out.put(c.group(1), Integer.parseInt(c.group(2)));
        return out;
    }

    /** The Classic cast and a village of {@code residents} people around them. */
    public static BondWorld populate(long seed, int residents) {
        var w = Leaf.classic(seed, 0);
        var weights = weights();
        int total = weights.values().stream().mapToInt(Integer::intValue).sum();
        var rng = Seeds.stream(seed, "residents", "village");
        int n = 0, house = 0;
        while (n < residents) {
            int roll = rng.below(total), acc = 0; String group = "civilian";
            for (var e : weights.entrySet()) { acc += e.getValue(); if (roll < acc) { group = e.getKey(); break; } }
            String clan = group.equals("civilian") || group.equals("clanless") ? "" : group;
            boolean shinobi = !group.equals("civilian");
            String district = !clan.isEmpty() && ClanProfile.known(clan) && ClanProfile.of(clan).noble() ? "quarter:" + clan
                    : (shinobi ? SHINOBI_DISTRICTS : CIVIL_DISTRICTS).get(rng.below(3));
            int size = Math.min(residents - n, new int[]{1, 2, 2, 3, 3, 4, 4, 5}[rng.below(8)]);
            String hid = "household:" + (house++);
            var ids = new ArrayList<String>();
            for (int i = 0; i < size; i++) ids.add("resident:" + (n + i));
            String work = shinobi ? "" : "work:" + district + "_" + rng.below(6);
            for (int i = 0; i < size; i++) {
                var family = new TreeMap<String, String>();
                boolean adult = i < 2 || size == 1 || rng.chance(.35); // grown children still at home
                for (int j = 0; j < size; j++) {
                    if (i == j) continue;
                    boolean parentI = i < 2 || size == 1, parentJ = j < 2;
                    family.put(ids.get(j), parentI && parentJ ? "spouse" : parentI ? "child" : parentJ ? "parent" : "sibling");
                }
                String gender = i == 0 ? (rng.chance(.5) ? "MALE" : "FEMALE") : i == 1 ? "?" : rng.chance(.5) ? "MALE" : "FEMALE";
                var p = Personality.rolled(ARCHETYPES[rng.below(ARCHETYPES.length)], rng, .2);
                if (!clan.isEmpty() && ClanProfile.known(clan)) p = ClanProfile.of(clan).shape(p);
                int rank = !shinobi ? Person.CIVILIAN : !adult ? 0 : new int[]{1, 1, 2, 2, 2, 3}[rng.below(6)];
                var circles = new ArrayList<String>(List.of(hid));
                if (adult && !work.isEmpty() && rng.chance(.7)) circles.add(work);
                if (!adult) circles.add("class:academy_" + rng.below(4));
                String attraction = rng.chance(.2) ? "NONE" : "ANY";
                w.add(new Person(ids.get(i), clan, district, rank, adult ? Person.Stage.ADULT : Person.Stage.CHILD, p,
                        gender.equals("?") ? "NON_BINARY" : gender, attraction, rng.below(BondWorld.YEAR), family, circles));
            }
            n += size;
        }
        return w;
    }

    /** Lives {@code days} days; the player meets {@code meetPerDay} people a day and resolves about half the hooks they see. */
    public static Report run(long seed, int residents, int days, int meetPerDay) {
        var w = populate(seed, residents);
        var v = Village.settle(w);
        var rng = Seeds.stream(seed, "playthrough", "village");
        var people = w.people().stream().map(Person::id).filter(id -> id.startsWith("resident:")).toList();
        int resolved = 0; double visible = 0; long nanos = 0, worst = 0; long before = v.updates();
        var seenHooks = new java.util.HashSet<String>();
        var moodLog = new ArrayList<String>();
        var home = people.stream().filter(id -> List.of("residential", "market").contains(w.person(id).district())).toList();
        for (int d = 0; d < days; d++) {
            if (d == days / 2) { w.setPlayerStage(Person.Stage.TEEN); for (String c : Leaf.CLASSMATES) w.grow(c, Person.Stage.TEEN); }
            for (int i = 0; i < meetPerDay; i++) {
                var pool = rng.chance(.7) ? home : people;
                String who = pool.get(rng.below(pool.size())); v.meet(who); w.talk(who);
            }
            if (d % 7 == 3) w.act(people.get(rng.below(people.size())), Act.HELPED_RESIDENT, List.of());
            if (d == 40) v.push("village", .6, 0);                               // the Leaf Festival
            if (d == 120) w.deed(Act.DEFENDED_VILLAGE, "", List.of(Leaf.TEAMMATE_A)); // a border incident beaten back
            if (d == 40 || d == 41 || d == 50 || d == 121 || d == 135) moodLog.add("day " + d + " " + v.mood("village").label().id());
            for (var h : v.visibleHooks()) {
                if (seenHooks.add(h.id())) visible++;
                if (rng.chance(.08)) { var outcomes = SocietyHook.OUTCOMES.get(h.type()); if (v.resolve(h.id(), outcomes.getFirst()).isEmpty()) resolved++; }
            }
            long t0 = System.nanoTime();
            w.endDay();
            long dt = System.nanoTime() - t0;
            nanos += dt; worst = Math.max(worst, dt);
            w.drainEvents();
        }
        var kinds = v.tieKinds();
        int chosenMax = 0; double chosenSum = 0;
        for (String id : people) {
            int c = 0;
            for (String o : v.tiesOf(id)) if (v.tie(id, o).chosen()) c++;
            chosenMax = Math.max(chosenMax, c); chosenSum += c;
        }
        var drift = new ArrayList<String>();
        var pairs = new TreeMap<Double, String>();
        var groups = new ArrayList<>(v.houses().stream().map(Village.House::clan).toList());
        groups.add(ClanProfile.CIVILIAN); groups.add(ClanProfile.CLANLESS);
        for (String a : groups) for (String b : groups) if (a.compareTo(b) < 0) {
            double moved = v.relations().get(a, b) - v.relations().base(a, b);
            if (Math.abs(moved) >= 1) pairs.put(-Math.abs(moved) + pairs.size() * 1e-9, String.format("%s-%s %+.0f -> %.0f (%s)", a, b, moved, v.relations().get(a, b), v.relations().label(a, b).id()));
        }
        pairs.values().stream().limit(8).forEach(drift::add);
        int marriages = kinds.getOrDefault("spouse", 0), fresh = 0, cross = 0;
        for (String id : people) for (String o : v.tiesOf(id))
            if (id.compareTo(o) < 0 && v.tie(id, o).kind().equals("spouse") && !w.person(id).family().containsKey(o)) {
                fresh++;
                if (!ClanRelations.groupOf(w.person(id)).equals(ClanRelations.groupOf(w.person(o)))) cross++;
            }
        var moods = new TreeMap<String, String>();
        for (String c : List.of("village", "district:market", "district:residential")) moods.put(c, v.mood(c).label().id());
        int known = (int) people.stream().filter(w::knows).count();
        return new Report(people.size(), days, nanos / 1e6 / days, worst / 1e6, (v.updates() - before) / days, v.tieCount(), kinds,
                chosenSum / people.size(), chosenMax, v.raisedByType(), v.raisedTotal() * 7.0 / days, visible * 7 / days, resolved, drift,
                marriages, fresh, cross, moods, moodLog, known, w);
    }

    public static String format(Report r) {
        var sb = new StringBuilder();
        sb.append(String.format("Village of %d residents (plus the cast), %d days%n", r.residents(), r.days()));
        sb.append(String.format("  cost: %.2f ms a day on average, %.2f at worst; %d tie and resident updates a day%n", r.msPerDay(), r.maxMsPerDay(), r.updatesPerDay()));
        sb.append(String.format("  ties: %d (%s); chosen ties per resident %.1f on average, %d at most%n", r.ties(), r.tieKinds(), r.chosenPerResident(), r.maxChosen()));
        sb.append(String.format("  marriages: %d spouse ties, %d new in these days (%d across clans or groups)%n", r.marriages(), r.newMarriages(), r.crossClanMarriages()));
        sb.append(String.format("  hooks raised: %.1f a week (%s); the player sees %.1f a week and resolved %d%n", r.raisedPerWeek(), r.raised(), r.visiblePerWeek(), r.resolvedByPlayer()));
        sb.append("  clan relations that moved most:\n");
        r.drift().forEach(d -> sb.append("    ").append(d).append('\n'));
        sb.append("  village mood: ").append(r.moodLog()).append("; at the end ").append(r.moods()).append('\n');
        sb.append(String.format("  residents the player knows: %d%n", r.known()));
        return sb.toString();
    }

    public static void main(String[] args) {
        long seed = args.length > 0 ? Long.parseLong(args[0]) : 20261029L;
        run(seed, 300, 14, 2); // warm the JIT
        System.out.print(format(run(seed, 300, 180, 2)));
    }

    private VillageSim() {}
}
