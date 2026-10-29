package dev.shinobi.life.economy.sim;

import dev.shinobi.life.economy.Catalogue;
import dev.shinobi.life.economy.Json;
import dev.shinobi.life.economy.Prices;
import dev.shinobi.life.economy.Streams;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import static dev.shinobi.life.economy.Json.integer;
import static dev.shinobi.life.economy.Json.list;
import static dev.shinobi.life.economy.Json.num;
import static dev.shinobi.life.economy.Json.obj;
import static dev.shinobi.life.economy.Json.str;

/**
 * Plays the beta's 48 in-game days of ryo (economy.json "calendar": Beta 1 days 1 to 12, Beta 2 13 to 36, Beta 3
 * 37 to 48) for a frugal, a typical and a spending player, and reports their ryo against ROADMAP's rules of thumb:
 * a day of D-ranks covers food and leaves about half, and the first proper furniture set takes about a week.
 *
 * <p>Each day: income (the welcome purse, the orphan's stipend, part-time shifts, board missions, story and board
 * C-ranks with their camp loot, side quests by the day they open, small favours), then the day's meals at shop
 * prices (or a home-cooked meal at its ingredients' price), mission upkeep (thrown tools and medicine used up) and
 * tools lost on a death, then the profile's wishlist in order, keeping a few days of food in reserve. Everything a
 * profile does is from economy.json; every roll is from a seed stream, so a seed always plays out the same way.
 *
 * <pre>./gradlew :life:economy:simulate [-Pseed=N] [-Pdaily=typical]</pre>
 */
public final class EconomySim {
    public record Day(int day, String slice, int earned, int spent, int balance) {}
    public record Result(String profile, List<Day> days, Map<String, Integer> earnedBy, Map<String, Integer> spentBy,
                         Map<String, Integer> boughtOn, int starterSetDay, int hungryDays, int minBalance) {
        public int finalBalance() { return days.getLast().balance(); }
        public int earned() { return earnedBy.values().stream().mapToInt(Integer::intValue).sum(); }
        public int spent() { return spentBy.values().stream().mapToInt(Integer::intValue).sum(); }
        public int balanceOn(int day) { return days.get(day - 1).balance(); }
    }

    private final Catalogue c;
    private final Prices prices;
    private final Map<String, Object> eco;
    private final Map<String, Integer> outfitPrices = new HashMap<>();

    public EconomySim(Catalogue catalogue, Path dataDir) {
        this.c = catalogue;
        this.prices = new Prices(catalogue);
        this.eco = catalogue.economy;
        try {
            var outfits = obj(Json.parse(Files.readString(dataDir.resolve("outfits.json"))));
            obj(outfits.get("prices")).forEach((k, v) -> outfitPrices.put(k, integer(v, 0)));
        } catch (IOException e) {
            throw new java.io.UncheckedIOException(e);
        }
    }

    // -- the calendar ------------------------------------------------------------------------------------------------

    public String slice(int day) {
        for (var e : obj(eco.get("calendar")).entrySet()) {
            var range = list(e.getValue());
            if (day >= integer(range.get(0), 0) && day <= integer(range.get(1), 0)) return e.getKey();
        }
        return "later";
    }
    public int lastDay() {
        int last = 0;
        for (var range : obj(eco.get("calendar")).values()) last = Math.max(last, integer(list(range).get(1), 0));
        return last;
    }
    static String rank(String slice) { return slice.equals("beta1") ? "academy" : "genin"; }
    /** The player's standing title by day: the sim's stand-in for the bond engine's standing, used for discounts. */
    static String title(int day) { return day < 8 ? "newcomer" : day < 26 ? "helping_hand" : "good_neighbor"; }

    // -- daily costs -------------------------------------------------------------------------------------------------

    /** What one meal costs: a shop dish at its price, or a home-cooked bundle at its ingredients' price. */
    public double mealCost(String meal, String slice, int day) {
        var bundles = obj(eco.get("meal_bundles"));
        if (bundles.containsKey(meal)) {
            var b = obj(bundles.get(meal));
            if (b.containsKey("item")) return prices.buy(str(b.get("item"), ""), null, "standard", title(day), 0) / num(b.get("every_days"), 1);
            String recipe = str(b.getOrDefault(slice, b.get("recipe")), "");
            var r = c.recipes.get(recipe);
            if (r == null) throw new IllegalArgumentException("meal bundle " + meal + " names unknown recipe " + recipe);
            return (c.inputCost(r) - (r.vessel() == null ? 0 : c.item(r.vessel()).price())) / (double) r.count();
        }
        return prices.buy(meal, null, "standard", title(day), 0);
    }
    /** A day's meals for a profile in a slice. */
    public int dailyFood(String profile, String slice, int day) {
        double total = 0;
        for (Object meal : list(obj(obj(profile(profile).get("meals"))).get(slice))) total += mealCost((String) meal, slice, day);
        return (int) Math.round(total);
    }
    /** Thrown tools and medicine a mission of a rank uses up. */
    public int upkeep(String missionRank) {
        double total = 0;
        for (var e : obj(obj(eco.get("upkeep")).get(missionRank)).entrySet()) total += c.item(e.getKey()).price() * num(e.getValue(), 0);
        return (int) Math.round(total);
    }
    int deathLoss() {
        double total = 0;
        for (var e : obj(obj(eco.get("upkeep")).get("death_tool_loss")).entrySet()) total += c.item(e.getKey()).price() * num(e.getValue(), 0);
        return (int) Math.round(total);
    }

