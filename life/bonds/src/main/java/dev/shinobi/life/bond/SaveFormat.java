package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

/**
 * The bond engine's save, as plain maps, lists, strings, numbers and booleans, so the Life mod's player attachment
 * can wrap it in a Codec (or NBT) without the engine knowing Minecraft. People are not saved here: the cast and
 * the residents come from Shinobi Village on load, and the bonds attach to them by id.
 *
 * <p>Every save carries {@code "format"}. {@link #FORMAT} is current; older formats are migrated on load
 * ({@link #migrate}); a newer one is refused with a clear message rather than misread. Format 0 is Village
 * Friends' own player friendship ({@code FriendshipState} points and {@code BondState} trust and level per
 * resident), so a VF world that gains Shinobi Life keeps its friendships.
 */
public final class SaveFormat {
    public static final int FORMAT = 1;

    public static Map<String, Object> write(BondWorld w) {
        var out = new LinkedHashMap<String, Object>();
        out.put("format", FORMAT);
        out.put("day", w.day);
        out.put("next_serial", w.nextSerial);
        out.put("flags", List.copyOf(w.flags));
        out.put("player", map("stage", w.playerStage.id(), "rank", w.playerRank, "gender", w.playerGender, "clan", w.playerClan));
        var bonds = new LinkedHashMap<String, Object>();
        for (var e : w.bonds.entrySet()) bonds.put(e.getKey(), bond(e.getValue()));
        out.put("bonds", bonds);
        if (w.squad != null) out.put("squad", squad(w.squad));
        var deeds = new ArrayList<Object>();
        for (var d : w.deeds) {
            var knowers = new LinkedHashMap<String, Object>();
            d.knowers.forEach((id, k) -> knowers.put(id, map("how", id(k.how()), "day", k.day(), "from", k.from(), "slant", k.slant())));
            deeds.add(map("serial", d.serial, "act", d.act.id(), "day", d.day, "about", d.about, "note", d.note, "forgiven", d.forgiven, "quiet", d.quiet, "knowers", knowers));
        }
        out.put("deeds", deeds);
        out.put("plans", w.plans.stream().map(p -> (Object) map("id", p.id(), "with", p.with(), "activity", p.activity(), "day", p.day(), "hour", p.hour(), "host", p.host())).toList());
        out.put("invitations", w.invitations.stream().map(i -> (Object) map("id", i.id(), "from", i.from(), "activity", i.activity(), "day", i.day(), "hour", i.hour(), "expires", i.expires())).toList());
        out.put("invited_on", new TreeMap<>(w.invitedOn));
        out.put("plan_serial", w.planSerial);
        out.put("gift_serial", w.giftSerial);
        out.put("received", w.received.stream().map(r -> (Object) map("id", r.id(), "item", r.item(), "from", r.from(), "day", r.day(),
                "occasion", r.occasion(), "seen", r.seen())).toList());
        out.put("questions_today", w.questionsToday); out.put("questions_day", w.questionsDay);
        return out;
    }

