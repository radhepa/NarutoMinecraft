package dev.shinobi.village;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.*;

class LeafWardrobeTest {
    static final String VF = "/assets/villagefriends/wardrobe/catalog.json";

    static Set<String> strings(JsonArray a) {
        var s = new HashSet<String>();
        for (JsonElement e : a) s.add(e.getAsString());
        return s;
    }

    @Test void theLeafCatalogIsOneVillageFriendsCanLoad() {
        var vf = LeafWardrobe.read(VF);
        var c = LeafWardrobe.catalog(vf);
        assertEquals(vf.get("keys"), c.get("keys"));
        var garments = new HashSet<String>();
        for (String k : new String[]{"hair", "tops", "bottoms"}) garments.addAll(strings(c.getAsJsonArray(k)));
        var outfits = new HashSet<String>();
        for (var o : c.getAsJsonArray("outfits")) {
            var t = o.getAsJsonObject();
            assertTrue(outfits.add(t.get("id").getAsString()), "unique outfit " + t.get("id"));
            assertTrue(garments.contains(t.get("top").getAsString()) && garments.contains(t.get("bottom").getAsString()), "known pieces in " + t);
        }
        assertEquals(vf.getAsJsonObject("professions").keySet(), c.getAsJsonObject("professions").keySet());
        assertTrue(c.getAsJsonObject("professions").getAsJsonArray("NONE").size() > 0);
    }

    // The Leaf pieces ship in VF's namespace (village/build.gradle), so they must not replace VF's own files.
    @Test void noLeafPieceHasAVillageFriendsId() {
        var vf = LeafWardrobe.read(VF);
        var leaf = LeafWardrobe.read(LeafWardrobe.CATALOG);
        for (String k : new String[]{"hair", "tops", "bottoms"}) {
            var shared = strings(vf.getAsJsonArray(k));
            shared.retainAll(strings(leaf.getAsJsonArray(k)));
            assertEquals(Set.of(), shared, k);
        }
    }
}
