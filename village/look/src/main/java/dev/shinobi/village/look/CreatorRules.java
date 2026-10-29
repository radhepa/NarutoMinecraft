package dev.shinobi.village.look;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * The creator's rules, read from the compiled file (data/narutominecraft/creator/creator.json, written by
 * tools/creator/creator.py): what each origin (clanless or a clan) may pick at each age stage, the opening looks, and
 * the server's check of a creator submission. The client screen only offers allowed choices; the server checks again,
 * because single player runs an integrated server and multiplayer may follow.
 */
public final class CreatorRules {
    public static final String CLANLESS = "clanless";

    /** One outfit template: its pieces, rank, the bodies it fits and its own palettes. */
    public record Outfit(String id, String top, String bottom, String rank, List<String> palettes, List<String> bodies) {}

    /** Everything one origin may pick at one stage, with each outfit's palettes widened by the clan's own. */
    public record Choices(List<String> hair, List<String> hairColors, List<String> eyeColors, List<String> marks,
                          List<String> headwear, Map<String, List<Outfit>> outfits) {
        public Outfit outfit(String body, String id) {
            for (var o : outfits.getOrDefault(body, List.of())) if (o.id().equals(id)) return o;
            return null;
        }
    }

    final Map<String, Object> data;
    private final Map<String, Outfit> outfits = new LinkedHashMap<>();
    public final int maxMarks, nameMin, nameMax;
    public final List<String> bodies, eyeStyles, brows;
    public final List<Integer> complexions;

    @SuppressWarnings("unchecked")
    public CreatorRules(Map<String, Object> data) {
        this.data = data;
        long format = ((Number) data.get("format")).longValue();
        if (format != 1) throw new IllegalArgumentException("creator.json format " + format + " is not 1");
        for (var e : map(data.get("outfits")).entrySet()) {
            var o = map(e.getValue());
            outfits.put(e.getKey(), new Outfit(e.getKey(), (String) o.get("top"), (String) o.get("bottom"), (String) o.get("rank"),
                    strings(o.get("palettes")), strings(o.get("bodies"))));
        }
        maxMarks = ((Number) data.get("max_marks")).intValue();
        var name = map(data.get("name"));
        nameMin = ((Number) name.get("min")).intValue();
        nameMax = ((Number) name.get("max")).intValue();
        bodies = strings(data.get("bodies"));
        eyeStyles = strings(data.get("eye_styles"));
        brows = strings(data.get("brows"));
        complexions = new ArrayList<>();
        for (Object c : (List<Object>) data.get("complexions")) complexions.add(((Number) c).intValue());
    }

    public static CreatorRules load(Path file) throws IOException {
        return new CreatorRules(map(Json.parse(Files.readString(file, StandardCharsets.UTF_8))));
    }

    public List<String> origins() { return List.copyOf(origins0().keySet()); }

    public boolean isClan(String origin) { return !CLANLESS.equals(origin) && origins0().containsKey(origin); }

    /** The clan's display name (also the player's family name), or null for the clanless. */
    public String clanName(String origin) { return (String) origin(origin).get("name"); }

    /** The family names an origin may carry: the clan's own name, or the ordinary pool for the clanless. */
    public List<String> familyNames(String origin) { return strings(origin(origin).get("family_names")); }

    public Outfit outfit(String id) { return outfits.get(id); }

    public Choices choices(String origin, AgeStage stage) {
        var o = origin(origin);
        var st = map(map(o.get("stages")).get(stage.id()));
        var stageHair = map(data.get("stage_hair"));
        var hair = new ArrayList<String>();
        for (String h : strings(o.get("hair"))) {
            Object from = stageHair.get(h);
            if (from == null || stage.atLeast(AgeStage.of((String) from))) hair.add(h);
        }
        var clanPalettes = strings(o.get("clan_palettes"));
        var byBody = new LinkedHashMap<String, List<Outfit>>();
        for (String b : bodies) byBody.put(b, new ArrayList<>());
        for (String id : strings(st.get("outfits"))) {
            var base = outfits.get(id);
            var palettes = new ArrayList<>(base.palettes());
            for (String p : clanPalettes) if (!palettes.contains(p)) palettes.add(p);
            var wide = new Outfit(id, base.top(), base.bottom(), base.rank(), List.copyOf(palettes), base.bodies());
            for (String b : base.bodies()) byBody.get(b).add(wide);
        }
        return new Choices(List.copyOf(hair), strings(o.get("hair_colors")), strings(o.get("eye_colors")), strings(st.get("marks")),
                nullableStrings(st.get("headwear")), byBody);
    }

    /** The look the creator opens on for an origin and body. */
    public Look defaults(String origin, String body) {
        return Look.fromMap(map(map(origin(origin).get("defaults")).get(body)));
    }

    /** Why a look is not allowed for an origin at a stage; empty when it is. The same rules as creator.py's validate_look. */
    public List<String> validate(String origin, AgeStage stage, Look look) {
        var errors = new ArrayList<String>();
        if (!origins0().containsKey(origin)) return List.of("unknown origin " + origin);
        if (!bodies.contains(look.body())) return List.of("unknown body " + look.body());
        var c = choices(origin, stage);
        if (!complexions.contains(look.complexion())) errors.add("complexion " + look.complexion() + " is not allowed");
        if (!eyeStyles.contains(look.eyeStyle())) errors.add("eye style " + look.eyeStyle() + " is not allowed");
        if (!brows.contains(look.brows())) errors.add("brows " + look.brows() + " are not allowed");
        if (!c.hair().contains(look.hair())) errors.add("hair " + look.hair() + " is not allowed");
        if (!c.hairColors().contains(look.hairColor())) errors.add("hair_color " + look.hairColor() + " is not allowed");
        if (!c.eyeColors().contains(look.eyeColor())) errors.add("eye_color " + look.eyeColor() + " is not allowed");
        if (!c.headwear().contains(look.headwear())) errors.add("headwear " + look.headwear() + " is not allowed");
        if (look.marks().size() > maxMarks || look.marks().stream().distinct().count() != look.marks().size())
            errors.add("at most " + maxMarks + " different marks");
        for (String m : look.marks()) if (!c.marks().contains(m)) errors.add("mark " + m + " is not allowed");
        var outfit = c.outfit(look.body(), look.outfit());
        if (outfit == null) errors.add("outfit " + look.outfit() + " is not allowed for this body");
        else if (!outfit.palettes().contains(look.palette())) errors.add("palette " + look.palette() + " is not offered for " + outfit.id());
        return errors;
    }

    /** The shinobi groups' population weights (clanless and each clan), for Roll a life. */
    public Map<String, Integer> population() {
        var out = new LinkedHashMap<String, Integer>();
        map(data.get("population")).forEach((k, v) -> out.put(k, ((Number) v).intValue()));
        return out;
    }

    Map<String, Object> origin(String origin) {
        var o = origins0().get(origin);
        if (o == null) throw new IllegalArgumentException("unknown origin " + origin);
        return map(o);
    }
    private Map<String, Object> origins0() { return map(data.get("origins")); }

    @SuppressWarnings("unchecked")
    static Map<String, Object> map(Object o) { return (Map<String, Object>) o; }

    @SuppressWarnings("unchecked")
    static List<String> strings(Object o) { return o == null ? List.of() : List.copyOf((List<String>) o); }

    @SuppressWarnings("unchecked")
    static List<String> nullableStrings(Object o) { return java.util.Collections.unmodifiableList(new ArrayList<>((List<String>) o)); }
}
