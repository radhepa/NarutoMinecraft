package dev.shinobi.life.bond.sim;

import static dev.shinobi.life.bond.Leaf.*;

import dev.shinobi.life.bond.Act;
import dev.shinobi.life.bond.BondEvent;
import dev.shinobi.life.bond.BondWorld;
import dev.shinobi.life.bond.Conflict;
import dev.shinobi.life.bond.Household;
import dev.shinobi.life.bond.Kindling;
import dev.shinobi.life.bond.Standing;
import dev.shinobi.life.bond.Activity;
import dev.shinobi.life.bond.BondDialogue;
import dev.shinobi.life.bond.Conversation;
import dev.shinobi.life.bond.LifeEvents;
import dev.shinobi.life.bond.Schedule;
import dev.shinobi.life.bond.Together;
import dev.shinobi.life.bond.Question;
import dev.shinobi.life.bond.Questions;
import dev.shinobi.life.bond.SampleQuestions;
import dev.shinobi.life.bond.Leaf;
import dev.shinobi.life.bond.Levels;
import dev.shinobi.life.bond.Person;
import dev.shinobi.life.bond.Recruitment;
import dev.shinobi.life.bond.Seeds;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.function.Consumer;

/**
 * A seeded whole save: the scripted 60-hour main path (ROADMAP.md's chapters and hour budget, three in-game days to an
 * hour of play) with the Classic cast and a rolled village, played by three kinds of player. It prints how each bond
 * grows per chapter, so pacing can be checked against the roadmap's friendship gates. Chapter beats are the roadmap's
 * neutral descriptions; the later arcs are only hour budgets.
 *
 * <p>Run it with {@code ./gradlew :life:bonds:simulate} (optionally {@code -Pseed=N}).
 */
public final class Playthrough {
    /** Kinds of player: how often they talk, give, follow orders, keep secrets and spread their attention. */
    public enum Profile {
        DEVOTED(.95, .6, .5, .25, .6, 1, .97, .5, true, 1, 1),
        TYPICAL(.6, .3, .3, .1, .25, .6, .92, .72, true, .7, .6),
        RECKLESS(.3, .1, .1, .05, .08, .1, .45, .9, false, .15, .2);

        final double talkSquad, talkSensei, talkClass, talkVillage, gift, birthdays, orders, favoriteBias, keepsSecrets, apologizes, sideQuests;
        Profile(double talkSquad, double talkSensei, double talkClass, double talkVillage, double gift, double birthdays, double orders,
                double favoriteBias, boolean keepsSecrets, double apologizes, double sideQuests) {
            this.talkSquad = talkSquad; this.talkSensei = talkSensei; this.talkClass = talkClass; this.talkVillage = talkVillage; this.gift = gift;
            this.birthdays = birthdays; this.orders = orders; this.favoriteBias = favoriteBias; this.keepsSecrets = keepsSecrets ? 1 : 0;
            this.apologizes = apologizes; this.sideQuests = sideQuests;
        }
        public String id() { return name().toLowerCase(Locale.ROOT); }
    }
    enum Phase { ACADEMY, GENIN, EXAMS, LATER }
    record Chapter(String id, String title, double hours, int days, Phase phase, Consumer<Run> start, Consumer<Run> end) {
        Chapter(String id, String title, double hours, int days, Phase phase, Consumer<Run> start) { this(id, title, hours, days, phase, start, null); }
    }
    public record Row(String chapter, String title, double hours, long day, Map<String, Integer> levels, double cohesion, String village, String notes) {}
    public record Result(Profile profile, List<Row> rows, Map<String, String> checks, BondWorld world, List<BondEvent> events, Map<Integer, Standings> standing) {}
    /**
     * Standing at a checkpoint: with the village overall (the Hokage needs Hero), and in every district and clan quarter
     * (the Hokage needs Good Neighbor in each); {@code lowest} is the weakest of those.
     */
    public record Standings(double village, String villageTitle, int goodNeighbor, int communities, String lowest, String lowestTitle) {
        public boolean hero() { return villageTitle.equals("hero"); }
        public boolean everywhere() { return goodNeighbor == communities; }
        @Override public String toString() {
            return String.format("village %s (%.1f); good neighbor in %d of %d districts and clans, lowest %s %s", villageTitle, village, goodNeighbor, communities, lowest, lowestTitle);
        }
    }
    public static final int[] STANDING_HOURS = {45, 60};
    static Standings standings(BondWorld w) {
        var places = new java.util.TreeSet<String>();
        for (var p : w.people()) for (String c : p.communities()) if (c.startsWith("district:") || c.startsWith("clan:")) places.add(c);
        int good = 0; String lowest = ""; double low = Double.POSITIVE_INFINITY;
        for (String c : places) {
            double s = w.standing(c);
            if (s >= Standing.Title.GOOD_NEIGHBOR.from) good++;
            if (s < low) { low = s; lowest = c; }
        }
        return new Standings(w.standing("village"), w.title("village").id(), good, places.size(), lowest, places.isEmpty() ? "" : Standing.Title.of(low).id());
    }

    public static final List<String> SHOWN = List.of(TEAMMATE_A, TEAMMATE_B, SENSEI, INSTRUCTOR, CLASSMATE_C, CLASSMATE_D, RIVAL);