    private static Map<String, Object> bond(Bond b) {
        var m = new LinkedHashMap<String, Object>();
        m.put("met", b.met); m.put("last_contact", b.lastContact); m.put("last_together", b.lastTogether);
        m.put("talk_day", b.talkDay); m.put("gift_day", b.giftDay); m.put("gifts_today", b.giftsToday); m.put("last_gift", b.lastGift);
        m.put("contact_days", b.contactDays); m.put("together", b.together); m.put("warmth", b.warmth);
        m.put("level", b.level); m.put("floor", b.floor); m.put("low_days", b.lowDays); m.put("kindled", b.kindled); m.put("resonance", b.resonance); m.put("resonance_day", b.resonanceDay);
        m.put("romance", b.romance.id()); m.put("romance_since", b.romanceSince); m.put("teen_since", b.teenSince);
        var memories = new ArrayList<Object>();
        for (var mem : b.memories) {
            var d = mem.delta();
            memories.add(map("act", mem.act().id(), "day", mem.day(), "delta", List.of(d.affection(), d.trust(), d.respect(), d.rivalry(), d.romance()),
                    "source", id(mem.source()), "about", mem.about(), "count", mem.count()));
        }
        m.put("memories", memories);
        var exp = new LinkedHashMap<String, Object>();
        b.experiences.forEach((k, v) -> exp.put(id(k), v));
        m.put("experiences", exp);
        var hang = new LinkedHashMap<String, Object>();
        b.hangouts.forEach((k, v) -> hang.put(k, List.copyOf(v)));
        m.put("hangouts", hang); m.put("rituals", List.copyOf(b.rituals));
        m.put("highlights", b.highlights.stream().map(h -> (Object) map("activity", h.activity(), "day", h.day(), "key", h.key(), "with", h.with())).toList());
        m.put("last_asked", b.lastAsked); m.put("quiet_until", b.quietUntil); m.put("declined_by_them", b.declinedByThem); m.put("declined_by_you", b.declinedByYou);
        m.put("news", b.news.stream().map(n -> (Object) map("kind", n.kind().id(), "day", n.day(), "shared", n.shared(), "shared_day", n.sharedDay(), "response", n.response())).toList());
        m.put("follow_ups", b.followUps.stream().map(f -> (Object) map("topic", f.topic(), "due", f.due(), "they_ask", f.theyAsk())).toList());
        m.put("answers", b.answers.stream().map(a -> (Object) map("question", a.question(), "answer", a.answer(), "day", a.day(), "about", a.about(),
                "stance", a.stance(), "recalled", a.recalled())).toList());
        m.put("pending_question", b.pendingQuestion); m.put("pending_since", b.pendingSince); m.put("last_question", b.lastQuestion);
        m.put("nudges", new TreeMap<>(b.nudges)); m.put("mood", b.mood); m.put("mood_day", b.moodDay);
        m.put("moments", List.copyOf(b.moments)); m.put("facts", List.copyOf(b.facts)); m.put("flags", List.copyOf(b.flags));
        var c = b.conflict;
        m.put("conflict", map("state", c.state().id(), "since", c.since(), "until", c.until(), "severity", c.severity(),
                "cause", c.cause() == null ? "" : c.cause().id(), "strikes", c.strikes()));
        return m;
    }
    private static Map<String, Object> squad(Squad s) {
        var departed = new LinkedHashMap<String, Object>();
        s.departed.forEach((id, d) -> departed.put(id, map("reason", d.reason(), "day", d.day(), "replaced_by", d.replacedBy())));
        return map("id", s.id, "sensei", s.sensei == null ? "" : s.sensei, "teammates", List.copyOf(s.teammates), "bench", List.copyOf(s.bench),
                "formed", s.formed, "missions", s.missions, "attention", new TreeMap<>(s.attention), "jealousy", new TreeMap<>(s.jealousy),
                "low_days", new TreeMap<>(s.lowDays), "overlooked", new TreeMap<>(s.overlooked), "departed", departed);
    }

