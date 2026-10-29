package dev.shinobi.progression.mission;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

import static dev.shinobi.progression.mission.Json.*;

/**
 * Every board-mission template and the desk's tables, read from the Adventure datapack's {@code missions/} folder
 * ({@code templates/<rank>/*.json}, {@code economy.json}, {@code desk.json}, {@code clients.json},
 * {@code squad.json}), as {@code tools/missions/missions.py} compiles them.
 */
public final class Catalogue {
    final Map<String, Template> templates = new LinkedHashMap<>();
    public final Economy economy;
    public final Map<String, Object> desk, clients, squad;

    public Catalogue(List<Template> templates, Map<String, Object> economy, Map<String, Object> desk,
                     Map<String, Object> clients, Map<String, Object> squad) {
        templates.stream().sorted(Comparator.comparing(Template::id)).forEach(t -> this.templates.put(t.id(), t));
        this.economy = new Economy(economy);
        this.desk = desk;
        this.clients = clients;
        this.squad = squad;
    }

    public static Catalogue load(Path dir) {
        var ts = new ArrayList<Template>();
        try (Stream<Path> files = Files.walk(dir.resolve("templates"))) {
            for (Path f : files.filter(x -> x.toString().endsWith(".json")).sorted().toList()) ts.add(Template.of(object(read(f))));
        } catch (IOException e) { throw new UncheckedIOException(e); }
        return new Catalogue(ts, object(read(dir.resolve("economy.json"))), object(read(dir.resolve("desk.json"))),
                object(read(dir.resolve("clients.json"))), object(read(dir.resolve("squad.json"))));
    }

    /** The datapack folder from the {@code missions.dir} system property (Gradle sets it), or the repository path. */
    public static Catalogue load() {
        String dir = System.getProperty("missions.dir", "adventure/data/shinobi_adventure/missions");
        return load(Path.of(dir));
    }

    static String read(Path f) {
        try { return Files.readString(f, StandardCharsets.UTF_8); } catch (IOException e) { throw new UncheckedIOException(e); }
    }

    public Template get(String id) { return templates.get(id); }
    public List<Template> all() { return List.copyOf(templates.values()); }
    public List<Template> of(Rank r) { return templates.values().stream().filter(t -> t.rank() == r).toList(); }

    @SuppressWarnings("unchecked")
    public List<Map<String, Object>> chains() { return (List<Map<String, Object>>) (List<?>) list(clients.get("chains")); }

    /** Every problem in the catalogue: each template's own, and the tables' references to templates. */
    public List<String> problems() {
        var p = new ArrayList<String>();
        templates.values().forEach(t -> p.addAll(t.problems()));
        for (String id : strings(desk.get("classic_opening")))
            if (!templates.containsKey(id)) p.add("desk: classic opening names " + id);
        for (var chain : chains()) {
            var ids = new ArrayList<>(strings(chain.get("templates")));
            list(chain.get("stages")).forEach(s -> ids.add((String) map(s).get("template")));
            for (String id : ids) {
                Template t = templates.get(id);
                if (t == null) p.add("clients: " + chain.get("id") + " names " + id);
                else if (!chain.get("id").equals(t.chain())) p.add("clients: " + id + " is not marked as " + chain.get("id"));
            }
        }
        for (Rank r : Rank.values()) if (economy.band(r) == null) p.add("economy: no band for " + r);
        return p;
    }
}