    /** One run in progress. */
    static final class Run {
        final BondWorld w; final Profile p; final Seeds.Rng rng; final List<String> notes = new ArrayList<>();
        final Map<String, String> checks = new LinkedHashMap<>(); final List<BondEvent> events = new ArrayList<>();
        final List<String> villagers = new ArrayList<>();
        double hours; int bondQuests, part; long betaEnd = -1;
        int asked, hangouts, invited, acceptedInvites, stoodUp, highlights, rituals, newsTold, newsAnswered, deepTalks, questions, contradictions, noticed;
        final Map<String, Integer> questionsBy = new java.util.TreeMap<>();
        /** The hour each Kindling tier was first reached with anyone. */
        final Map<String, Double> tierHours = new java.util.LinkedHashMap<>();
        int kindles;
        Run(BondWorld w, Profile p, long seed) {
            this.w = w; this.p = p; this.rng = Seeds.stream(seed, "playthrough", p.id());
            for (var person : w.people()) if (person.id().startsWith("resident:")) villagers.add(person.id());
        }
        boolean roll(double chance) { return rng.unit() < chance; }
        List<String> squad() { return w.squad() == null ? List.of() : w.squad().members(); }
        List<String> teammates() { return w.squad() == null ? TEAMMATES : w.squad().teammates(); }
        String villager() { return villagers.get(rng.below(villagers.size())); }
        List<String> with(String extra) { var l = new ArrayList<>(squad()); l.add(extra); return l; }
        List<String> others(String who) { return squad().stream().filter(m -> !m.equals(who)).toList(); }
        /** A time skip: the squad stays together if it holds (cohesion 45), a sweetheart too; everyone grows up. */
        void timeSkip(Person.Stage stage) {
            var companions = new ArrayList<>(w.cohesion() >= 45 ? squad() : List.of(SENSEI));
            w.bonded().stream().filter(id -> w.bond(id).romance().committed()).forEach(companions::add);
            w.timeSkip(stage == Person.Stage.TEEN ? BondWorld.YEAR : 3 * BondWorld.YEAR, companions);
            w.setPlayerStage(stage);
            for (String c : CLASSMATES) w.grow(c, stage);
            note("time skip, " + (companions.size() > 1 ? "squad together" : "squad apart"));
        }
        void note(String s) { notes.add(s); }
        /** Whom the player spends extra attention on: their favorite, or an even split. */
        String pick() {
            var team = teammates();
            if (team.isEmpty()) return TEAMMATE_A;
            String fav = p == Profile.RECKLESS ? TEAMMATE_B : TEAMMATE_A;
            if (team.contains(fav) && roll(p.favoriteBias)) return fav;
            var others = team.stream().filter(t -> !t.equals(fav)).toList();
            return others.isEmpty() ? fav : others.get(rng.below(others.size()));
        }
        String item(String who) {
            var pp = w.person(who).personality();
            return switch (p) {
                case DEVOTED -> w.effectiveLevel(who) >= Levels.FIRST_BOND_QUEST ? pp.loves().getFirst() : "food:ramen";
                case TYPICAL -> roll(.4) && w.effectiveLevel(who) >= 2 ? pp.loves().getFirst() : roll(.6) ? "food:ramen" : "item:pebble";
                case RECKLESS -> roll(.3) ? pp.dislikes().getFirst() : "item:pebble";
            };
        }
        /** A beat of the squad bonding arc (main path): a moment with everyone in it who is not quarrelling with you. */
        void beat(String id, List<String> who) {
            for (String p : who) if (!w.bond(p).conflict().active() && !w.bond(p).conflict().broken() && w.effectiveLevel(p) >= 2) w.moment(p, id);
        }
        /** A bond quest: once their level allows it and the player does side quests; its scene is a moment. */
        void bondQuest(String who, int n, int needs, Act also) {
            String id = "bond." + who.substring(5) + "." + n;
            if (w.bond(who).moments().contains(id) || w.effectiveLevel(who) < needs || !roll(p.sideQuests)) return;
            w.moment(who, id); w.together(who); bondQuests++;
            if (also != null) w.act(who, also);
        }
    }