    /** Restores a save onto a world that already holds the people (the cast and residents). */
    @SuppressWarnings("unchecked")
    public static BondWorld read(Map<String, Object> saved, long seed, List<Person> people) {
        var in = migrate(saved);
        var w = new BondWorld(seed, lng(in.get("day")));
        for (var p : people) w.add(p);
        w.nextSerial = (int) lng(in.getOrDefault("next_serial", 1));
        w.flags.addAll((List<String>) in.getOrDefault("flags", List.of()));
        var player = (Map<String, Object>) in.getOrDefault("player", Map.of());
        w.playerStage = Person.Stage.valueOf(((String) player.getOrDefault("stage", "child")).toUpperCase(Locale.ROOT));
        w.playerRank = (int) lng(player.getOrDefault("rank", 0));
        w.playerGender = (String) player.getOrDefault("gender", "NON_BINARY");
        w.playerClan = (String) player.getOrDefault("clan", "");
        for (var e : ((Map<String, Object>) in.getOrDefault("bonds", Map.of())).entrySet()) {
            String[] ends = e.getKey().split(">", 2);
            if (w.person(ends[0]) == null || !ends[1].equals(BondWorld.PLAYER) && w.person(ends[1]) == null) continue; // someone gone from the pack
            readBond(w.bond(ends[0], ends[1]), (Map<String, Object>) e.getValue());
        }
        if (in.get("squad") instanceof Map<?, ?> sq) w.squad = readSquad((Map<String, Object>) sq);
        for (Object o : (List<Object>) in.getOrDefault("deeds", List.of())) {
            var d = (Map<String, Object>) o;
            var act = known(Act.class, d.get("act"));
            if (act == null) continue; // an act this pack no longer has
            var deed = new Deed((int) lng(d.get("serial")), act, lng(d.get("day")), (String) d.getOrDefault("about", ""));
            deed.note = (String) d.getOrDefault("note", "");
            deed.forgiven = Boolean.TRUE.equals(d.get("forgiven"));
            deed.quiet = (int) lng(d.getOrDefault("quiet", 0));
            for (var k : ((Map<String, Object>) d.getOrDefault("knowers", Map.of())).entrySet()) {
                var km = (Map<String, Object>) k.getValue();
                var how = known(Reaction.Source.class, km.get("how"));
                if (how != null) deed.knowers.put(k.getKey(), new Deed.Know(how, lng(km.get("day")), (String) km.getOrDefault("from", ""), dbl(km.getOrDefault("slant", 0))));
            }
            w.deeds.add(deed);
        }
        for (Object o : (List<Object>) in.getOrDefault("plans", List.of())) {
            var p = (Map<String, Object>) o;
            w.plans.add(new Together.Plan((String) p.get("id"), (List<String>) p.get("with"), (String) p.get("activity"), lng(p.get("day")), (int) lng(p.get("hour")), (String) p.get("host")));
        }
        for (Object o : (List<Object>) in.getOrDefault("invitations", List.of())) {
            var i = (Map<String, Object>) o;
            w.invitations.add(new Together.Invitation((String) i.get("id"), (String) i.get("from"), (String) i.get("activity"), lng(i.get("day")), (int) lng(i.get("hour")), lng(i.get("expires"))));
        }
        ((Map<String, Object>) in.getOrDefault("invited_on", Map.of())).forEach((k, v) -> w.invitedOn.put(k, lng(v)));
        w.planSerial = (int) lng(in.getOrDefault("plan_serial", 0));
        w.giftSerial = (int) lng(in.getOrDefault("gift_serial", 0));
        for (Object o : (List<Object>) in.getOrDefault("received", List.of())) {
            var r = (Map<String, Object>) o;
            if (w.person((String) r.get("from")) == null) continue;
            w.received.add(new Gifts.Received((int) lng(r.get("id")), (String) r.get("item"), (String) r.get("from"), lng(r.get("day")),
                    (String) r.get("occasion"), (Boolean) r.get("seen")));
        }
        w.questionsToday = (int) lng(in.getOrDefault("questions_today", 0)); w.questionsDay = lng(in.getOrDefault("questions_day", -1));
        // Answers that shaped someone: their personality as the answers left it.
        for (var b : w.bonds.values()) {
            if (b.nudges.isEmpty()) continue;
            var p = w.person(b.from);
            w.unnudged.put(p.id(), p.personality());
            w.add(p.withPersonality(Questions.nudged(p.personality(), b.nudges)));
        }
        return w;
    }
    @SuppressWarnings("unchecked")
    private static void readBond(Bond b, Map<String, Object> m) {
        b.met = lng(m.getOrDefault("met", -1)); b.lastContact = lng(m.getOrDefault("last_contact", -1)); b.lastTogether = lng(m.getOrDefault("last_together", -1));
        b.talkDay = lng(m.getOrDefault("talk_day", -1)); b.giftDay = lng(m.getOrDefault("gift_day", -1)); b.giftsToday = (int) lng(m.getOrDefault("gifts_today", 0));
        b.lastGift = (String) m.getOrDefault("last_gift", "");
        b.contactDays = (int) lng(m.getOrDefault("contact_days", 0)); b.together = (int) lng(m.getOrDefault("together", 0));
        b.warmth = dbl(m.getOrDefault("warmth", 0)); b.level = (int) lng(m.getOrDefault("level", 0)); b.floor = (int) lng(m.getOrDefault("floor", 0)); b.kindled = (int) lng(m.getOrDefault("kindled", 0)); b.resonance = (int) lng(m.getOrDefault("resonance", 0)); b.resonanceDay = lng(m.getOrDefault("resonance_day", -1)); b.lowDays = (int) lng(m.getOrDefault("low_days", 0));
        b.romance = Courtship.Stage.of((String) m.getOrDefault("romance", "none"));
        b.romanceSince = lng(m.getOrDefault("romance_since", -1)); b.teenSince = lng(m.getOrDefault("teen_since", -1));
        for (Object o : (List<Object>) m.getOrDefault("memories", List.of())) {
            var mm = (Map<String, Object>) o; var d = (List<Object>) mm.get("delta");
            var act = known(Act.class, mm.get("act")); var how = known(Reaction.Source.class, mm.getOrDefault("source", "self"));
            if (act == null || how == null) continue; // a memory of an act this pack no longer has
            b.memories.add(new Memory(act, lng(mm.get("day")),
                    new Meters(dbl(d.get(0)), dbl(d.get(1)), dbl(d.get(2)), dbl(d.get(3)), dbl(d.get(4))),
                    how, (String) mm.getOrDefault("about", ""), (int) lng(mm.getOrDefault("count", 1))));
        }
        for (var e : ((Map<String, Object>) m.getOrDefault("experiences", Map.of())).entrySet()) {
            var kind = known(Act.Experience.class, e.getKey());
            if (kind != null) b.experiences.put(kind, (int) lng(e.getValue()));
        }
        b.moments.addAll((List<String>) m.getOrDefault("moments", List.of()));
        ((Map<String, Object>) m.getOrDefault("hangouts", Map.of())).forEach((k, v) -> b.hangouts.put(k, new ArrayList<>(((List<Object>) v).stream().map(SaveFormat::lng).toList())));
        b.rituals.addAll((List<String>) m.getOrDefault("rituals", List.of()));
        for (Object o : (List<Object>) m.getOrDefault("answers", List.of())) {
            var a = (Map<String, Object>) o;
            b.answers.add(new Questions.Answered((String) a.get("question"), (String) a.get("answer"), lng(a.get("day")), (String) a.get("about"),
                    (String) a.get("stance"), (Boolean) a.get("recalled")));
        }
        b.pendingQuestion = (String) m.getOrDefault("pending_question", ""); b.pendingSince = lng(m.getOrDefault("pending_since", -1));
        b.lastQuestion = lng(m.getOrDefault("last_question", -1));
        ((Map<String, Object>) m.getOrDefault("nudges", Map.of())).forEach((k, v) -> b.nudges.put(k, dbl(v)));
        b.mood = (String) m.getOrDefault("mood", ""); b.moodDay = lng(m.getOrDefault("mood_day", -1));
        for (Object o : (List<Object>) m.getOrDefault("highlights", List.of())) {
            var h = (Map<String, Object>) o;
            b.highlights.add(new Together.Highlight((String) h.get("activity"), lng(h.get("day")), (String) h.get("key"), (List<String>) h.get("with")));
        }
        b.lastAsked = lng(m.getOrDefault("last_asked", -1)); b.quietUntil = lng(m.getOrDefault("quiet_until", -1));
        b.declinedByThem = (int) lng(m.getOrDefault("declined_by_them", 0)); b.declinedByYou = (int) lng(m.getOrDefault("declined_by_you", 0));
        for (Object o : (List<Object>) m.getOrDefault("news", List.of())) {
            var n = (Map<String, Object>) o;
            b.news.add(new LifeEvents.News(LifeEvents.Kind.of((String) n.get("kind")), lng(n.get("day")), (Boolean) n.get("shared"), lng(n.get("shared_day")), (String) n.get("response")));
        }
        for (Object o : (List<Object>) m.getOrDefault("follow_ups", List.of()))
            { var f = (Map<String, Object>) o; b.followUps.add(new Together.FollowUp((String) f.get("topic"), lng(f.get("due")), (Boolean) f.get("they_ask"))); }
        b.facts.addAll((List<String>) m.getOrDefault("facts", List.of()));
        b.flags.addAll((List<String>) m.getOrDefault("flags", List.of()));
        var c = (Map<String, Object>) m.getOrDefault("conflict", Map.of());
        String cause = (String) c.getOrDefault("cause", "");
        b.conflict = new Conflict(Conflict.State.of((String) c.getOrDefault("state", "none")), lng(c.getOrDefault("since", -1)), lng(c.getOrDefault("until", -1)),
                dbl(c.getOrDefault("severity", 0)), known(Act.class, cause), (int) lng(c.getOrDefault("strikes", 0)));
    }
    @SuppressWarnings("unchecked")
    private static Squad readSquad(Map<String, Object> m) {
        String sensei = (String) m.getOrDefault("sensei", "");
        var s = new Squad((String) m.get("id"), sensei.isEmpty() ? null : sensei, (List<String>) m.getOrDefault("teammates", List.of()),
                (List<String>) m.getOrDefault("bench", List.of()), lng(m.getOrDefault("formed", 0)));
        s.missions = (int) lng(m.getOrDefault("missions", 0));
        ((Map<String, Object>) m.getOrDefault("attention", Map.of())).forEach((k, v) -> s.attention.put(k, dbl(v)));
        ((Map<String, Object>) m.getOrDefault("jealousy", Map.of())).forEach((k, v) -> s.jealousy.put(k, dbl(v)));
        ((Map<String, Object>) m.getOrDefault("low_days", Map.of())).forEach((k, v) -> s.lowDays.put(k, (int) lng(v)));
        ((Map<String, Object>) m.getOrDefault("overlooked", Map.of())).forEach((k, v) -> s.overlooked.put(k, (Boolean) v));
        ((Map<String, Object>) m.getOrDefault("departed", Map.of())).forEach((k, v) -> {
            var d = (Map<String, Object>) v;
            s.departed.put(k, new Squad.Departure((String) d.get("reason"), lng(d.get("day")), (String) d.getOrDefault("replaced_by", "")));
        });
        return s;
    }

