package dev.shinobi.life.home.sim;

import dev.shinobi.life.bond.Act;
import dev.shinobi.life.bond.BondWorld;
import dev.shinobi.life.bond.Seeds;
import dev.shinobi.life.bond.Together;
import dev.shinobi.life.home.BondFriends;
import dev.shinobi.life.home.Cast;
import dev.shinobi.life.home.Catalog;
import dev.shinobi.life.home.Comfort;
import dev.shinobi.life.home.Flat;
import dev.shinobi.life.home.Home;
import dev.shinobi.life.home.Practice;
import dev.shinobi.life.home.Rest;
import dev.shinobi.life.home.Visits;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * A typical player's first 15 hours (the beta, Academy to Chunin): 45 in-game days of 20 real minutes. The chapter
 * days follow ROADMAP.md section 8 (Beta 1 about 12 days, Beta 2 about 24, Beta 3 about 9, with the Forest of Death
 * five days away from home). The typical player goes home most nights, sleeps before midnight most of the time,
 * eats breakfast from the cupboard, buys furniture with what is left after food, does about two thirds of the side
 * quests, talks to the squad most days and cleans up when it gets messy about half the time.
 *
 * <p>{@code ./gradlew :life:home:simulate [-Pseed=N]}
 */
public final class FirstFifteenHours {
    public static final int DAYS = 46, BETA2 = 12, BETA3 = 36;
    /** Real seconds in an in-game hour (a day is 20 minutes). */
    static final double HOUR_SECONDS = 50;

    public record Slice(String name, int days, int nightsHome, int nightsAway, double homeMinutes, Map<String, Integer> visits,
            int met, int notes, int hosted, int rested, double regen) {}
    public record Snapshot(int day, double comfort, String tier, double style, int pieces, int spent, String perks, int keepsakes, int photos, String plant) {}
    public record Result(List<Slice> slices, List<Snapshot> comfort, int ryoEnd, int spent, int cleanings, int messyEvenings,
            int staleMeals, int keys, String plantStage, double practice, int storageSlots, Map<String, Integer> visitsByKind) {}

    /** The chapters that keep the player away overnight (camp, the far village, the Forest of Death). */
    static boolean awayNight(int d) { return d == 17 || d == 18 || d == 24 || d == 25 || d == 31 || d == 32 || d == 21 || d == 28 || (d >= 37 && d <= 41); }
    static boolean dRank(int d) { return d >= 13 && d < BETA3 && !awayNight(d) && d % 2 == 1; }
    static boolean cRankReturn(int d) { return d == 19 || d == 22 || d == 26 || d == 29 || d == 33; }
    static int rank(int d) { return d < BETA2 ? 0 : d < 45 ? 1 : 2; }
    static String slice(int d) { return d < BETA2 ? "Beta 1" : d < BETA3 ? "Beta 2" : "Beta 3"; }

    /** Side quests a typical player finishes, by day: the keepsakes and pieces they bring home, and their ryo. */
    static final Map<Integer, List<String>> REWARDS = new TreeMap<>(Map.ofEntries(
            Map.entry(3, List.of("keepsake:keepsake_shogi_set")), Map.entry(6, List.of("keepsake:keepsake_cat_figurine")),
            Map.entry(9, List.of("keepsake:keepsake_framed_ladle", "piece:ichiraku_stool")), Map.entry(16, List.of("keepsake:keepsake_race_ribbon")),
            Map.entry(20, List.of("piece:tea_set")), Map.entry(23, List.of("keepsake:keepsake_peace_offering")),
            Map.entry(27, List.of("keepsake:keepsake_ferry_lantern", "keepsake:keepsake_clan_nara")), Map.entry(30, List.of("keepsake:keepsake_lake_lantern")),
            Map.entry(34, List.of("keepsake:keepsake_price_war", "keepsake:keepsake_clan_akimichi")), Map.entry(43, List.of("keepsake:keepsake_post_splinter"))));
    static final Map<Integer, String> PHOTOS = Map.of(2, "photo.class", 11, "photo.graduation", 12, "photo.squad", 19, "photo.first_c_rank",
            30, "photo.leaf_festival", 45, "photo.chunin_exams");
    /** What a typical player buys, in order, once it is in the shops and they can afford it. */
    static final List<String> WISHLIST = List.of("zabuton", "tatami", "andon_lamp", "potted_fern", "display_shelf", "photo_frame", "scroll_shelf",
            "pet_bed", "pet_bowl", "shoji_screen", "leaf_banner", "barrel", "rug", "curtains", "training_dummy", "photo_frame",
            "noren", "poster", "ramen_cup_tower", "bowl_shelf", "low_desk", "futon_deluxe", "meditation_mat", "icebox",
            "andon_lamp", "tea_table", "zabuton", "photo_frame", "balcony_planter", "wind_chime", "display_case", "kotatsu",
            "hanging_scroll", "curio_cabinet", "ikebana", "lantern_string", "festival_mask", "photo_frame", "weight_rack", "balcony_bench", "potted_bonsai");

