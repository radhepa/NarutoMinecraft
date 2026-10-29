package dev.shinobi.village.dialogue.sim;

import dev.shinobi.village.dialogue.Bank;
import dev.shinobi.village.dialogue.Conditions;
import dev.shinobi.village.dialogue.Context;
import dev.shinobi.village.dialogue.Heard;
import dev.shinobi.village.dialogue.Names;
import dev.shinobi.village.dialogue.Talk;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Set;
import java.util.TreeMap;

/**
 * Plays the beta's talk against the real compiled bank (DIALOGUE.md, "Simulation"): a village of 300 residents by the
 * population weights plus the beta's cast, and a player who talks at a realistic rate for the beta's in-game days.
 * Reports how often a request finds nothing fresh (a repeat the player would notice), how often speakers reach their
 * budget, the filler share, which pools run lowest, and the ledger's size.
 *
 * <pre>./gradlew :village:dialogue:simulate [-Pseed=N]</pre>
 */
public final class BetaTalk {
    static final List<String> ARCH = List.of("warmhearted", "thoughtful", "playful", "adventurous", "meticulous", "steadfast", "reserved",
            "imaginative", "pragmatic", "curious", "protective", "gentle", "proud", "fiery", "shy", "stern");
    static final List<String> NOBLE = List.of("uchiha", "hyuga", "nara", "akimichi", "yamanaka", "inuzuka", "aburame", "sarutobi", "shimura",
            "yuhi", "gekko", "senju", "uzumaki", "kurama", "hatake");
    static final int[] NOBLE_W = {15, 15, 12, 12, 12, 12, 12, 8, 5, 5, 5, 4, 4, 4, 2};
    static final List<String> MINOR = List.of("shiranui", "morino", "umino", "haruno", "namiashi", "hagane", "kinoshita", "tsuchigumo", "suzuran", "tobari");
    static final int[] MINOR_W = {17, 17, 17, 17, 17, 17, 17, 10, 10, 10};
    static final List<String> JOBS = List.of("ramen_cook", "cook", "grocer", "fishmonger", "farmer", "carpenter", "tailor", "smith", "florist",
            "teacher", "medic", "nurse", "merchant", "librarian", "tea_master", "bath_keeper", "pawnbroker", "vet", "priest", "painter",
            "courier", "dango_maker", "barbecue_cook", "ferryman", "herbalist", "kennel_keeper");
    static final List<String> DISTRICTS = List.of("market", "main_street", "residential", "academy", "gate", "training", "hospital", "shrine",
            "river", "clan_quarter", "apartments", "hokage_rock");
    static final List<String> TOPICS = List.of("small_talk", "food", "training", "compliment", "village_news", "their_hobby", "their_family",
            "your_story", "tease", "their_values", "ask_advice", "their_dream", "their_worries");
    static final int[] TOPIC_LEVEL = {0, 1, 1, 1, 3, 2, 4, 4, 4, 5, 5, 6, 7};

    record Person(String id, String personality, String group, String clan, String rank, String stage, String job, String district, String tier) {}

    /** How a player talks: residents met per time of day, topics per conversation, questions answered. */
    record Player(String name, int days, int residentsPerPeriod, int castPerDay, int topicsMin, int topicsMax) {}

    public static void main(String[] args) {
        long seed = args.length > 0 ? Long.parseLong(args[0]) : 20261029L;
        var bank = Bank.load(Path.of(System.getProperty("dialogue.bank", "src/main/resources/data/narutominecraft/dialogue")));
        System.out.printf("Bank: %,d lines in %,d pools, %d questions (ids up to %,d)%n%n", bank.lineCount(), bank.poolKeys().size(),
                bank.questions().size(), bank.maxId());
        var players = List.of(
                new Player("thorough (beta, 75 days)", 75, 3, 4, 1, 3),
                new Player("talks to everyone (beta, 75 days)", 75, 8, 7, 3, 6),
                new Player("thorough, whole game on beta pools (300 days)", 300, 3, 4, 1, 3));
        for (var p : players) run(bank, p, seed);
    }