    static List<Chapter> chapters() {
        var list = new ArrayList<Chapter>();
        // Beta 1: the opening and the Academy (~4 h, 12 in-game days).
        list.add(new Chapter("Ch 0", "Prologue", .33, 1, Phase.ACADEMY, r -> {
            r.w.act(SENSEI, Act.SAVED_BY_THEM); r.w.talk(INSTRUCTOR); r.w.talk(MEDIC);
        }));
        list.add(new Chapter("Ch 1", "First morning", .33, 1, Phase.ACADEMY, r -> {
            r.w.experience(Act.MEAL_TOGETHER, List.of(INSTRUCTOR)); r.w.talk(COOK);
            for (String c : CLASSMATES) r.w.talk(c);
        }));
        list.add(new Chapter("Ch 2", "First lessons", .33, 2, Phase.ACADEMY, r -> {
            r.w.experience(Act.TRAINED_TOGETHER, CLASSMATES);
            r.w.act(RIVAL, Act.SPAR_WON);
            if (r.p == Profile.RECKLESS) r.w.act(RIVAL, Act.BRAGGED, List.of(TEAMMATE_A, TEAMMATE_B, CLASSMATE_C, CLASSMATE_D));
        }));
        list.add(new Chapter("Ch 3", "Chakra", .42, 2, Phase.ACADEMY, r -> {
            r.w.experience(Act.TRAINED_TOGETHER, List.of(TEAMMATE_A)); r.w.favor(TEAMMATE_A, 2);
        }));
        list.add(new Chapter("Ch 4", "Night", .42, 1, Phase.ACADEMY, r -> {
            for (int i = 0; i < 3; i++) r.w.talk(r.villager());
            if (r.p == Profile.RECKLESS) r.w.act(r.villager(), Act.RUDE);
        }));
        list.add(new Chapter("Ch 5", "Errands at the Academy", .25, 1, Phase.ACADEMY, r -> {
            String client = r.villager();
            r.w.act(client, Act.HELPED_RESIDENT, List.of(INSTRUCTOR));
            r.w.experience(Act.TRAINED_TOGETHER, List.of(INSTRUCTOR));
        }));
        list.add(new Chapter("Ch 6", "Exam eve", .33, 2, Phase.ACADEMY, r -> {
            r.w.experience(Act.STUDIED_TOGETHER, CLASSMATES);
            r.w.experience(Act.MEAL_TOGETHER, CLASSMATES);
            r.beat("bond.study_night", CLASSMATES);
            // The second bond quest of the loud classmate: they confide something.
            if (r.w.effectiveLevel(TEAMMATE_B) >= 2) r.w.act(TEAMMATE_B, r.p.keepsSecrets > 0 ? Act.KEPT_SECRET : Act.BROKE_SECRET);
        }));
        list.add(new Chapter("Ch 7", "Graduation", .42, 2, Phase.ACADEMY, r -> {
            r.w.promote(1, List.of(INSTRUCTOR, TEAMMATE_A, TEAMMATE_B, CLASSMATE_C, CLASSMATE_D, RIVAL));
            for (String c : CLASSMATES) r.w.setRank(c, 1);
        }));
        // Beta 2: Genin life (~8 h, 24 days).
        list.add(new Chapter("Ch 8", "Team assignment", .58 + .3, 3, Phase.GENIN, r -> {
            r.w.formSquad("squad:7", SENSEI, TEAMMATES, List.of(CLASSMATE_C));
            r.w.experience(Act.TRAINED_TOGETHER, r.squad());
            if (r.p == Profile.RECKLESS) { r.w.act(SENSEI, Act.DISOBEYED_ORDERS); r.w.act(TEAMMATE_A, Act.RECKLESS_CHARGE); }
            else { for (String t : TEAMMATES) r.w.act(t, Act.STOOD_BY_THEM); r.beat("bond.bells", r.squad()); }
        }));
        list.add(new Chapter("Ch 9", "The Mission Desk", .25 + 1, 4, Phase.GENIN, r -> {
            if (r.p == Profile.RECKLESS) for (String m : r.squad()) r.w.act(m, Act.ABANDONED_MISSION, List.of());
        }));
        list.add(new Chapter("Ch 10", "Tree walking", .42 + .6, 3, Phase.GENIN, r -> r.w.experience(Act.TRAINED_TOGETHER, r.squad())));
        list.add(new Chapter("Ch 11", "First C-rank", .75 + .6, 4, Phase.GENIN, r -> {
            r.w.experience(Act.MISSION_TOGETHER, r.with(MERCHANT));
            r.w.act(MERCHANT, Act.PROTECTED_THEM, r.squad());
        }, r -> {
            // The night at camp, where the quest branches on friendship with teammate_a (ROADMAP's quest example).
            r.w.experience(Act.CAMP_NIGHT, r.squad());
            int a = r.w.effectiveLevel(TEAMMATE_A);
            r.checks.put("ch11 campfire (teammate_a level " + a + ")", a >= 5 ? "plays" : "skipped");
            if (a >= 5) { r.w.moment(TEAMMATE_A, "bond.campfire.a"); r.w.act(TEAMMATE_A, Act.HEART_TO_HEART); }
        }));
        list.add(new Chapter("Ch 12", "Water walking and natures", .5 + .6, 3, Phase.GENIN, r -> {
            r.w.experience(Act.TRAINED_TOGETHER, r.squad());
            if (r.p == Profile.TYPICAL && r.teammates().contains(TEAMMATE_B)) { r.w.quarrel(TEAMMATE_B, Act.QUARREL); r.note("a quarrel with teammate_b"); }
        }));
        list.add(new Chapter("Ch 13", "A far village", .75 + .6, 3, Phase.GENIN, r -> {
            r.w.experience(Act.MISSION_TOGETHER, r.squad());
            for (String t : r.teammates()) r.w.act(t, r.p == Profile.RECKLESS ? Act.WENT_OVER_THEIR_HEAD : Act.STOOD_BY_THEM);
        }));
        list.add(new Chapter("Ch 14", "Second C-rank", .83 + .7, 4, Phase.GENIN, r -> {
            r.w.experience(Act.MISSION_TOGETHER, r.with(MERCHANT));
            r.w.experience(Act.CAMP_NIGHT, r.squad());
            if (r.p == Profile.RECKLESS) { r.w.act(SENSEI, Act.DISOBEYED_ORDERS); for (String t : r.teammates()) r.w.act(t, Act.RECKLESS_CHARGE); }
            else if (r.teammates().contains(TEAMMATE_B)) r.w.act(TEAMMATE_B, Act.SAVED_LIFE, r.others(TEAMMATE_B));
            r.w.experience(Act.MEAL_TOGETHER, r.squad());
            if (r.p != Profile.RECKLESS) r.beat("bond.squad_dinner", r.squad());
        }));
        // Beta 3: the Chunin Exams (~3 h).
        list.add(new Chapter("Ch 15", "Written test", .33, 1, Phase.EXAMS, r -> r.w.experience(Act.STUDIED_TOGETHER, r.teammates())));
        list.add(new Chapter("Ch 16", "Forest of Death", 1, 5, Phase.EXAMS, r -> {
            r.w.experience(Act.CAMP_NIGHT, r.squad());
            r.beat("bond.night_watch", r.teammates());
        }));
        list.add(new Chapter("Ch 17", "Preliminaries", .33, 1, Phase.EXAMS, r -> {
            r.w.act(CLASSMATE_D, Act.SPAR_LOST); r.w.experience(Act.TRAINED_TOGETHER, r.teammates());
        }));
        list.add(new Chapter("Ch 18", "Training break", .5, 6, Phase.EXAMS, r -> r.w.experience(Act.FESTIVAL_TOGETHER, r.squad())));
        list.add(new Chapter("Ch 19", "Chunin Exams finals", .67, 1, Phase.EXAMS, r -> {
            r.w.act(RIVAL, r.p == Profile.RECKLESS ? Act.SPAR_LOST : Act.SPAR_WON);
            r.w.deed(Act.DEFENDED_VILLAGE, "", r.squad());
            for (String t : r.teammates()) r.w.act(t, r.p == Profile.RECKLESS ? Act.RECKLESS_CHARGE : Act.PROTECTED_THEM);
            r.beat("bond.finals", r.teammates());
        }));
        list.add(new Chapter("Ch 20", "Results", .17, 1, Phase.EXAMS, r -> {
            if (r.p != Profile.RECKLESS) r.w.promote(2, r.with(INSTRUCTOR));
            r.w.experience(Act.MEAL_TOGETHER, r.squad());
        }));
        // After the beta: hour budgets only (Chunin ~13 h, Jonin ~17 h, the road to Hokage ~15 h).
        for (int i = 1; i <= 4; i++) {
            int part = i;
            list.add(new Chapter("Chunin " + i, part == 1 ? "A year later" : "Chunin arc", 3.25, 10, Phase.LATER, r -> {
                if (part == 1) r.timeSkip(Person.Stage.TEEN);
                if (part == 1 && r.p == Profile.RECKLESS) r.w.promote(2, r.squad());
                if (part == 2) { r.w.setFlag(Kindling.UNLOCK_FLAG, true); r.note("Kindling Bond unlocks"); }
            }));
        }
        for (int i = 1; i <= 4; i++) {
            int part = i;
            list.add(new Chapter("Jonin " + i, part == 1 ? "Three years later" : "Jonin arc", 4.25, 13, Phase.LATER, r -> {
                if (part == 1) { r.timeSkip(Person.Stage.ADULT); r.w.promote(3, r.squad()); }
            }));
        }
        for (int i = 1; i <= 3; i++) {
            int part = i;
            list.add(new Chapter("Road " + i, "The road to Hokage", 5, 15, Phase.LATER, r -> {
                if (part == 3) { r.w.deed(Act.DEFENDED_VILLAGE, "", r.squad()); r.w.promote(5, r.squad()); }
            }));
        }
        return list;
    }

