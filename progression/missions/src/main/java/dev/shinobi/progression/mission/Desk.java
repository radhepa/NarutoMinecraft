package dev.shinobi.progression.mission;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.EnumMap;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import static dev.shinobi.progression.mission.Json.*;

/**
 * The Mission Desk (MISSIONS.md section 2): the board the player picks missions from, one column per rank they may
 * take, rolled from the save's {@code missions} stream so the same seed always shows the same board.
 *
 * <ul>
 * <li><b>Columns and refresh.</b> {@code desk.json} sets how many offers each rank shows for the player's rank and
 *     how often a column refreshes. Offers stay up for their lifetime; other squads take some of what the player
 *     leaves ({@code npc_squads}), and the board says who.</li>
 * <li><b>What may appear.</b> A template appears if its rank's gate and its own unlock pass, its season or event
 *     window is open, the {@link VarietyGuard} allows it and its slots can be filled. At most
 *     {@code max_same_category} offers of one category share a column. Classic saves use the curated pool and open
 *     with a fixed teaching order; Varied saves use every template with per-save weights.</li>
 * <li><b>Twists</b> are rolled per offer ({@code twist_chance} by mode), never the twist a template showed last time.</li>
 * <li><b>Clients who know you</b> post requests by name ({@link Clients}); <b>chains</b> bring back recurring clients
 *     stage by stage; once a week the <b>rival squad</b> races you for a contested job.</li>
 * <li><b>Caps.</b> One mission in hand; two D-ranks a day, or one mission of C rank or above, which takes the day;
 *     weekly caps per rank by the player's rank.</li>
 * </ul>
 */
public final class Desk {
    public enum Mode { CLASSIC, VARIED }

    final Catalogue cat;
    final long seed;
    final Mode mode;
    final World world;
    final SlotFiller filler;
    public final VarietyGuard guard;
    public final Clients clients;
    final boolean allowLater;
    final Map<Rank, List<Offer>> board = new EnumMap<>(Rank.class);
    final Map<Rank, Integer> refreshed = new EnumMap<>(Rank.class);
    final Deque<String> opening = new ArrayDeque<>();
    final Map<String, Integer> chainWeek = new HashMap<>();
    final Set<String> chainDone = new HashSet<>();
    final Map<Integer, Integer> perDay = new HashMap<>();
    final Map<String, Integer> perWeek = new HashMap<>();
    final List<String> takenByOthers = new ArrayList<>();
    int contestWeek = Integer.MIN_VALUE;
    Offer inHand;
    int serial;

    /** {@code allowLater} admits templates marked {@code later} (the full game; the beta builds leave it off). */
    public Desk(Catalogue cat, long seed, Mode mode, World world, boolean allowLater) {
        this.cat = cat; this.seed = seed; this.mode = mode; this.world = world; this.allowLater = allowLater;
        this.filler = new SlotFiller(world);
        this.guard = new VarietyGuard(map(cat.desk.get("variety")));
        this.clients = new Clients(cat.clients);
        if (mode == Mode.CLASSIC) opening.addAll(strings(cat.desk.get("classic_opening")));
    }

    // --- the board -------------------------------------------------------------------------------------------

    /** Opens the desk for the day: refreshes due columns, adds requests, chains and contests, and returns the board. */
    public List<Offer> open(int day, Player p) {
        for (Rank r : Rank.values()) {
            int size = size(p, r);
            if (size == 0 || !Unlocks.test(gate(r), p, day)) { board.remove(r); continue; }
            Integer last = refreshed.get(r);
            int every = (int) num(map(cat.desk.get("refresh_days")).get(r.id()), 1);
            if (last != null && day - last < every) continue;
            refreshed.put(r, day);
            var column = board.computeIfAbsent(r, k -> new ArrayList<>());
            settle(column, day, r);
            topUp(column, r, size, day, p);
        }
        requests(day, p);
        chains(day, p);
        contest(day, p);
        return offers();
    }

    public List<Offer> offers() { return board.values().stream().flatMap(List::stream).toList(); }
    public List<Offer> column(Rank r) { return List.copyOf(board.getOrDefault(r, List.of())); }
    public List<String> takenByOthers() { return List.copyOf(takenByOthers); }

