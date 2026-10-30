package dev.shinobi.village.look;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/** Japanese given names and the save's names stream, shared by residents and role-bound shinobi. */
public final class ResidentNames {
    private final Map<String, List<String>> pools = new LinkedHashMap<>();

    public ResidentNames(String json) {
        if (!(Json.parse(json) instanceof Map<?, ?> data)) throw new IllegalArgumentException("Given names need an object");
        for (String gender : List.of("male", "female", "unisex")) {
            if (!(data.get(gender) instanceof List<?> raw) || raw.stream().anyMatch(n -> !(n instanceof String)))
                throw new IllegalArgumentException("Missing given-name pool: " + gender);
            var names = raw.stream().map(String.class::cast).toList();
            if (names.isEmpty() || names.stream().distinct().count() != names.size()
                    || names.stream().anyMatch(n -> !n.matches("[A-Z][a-z]{0,63}")))
                throw new IllegalArgumentException("Invalid given-name pool: " + gender);
            pools.put(gender, names);
        }
    }

    public List<String> given(String gender) {
        var pool = pools.get("nonbinary".equals(gender) ? "unisex" : gender);
        if (pool == null) throw new IllegalArgumentException("Unknown name gender: " + gender);
        return pool;
    }

    /** The clan's surname comes from the same compiled clan data the creator uses. */
    public Names.PlayerName roll(long saveSeed, String key, String gender, String clan, CreatorRules rules) {
        String origin = clan == null || clan.equals("civilian") ? CreatorRules.CLANLESS : clan;
        if (!CreatorRules.CLANLESS.equals(origin) && !rules.isClan(origin))
            throw new IllegalArgumentException("Unknown name clan: " + clan);
        var rng = Seeds.stream(saveSeed, "names", key);
        return new Names.PlayerName(rng.pick(given(gender)), rng.pick(rules.familyNames(origin)));
    }
}