    /** Plays one profile through the whole path. */
    public static Result play(long seed, Profile profile) {
        var w = Leaf.classic(seed, 40);
        Questions.load(w, SampleQuestions.bank());
        var r = new Run(w, profile, seed);
        var rows = new ArrayList<Row>();
        var standing = new java.util.TreeMap<Integer, Standings>();
        var path = chapters();
        for (var ch : path) {
            r.notes.clear(); r.part++;
            for (int d = 0; d < ch.days; d++) {
                if (d == 0) ch.start.accept(r);
                if (d == ch.days - 1 && ch.end != null) ch.end.accept(r);
                day(r, ch.phase, d);
                w.endDay();
                for (var e : w.drainEvents()) { r.events.add(e); notable(r, e); }
            }
            r.hours += ch.hours;
            if (ch == path.getLast()) { w.deed(Act.SAVED_THE_VILLAGE, "", List.of()); w.endDay(); w.drainEvents(); }
            for (int h : STANDING_HOURS) if (r.hours >= h && !standing.containsKey(h)) standing.put(h, standings(w));
            for (var f : Kindling.flames(w)) r.tierHours.putIfAbsent(f.tier().id(), Math.round(r.hours * 10) / 10.0);
            for (var f : Kindling.flames(w)) for (var t : Kindling.Tier.values())
                if (t != Kindling.Tier.NONE && t.compareTo(f.tier()) <= 0) r.tierHours.putIfAbsent(t.id(), Math.round(r.hours * 10) / 10.0);
            if (ch.id.equals("Ch 7")) r.checks.put("academy end: teammates level", w.level(TEAMMATE_A) + " / " + w.level(TEAMMATE_B));
            if (ch.id.equals("Ch 20")) r.betaEnd = w.day();
            if (ch.id.equals("Ch 20")) r.checks.put("beta end: teammates level", r.teammates().stream().map(t -> t.substring(5) + " " + w.level(t)).toList().toString());
            var levels = new LinkedHashMap<String, Integer>();
            for (String who : SHOWN) levels.put(who, w.effectiveLevel(who));
            if (EXPLAIN != null && (ch.id.equals("Ch 7") || ch.id.equals("Ch 11") || ch.id.equals("Ch 14") || ch.id.equals("Ch 20") || ch.id.startsWith("Road 3")))
                System.out.println(profile.id() + " " + ch.id + " " + explain(w, EXPLAIN));
            rows.add(new Row(ch.id, ch.title, Math.round(r.hours * 10) / 10.0, w.day(), levels, w.cohesion(), w.title("village").id(), String.join("; ", r.notes)));
        }
        epilogue(r);
        r.checks.put("romance before the first time skip", r.events.stream().anyMatch(e -> e.kind().equals("romance") && e.day() < r.betaEnd) ? "YES (bug)" : "none");
        r.checks.put("bonds at level 10", Long.toString(w.bonded().stream().filter(id -> w.level(id) >= 10).count()));
        r.checks.put("bond quests played", Integer.toString(r.bondQuests));
        r.checks.put("time together", String.format("asked %d, hung out %d, highlights %d, rituals %d; invited %d times, accepted %d; stood someone up %d",
                r.asked, r.hangouts, r.highlights, r.rituals, r.invited, r.acceptedInvites, r.stoodUp));
        var close = w.bonded().stream().filter(id -> w.level(id) >= 5).toList();
        double perClose = close.stream().mapToInt(id -> r.questionsBy.getOrDefault(id, 0)).average().orElse(0);
        int maxClose = close.stream().mapToInt(id -> r.questionsBy.getOrDefault(id, 0)).max().orElse(0);
        r.checks.put("questions", String.format("%d asked; %.1f per close friend (level 5+, %d of them), %d at most; contradictions %d, noticed %d; bank ran dry %d times",
                r.questions, perClose, close.size(), maxClose, r.contradictions, r.noticed, w.questionsDry()));
        r.checks.put("their lives", String.format("news told %d, responded to %d; deeper talks %d", r.newsTold, r.newsAnswered, r.deepTalks));
        for (int h : STANDING_HOURS) { standing.putIfAbsent(h, standings(w)); r.checks.put("standing at " + h + " h", standing.get(h).toString()); }
        return new Result(profile, rows, r.checks, w, r.events, Map.copyOf(standing));
    }

