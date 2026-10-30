package dev.shinobi.village.look;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * The player's look, as the creator builds it and the player record keeps it: the same fields a wardrobe character
 * has (tools/wardrobe/characters/*.json), with the outfit named by its template ({@code collection.outfit} or
 * {@code clan.outfit}) and a palette. {@code headwear} may be null (bare head).
 */
public record Look(String body, int complexion, String eyeStyle, String brows, String hair, String hairColor, String eyeColor,
                   List<String> marks, String outfit, String palette, String headwear) {

    public Look {
        marks = List.copyOf(marks);
    }

    public Look withComplexion(int v) { return new Look(body, v, eyeStyle, brows, hair, hairColor, eyeColor, marks, outfit, palette, headwear); }
    public Look withHair(String v) { return new Look(body, complexion, eyeStyle, brows, v, hairColor, eyeColor, marks, outfit, palette, headwear); }
    public Look withHairColor(String v) { return new Look(body, complexion, eyeStyle, brows, hair, v, eyeColor, marks, outfit, palette, headwear); }
    public Look withBrows(String v) { return new Look(body, complexion, eyeStyle, v, hair, hairColor, eyeColor, marks, outfit, palette, headwear); }
    public Look withMarks(List<String> v) { return new Look(body, complexion, eyeStyle, brows, hair, hairColor, eyeColor, v, outfit, palette, headwear); }
    public Look withOutfit(String v, String p) { return new Look(body, complexion, eyeStyle, brows, hair, hairColor, eyeColor, marks, v, p, headwear); }
    public Look withHeadwear(String v) { return new Look(body, complexion, eyeStyle, brows, hair, hairColor, eyeColor, marks, outfit, palette, v); }
    public Look withEyeColor(String v) { return new Look(body, complexion, eyeStyle, brows, hair, hairColor, v, marks, outfit, palette, headwear); }

    /** The look as the compiled file and the save write it (snake_case keys). */
    public Map<String, Object> toMap() {
        var m = new LinkedHashMap<String, Object>();
        m.put("body", body); m.put("complexion", (long) complexion); m.put("eye_style", eyeStyle); m.put("brows", brows);
        m.put("hair", hair); m.put("hair_color", hairColor); m.put("eye_color", eyeColor); m.put("marks", marks);
        m.put("outfit", outfit); m.put("palette", palette); m.put("headwear", headwear);
        return m;
    }

    @SuppressWarnings("unchecked")
    public static Look fromMap(Map<String, Object> m) {
        return new Look((String) m.get("body"), ((Number) m.get("complexion")).intValue(), (String) m.get("eye_style"),
                (String) m.get("brows"), (String) m.get("hair"), (String) m.get("hair_color"), (String) m.get("eye_color"),
                (List<String>) m.getOrDefault("marks", List.of()), (String) m.get("outfit"), (String) m.get("palette"),
                (String) m.get("headwear"));
    }
}
