package dev.shinobi.combat;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

/**
 * Everything in data/combat/ (compiled by tools/combat/build.py), read into typed records. Phase 0's mod builds the
 * same records from the datapack through Minecraft's resource manager; tests and the simulator read the folder.
 */
public final class CombatData {
    public record Technique(String id, String name, String kind, Nature nature, String rank, int level, List<HandSign> signs, double chakra,
                            int castTicks, int cooldownTicks, double power, Map<String, Object> shape, List<Map<String, Object>> effects,
                            String slice, String clan, int tier, boolean beta, List<String> requires) {
        static Technique of(Map<String, Object> m) {
            var fx = new ArrayList<Map<String, Object>>();
            for (Object o : Json.list(m, "effects")) fx.add(Json.obj(o));
            return new Technique(Json.str(m, "id", "?"), Json.str(m, "name", "?"), Json.str(m, "kind", "ninjutsu"), Nature.of(Json.str(m, "nature", "none")),
                    Json.str(m, "rank", "e"), Json.integer(m, "level", 1), HandSign.sequence(Json.strings(m, "signs")), Json.num(m, "chakra", 0),
                    Json.integer(m, "cast_ticks", 0), Json.integer(m, "cooldown_ticks", 0), Json.num(m, "power", 0), Json.obj(m, "shape"), fx,
                    Json.str(m, "slice", "beta1"), Json.str(m, "clan", null), Json.integer(m, "tier", 0), Json.bool(m, "beta"), Json.strings(m, "requires"));
        }
        public String shapeType() { return Json.str(shape, "type", "self"); }
        public double range() {
            return switch (shapeType()) {
                case "melee" -> Json.num(shape, "range", 3);
                case "area" -> Json.num(shape, "radius", 4) + Json.num(shape, "offset", 0);
                case "self" -> 0;
                case "entity" -> Json.num(shape, "range", 12);
                default -> Json.num(shape, "range", 12);
            };
        }
        /** Blocks a tick for projectiles; instant shapes report a large number. */
        public double speed() { return "projectile".equals(shapeType()) ? Json.num(shape, "speed", 1) : 99; }
        public double radius() { return Math.max(Json.num(shape, "radius", 0), Math.max(Json.num(shape, "burst", 0), Json.num(shape, "width", 0) / 2)); }
        public int count() { return Json.integer(shape, "count", 1); }
        public double homing() { return Json.num(shape, "homing", 0); }
        public boolean dash() { return Json.bool(shape, "dash"); }
        public boolean breaksGuard() { return Json.bool(shape, "breaks_guard") || Json.num(shape, "guard_pierce", 0) >= 1; }
        /** The damage type of the first damage effect, or null for techniques that do no damage. */
        public String damageType() {
            for (var e : effects) if (e.get("damage") instanceof String t) return t;
            return null;
        }
        /** (status, ticks) pairs the technique applies. */
        public List<Map.Entry<String, Integer>> statuses() {
            var out = new ArrayList<Map.Entry<String, Integer>>();
            for (var e : effects) if (e.get("status") instanceof String s) out.add(Map.entry(s, Json.integer(e, "ticks", 0)));
            return out;
        }
        public boolean signless() { return signs.isEmpty(); }
    }
    public record Weapon(String item, String cls, Map<String, Object> melee, Map<String, Object> thrown, String style) {
        static Weapon of(Map<String, Object> m) {
            return new Weapon(Json.str(m, "item", "?"), Json.str(m, "class", "melee"), Json.obj(m, "melee"), Json.obj(m, "throw"), Json.str(m, "style", null));
        }
        public boolean canThrow() { return !thrown.isEmpty(); }
        public boolean canMelee() { return !melee.isEmpty(); }
    }
    public record Enemy(String id, String kind, String tier, String rank, int minLevel, int maxLevel, String band, String style, List<String> weapons,
                        List<String> techniques, Map<String, Object> tools, Nature nature, Map<String, Object> armour, List<String> traits,
                        Map<String, Object> ai, double hpMult, double poise, double damageMult, int thinkTicks) {
        static Enemy of(Map<String, Object> m, Map<String, Object> tiers) {
            var lv = Json.list(m, "levels");
            String tier = Json.str(m, "tier", "mook");
            var t = Json.obj(tiers, tier);
            return new Enemy(Json.str(m, "id", "?"), Json.str(m, "kind", "human"), tier, Json.str(m, "rank", "genin"),
                    ((Number) lv.get(0)).intValue(), ((Number) lv.get(1)).intValue(), Json.str(m, "band", "close"), Json.str(m, "style", null),
                    Json.strings(m, "weapons"), Json.strings(m, "techniques"), Json.obj(m, "tools"), Nature.of(Json.str(m, "nature", "none")),
                    Json.obj(m, "armour"), Json.strings(m, "traits"), Json.obj(m, "ai"), Json.num(m, "hp_mult", Json.num(t, "hp", 1)),
                    Json.num(m, "poise", Json.num(t, "poise", 15)), Json.num(t, "damage", 1), Json.integer(t, "think_ticks", 6));
        }
        public boolean animal() { return "animal".equals(kind); }
        public boolean has(String trait) { return traits.contains(trait); }
    }
    public record Phase(double atHp, String name, List<String> adds) {}
    public record Boss(String id, String slice, String base, int level, boolean nonlethal, double hpMult, double poise, List<Phase> phases,
                       List<String> techniques, List<String> weapons, String style, String role, Map<String, Object> armour, double damageMult,
                       boolean npcOnly) {
        static Boss of(Map<String, Object> m) {
            var ph = new ArrayList<Phase>();
            for (Object o : Json.list(m, "phases")) {
                var p = Json.obj(o);
                ph.add(new Phase(Json.num(p, "at_hp", 1), Json.str(p, "name", "?"), Json.strings(p, "adds")));
            }
            return new Boss(Json.str(m, "id", "?"), Json.str(m, "slice", "beta1"), Json.str(m, "base", "?"), Json.integer(m, "level", 1),
                    Json.bool(m, "nonlethal"), Json.num(m, "hp_mult", 7), Json.num(m, "poise", 100), ph, Json.strings(m, "techniques"),
                    Json.strings(m, "weapons"), Json.str(m, "style", null), Json.str(m, "role", null), Json.obj(m, "armour"),
                    Json.num(m, "damage_mult", 1), Json.bool(m, "npc_only"));
        }
    }
    public record Build(String id, String focus, int level, Nature nature, Map<Scaling.Pillar, Integer> ranks, int control, double physical,
                        double chakraArmour, List<String> techniques, String style, int styleTier, String melee, String thrown, int gates,
                        Map<String, Object> tools, String niche, double nicheEdge, boolean pup) {
        static Build of(Map<String, Object> m) {
            var r = Json.obj(m, "ranks");
            var ranks = new LinkedHashMap<Scaling.Pillar, Integer>();
            ranks.put(Scaling.Pillar.TAIJUTSU, Json.integer(r, "taijutsu", 1));
            ranks.put(Scaling.Pillar.WEAPONS, Json.integer(r, "weapons", 1));
            ranks.put(Scaling.Pillar.NINJUTSU, Json.integer(r, "ninjutsu", 1));
            var a = Json.obj(m, "armour");
            return new Build(Json.str(m, "id", "?"), Json.str(m, "focus", "balanced"), Json.integer(m, "level", 1), Nature.of(Json.str(m, "nature", "none")),
                    ranks, Json.integer(m, "control", 30), Json.num(a, "physical", 0), Json.num(a, "chakra", 0), Json.strings(m, "techniques"),
                    Json.str(m, "style", "combat:style.academy_basics"), Json.integer(m, "style_tier", 1), Json.str(m, "melee", null),
                    Json.str(m, "thrown", null), Json.integer(m, "gates", 0), Json.obj(m, "tools"), Json.str(m, "niche", null),
                    Json.num(m, "niche_edge", 0), Json.bool(m, "pup"));
        }
        public int rank(Scaling.Pillar p) { return ranks.get(p); }
    }