    /** One in-game day of systemic play around the chapter's beat. */
    static void day(Run r, Phase phase, int index) {
        var w = r.w; var p = r.p;
        switch (phase) {
            case ACADEMY -> {
                for (String c : CLASSMATES) w.together(c);
                w.together(INSTRUCTOR);
                if (index % 2 == 1) w.experience(Act.STUDIED_TOGETHER, List.of(CLASSMATES.get(r.rng.below(CLASSMATES.size()))));
                // Beta 1: one bond quest per classmate (ROADMAP.md, "Friendship and bonds").
                for (String c : CLASSMATES) r.bondQuest(c, 1, Levels.FIRST_BOND_QUEST, null);
            }
            case GENIN, EXAMS, LATER -> {
                var squad = r.squad();
                for (String m : squad) w.together(m);
                boolean mission = phase != Phase.EXAMS && index % 3 != 2;
                if (mission) {
                    w.experience(Act.MISSION_TOGETHER, squad);
                    if (r.roll(p == Profile.RECKLESS ? .4 : .8)) w.act(r.villager(), Act.HELPED_RESIDENT, squad);
                    if (p == Profile.RECKLESS && r.roll(.35)) for (String t : r.teammates()) w.act(t, Act.RECKLESS_CHARGE);
                    w.act(SENSEI, r.roll(p.orders) ? Act.FOLLOWED_ORDERS : Act.DISOBEYED_ORDERS);
                    // Once the gift awakens, kindle a squadmate in the fight now and then.
                    if (Kindling.unlocked(w)) for (String m : squad)
                        if (Kindling.tier(w, m) != Kindling.Tier.NONE && r.roll(p == Profile.DEVOTED ? .5 : p == Profile.TYPICAL ? .3 : .2)) { w.kindle(m); r.kindles++; }
                    w.act(SENSEI, r.roll(p == Profile.RECKLESS ? .7 : .92) ? Act.MISSION_SUCCESS : Act.MISSION_FAILED);
                } else if (p == Profile.RECKLESS && r.roll(.5)) { for (String m : squad) w.act(m, Act.SKIPPED_TRAINING); }
                else w.experience(Act.TRAINED_TOGETHER, squad);
                // Beta 2: two per teammate; Beta 3: one more per teammate, in the training break.
                if (phase == Phase.GENIN) for (String t : r.teammates()) { r.bondQuest(t, 3, 4, null); r.bondQuest(t, 4, 5, Act.SUPPORTED_DREAM); }
                if (phase == Phase.EXAMS && index >= 1) for (String t : r.teammates()) r.bondQuest(t, 5, 5, Act.HEART_TO_HEART);
                if (phase == Phase.LATER) later(r, index);
                if (r.roll(.3)) w.talk(CLASSMATES.get(r.rng.below(CLASSMATES.size())));
            }
        }
        // Talk, gifts, a meal: how much the player tends their bonds.
        for (String t : r.teammates()) if (r.roll(p.talkSquad)) w.talk(t);
        if (w.squad() != null && r.roll(p.talkSensei)) w.talk(SENSEI);
        for (String c : List.of(CLASSMATE_C, CLASSMATE_D, RIVAL, INSTRUCTOR)) if (r.roll(p.talkClass)) w.talk(c);
        for (int i = 0; i < 3; i++) if (r.roll(p.talkVillage)) w.talk(r.villager());
        if (r.roll(p.gift)) { String who = r.pick(); w.gift(who, r.item(who)); }
        if (r.roll(p.gift * .6)) { String who = r.pick(); w.experience(Act.MEAL_TOGETHER, List.of(who)); w.favor(who, 2); }
        for (String who : w.bonded()) if (w.birthday(who) && r.roll(p.birthdays)) w.celebrate(who);
        together(r);
        // Quarrels: say sorry, then make up when they are ready.
        for (String who : w.bonded()) {
            var c = w.bond(who).conflict();
            if ((c.state() == Conflict.State.ARGUMENT || c.state() == Conflict.State.COLD_SHOULDER) && r.roll(p.apologizes * .5)) w.apologize(who);
            if (c.canReconcile() && r.roll(p.apologizes)) { w.reconcile(who); r.note("made up with " + who.substring(5)); }
        }
        if (w.squad() != null) for (String gone : w.squad().departed().keySet()) if (w.canReturn(gone) && r.roll(p.sideQuests)) { w.returnToSquad(gone); r.note(gone.substring(5) + " came back"); }
    }