    public static Result run(long seed) {
        var w = Cast.world(seed);
        var f = new BondFriends(w);
        var home = new Home(BondWorld.PLAYER, Flat.CLASSIC);
        var practice = new Practice();
        var rng = Seeds.stream(seed, "home_sim", "typical");
        int ryo = 60, spent = 0, staleMeals = 0, messyEvenings = 0, keys = 0;
        var slices = new ArrayList<Slice>();
        var snaps = new ArrayList<Snapshot>();
        var byKind = new TreeMap<String, Integer>();
        int[] sl = new int[6]; double[] sd = new double[2];
        var sliceVisits = new TreeMap<String, Integer>();
        var wishlist = new ArrayList<>(WISHLIST);
        String current = slice(0);
        for (int d = 0; d < DAYS; d++) {
            if (!slice(d).equals(current)) {
                slices.add(new Slice(current, sliceDays(current), sl[0], sl[1], sd[0], Map.copyOf(sliceVisits), sl[2], sl[3], sl[4], sl[5], sd[1]));
                sl = new int[6]; sd = new double[2]; sliceVisits.clear(); current = slice(d);
            }
            int season = d / 28, rank = rank(d);
            boolean away = awayNight(d), awayMorning = d > 0 && awayNight(d - 1);
            // The day's company, roughly the bond engine's typical player (LIFE_TOGETHER.md section 9): lessons with the
            // class and the instructor, training and missions with the squad, talks, a hangout every few days, and the
            // bond quests and squad beats as they open.
            if (rank == 0 && d % 7 < 5) {
                var cls = new ArrayList<>(Cast.CLASSMATES.subList(0, 3 + (int) (rng.unit() * 3))); cls.add(Cast.INSTRUCTOR);
                w.experience(Act.STUDIED_TOGETHER, cls);
            }
            if (dRank(d) || cRankReturn(d)) w.experience(Act.MISSION_TOGETHER, List.of(Cast.TEAMMATE_A, Cast.TEAMMATE_B, Cast.SENSEI));
            else if (rank >= 1 && !away && rng.chance(.6)) w.experience(Act.TRAINED_TOGETHER, List.of(Cast.TEAMMATE_A, Cast.TEAMMATE_B, Cast.SENSEI));
            if (away) w.experience(Act.CAMP_NIGHT, List.of(Cast.TEAMMATE_A, Cast.TEAMMATE_B));
            for (String who : Cast.CLASSMATES) if (rng.chance(.8)) w.talk(who);
            if (rng.chance(.5)) w.talk(Cast.LANDLADY);
            if (rank >= 1 && rng.chance(.5)) w.talk(Cast.SENSEI);
            if (d % 3 == 1 && !away) {
                var pick = Cast.CLASSMATES.get((int) (rng.unit() * Cast.CLASSMATES.size()));
                var ans = Together.invite(w, List.of(pick), d % 2 == 0 ? "ramen" : "train", w.day(), 17);
                if (ans.plan() != null) Together.go(w, ans.plan().id(), true);
            }
            for (var inv : Together.invitations(w)) { var plan = Together.answer(w, inv.id(), rng.chance(.6)); if (plan != null) Together.go(w, plan.id(), true); }
            for (String who : Cast.CLASSMATES) if (w.level(who) >= 3 && d >= 2) w.moment(who, "bond.b1." + who);
            for (String who : Cast.SQUAD) {
                if (d == BETA2) w.moment(who, "ch8.bell_test");
                if (d == 18) w.moment(who, "ch11.campfire");
                if (rank >= 1 && w.level(who) >= 4) w.moment(who, "bond.b2." + who + ".1");
                if (rank >= 1 && w.level(who) >= 5) w.moment(who, "bond.b2." + who + ".2");
                if (d == 39 && w.level(who) >= 5) w.moment(who, "bond.b3." + who);
            }
            if (d == BETA2) { w.moment(Cast.SENSEI, "ch8.bell_test"); for (String who : Cast.CLASSMATES) w.setRank(who, 1); }

            // Money: the stipend in the mailbox, jobs, missions; food; rent on Market Day.
            ryo += awayMorning ? Home.STIPEND : home.morning(d);
            if (rank == 0 && rng.chance(.5)) ryo += 60;
            if (dRank(d)) ryo += 100;
            if (cRankReturn(d)) ryo += 450;
            ryo -= rank == 0 ? 15 : 20;
            for (var r : REWARDS.getOrDefault(d, List.of())) {
                if (r.startsWith("keepsake:")) {
                    var k = Catalog.KEEPSAKES.get(r.substring(9));
                    home.keep(k);
                    ryo += 80;
                } else home.place(r.substring(6));
            }
            if (d == 8 && w.level(Cast.TEAMMATE_A) >= 3) home.keep(Catalog.KEEPSAKES.get("keepsake_bond_teammate_a_1"));
            if (d == 5) home.pet("ninken");
            if (d == 30) home.place("goldfish_bowl");
            if (PHOTOS.containsKey(d)) {
                var people = rank == 0 ? Cast.CLASSMATES : List.of(Cast.TEAMMATE_A, Cast.TEAMMATE_B, Cast.SENSEI);
                home.photo(PHOTOS.get(d), d, people, "child");
            }

            if (!away) {
                // Morning at home: the mailbox, breakfast from the cupboard, the plant.
                home.mailbox.collect();
                var meal = rng.chance(.3) ? home.pantry.eatOldest(d) : home.pantry.eat(d, null);
                if (meal != null) { home.mess(1, "meal"); if (!meal.freshness().equals("fresh")) staleMeals++; }
                if (rng.chance(.6)) home.plant.water(d);
                if (d % 3 == 0) { for (String food : List.of("milk", "bread", "onigiri", "instant_ramen", "instant_ramen", "vegetables")) home.pantry.store(food, d, 1); ryo -= 25; }
                // A free afternoon at the furniture shop now and then.
                if (d % 2 == 0 || cRankReturn(d)) {
                    int bought = 0;
                    for (var it = wishlist.iterator(); it.hasNext(); ) {
                        var p = Catalog.piece(it.next());
                        boolean inShops = p.slice().equals("b1") || (p.slice().equals("b2") && d >= BETA2 && (!p.set().equals("festival") || d >= 30));
                        if (!inShops || ryo - p.price() < 60) continue;
                        if (home.place(p.id()).equals("ok")) { ryo -= p.price(); spent += p.price(); bought++; }
                        it.remove();
                        if (bought >= 3) break;
                    }
                }
                for (var k : home.owned()) home.display(k.id());
                for (String m : home.album().keySet()) home.hang(m);
            }

            // The evening: when they get home, what they eat, practice, cleaning, bed.
            int back = away ? 24 : d == 4 ? 23 : 18 + (int) (rng.unit() * 3);
            int bed = away ? -1 : d == 4 ? 2 : rng.chance(.85) ? 22 : rng.chance(.6) ? 0 : 2;
            var atHome = new boolean[24];
            if (!awayMorning) for (int h = 0; h < 8; h++) atHome[h] = true;
            if (!away) for (int h = back; h < 24; h++) atHome[h] = true;
            if (!away) {
                double roll = rng.unit();
                if (roll < .3) { if (home.pantry.eat(d, "instant_ramen") != null) home.mess(1, "ramen_cup"); }
                else if (roll < .5 && home.has("cooking_pot")) home.mess(2, "cooking");
                else if (roll < .6) { var m = home.pantry.eatOldest(d); if (m != null) { home.mess(1, "meal"); if (!m.freshness().equals("fresh")) staleMeals++; } }
                if (rng.chance(.3)) practice.session(home, Comfort.of(home, d, season, ""), d, rng.chance(.5) ? "dummy" : "signs", .5);
            }
            var day = new Visits.Day(d, season, rank, "", atHome, (dRank(d) || cRankReturn(d)) && !away, Cast.SQUAD, Cast.SENSEI, Cast.INSTRUCTOR, Cast.NEIGHBOURS);
            var visits = new ArrayList<>(Visits.daily(seed, home, f, day));
            // Hosting: now and then the player has friends over.
            if (!away && d % 8 == 5 && back <= 19) {
                var guests = Cast.CLASSMATES.stream().filter(x -> w.level(x) >= (rank == 0 ? 2 : 3)).limit(2).toList();
                if (!guests.isEmpty()) visits.add(Visits.host(home, f, day, guests, rank == 0 ? "study_night" : "cook_together", 19));
            }
            for (String who : Cast.CLASSMATES) if (home.keys().size() < 1 && w.level(who) >= Home.KEY_LEVEL) if (Visits.giveKey(home, f, who, d).equals("ok")) keys++;
            for (var v : visits) {
                String kind = v.kind().replace(".waited_inside", "").replaceAll("^neighbour\\..*", "neighbour").replaceAll("^hosted\\..*", "hosted");
                if (v.kind().startsWith("hosted") && !v.met()) continue;
                byKind.merge(kind, 1, Integer::sum);
                sliceVisits.merge(kind, 1, Integer::sum);
                if (v.met()) sl[2]++; else if (!kind.equals("left_food") && !kind.equals("tidied")) sl[3]++;
                if (kind.equals("hosted")) sl[4]++;
            }
            if (!away) {
                if (home.tidiness() == Home.Tidiness.MESSY) { messyEvenings++; if (rng.chance(.5)) home.clean(); }
                else if (home.tidiness() == Home.Tidiness.LIVED_IN && rng.chance(.15)) home.clean();
                var score = Comfort.of(home, d, season, "");
                var rest = Rest.sleep(score, bed, true);
                sl[0]++;
                if (rest.any()) { sl[5]++; sd[1] += rest.regen(); }
                int awake = 0;
                for (int h = 6; h < 24; h++) if (atHome[h] && (h < 8 || h < (bed >= 18 ? bed : 24))) awake++;
                sd[0] += awake * HOUR_SECONDS / 60;
            } else sl[1]++;
            var score = Comfort.of(home, d, season, "");
            home.endDay(d, season, score);
            if (d % 3 == 0 || d == DAYS - 1)
                snaps.add(new Snapshot(d, score.comfort(), score.tier().id(), score.style(), home.placed().size(), spent, String.join(",", score.perks()),
                        home.displayed().size(), home.wall().size(), home.plant.stage().name().toLowerCase()));
            if (System.getProperty("levels") != null && d % 6 == 0) {
                var sb = new StringBuilder("day " + d + ":");
                for (String who : List.of(Cast.TEAMMATE_A, Cast.TEAMMATE_B, Cast.CLASSMATE_C, Cast.CLASSMATE_D, Cast.RIVAL, Cast.SENSEI, Cast.INSTRUCTOR, Cast.LANDLADY))
                    sb.append(' ').append(who.replace("role:", "").replace("resident:", "")).append('=').append(w.level(who));
                System.out.println(sb);
            }
            w.endDay();
        }
        slices.add(new Slice(current, sliceDays(current), sl[0], sl[1], sd[0], Map.copyOf(sliceVisits), sl[2], sl[3], sl[4], sl[5], sd[1]));
        return new Result(slices, snaps, ryo, spent, home.cleanings(), messyEvenings, staleMeals, keys,
                home.plant.stage().name().toLowerCase(), practice.total(), home.storageSlots(), byKind);
    }
    static int sliceDays(String s) { return s.equals("Beta 1") ? BETA2 : s.equals("Beta 2") ? BETA3 - BETA2 : DAYS - BETA3; }