    int size(Player p, Rank r) { return (int) num(map(map(cat.desk.get("board")).get(p.rank)).get(r.id()), 0); }
    Map<String, Object> gate(Rank r) { return map(map(cat.desk.get("rank_gates")).get(r.id())); }

    /** Drops expired offers (requests excepted until their own day) and lets other squads take unclaimed ones. */
    void settle(List<Offer> column, int day, Rank r) {
        var npc = map(map(cat.clients.get("rival_squads")).get("npc_squads"));
        double chance = num(npc.get("chance"), 0);
        int after = (int) num(npc.get("take_unclaimed_after_days"), 1);
        var rng = Seeds.stream(seed, "missions", "others|" + day + "|" + r.id());
        column.removeIf(o -> {
            if (day >= o.expires()) return true;
            if (!o.requested() && !o.contest() && day - o.posted() >= after && rng.chance(chance)) {
                takenByOthers.add(day + " " + o.template());
                return true;
            }
            return false;
        });
    }

    void topUp(List<Offer> column, Rank r, int size, int day, Player p) {
        var rng = Seeds.stream(seed, "missions", "desk|" + day + "|" + r.id());
        if (mode == Mode.CLASSIC && r == Rank.D) {
            int fromOpening = 0;
            while (column.size() < size && fromOpening < 2 && !opening.isEmpty()) {
                Template t = cat.get(opening.pollFirst());
                if (t == null || !eligible(t, day, p)) continue;
                Offer o = roll(t, rng, day, null, null, false);
                if (o != null) { column.add(o); fromOpening++; }
            }
        }
        var pool = new ArrayList<Template>();
        for (Template t : cat.of(r)) if (eligible(t, day, p)) pool.add(t);
        var skipped = new ArrayList<Template>();
        boolean relaxed = false;
        while (column.size() < size) {
            if (pool.isEmpty()) {
                if (relaxed || skipped.isEmpty()) break;
                relaxed = true;
                pool.addAll(skipped);
                continue;
            }
            double[] w = new double[pool.size()];
            for (int k = 0; k < w.length; k++) w[k] = weight(pool.get(k), day);
            int k = rng.weighted(w);
            Template t = pool.remove(k);
            if (!relaxed && sameCategory(column, t) >= guard.maxSameCategory()) { skipped.add(t); continue; }
            Offer o = roll(t, rng, day, null, null, false);
            if (o != null) column.add(o);
        }
    }

    /** Whether a template may go up today. Stage-chain templates only come through their chain. */
    boolean eligible(Template t, int day, Player p) {
        if (t.later() && !allowLater) return false;
        if (mode == Mode.CLASSIC && !t.classic()) return false;
        if (stageChain(t.id())) return false;
        if (t.party().equals("anbu_cell") && !p.atLeast("anbu")) return false;
        if (!Unlocks.test(t.unlock(), p, day) || !Unlocks.window(t, p, day)) return false;
        if (!guard.templateFree(t, day)) return false;
        if (offers().stream().anyMatch(o -> o.template().equals(t.id()))) return false;
        return true;
    }

    double weight(Template t, int day) {
        double w = 1;
        if (mode == Mode.VARIED) {
            var range = list(cat.desk.get("varied_weight_range"));
            double lo = num(range.get(0), 0.5), hi = num(range.get(1), 1.5);
            w *= lo + (hi - lo) * Seeds.roll(seed, "missions", "weight", t.id());
        }
        if (guard.recentlyOffered(t, day)) w *= 0.35;
        return w;
    }

    int sameCategory(List<Offer> column, Template t) {
        return (int) column.stream().filter(o -> cat.get(o.template()).category().equals(t.category())).count();
    }

    boolean stageChain(String template) {
        for (var chain : cat.chains())
            for (Object s : list(chain.get("stages"))) if (template.equals(map(s).get("template"))) return true;
        return false;
    }