    /** How often each kind of player hangs out, answers invitations, turns up, responds to news and talks deeper. */
    static final java.util.Map<Profile, double[]> TOGETHER = java.util.Map.of(
            // ask every n days, accept an invitation, turn up, respond kindly to news, a deeper talk a day
            Profile.DEVOTED, new double[]{2, .9, 1, .95, .8},
            Profile.TYPICAL, new double[]{4, .6, .95, .7, .35},
            Profile.RECKLESS, new double[]{10, .3, .6, .3, .05});

    /** One day of time together: invitations answered, a hangout asked for, plans kept, news heard, a conversation. */
    static void together(Run r) {
        var w = r.w; var t = TOGETHER.get(r.p);
        for (var inv : Together.invitations(w)) {
            r.invited++;
            boolean yes = r.roll(t[1]);
            if (Together.answer(w, inv.id(), yes) != null) r.acceptedInvites++;
        }
        for (var plan : Together.plans(w)) if (plan.day() == w.day()) {
            boolean came = r.roll(t[2]);
            var out = Together.go(w, plan.id(), came);
            if (!came) r.stoodUp++; else { r.hangouts++; if (out.highlight() != null) r.highlights++; r.rituals += out.newRituals().size(); }
        }
        if (w.day() % (long) t[0] == 0) {
            var friends = w.bonded().stream().filter(id -> w.effectiveLevel(id) >= 1 && !id.equals(MERCHANT)).limit(6).toList();
            if (!friends.isEmpty()) {
                // Most hangouts are with the teammate they favor; the rest go around their circle.
                String who = w.squad() != null && r.roll(r.p.favoriteBias) ? r.pick() : friends.get(r.rng.below(friends.size()));
                String act = w.bond(who).facts().contains("favorite_hangout") ? Activity.favorite(w.seed(), who)
                        : List.of("ramen", "dango", "spar", "market_stroll", "train").get(r.rng.below(5));
                var slot = Schedule.nextFree(w.seed(), List.of(w.person(who)), Activity.of(act), w.day() + 1, 10, 3);
                if (slot != null) { r.asked++; Together.invite(w, List.of(who), act, slot[0], (int) slot[1]); }
            }
        }
        for (String who : w.bonded()) {
            if (w.bond(who).contactDays() == 0 || w.bond(who).talkDayIsToday(w.day())) {
                var news = LifeEvents.tell(w, who);
                if (news.isPresent()) {
                    r.newsTold++;
                    boolean hard = LifeEvents.Kind.of(news.get().substring(5)).valence < 0;
                    String response = r.roll(t[3]) ? (hard ? "comfort" : "congratulate") : "shrug";
                    if (LifeEvents.respond(w, who, response).isEmpty()) r.newsAnswered++;
                }
                BondDialogue.followUp(w, who);
                question(r, who);
            }
        }
        if (r.roll(t[4])) {
            var close = w.bonded().stream().filter(id -> w.effectiveLevel(id) >= 2).toList();
            if (!close.isEmpty()) {
                String who = close.get(r.rng.below(close.size()));
                var topics = Conversation.topics(w, who);
                Conversation.talk(w, who, topics.getLast(), null);
                r.deepTalks++;
            }
        }
    }

    /** A question from someone the player talked to today, answered as this kind of player would. */
    static void question(Run r, String who) {
        var w = r.w;
        var q = Questions.next(w, who);
        if (q.isEmpty()) return;
        Question.Answer pick;
        var answers = q.get().answers();
        var best = answers.stream().max(java.util.Comparator.comparingDouble(a -> {
            var d = Questions.preview(w, who, q.get(), a.id()); return d.affection() + d.trust() + .5 * d.respect(); })).orElseThrow();
        var worst = answers.stream().min(java.util.Comparator.comparingDouble(a -> {
            var d = Questions.preview(w, who, q.get(), a.id()); return d.affection() + d.trust() + .5 * d.respect(); })).orElseThrow();
        double reads = switch (r.p) { case DEVOTED -> .85; case TYPICAL -> .5; case RECKLESS -> .1; };
        pick = r.roll(reads) ? best : r.p == Profile.RECKLESS && r.roll(.5) ? worst : answers.get(r.rng.below(answers.size()));
        var out = Questions.answer(w, who, q.get().id(), pick.id());
        r.questions++; r.questionsBy.merge(who, 1, Integer::sum);
        if (out.contradiction()) r.contradictions++;
        if (out.noticed()) r.noticed++;
    }

