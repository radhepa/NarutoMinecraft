package dev.shinobi.village;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.util.List;

/** The Leaf wardrobe in the catalog form Village Friends reads (VF's outfit/Wardrobe), so every resident wears it. */
public final class LeafWardrobe {
    static final String CATALOG = "/assets/narutominecraft/wardrobe/catalog.json";

    private LeafWardrobe() {}

    /**
     * VF's key colors with the Leaf hair, tops and bottoms, and one outfit template per collection outfit.
     * shortcut: every profession wears every collection and VF's ten palettes, until the population draw and Leaf palettes land.
     */
    public static JsonObject catalog(JsonObject vf) {
        JsonObject leaf = read(CATALOG), out = new JsonObject();
        for (String k : List.of("schemaVersion", "keys", "shadowKeys")) out.add(k, vf.get(k));
        for (String k : List.of("hair", "tops", "bottoms")) out.add(k, leaf.get(k));
        JsonArray outfits = new JsonArray(), ids = new JsonArray();
        for (var c : leaf.getAsJsonArray("collections")) {
            String collection = c.getAsJsonObject().get("id").getAsString();
            for (var o : c.getAsJsonObject().getAsJsonArray("outfits")) {
                var src = o.getAsJsonObject();
                var t = new JsonObject();
                // Two collections share some outfit ids; VF needs them unique.
                t.addProperty("id", collection + "/" + src.get("id").getAsString());
                for (String f : List.of("name", "top", "bottom")) t.add(f, src.get(f));
                outfits.add(t);
                ids.add(t.get("id"));
            }
        }
        var jobs = new JsonObject();
        for (String job : vf.getAsJsonObject("professions").keySet()) jobs.add(job, ids);
        out.add("outfits", outfits);
        out.add("professions", jobs);
        return out;
    }

    static JsonObject read(String path) {
        try (var in = LeafWardrobe.class.getResourceAsStream(path)) {
            if (in == null) throw new IllegalStateException("Missing " + path);
            return JsonParser.parseReader(new InputStreamReader(in, StandardCharsets.UTF_8)).getAsJsonObject();
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    }
}