    /** Rolls one offer: slots, twist, pay and XP. Null if the slots cannot be filled. */
    Offer roll(Template t, Seeds.Rng rng, int day, String forcedClient, String chain, boolean contest) {
        var slots = filler.fill(t, rng, guard, day, forcedClient, returning(rng));
        if (slots == null) return null;
        String twist = null;
        boolean harder = false;
        double chance = num(map(cat.desk.get("twist_chance")).get(mode == Mode.CLASSIC ? "classic" : "varied"), 0.5);
        if (!t.twists().isEmpty() && rng.chance(chance)) {
            String avoid = guard.avoidTwist(t, day);
            var options = t.twists().stream().filter(x -> !x.id().equals(avoid)).toList();
            double[] w = options.stream().mapToDouble(Template.Twist::weight).toArray();
            int k = rng.weighted(w);
            if (k >= 0) { twist = options.get(k).id(); harder = options.get(k).harder(); }
        }
        // Rolled culprits and spies are modifier twists the template always needs: pick one if none was rolled.
        if (twist == null && t.twists().stream().allMatch(Template.Twist::modifier) && t.slots().values().stream()
                .anyMatch(s -> "suspect".equals(s.get("pick")))) {
            twist = t.twists().get(rng.below(t.twists().size())).id();
        }
        boolean requested = forcedClient != null && chain == null;
        int pay = cat.economy.pay(t, rng.unit(), harder, requested);
        int xp = cat.economy.xp(t, rng.unit(), harder);
        int life = requested ? clients.requestLifetime() : (int) num(map(cat.desk.get("offer_lifetime_days")).get(t.rank().id()), 2);
        guard.offered(t.id(), day);
        return new Offer("offer." + day + "." + (serial++), t.id(), t.rank(), slots, twist, harder, pay, xp, day,
                day + life, requested ? forcedClient : null, chain, contest);
    }

    /** Today's returning client for the next cast, if the roll asks for one: someone the player already worked for. */
    java.util.function.Predicate<String> returning(Seeds.Rng rng) {
        var cfg = map(cat.clients.get("returning"));
        if (!rng.chance(num(cfg.get("chance"), 0))) return null;
        String tier = str(cfg.get("min_tier"), "known");
        return id -> clients.atLeast(id, tier);
    }

    void requests(int day, Player p) {
        long onBoard = offers().stream().filter(Offer::requested).count();
        if (onBoard >= clients.maxRequests()) return;
        var rng = Seeds.stream(seed, "missions", "request|" + day);
        if (!rng.chance(clients.requestChance())) return;
        for (String client : clients.requesters(day)) {
            if (offers().stream().anyMatch(o -> client.equals(o.client()))) continue;
            Resident who = filler.resident(client);
            if (who == null) continue;
            var fits = new ArrayList<Template>();
            for (Rank r : board.keySet())
                for (Template t : cat.of(r))
                    if (eligible(t, day, p) && t.slots().containsKey("client")
                            && "resident".equals(t.slots().get("client").get("pick"))
                            && who.matches(map(t.slots().get("client").get("where")), Map.of(), Map.of())) fits.add(t);
            if (fits.isEmpty()) continue;
            Template t = fits.get(rng.below(fits.size()));
            Offer o = roll(t, rng, day, client, null, false);
            if (o != null) { board.get(t.rank()).add(o); return; }
        }
    }

    void chains(int day, Player p) {
        int week = Unlocks.week(day);
        for (var chain : cat.chains()) {
            String id = (String) chain.get("id");
            if (!Unlocks.test(map(chain.get("unlock")), p, day)) continue;
            if (chainWeek.getOrDefault(id, Integer.MIN_VALUE) == week) continue;
            if (offers().stream().anyMatch(o -> id.equals(o.chain()))) continue;
            var rng = Seeds.stream(seed, "missions", "chain|" + id + "|" + day);
            Template t = null;
            String client = null;
            if (chain.get("role") != null) {
                client = world.role((String) chain.get("role"));
                if (client == null) continue;
                var fits = strings(chain.get("templates")).stream().map(cat::get)
                        .filter(x -> x != null && board.containsKey(x.rank()) && eligible(x, day, p)).toList();
                if (!fits.isEmpty()) t = fits.get(rng.below(fits.size()));
            } else {
                for (Object s : list(chain.get("stages"))) {
                    var stage = map(s);
                    String tid = (String) stage.get("template");
                    if (chainDone.contains(tid)) continue;
                    Object after = stage.get("after");
                    if (after != null && !chainDone.contains((String) after)) break;
                    if (stage.get("min_tier") != null && !clients.atLeast(id, (String) stage.get("min_tier"))) break;
                    Template cand = cat.get(tid);
                    if (cand == null || (cand.later() && !allowLater) || !board.containsKey(cand.rank())) break;
                    if (!Unlocks.test(cand.unlock(), p, day) || !Unlocks.window(cand, p, day) || !guard.templateFree(cand, day)) break;
                    t = cand;
                    break;
                }
            }
            if (t == null) continue;
            Offer o = roll(t, rng, day, client, id, false);
            if (o != null) { board.get(t.rank()).add(o); chainWeek.put(id, week); }
        }
    }

