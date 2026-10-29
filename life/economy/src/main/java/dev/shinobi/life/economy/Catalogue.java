package dev.shinobi.life.economy;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import static dev.shinobi.life.economy.Json.integer;
import static dev.shinobi.life.economy.Json.list;
import static dev.shinobi.life.economy.Json.obj;
import static dev.shinobi.life.economy.Json.str;

/**
 * The compiled item data (data/items/, written by tools/items/items.py): every item with its price, the shops and
 * their stock, part-time jobs, services, stations, recipes, kits, and the economy's tuning (economy.json).
 */
public final class Catalogue {
    /** One registry entry. {@code sell} is what it sells back for (0: it cannot be sold). */
    public record Item(String id, String name, String category, String group, String rank, String slice, int stack,
                       int price, int sell, Map<String, String> props, Map<String, Variant> variants) {
        public String prop(String key) { return props.getOrDefault(key, ""); }
        public boolean has(String key) { return props.containsKey(key); }
    }
    /** A component value of one item (a technique scroll's technique) with its own price. */
    public record Variant(String id, String name, String rank, String slice, int price) {}
    /** One line of a shop's stock. {@code qty} 0 is unlimited; {@code price} 0 means the item's price. */
    public record Line(String item, String variant, String rank, String slice, int qty, String restock, int price, boolean core) {}
    public record Shop(String id, String name, String district, String keeper, String opens, String closes, String closed,
                       String slice, String rank, String standing, String haggle, double markup, int rotating,
                       List<String> orders, List<String> interior, List<Line> stock) {
        public boolean haggles() { return !haggle.equals("no"); }
        public List<Line> core() { return stock.stream().filter(Line::core).toList(); }
        public List<Line> rotation() { return stock.stream().filter(l -> !l.core()).toList(); }
    }
    public record Job(String id, String shop, String rank, String slice, int pay, int hours) {}
    public record Service(String id, String provider, String rank, String slice, int price) {}
    public record Ingredient(String item, int count) {}
    public record Recipe(String id, String station, List<Ingredient> inputs, String vessel, String output, int count,
                         String rank, String slice, String unlock, int difficulty) {}
    public record Station(String id, String name, String slice, String rank, String maxGrade) {}

    public final Map<String, Item> items = new LinkedHashMap<>();
    public final Map<String, Shop> shops = new LinkedHashMap<>();
    public final Map<String, Job> jobs = new LinkedHashMap<>();
    public final Map<String, Service> services = new LinkedHashMap<>();
    public final Map<String, Recipe> recipes = new LinkedHashMap<>();
    public final Map<String, Station> stations = new LinkedHashMap<>();
    public final Map<String, List<Ingredient>> kits = new LinkedHashMap<>();
    public final Map<String, Object> economy;