    /** A keyed clip of animations.json: each part's {tick, x, y, z} keys (degrees), in tick order. */
    public record Clip(int ticks, boolean loop, Map<String, List<double[]>> keys) {
        static Clip of(Map<String, Object> m) {
            var keys = new LinkedHashMap<String, List<double[]>>();
            for (Object o : Json.list(m, "keys")) {
                var k = Json.obj(o);
                var r = Json.list(k, "rot");
                keys.computeIfAbsent(Json.str(k, "part", "?"), p -> new ArrayList<>())
                        .add(new double[]{Json.num(k, "tick", 0), ((Number) r.get(0)).doubleValue(), ((Number) r.get(1)).doubleValue(), ((Number) r.get(2)).doubleValue()});
            }
            for (var l : keys.values()) l.sort(Comparator.comparingDouble(k -> k[0]));
            return new Clip(Json.integer(m, "ticks", 0), Json.bool(m, "loop"), keys);
        }
        /** A part's rotation (x, y, z degrees) {@code t} ticks in: linear between keys, wrapped when looping, held after the last; null if the clip leaves the part alone. */
        public double[] rot(String part, double t) {
            var ks = keys.get(part);
            if (ks == null) return null;
            if (loop && ticks > 0) t = ((t % ticks) + ticks) % ticks;
            int i = 0;
            while (i < ks.size() && ks.get(i)[0] <= t) i++;
            if (i == 0 || i == ks.size()) { var k = ks.get(i == 0 ? 0 : i - 1); return new double[]{k[1], k[2], k[3]}; }
            double[] a = ks.get(i - 1), b = ks.get(i);
            double f = (t - a[0]) / (b[0] - a[0]);
            return new double[]{a[1] + (b[1] - a[1]) * f, a[2] + (b[2] - a[2]) * f, a[3] + (b[3] - a[3]) * f};
        }
    }

