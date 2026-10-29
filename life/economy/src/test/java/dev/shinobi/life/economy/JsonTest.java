package dev.shinobi.life.economy;

import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class JsonTest {
    @Test void readsWhatTheCompilerWrites() {
        var o = Json.obj(Json.parse("{\"a\": [1, 2.5, \"x\\u00e9\\n\"], \"b\": {\"c\": null, \"d\": true}, \"e\": -3}"));
        assertEquals(List.of(1L, 2.5, "xé\n"), o.get("a"));
        assertEquals(Map.of("d", true), Map.of("d", Json.obj(o.get("b")).get("d")));
        assertNull(Json.obj(o.get("b")).get("c"));
        assertEquals(-3, Json.integer(o.get("e"), 0));
        assertThrows(IllegalArgumentException.class, () -> Json.parse("{\"a\": 1,}"));
        assertThrows(IllegalArgumentException.class, () -> Json.parse("[1] 2"));
    }
}