    static void run(Bank bank, Player player, long seed) {
        var r = new Random(seed);
        var village = village(r);
        var cast = cast();
        var heard = new Heard();
        var names = names();
        var talk = new Talk(bank, heard, Conditions.basic(heard, Set.of()), names);
        var contact = new HashMap<String, Integer>();
        var stats = new TreeMap<String, int[]>(); // topic family -> requests, fresh, budget, exhausted
        int conversations = 0, budgetConversations = 0, questions = 0, contradictions = 0;
        int firstExhausted = -1;
        var fillCounts = new int[2];
        for (int day = 1; day <= player.days(); day++) {
            var world = world(day, r);
            for (String period : List.of("morning", "afternoon", "evening")) {
                String district = DISTRICTS.get(r.nextInt(DISTRICTS.size()));
                var here = new ArrayList<Person>();
                for (var p : village) if (p.district().equals(district) || r.nextInt(12) == 0) here.add(p);
                // Known faces first: the player returns to people they like, and meets someone new now and then.
                here.sort((a, b) -> Integer.compare(contact.getOrDefault(b.id(), 0), contact.getOrDefault(a.id(), 0)));
                int n = Math.min(player.residentsPerPeriod(), here.size());
                var met = new ArrayList<Person>();
                for (int k = 0; k < n; k++) met.add(r.nextInt(3) == 0 ? here.get(r.nextInt(here.size())) : here.get(k));
                if (period.equals("morning")) for (int k = 0; k < player.castPerDay(); k++) met.add(cast.get(r.nextInt(cast.size())));
                for (var p : met) {
                    int days = contact.merge(p.id(), 1, Integer::sum);
                    int level = p.tier().equals("cast") ? Math.min(9, 1 + days / 6) : Math.min(7, days / 4);
                    var c = context(p, world, period, district, level, day);
                    conversations++;
                    boolean hitBudget = false;
                    var g = talk.greet(p.id(), c, day, r);
                    String who = p.stage().equals("child") ? (p.tier().equals("cast") ? " (child cast)" : " (children)") : p.tier().equals("cast") ? " (adult cast)" : "";
                    hitBudget |= count(stats, "greet" + who, g);
                    if (g.why() == Talk.Why.EXHAUSTED && firstExhausted < 0) firstExhausted = day;
                    int topics = player.topicsMin() + r.nextInt(player.topicsMax() - player.topicsMin() + 1);
                    for (int t = 0; t < topics; t++) {
                        Talk.Said s;
                        String fam;
                        int roll = r.nextInt(10);
                        if (roll == 0 && level >= 1) {
                            var q = talk.ask(p.id(), c, day, r);
                            if (q != null) {
                                var a = talk.answer(p.id(), q, q.answers().get(r.nextInt(q.answers().size())).id(), c, day);
                                questions++;
                                if (a.contradicts() != null) contradictions++;
                                continue;
                            }
                        }
                        if (roll < 6) { s = talk.chat(p.id(), c, day, r); fam = "chat"; }
                        else {
                            int k = r.nextInt(TOPICS.size());
                            if (TOPIC_LEVEL[k] > level) k = 0;
                            String key = "talk." + TOPICS.get(k);
                            s = talk.topic(p.id(), key, c, day, r);
                            fam = k == 0 ? "chat" : "talk";
                        }
                        hitBudget |= count(stats, fam + who, s);
                        if (s.line() != null && s.fresh()) fillCounts[s.line().filler() ? 1 : 0]++;
                        if (s.why() == Talk.Why.EXHAUSTED && firstExhausted < 0) firstExhausted = day;
                        if (s.ended()) break;
                    }
                    if (hitBudget) budgetConversations++;
                }
            }
        }
        System.out.println("== " + player.name());
        System.out.printf("%,d conversations with %d people; %d questions answered (%d contradicting an earlier answer)%n", conversations,
                contact.size(), questions, contradictions);
        System.out.println("| Requests | Asked | Fresh | Past the budget | Nothing fresh left (a repeat) |");
        System.out.println("|---|---|---|---|---|");
        int[] all = new int[4];
        for (var e : stats.entrySet()) {
            var v = e.getValue();
            for (int k = 0; k < 4; k++) all[k] += v[k];
            row(e.getKey(), v);
        }
        row("all", all);
        System.out.printf("Conversations that reached a speaker's budget: %.1f%%; first day anything ran dry: %s%n",
                100.0 * budgetConversations / Math.max(1, conversations), firstExhausted < 0 ? "never" : "day " + firstExhausted);
        System.out.printf("Filler share of fresh lines: %.1f%%; lines heard: %,d; ledger size: %,d bytes%n",
                100.0 * fillCounts[1] / Math.max(1, fillCounts[0] + fillCounts[1]), heard.heardCount(), heard.size());
        lowest(bank, heard);
        System.out.println();
    }