    void contest(int day, Player p) {
        var rival = map(map(cat.clients.get("rival_squads")).get("rival"));
        if (rival.isEmpty() || !Unlocks.test(map(rival.get("unlock")), p, day)) return;
        int week = Unlocks.week(day);
        if (contestWeek == week || world.role((String) rival.get("role")) == null) return;
        var rng = Seeds.stream(seed, "missions", "contest|" + day);
        var fits = new ArrayList<Template>();
        for (Rank r : board.keySet())
            for (Template t : cat.of(r)) if (t.contested() && eligible(t, day, p)) fits.add(t);
        if (fits.isEmpty()) return;
        Template t = fits.get(rng.below(fits.size()));
        Offer o = roll(t, rng, day, null, null, true);
        if (o != null) { board.get(t.rank()).add(o); contestWeek = week; }
    }

    // --- taking and turning in ---------------------------------------------------------------------------------

    /** Why the player cannot take this offer now, or null if they can. */
    public String refusal(Offer o, Player p, int day) {
        if (inHand != null) return "in_hand";
        if (!offers().contains(o)) return "gone";
        int today = perDay.getOrDefault(day, 0);
        int cap = (int) num(map(cat.desk.get("caps")).get("per_day"), 2);
        if (o.rank() == Rank.D ? today >= cap : today > 0) return "day_full";
        var weekly = map(map(map(cat.desk.get("caps")).get("per_week")).get(o.rank().id()));
        if (weekly.get(p.rank) != null && perWeek.getOrDefault(Unlocks.week(day) + "|" + o.rank().id(), 0) >= num(weekly.get(p.rank), 0))
            return "week_full";
        return null;
    }

    public Offer inHand() { return inHand; }

    public void take(Offer o, int day) {
        board.values().forEach(c -> c.remove(o));
        int cap = (int) num(map(cat.desk.get("caps")).get("per_day"), 2);
        perDay.merge(day, o.rank() == Rank.D ? 1 : cap, Integer::sum);
        perWeek.merge(Unlocks.week(day) + "|" + o.rank().id(), 1, Integer::sum);
        guard.taken(o, cat.get(o.template()), day);
        inHand = o;
    }

    /** Hands the mission back before starting it: a small rapport cost with the client, nothing else. */
    public void handBack(Offer o, int day) {
        if (o.client() != null) clients.of(o.client()).points += cat.economy.handedBackRapport();
        inHand = null;
    }

    /** Turns the mission in: grade, pay, XP and rapport (with the client, and with the chain's family). */
    public Economy.Result turnIn(Offer o, Economy.Performance perf, double cohesion, boolean goodAssignment, int day) {
        Template t = cat.get(o.template());
        var r = cat.economy.settle(t, o, perf, cohesion, goodAssignment);
        clients.record(o.client(), r, day);
        if (o.chain() != null) {
            clients.record(o.chain(), r, day);
            if (r.success()) chainDone.add(o.template());
        }
        inHand = null;
        return r;
    }

    public Catalogue catalogue() { return cat; }

    /** The rolled board as plain data, for the journal, saves and tests: offer id to template and slots. */
    public Map<String, String> describe() {
        var m = new LinkedHashMap<String, String>();
        for (Offer o : offers()) m.put(o.id(), o.template() + " " + o.slots() + (o.twist() == null ? "" : " +" + o.twist()));
        return m;
    }
}