    /**
     * Brings an older save up to {@link #FORMAT}. Format 0, Village Friends' player friendship:
     * <pre>{"format": 0, "day": 40, "friendships": {"&lt;resident&gt;": {"points": 120, "trust": 65, "level": 6}}}</pre>
     * Points become warmth (a fifth, at most 40) and contact days (a third, at most 60); VF trust above or below its
     * starting 50 becomes a permanent memory of time together; VF's level is kept as a floor, so nobody loses a level
     * they earned.
     */
    @SuppressWarnings("unchecked")
    public static Map<String, Object> migrate(Map<String, Object> saved) {
        int format = (int) lng(saved.getOrDefault("format", 0));
        if (format > FORMAT) throw new IllegalStateException("bond save format " + format + " is newer than this pack's " + FORMAT + "; update Shinobi Life");
        if (format == FORMAT) return saved;
        var out = new LinkedHashMap<String, Object>();
        long day = lng(saved.getOrDefault("day", 0));
        out.put("format", FORMAT); out.put("day", day);
        var bonds = new LinkedHashMap<String, Object>();
        for (var e : ((Map<String, Object>) saved.getOrDefault("friendships", Map.of())).entrySet()) {
            var f = (Map<String, Object>) e.getValue();
            double points = dbl(f.getOrDefault("points", 0)), trust = dbl(f.getOrDefault("trust", 50));
            var memories = new ArrayList<Object>();
            if (trust != 50) memories.add(map("act", Act.YEARS_TOGETHER.id(), "day", day, "delta", List.of(0.0, (trust - 50) * .6, 0.0, 0.0, 0.0), "source", "self", "about", "", "count", 1));
            bonds.put(e.getKey() + ">" + BondWorld.PLAYER, map("met", Math.max(0, day - 1), "last_contact", day, "contact_days", (long) Math.min(60, points / 3),
                    "warmth", Math.min(Bond.WARMTH_CAP, points / 5), "level", lng(f.getOrDefault("level", Levels.byPoints(points))),
                    "floor", lng(f.getOrDefault("level", Levels.byPoints(points))), "memories", memories,
                    "experiences", points >= 40 ? map("meal", 1) : Map.of(), "moments", points >= 105 ? List.of("vf.story") : List.of()));
        }
        out.put("bonds", bonds);
        return out;
    }

    private static Map<String, Object> map(Object... kv) {
        var m = new LinkedHashMap<String, Object>();
        for (int i = 0; i < kv.length; i += 2) m.put((String) kv[i], kv[i + 1]);
        return m;
    }
    /** The constant an id names, or null for an id this pack no longer has (an act or a kind renamed or removed). */
    static <E extends Enum<E>> E known(Class<E> type, Object id) {
        if (!(id instanceof String s) || s.isEmpty()) return null;
        try { return Enum.valueOf(type, s.toUpperCase(Locale.ROOT)); } catch (IllegalArgumentException e) { return null; }
    }
    private static String id(Enum<?> e) { return e.name().toLowerCase(Locale.ROOT); }
    static long lng(Object o) { return o instanceof Number n ? n.longValue() : Long.parseLong(o.toString()); }
    static double dbl(Object o) { return o instanceof Number n ? n.doubleValue() : Double.parseDouble(o.toString()); }

    private SaveFormat() {}
}