    public static void main(String[] args) {
        long seed = args.length > 0 ? Long.parseLong(args[0]) : 20261029;
        var r = run(seed);
        System.out.printf("%n## A typical player's first 15 hours (seed %d)%n%n", seed);
        System.out.println("| Slice | Days | Nights home / away | Minutes awake at home a day | Visits a week | Met / notes | Hosted | Well Rested nights | Mean bonus |");
        System.out.println("|---|---|---|---|---|---|---|---|---|");
        for (var s : r.slices()) {
            int total = s.visits().values().stream().mapToInt(Integer::intValue).sum();
            System.out.printf("| %s | %d | %d / %d | %.1f | %.1f | %d / %d | %d | %d | +%.0f%% |%n", s.name(), s.days(), s.nightsHome(), s.nightsAway(),
                    s.homeMinutes() / Math.max(1, s.nightsHome()), total * 7.0 / s.days(), s.met(), s.notes(), s.hosted(), s.rested(),
                    100 * s.regen() / Math.max(1, s.rested()));
        }
        System.out.println("\nVisits by kind, whole beta: " + r.visitsByKind());
        for (var s : r.slices()) System.out.println("  " + s.name() + ": " + new TreeMap<>(s.visits()));
        System.out.println("\n| Day | Comfort | Tier | Style | Pieces | Ryo spent | Keepsakes shown | Photos hung | Plant | Perks |");
        System.out.println("|---|---|---|---|---|---|---|---|---|---|");
        for (var c : r.comfort())
            System.out.printf("| %d | %.1f | %s | %.1f | %d | %d | %d | %d | %s | %s |%n", c.day(), c.comfort(), c.tier(), c.style(), c.pieces(), c.spent(),
                    c.keepsakes(), c.photos(), c.plant(), c.perks());
        System.out.printf("%nCleanings %d, messy evenings %d, stale meals %d, keys given %d, home practice %.1f training-ground hours, chest slots %d%n",
                r.cleanings(), r.messyEvenings(), r.staleMeals(), r.keys(), r.practice(), r.storageSlots());
        System.out.printf("Ryo at the end %d, spent on furniture %d%n", r.ryoEnd(), r.spent());
    }

    private FirstFifteenHours() {}
}