    private Catalogue(Map<String, Object> items, Map<String, Object> shops, Map<String, Object> recipes,
                      Map<String, Object> kits, Map<String, Object> economy) {
        this.economy = economy;
        for (Object o : list(items.get("items"))) {
            var m = obj(o);
            var props = new LinkedHashMap<String, String>();
            if (m.get("props") != null) obj(m.get("props")).forEach((k, v) -> props.put(k, String.valueOf(v)));
            var variants = new LinkedHashMap<String, Variant>();
            if (m.get("variants") != null) obj(m.get("variants")).forEach((k, v) -> {
                var vm = obj(v);
                variants.put(k, new Variant(k, str(vm.get("name"), k), str(vm.get("rank"), "any"), str(vm.get("slice"), "beta1"),
                        integer(vm.get("price"), 0)));
            });
            var item = new Item(str(m.get("id"), ""), str(m.get("name"), ""), str(m.get("category"), ""), str(m.get("group"), ""),
                    str(m.get("rank"), "any"), str(m.get("slice"), "beta1"), integer(m.get("stack"), 1), integer(m.get("price"), 0),
                    integer(m.get("sell"), 0), Map.copyOf(props), Map.copyOf(variants));
            this.items.put(item.id(), item);
        }
        for (Object o : list(shops.get("shops"))) {
            var m = obj(o);
            var hours = obj(m.get("hours"));
            var stock = new ArrayList<Line>();
            for (Object l : list(m.get("stock"))) {
                var lm = obj(l);
                stock.add(new Line(str(lm.get("item"), ""), str(lm.get("variant"), ""), str(lm.get("rank"), ""), str(lm.get("slice"), ""),
                        integer(lm.get("qty"), 0), str(lm.get("restock"), "daily"), integer(lm.get("price"), 0),
                        "core".equals(lm.get("pool"))));
            }
            var shop = new Shop(str(m.get("id"), ""), str(m.get("name"), ""), str(m.get("district"), ""), str(m.get("keeper"), ""),
                    str(hours.get("opens"), "07:00"), str(hours.get("closes"), "19:00"), str(hours.get("closed"), ""),
                    str(m.get("slice"), "beta1"), str(m.get("rank"), "any"), str(m.get("standing"), "village"),
                    str(m.get("haggle"), "no"), Json.num(m.get("markup"), 1), integer(m.get("rotating"), 0),
                    strings(m.get("orders")), strings(m.get("interior")), List.copyOf(stock));
            this.shops.put(shop.id(), shop);
        }
        for (Object o : list(shops.get("jobs"))) {
            var m = obj(o);
            var job = new Job(str(m.get("id"), ""), str(m.get("shop"), ""), str(m.get("rank"), "any"), str(m.get("slice"), "beta1"),
                    integer(m.get("pay"), 0), integer(m.get("hours"), 3));
            jobs.put(job.id(), job);
        }
        for (Object o : list(shops.get("services"))) {
            var m = obj(o);
            var sv = new Service(str(m.get("id"), ""), str(m.get("provider"), ""), str(m.get("rank"), "any"), str(m.get("slice"), "beta1"),
                    integer(m.get("price"), 0));
            services.put(sv.id(), sv);
        }
        for (Object o : list(recipes.get("stations"))) {
            var m = obj(o);
            var st = new Station(str(m.get("id"), ""), str(m.get("name"), ""), str(m.get("slice"), "beta1"), str(m.get("rank"), "any"),
                    str(m.get("max_grade"), "fine"));
            stations.put(st.id(), st);
        }
        for (Object o : list(recipes.get("recipes"))) {
            var m = obj(o);
            var inputs = new ArrayList<Ingredient>();
            for (Object in : list(m.get("inputs"))) inputs.add(new Ingredient(str(obj(in).get("item"), ""), integer(obj(in).get("count"), 1)));
            var out = obj(m.get("output"));
            var r = new Recipe(str(m.get("id"), ""), str(m.get("station"), ""), List.copyOf(inputs), str(m.get("vessel"), null),
                    str(out.get("item"), ""), integer(out.get("count"), 1), str(m.get("rank"), "any"), str(m.get("slice"), "beta1"),
                    str(m.get("unlock"), null), integer(m.get("difficulty"), 0));
            this.recipes.put(r.id(), r);
        }
        obj(kits.get("kits")).forEach((kit, entries) -> {
            var parts = new ArrayList<Ingredient>();
            for (Object e : list(entries)) parts.add(new Ingredient(str(obj(e).get("item"), ""), integer(obj(e).get("count"), 1)));
            this.kits.put(kit, List.copyOf(parts));
        });
    }

    private static List<String> strings(Object o) { return list(o).stream().map(String::valueOf).toList(); }

    /** Reads the compiled files from a data/items directory. */
    public static Catalogue load(Path dir) {
        return new Catalogue(read(dir.resolve("items.json")), read(dir.resolve("shops.json")), read(dir.resolve("recipes.json")),
                read(dir.resolve("kits.json")), read(dir.resolve("economy.json")));
    }
    private static Map<String, Object> read(Path file) {
        try {
            return obj(Json.parse(Files.readString(file)));
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    }

    public Item item(String id) {
        var item = items.get(id);
        if (item == null) throw new IllegalArgumentException("unknown item " + id);
        return item;
    }
    /** Base price of an item, or of one of its variants ({@code "technique_scroll@fire.phoenix_flower"}). */
    public int price(String key) {
        int at = key.indexOf('@');
        if (at < 0) return item(key).price();
        var v = item(key.substring(0, at)).variants().get(key.substring(at + 1));
        if (v == null) throw new IllegalArgumentException("unknown variant " + key);
        return v.price();
    }
    /** What the inputs of a recipe cost at base prices (the vessel too). */
    public int inputCost(Recipe r) {
        int cost = r.inputs().stream().mapToInt(in -> item(in.item()).price() * in.count()).sum();
        return r.vessel() == null ? cost : cost + item(r.vessel()).price();
    }
    /** A section of economy.json. */
    public Map<String, Object> tuning(String key) { return obj(economy.get(key)); }
}