    static boolean count(Map<String, int[]> stats, String family, Talk.Said s) {
        var v = stats.computeIfAbsent(family, k -> new int[4]);
        v[0]++;
        if (s.fresh()) v[1]++;
        else if (s.why() == Talk.Why.BUDGET) v[2]++;
        else v[3]++;
        return s.why() == Talk.Why.BUDGET;
    }
    static void row(String name, int[] v) {
        System.out.printf("| %s | %,d | %,d (%.1f%%) | %,d (%.1f%%) | %,d (%.2f%%) |%n", name, v[0], v[1], pct(v[1], v[0]), v[2], pct(v[2], v[0]),
                v[3], pct(v[3], v[0]));
    }
    static double pct(int a, int b) { return 100.0 * a / Math.max(1, b); }

    /** The pools most used up, among those the talk draws from. */
    static void lowest(Bank bank, Heard heard) {
        var used = new ArrayList<Object[]>();
        for (String k : bank.poolKeys()) {
            if (!(k.startsWith("greet.") || k.startsWith("chat.") || k.startsWith("talk."))) continue;
            int total = 0, h = 0;
            for (var l : bank.pool(k)) { if (l.kind() != dev.shinobi.village.dialogue.Line.Kind.LINE) continue; total++; if (heard.heard(l.id())) h++; }
            if (total >= 5) used.add(new Object[] {k, h, total});
        }
        used.sort((a, b) -> Double.compare((int) b[1] / (double) (int) b[2], (int) a[1] / (double) (int) a[2]));
        var b = new StringBuilder("Most used pools:");
        for (int k = 0; k < Math.min(8, used.size()); k++) b.append(String.format(" %s %d/%d;", used.get(k)[0], (int) used.get(k)[1], (int) used.get(k)[2]));
        System.out.println(b);
    }

    static List<Person> village(Random r) {
        var out = new ArrayList<Person>();
        for (int k = 0; k < 300; k++) {
            int roll = r.nextInt(1000);
            String group, clan = null;
            if (roll < 450) group = "civilian";
            else if (roll < 730) group = "clanless";
            else if (roll < 870) { group = "minor"; clan = pick(MINOR, MINOR_W, r); }
            else { group = "noble"; clan = pick(NOBLE, NOBLE_W, r); }
            boolean child = r.nextInt(100) < 15;
            String rank = child ? "academy" : group.equals("civilian") ? "civilian" : List.of("genin", "genin", "chunin", "chunin", "chunin", "jonin").get(r.nextInt(6));
            String job = child ? null : group.equals("civilian") || r.nextInt(4) == 0 ? JOBS.get(r.nextInt(JOBS.size())) : null;
            String tier = k < 30 ? "named" : "resident";
            out.add(new Person("resident:" + k, ARCH.get(r.nextInt(ARCH.size())), group, clan, rank, child ? "child" : "adult", job,
                    DISTRICTS.get(r.nextInt(DISTRICTS.size())), tier));
        }
        return out;
    }
    static List<Person> cast() {
        return List.of(
                new Person("role:sensei", "reserved", "clanless", null, "jonin", "adult", null, "training", "cast"),
                new Person("role:instructor", "warmhearted", "clanless", null, "chunin", "adult", "teacher", "academy", "cast"),
                new Person("role:medic", "gentle", "clanless", null, "chunin", "adult", "medic", "hospital", "cast"),
                new Person("role:teammate_a", "shy", "noble", "kurama", "genin", "child", null, "academy", "cast"),
                new Person("role:teammate_b", "fiery", "clanless", null, "genin", "child", null, "academy", "cast"),
                new Person("role:classmate_c", "thoughtful", "minor", "kinoshita", "genin", "child", null, "academy", "cast"),
                new Person("role:classmate_d", "protective", "noble", "gekko", "genin", "child", null, "academy", "cast"),
                new Person("role:rival", "proud", "noble", "uchiha", "genin", "child", null, "academy", "cast"),
                new Person("role:merchant", "pragmatic", "civilian", null, "civilian", "adult", "merchant", "market", "cast"));
    }
    static String pick(List<String> items, int[] w, Random r) {
        int total = 0;
        for (int x : w) total += x;
        int roll = r.nextInt(total);
        for (int k = 0; k < w.length; k++) { roll -= w[k]; if (roll < 0) return items.get(k); }
        return items.getFirst();
    }