    /**
     * The first rule of thumb: on a day of D-ranks (economy.json rule_of_thumb, two by default) at Beta 2's mean
     * pay, the share left after the profile's food and the missions' upkeep.
     */
    public double dRankDayLeft(String profile, int day) {
        var rule = obj(obj(eco.get("rule_of_thumb")).get("d_rank_day"));
        int missions = integer(rule.get("missions"), 2);
        double income = missions * num(obj(obj(eco.get("missions")).get("d")).get("beta2_mean"), 85);
        double costs = dailyFood(profile, slice(day), day) + missions * upkeep("d");
        return (income - costs) / income;
    }

    // -- the run -----------------------------------------------------------------------------------------------------

    Map<String, Object> profile(String name) { return obj(obj(eco.get("profiles")).get(name)); }

    public Result run(String profileName, long seed) {
        var p = profile(profileName);
        var income = obj(eco.get("income"));
        var missions = obj(eco.get("missions"));
        var days = new ArrayList<Day>();
        var earnedBy = new LinkedHashMap<String, Integer>();
        var spentBy = new LinkedHashMap<String, Integer>();
        var boughtOn = new LinkedHashMap<String, Integer>();
        var jobShifts = new HashMap<String, Integer>();
        var lastRecurring = new HashMap<String, Integer>();
        var setPieces = starterSet();
        int balance = 0, hungry = 0, minBalance = 0, starterDay = -1;
        double shiftAcc = 0, dAcc = 0, favourAcc = 0;
        int jobTurn = 0;
        var deathDays = deathDays(p, seed);

        for (int day = 1; day <= lastDay(); day++) {
            String slice = slice(day), rank = rank(slice);
            int earned = 0, spent = 0;
            var today = new TreeMap<String, Integer>();

            // Income.
            var purse = obj(income.get("welcome_purse"));
            if (day == integer(purse.get("day"), 1)) today.merge("welcome purse", integer(purse.get("ryo"), 0), Integer::sum);
            var stipend = obj(eco.get("stipend"));
            if (day >= integer(stipend.get("from_day"), 2) && (stipend.get("until") == null || day <= integer(stipend.get("until"), 0)))
                today.merge("stipend", integer(stipend.get("amount"), 0), Integer::sum);
            shiftAcc += num(obj(p.get("shifts_per_day")).get(slice), 0);
            var jobsOpen = c.jobs.values().stream().filter(j -> j.rank().equals(rank) || (rank.equals("genin") && j.rank().equals("academy")))
                    .filter(j -> dev.shinobi.life.economy.Ladder.sliceAllows(slice, j.slice())).toList();
            while (shiftAcc >= 1 && !jobsOpen.isEmpty()) {
                shiftAcc -= 1;
                var job = jobsOpen.get(jobTurn++ % jobsOpen.size());
                int done = jobShifts.merge(job.id(), 1, Integer::sum) - 1;
                today.merge("jobs", shiftPay(job.pay(), done), Integer::sum);
            }
            if (day >= 14) dAcc += num(obj(p.get("d_per_day")).get(slice), 0);
            int dToday = 0;
            var d = obj(missions.get("d"));
            while (dAcc >= 1) {
                dAcc -= 1;
                var rng = Streams.stream(seed, "missions", "board.d|" + day + "|" + dToday);
                int mean = integer(d.get("beta2_mean"), 85), spread = 25;
                int pay = Math.clamp(mean - spread + rng.below(2 * spread + 1), integer(d.get("min"), 60), integer(d.get("max"), 150));
                today.merge("D-ranks", pay, Integer::sum);
                dToday++;
            }
            int cToday = 0;
            for (Object o : list(income.get("board_c"))) if (integer(obj(o).get("day"), 0) == day) {
                today.merge("C-ranks", integer(obj(o).get("ryo"), 0), Integer::sum);
                cToday++;
            }
            for (Object o : list(income.get("chapters"))) if (integer(obj(o).get("day"), 0) == day) {
                today.merge("chapters", integer(obj(o).get("ryo"), 0), Integer::sum);
                if (!str(obj(o).get("id"), "").equals("main.ch20")) cToday++;
            }
            if (cToday > 0) today.merge("camp loot (pawn)", cToday * integer(missions.get("camp_loot_pawn_value"), 0), Integer::sum);
            double share = num(p.get("side_share"), 0.7);
            for (Object o : list(income.get("side"))) {
                var q = obj(o);
                if (integer(q.get("day"), 0) == day && Streams.roll(seed, "sidequests", profileName, str(q.get("id"), "")) < share)
                    today.merge("side quests", integer(q.get("ryo"), 0), Integer::sum);
            }
            var favour = obj(income.get("favour"));
            if (day >= integer(favour.get("from_day"), 4)) favourAcc += num(p.get("favour_per_day"), 0);
            while (favourAcc >= 1) { favourAcc -= 1; today.merge("favours", integer(favour.get("ryo"), 20), Integer::sum); }
            for (var e : today.entrySet()) { earned += e.getValue(); earnedBy.merge(e.getKey(), e.getValue(), Integer::sum); }
            balance += earned;

            // Upkeep: meals, then what missions and deaths used up.
            int usual = dailyFood(profileName, slice, day), food = usual;
            if (balance < 2 * usual) food = fallbackFood(day);   // short of ryo, a player eats onigiri until pay comes in
            if (balance >= food) { balance -= food; spent += food; spentBy.merge("food", food, Integer::sum); }
            else { hungry++; spent += balance; spentBy.merge("food", balance, Integer::sum); balance = 0; }
            int tools = dToday * upkeep("d") + cToday * upkeep("c") + (deathDays.contains(day) ? deathLoss() : 0);
            int paidTools = Math.min(balance, tools);
            balance -= paidTools; spent += paidTools; spentBy.merge("tools and medicine", paidTools, Integer::sum);

            // The wishlist, keeping a few days of food in reserve.
            int reserve = integer(p.get("reserve_days"), 3) * usual;
            var occurrences = new HashMap<String, Integer>();
            for (Object w : list(p.get("wishlist"))) {
                String wish = (String) w;
                int occurrence = occurrences.merge(wish, 1, Integer::sum) - 1;
                var def = obj(obj(eco.get("wishes")).get(wish));
                if (day < integer(def.get("from_day"), 0)) continue;
                int every = integer(def.get("every_days"), 0);
                if (every > 0) {
                    int last = lastRecurring.getOrDefault(wish, -999);
                    int price = wishPrice(def, day);
                    if (day - last >= every && balance - price >= reserve) {
                        balance -= price; spent += price; spentBy.merge(sink(def), price, Integer::sum); lastRecurring.put(wish, day);
                        boughtOn.putIfAbsent(wish, day);
                    }
                    continue;
                }
                String key = wish + "#" + occurrence;
                if (boughtOn.containsKey(key)) continue;
                if (str(def.get("kind"), "").equals("set")) {
                    while (!setPieces.isEmpty()) {
                        var piece = setPieces.getFirst();
                        int price = prices.buy(piece, c.shops.get("furniture_shop"), "standard", title(day), 0);
                        if (balance - price < reserve) break;
                        balance -= price; spent += price; spentBy.merge("furniture", price, Integer::sum);
                        setPieces.removeFirst();
                    }
                    if (!setPieces.isEmpty()) break;
                    boughtOn.put(key, day);
                    starterDay = day;
                    continue;
                }
                int price = wishPrice(def, day);
                if (balance - price < reserve) break;
                balance -= price; spent += price; spentBy.merge(sink(def), price, Integer::sum);
                boughtOn.put(key, day);
            }
            minBalance = Math.min(minBalance, balance);
            days.add(new Day(day, slice, earned, spent, balance));
        }
        var bought = new LinkedHashMap<String, Integer>();
        boughtOn.forEach((k, v) -> bought.put(k.replaceAll("#0$", ""), v));
        return new Result(profileName, days, earnedBy, spentBy, bought, starterDay, hungry, minBalance);
    }