    public final Map<String, Technique> techniques = new LinkedHashMap<>();
    public final Map<String, Style> styles = new LinkedHashMap<>();
    public final Map<String, Weapon> weapons = new LinkedHashMap<>();
    public final Map<String, Enemy> enemies = new LinkedHashMap<>();
    public final Map<String, Boss> bosses = new LinkedHashMap<>();
    public final Map<String, List<Map<String, Object>>> groups = new LinkedHashMap<>();
    public final Map<String, Build> builds = new LinkedHashMap<>();
    public final Map<String, Difficulty> difficulties = new LinkedHashMap<>();
    public final Map<String, StatusEffects.Def> statuses;
    public final Map<String, Object> gates, ai, tiers, damageTypes, index;
    public final List<String> clans = new ArrayList<>();
    /** The clips of animations.json that have keys. */
    public final Map<String, Clip> clips = new LinkedHashMap<>();

    private final Path root;

    public CombatData(Path root) {
        this.root = root;
        for (Path f : files("techniques")) {
            String n = f.getFileName().toString();
            if (n.equals("movement.json") || n.equals("rules.json")) continue;
            for (Object o : Json.list(read(f), "techniques")) add(Technique.of(Json.obj(o)));
        }
        for (Path f : files("clans")) {
            if (f.getFileName().toString().startsWith("_")) continue;
            var c = read(f);
            clans.add(Json.str(c, "id", "?"));
            for (Object o : Json.list(c, "techniques")) add(Technique.of(Json.obj(o)));
            if (c.get("lesser") != null) add(Technique.of(Json.obj(c, "lesser")));
        }
        for (String f : List.of("styles/taijutsu.json", "styles/weapons.json"))
            for (Object o : Json.list(read(root.resolve(f)), "styles")) { var s = Style.of(Json.obj(o)); styles.put(s.id(), s); }
        for (Object o : Json.list(read(root.resolve("weapons/weapons.json")), "weapons")) { var w = Weapon.of(Json.obj(o)); weapons.put(w.item(), w); }
        var aiFile = read(root.resolve("enemies/_ai.json"));
        ai = Json.obj(aiFile, "ai");
        tiers = Json.obj(aiFile, "tiers");
        for (Path f : files("enemies")) {
            if (f.getFileName().toString().startsWith("_")) continue;
            var e = Enemy.of(read(f), tiers);
            enemies.put(e.id(), e);
        }
        for (Object o : Json.list(read(root.resolve("enemies/_groups.json")), "groups")) {
            var g = Json.obj(o);
            var members = new ArrayList<Map<String, Object>>();
            for (Object m : Json.list(g, "members")) members.add(Json.obj(m));
            groups.put(Json.str(g, "id", "?"), members);
        }
        for (Path f : files("bosses")) { var b = Boss.of(read(f)); bosses.put(b.id(), b); }
        for (Object o : Json.list(read(root.resolve("sim/builds.json")), "builds")) { var b = Build.of(Json.obj(o)); builds.put(b.id(), b); }
        var diff = Json.obj(read(root.resolve("core/difficulty.json")), "modes");
        for (var e : diff.entrySet()) difficulties.put(e.getKey(), Difficulty.of(e.getKey(), Json.obj(e.getValue())));
        statuses = StatusEffects.defs(Json.obj(read(root.resolve("core/status_effects.json")), "statuses"));
        gates = read(root.resolve("styles/gates.json"));
        damageTypes = Json.obj(read(root.resolve("core/damage_types.json")), "types");
        index = Json.obj(read(root.resolve("index.json")), "counts");
        for (var e : Json.obj(read(root.resolve("animations.json")), "clips").entrySet())
            if (!Json.list(Json.obj(e.getValue()), "keys").isEmpty()) clips.put(e.getKey(), Clip.of(Json.obj(e.getValue())));
    }

    /** The folder the build writes to, from the {@code combat.data} system property or the working directory. */
    public static CombatData load() {
        String p = System.getProperty("combat.data");
        Path dir = p != null ? Path.of(p) : Path.of("data", "combat");
        if (!Files.isDirectory(dir)) dir = Path.of("..", "..", "data", "combat");
        return new CombatData(dir);
    }

    private void add(Technique t) {
        if (techniques.put(t.id(), t) != null) throw new IllegalStateException("duplicate technique " + t.id());
    }
    public Technique technique(String id) {
        var t = techniques.get(id);
        if (t == null) throw new IllegalArgumentException("unknown technique " + id);
        return t;
    }
    public Style style(String id) {
        var s = styles.get(id);
        if (s == null) throw new IllegalArgumentException("unknown style " + id);
        return s;
    }
    /** A style laid over Academy taijutsu, ready for a {@link ComboMachine}. */
    public Style moveset(String id) {
        var base = style("combat:style.academy_basics");
        return id == null || id.equals(base.id()) ? base : style(id).over(base);
    }

    private List<Path> files(String dir) {
        try (Stream<Path> s = Files.list(root.resolve(dir))) {
            return s.filter(p -> p.toString().endsWith(".json")).sorted().toList();
        } catch (IOException e) { throw new UncheckedIOException(e); }
    }
    private static Map<String, Object> read(Path f) {
        try { return Json.obj(Json.parse(Files.readString(f))); }
        catch (IOException e) { throw new UncheckedIOException(e); }
    }
}
