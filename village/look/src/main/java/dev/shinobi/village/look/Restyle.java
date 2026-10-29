package dev.shinobi.village.look;

import java.util.List;
import java.util.Map;

/**
 * Changing your look after creation (CHARACTER_CREATION.md, "Locked and changeable"): the barber for hair, hair
 * color, brows and marks; your home's wardrobe chest for outfits and headwear; the rest is locked. Every change is
 * checked against the same choices as the creator, for the player's origin and current stage, so a restyle can never
 * reach what the creator could not.
 */
public final class Restyle {
    /** Where a change happens. */
    public enum Venue {
        LOCKED, BARBER, HOME, TIME_SKIP;
        static Venue of(String id) { return valueOf(id.toUpperCase()); }
    }

    /** A refused or accepted change: the new look (unchanged when refused), its ryo cost and the reason if refused. */
    public record Result(Look look, int cost, String refused) {
        public boolean ok() { return refused == null; }
    }

    private final CreatorRules rules;

    public Restyle(CreatorRules rules) { this.rules = rules; }

    /** Where a field may change: locked, barber or home (the time skip's mirror may change its own fields too). */
    public Venue venue(String field) {
        var c = CreatorRules.map(CreatorRules.map(rules.data.get("changes")).get(field));
        if (c == null) throw new IllegalArgumentException("unknown look field " + field);
        return Venue.of((String) c.get("where"));
    }

    public int cost(String field) {
        var c = CreatorRules.map(CreatorRules.map(rules.data.get("changes")).get(field));
        return c.get("cost") == null ? 0 : ((Number) c.get("cost")).intValue();
    }

    /** The fields the Years Later mirror lets you re-pick for free. */
    public List<String> timeSkipFields() { return CreatorRules.strings(rules.data.get("time_skip_restyle")); }

    public boolean canChange(String field, Venue at) {
        if (at == Venue.TIME_SKIP) return timeSkipFields().contains(field);
        var where = venue(field);
        return where != Venue.LOCKED && where == at;
    }

    /**
     * Applies one change at a venue. {@code value} is the new id (a list of ids for marks; for an outfit, a two-element
     * list of outfit id and palette). Refused when the venue cannot change the field or the result is not allowed.
     */
    @SuppressWarnings("unchecked")
    public Result apply(Look look, String origin, AgeStage stage, String field, Object value, Venue at) {
        if (!canChange(field, at)) return new Result(look, 0, field + " cannot change at " + at.name().toLowerCase());
        Look next = switch (field) {
            case "hair" -> look.withHair((String) value);
            case "hair_color" -> look.withHairColor((String) value);
            case "brows" -> look.withBrows((String) value);
            case "marks" -> look.withMarks((List<String>) value);
            case "headwear" -> look.withHeadwear((String) value);
            case "outfit" -> look.withOutfit(((List<String>) value).get(0), ((List<String>) value).get(1));
            default -> null;
        };
        if (next == null) return new Result(look, 0, field + " has no restyle");
        var errors = rules.validate(origin, stage, next);
        if (!errors.isEmpty()) return new Result(look, 0, errors.get(0));
        return new Result(next, at == Venue.TIME_SKIP ? 0 : cost(field), null);
    }

    /** The changes table, for the UI's lock icons. */
    public Map<String, Object> table() { return CreatorRules.map(rules.data.get("changes")); }
}