    /** The meals a player falls back on when the usual ones are too dear (economy.json fallback_meals). */
    int fallbackFood(int day) {
        double total = 0;
        for (Object meal : list(eco.get("fallback_meals"))) total += mealCost((String) meal, slice(day), day);
        return (int) Math.round(total);
    }

    int shiftPay(int base, int done) {
        var j = obj(eco.get("jobs"));
        int raises = 0;
        for (Object at : list(j.get("raise_at"))) if (done >= integer(at, 0)) raises++;
        return (int) Math.min(num(j.get("cap"), 80), Math.round(base * (1 + num(j.get("raise"), .1) * raises)));
    }

    int wishPrice(Map<String, Object> def, int day) {
        return switch (str(def.get("kind"), "")) {
            case "service" -> c.services.get(str(def.get("id"), "")).price();
            case "outfit" -> outfitPrices.getOrDefault(str(def.get("rank"), "genin"), 0);
            case "budget" -> integer(def.get("ryo"), 0);
            case "item" -> {
                int total = 0;
                for (var e : obj(def.get("items")).entrySet()) {
                    String key = e.getKey();
                    int base = prices.buy(key, null, "standard", title(day), 0);
                    total += (int) Math.round(base * (1 - num(def.get("nature_discount"), 0))) * integer(e.getValue(), 1);
                }
                yield total;
            }
            default -> throw new IllegalArgumentException("unknown wish kind " + def.get("kind"));
        };
    }
    static String sink(Map<String, Object> def) {
        return switch (str(def.get("kind"), "")) {
            case "service" -> "services";
            case "outfit" -> "outfits";
            case "budget" -> str(def.get("sink"), "goods");
            default -> "goods";
        };
    }