    /** The later arcs: bond moments, romance, a clan. */
    static void later(Run r, int index) {
        var w = r.w;
        // Each part of a later arc: a bond quest for everyone close enough, and a notable moment on a harder mission.
        var close = List.of(TEAMMATE_A, TEAMMATE_B, SENSEI, RIVAL, CLASSMATE_C, CLASSMATE_D);
        if (index == 1) for (String who : close) r.bondQuest(who, 10 + r.part, 4, null);
        if (index == 7) for (String who : r.squad()) {
            Act[] beats = {Act.HEART_TO_HEART, Act.PROTECTED_THEM, Act.STOOD_BY_THEM, Act.KEPT_PROMISE};
            if (r.roll(r.p.sideQuests)) w.act(who, beats[r.part % beats.length]);
        }
        if (index == 9 && r.part % 4 == 0 && r.p != Profile.RECKLESS) {
            var team = r.teammates();
            if (!team.isEmpty()) w.act(team.get(r.part / 4 % team.size()), Act.SAVED_LIFE, r.squad());
        }
        if (index == 4) w.experience(Act.FESTIVAL_TOGETHER, r.squad());
        if (index == 6 && r.roll(.5)) w.act(RIVAL, r.roll(.5) ? Act.SPAR_WON : Act.SPAR_LOST);
        if (w.playerStage() == Person.Stage.CHILD || r.p == Profile.RECKLESS && index != 3) return;
        // Romance: court whoever the player clicks with most.
        String partner = w.bonded().stream().filter(w::romanceOpen).filter(id -> w.level(id) >= 5).max(java.util.Comparator.comparingDouble(id -> w.meters(id).romance())).orElse("");
        if (partner.isEmpty()) return;
        if (w.bond(partner).romance().committed() || r.roll(.5)) w.experience(Act.DATE, List.of(partner));
        for (String move : List.of("ask_out", "confess", "propose", "wed")) {
            String why = w.court(partner, move);
            if (why.isEmpty()) { r.note(move + " " + partner.substring(partner.indexOf(':') + 1)); break; }
        }
    }

    static void notable(Run r, BondEvent e) {
        String who = e.who().contains(":") ? e.who().substring(e.who().indexOf(':') + 1) : e.who();
        switch (e.kind()) {
            case "conflict" -> { if (!e.who().contains(">") && SHOWN.contains(e.who())) r.note(who + " " + e.detail()); }
            case "left_squad", "rejoined", "jealous" -> r.note(who + " " + e.kind() + (e.detail().isEmpty() ? "" : " (" + e.detail() + ")"));
            case "romance" -> { if (!e.detail().equals("interest")) r.note(who + " " + e.detail()); }
            default -> {}
        }
    }

    static void epilogue(Run r) {
        var w = r.w;
        var fire = Kindling.bonfire(w);
        long trials = Kindling.flames(w).stream().filter(Kindling.Flame::natureTrialReady).count();
        r.checks.put("kindling", String.format("first spark %s h, flame %s h, blaze %s h; %d flames, kindled %d times, %d nature trials ready; bonfire %.1f (%s)",
                r.tierHours.getOrDefault("spark", -1.0), r.tierHours.getOrDefault("flame", -1.0), r.tierHours.getOrDefault("blaze", -1.0),
                Kindling.flames(w).size(), r.kindles, trials, fire.strength(), fire.form()));
        r.checks.put("kindling with teammates", r.teammates().stream().map(t -> t.substring(5) + " " + Kindling.tier(w, t).id()).toList().toString());
        r.checks.put("spouse", w.spouse().isEmpty() ? "none" : w.spouse());
        int joined = 0;
        for (String who : w.bonded()) if (Recruitment.refuse(w, who, "player_clan", joined).isEmpty()) joined++;
        r.checks.put("would join a player clan", Integer.toString(joined));
        if (!w.spouse().isEmpty()) {
            w.setFlag(Household.POSTGAME_FLAG, true);
            r.checks.put("child in the post-game", Household.refuse(w, -1).isEmpty() ? Household.born(w, "resident:child_1", "FEMALE").id() : Household.refuse(w, -1));
        }
        r.checks.put("village standing", w.title("village").id() + " (" + Math.round(w.standing("village")) + ")");
        r.checks.put("conflicts started", Long.toString(r.events.stream().filter(e -> e.kind().equals("conflict") && e.detail().startsWith("argument")).count()));
        r.checks.put("fallings-out", Long.toString(r.events.stream().filter(e -> e.kind().equals("conflict") && e.detail().startsWith("falling_out")).count()));
        r.checks.put("squad departures", Long.toString(r.events.stream().filter(e -> e.kind().equals("left_squad")).count()));
    }

    /** Set {@code -Dexplain=role:teammate_a} to print where one bond's meters come from at a few chapters. */
    static final String EXPLAIN = System.getProperty("explain");

    /** Where one bond's meters come from: the base parts and each kind of memory. */
    public static String explain(BondWorld w, String who) {
        var b = w.bond(who); var sb = new StringBuilder();
        var m = w.meters(who);
        sb.append(String.format("L%d feeling %.0f A %.0f T %.0f R %.0f V %.0f Ro %.0f | warmth %.1f together %d contact %d moments %d%n",
                b.level(), dev.shinobi.life.bond.Levels.feeling(m), m.affection(), m.trust(), m.respect(), m.rivalry(), m.romance(), b.warmth(), b.together(), b.contactDays(), b.moments().size()));
        var byAct = new java.util.TreeMap<String, dev.shinobi.life.bond.Meters>();
        for (var mem : b.memories()) byAct.merge(mem.act().id() + (mem.source() == dev.shinobi.life.bond.Reaction.Source.SELF ? "" : "." + mem.source().name().toLowerCase(java.util.Locale.ROOT)),
                mem.now(w.day()), dev.shinobi.life.bond.Meters::plus);
        byAct.forEach((k, v) -> sb.append(String.format("    %-28s A %5.1f T %5.1f R %5.1f V %5.1f Ro %5.1f%n", k, v.affection(), v.trust(), v.respect(), v.rivalry(), v.romance())));
        return sb.toString();
    }