    record World(String season, String weather, boolean market, String event, String slice, String playerRank) {}

    static World world(int day, Random r) {
        int d = (day - 1) % 112;
        String season = List.of("spring", "summer", "autumn", "winter").get(d / 28);
        int dayOfSeason = d % 28 + 1;
        int w = r.nextInt(100);
        String weather = w < 70 ? "clear" : w < 88 ? (season.equals("winter") ? "snow" : "rain") : w < 94 ? "thunder" : season.equals("winter") ? "snow" : "rain";
        String event = null;
        if ((season.equals("spring") || season.equals("autumn")) && dayOfSeason == 7) event = "graduation";
        else if ((season.equals("spring") || season.equals("autumn")) && dayOfSeason >= 15 && dayOfSeason <= 21) event = "chunin_exams";
        else if (season.equals("summer") && dayOfSeason == 14) event = "leaf_festival";
        else if (season.equals("winter") && dayOfSeason == 28) event = "new_year";
        else if (season.equals("spring") && dayOfSeason == 3) event = "cherry_blossoms";
        else if (season.equals("winter") && dayOfSeason == 2) event = "first_snow";
        String slice = day <= 16 ? "beta1" : day <= 50 ? "beta2" : "beta3";
        String rank = day <= 16 ? "academy" : day <= 75 ? "genin" : day <= 150 ? "chunin" : "jonin";
        return new World(season, weather, d % 7 == 6, event, slice, rank);
    }

    static Context context(Person p, World w, String period, String district, int level, int day) {
        var c = Context.of("personality", p.personality(), "group", p.group(), "rank", p.rank(), "stage", p.stage(), "tier", p.tier(),
                "level", Integer.toString(level), "time", period, "weather", w.weather(), "season", w.season(), "district", district,
                "player_rank", w.playerRank(), "player_stage", day <= 150 ? "child" : "teen", "slice", w.slice(), "clan_status", "clanless",
                "quarrel", "none", "role", p.id().startsWith("role:") ? p.id() : null);
        if (p.clan() != null) c = c.with("clan", p.clan()).with("same_clan", "no");
        if (p.job() != null) c = c.with("job", p.job());
        if (w.market()) c = c.with("market", "yes");
        if (w.event() != null) c = c.with("event", w.event());
        for (var e : FILL.entrySet()) c = c.fill(e.getKey(), e.getValue());
        return c;
    }
    static final Map<String, String> FILL = Map.ofEntries(Map.entry("friend", "a friend"), Map.entry("neighbor", "the neighbour"),
            Map.entry("rival", "a rival"), Map.entry("partner", "a partner"), Map.entry("kin", "cousin"), Map.entry("place", "the market"),
            Map.entry("district", "the market"), Map.entry("item", "kunai"), Map.entry("dish", "miso ramen"), Map.entry("special", "pork ramen"),
            Map.entry("shop", "the grocer"), Map.entry("event", "the festival"), Map.entry("season", "spring"), Map.entry("weekday", "Market Day"),
            Map.entry("time", "eight"), Map.entry("clan", "Nara"), Map.entry("activity", "ramen"), Map.entry("village", "the Leaf"),
            Map.entry("speaker", "a resident"), Map.entry("squad", "your squad"), Map.entry("nature", "fire"), Map.entry("gift", "a flower"));

    static Names names() {
        var m = new HashMap<String, String>();
        m.put("player.given", "Player"); m.put("player.family", "Family"); m.put("player.full", "Player Family");
        m.put("player.rank", "Genin");
        for (String role : List.of("sensei", "instructor", "medic", "teammate_a", "teammate_b", "classmate_c", "classmate_d", "rival", "merchant")) {
            m.put("role:" + role + ".name", role); m.put("role:" + role + ".given", role); m.put("role:" + role + ".family", role);
        }
        for (int k = 1; k <= 8; k++) m.put("hokage." + k, "Hokage" + k);
        return Names.of(m);
    }
    private BetaTalk() {}
}