    /** The furniture marked set=starter, each as many times as its count, in catalogue order. */
    public List<String> starterSet() {
        var pieces = new ArrayList<String>();
        for (var item : c.items.values())
            if (item.prop("set").equals("starter")) for (int i = 0; i < Math.max(1, parseInt(item.prop("count"))); i++) pieces.add(item.id());
        return pieces;
    }
    public int starterSetPrice() { return starterSet().stream().mapToInt(id -> c.item(id).price()).sum(); }
    private static int parseInt(String s) { return s.isEmpty() ? 1 : Integer.parseInt(s); }

    private java.util.Set<Integer> deathDays(Map<String, Object> p, long seed) {
        var out = new java.util.HashSet<Integer>();
        double rate = num(p.get("deaths_per_slice"), 1);
        for (String slice : List.of("beta2", "beta3")) {
            var range = list(obj(eco.get("calendar")).get(slice));
            int from = integer(range.get(0), 0), to = integer(range.get(1), 0);
            var rng = Streams.stream(seed, "deaths", slice);
            int n = (int) rate + (rng.unit() < rate - (int) rate ? 1 : 0);
            for (int i = 0; i < n; i++) out.add(from + rng.below(to - from + 1));
        }
        return out;
    }

    // -- the report --------------------------------------------------------------------------------------------------

    public static void main(String[] args) {
        Path dir = Path.of(args.length > 0 ? args[0] : "data/items");
        long seed = args.length > 1 ? Long.parseLong(args[1]) : 20261029L;
        var catalogue = Catalogue.load(dir);
        var sim = new EconomySim(catalogue, dir);
        String daily = System.getProperty("daily", "");
        System.out.printf("The beta's ryo, seed %d. The first furniture set (set=starter) costs %d ryo: %s%n%n", seed,
                sim.starterSetPrice(), String.join(", ", sim.starterSet()));
        System.out.println("Rule of thumb 1, a day of D-ranks leaves (food and upkeep paid):");
        for (String profile : List.of("frugal", "typical", "spender"))
            System.out.printf("  %-8s %3.0f%% of %d ryo (food %d, upkeep %d a mission)%n", profile, 100 * sim.dRankDayLeft(profile, 20),
                    2 * integer(obj(obj(catalogue.economy.get("missions")).get("d")).get("beta2_mean"), 85),
                    sim.dailyFood(profile, "beta2", 20), sim.upkeep("d"));
        System.out.println();
        for (String profile : List.of("frugal", "typical", "spender")) {
            var r = sim.run(profile, seed);
            System.out.printf("== %s: earned %d, spent %d, ends with %d; first furniture set on day %d; hungry days %d%n",
                    profile, r.earned(), r.spent(), r.finalBalance(), r.starterSetDay(), r.hungryDays());
            System.out.println("   ryo at the end of Beta 1 (day 12): " + r.balanceOn(12) + ", Beta 2 (day 36): " + r.balanceOn(36)
                    + ", Beta 3 (day 48): " + r.balanceOn(48));
            System.out.println("   earned: " + r.earnedBy());
            System.out.println("   spent:  " + r.spentBy());
            System.out.println("   bought: " + r.boughtOn());
            if (daily.equals(profile) || daily.equals("all")) {
                System.out.println("   day slice   earned  spent  balance");
                for (var d : r.days()) System.out.printf("   %3d %-7s %6d %6d %8d%n", d.day(), d.slice(), d.earned(), d.spent(), d.balance());
            }
            System.out.println();
        }
    }
}