    public static String table(Result res) {
        var sb = new StringBuilder();
        sb.append("\n== ").append(res.profile().id()).append(" player ==\n");
        sb.append(String.format("%-9s %-24s %5s %4s | %3s %3s %3s %3s %3s %3s %3s | %4s %-13s %s%n", "chapter", "", "hours", "day",
                "tmA", "tmB", "sen", "ins", "clC", "clD", "riv", "coh", "village", "notes"));
        for (var row : res.rows()) {
            var l = row.levels();
            sb.append(String.format("%-9s %-24s %5.1f %4d | %3d %3d %3d %3d %3d %3d %3d | %4.0f %-13s %s%n", row.chapter(), row.title(), row.hours(), row.day(),
                    l.get(TEAMMATE_A), l.get(TEAMMATE_B), l.get(SENSEI), l.get(INSTRUCTOR), l.get(CLASSMATE_C), l.get(CLASSMATE_D), l.get(RIVAL),
                    row.cohesion(), row.village(), row.notes()));
        }
        sb.append("checks:\n");
        res.checks().forEach((k, v) -> sb.append("  ").append(k).append(": ").append(v).append('\n'));
        var w = res.world();
        sb.append("final meters (affection / trust / respect / rivalry / romance):\n");
        for (String who : SHOWN) {
            var m = w.meters(who);
            sb.append(String.format("  %-11s L%-2d %5.0f %5.0f %5.0f %5.0f %5.0f  %s%n", who.substring(5), w.level(who), m.affection(), m.trust(), m.respect(),
                    m.rivalry(), m.romance(), w.bond(who).conflict().state() == Conflict.State.NONE ? "" : w.bond(who).conflict().state().id()));
        }
        return sb.toString();
    }

    /** The Bonfire across seeds, per kind of player: min, median and max strength, and the forms. */
    public static String bonfires(long[] seeds) {
        var sb = new StringBuilder("\n== Bonfire across seeds ==\n");
        for (var profile : Profile.values()) {
            var strengths = new ArrayList<Double>(); var forms = new java.util.TreeMap<String, Integer>();
            for (long seed : seeds) { var b = Kindling.bonfire(play(seed, profile).world()); strengths.add(b.strength()); forms.merge(b.form(), 1, Integer::sum); }
            java.util.Collections.sort(strengths);
            sb.append(String.format("  %-8s min %.1f, median %.1f, max %.1f; %s%n", profile.id(), strengths.getFirst(), strengths.get(strengths.size() / 2), strengths.getLast(), forms));
        }
        return sb.toString();
    }

    /** The Hokage's standing across seeds, per kind of player and checkpoint: Hero with the village, Good Neighbor everywhere. */
    public static String standingsAcross(long[] seeds) {
        var sb = new StringBuilder("\n== Standing across seeds (Hero with the village; Good Neighbor in every district and clan) ==\n");
        for (var profile : Profile.values()) {
            var runs = java.util.Arrays.stream(seeds).mapToObj(s -> play(s, profile).standing()).toList();
            for (int h : STANDING_HOURS) {
                var at = runs.stream().map(m -> m.get(h)).toList();
                var villages = at.stream().mapToDouble(Standings::village).sorted().toArray();
                sb.append(String.format("  %-8s %2d h  village %.1f to %.1f, hero in %d of %d; good neighbor everywhere in %d of %d (places: %d to %d)%n",
                        profile.id(), h, villages[0], villages[villages.length - 1], at.stream().filter(Standings::hero).count(), seeds.length,
                        at.stream().filter(Standings::everywhere).count(), seeds.length, at.stream().mapToInt(Standings::goodNeighbor).min().orElse(0),
                        at.stream().mapToInt(Standings::communities).min().orElse(0), at.stream().mapToInt(Standings::communities).max().orElse(0)));
            }
        }
        return sb.toString();
    }

    /** {@code BondWeb.score} at the end of the path, per kind of player across seeds: for the finale's web tiers. */
    public static String websAcross(long[] seeds) {
        var sb = new StringBuilder("\n== Bond web at the finale (BondWeb.score) ==\n");
        for (var profile : Profile.values()) {
            var scores = java.util.Arrays.stream(seeds).mapToInt(s -> dev.shinobi.life.bond.BondWeb.score(play(s, profile).world())).sorted().toArray();
            sb.append(String.format("  %-8s %s%n", profile.id(), java.util.Arrays.toString(scores)));
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        long seed = args.length > 0 ? Long.parseLong(args[0]) : 20261029L;
        System.out.println("Bond pacing, seed " + seed + " (levels are the level each person acts on; coh = squad cohesion)");
        for (var profile : Profile.values()) System.out.print(table(play(seed, profile)));
        System.out.print(bonfires(new long[]{seed, 7, 11, 99, 2024}));
        System.out.print(standingsAcross(new long[]{seed, 7, 11, 99, 2024}));
        System.out.print(websAcross(new long[]{seed, 7, 11, 99, 2024}));
    }

    private Playthrough() {}
}
