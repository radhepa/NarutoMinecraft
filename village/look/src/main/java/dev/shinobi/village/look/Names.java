package dev.shinobi.village.look;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * The player's name. The given name is typed in the creator; the family name is the clan's for the clan-born, and for
 * the clanless an ordinary family name from population.json's pool (picked, or the one rolled on the save's
 * {@code names} stream). Text never contains the name: it uses the {@code {player}} tokens.
 */
public final class Names {
    /** A player's name: {@code given} as typed, {@code family} the clan's or the pool's. */
    public record PlayerName(String given, String family) {
        public String full() { return given + " " + family; }
    }

    /** Why a typed given name is refused; empty when it is fine. Letters of any script, spaces, apostrophes and hyphens. */
    public static List<String> validateGiven(String name, int min, int max) {
        var errors = new ArrayList<String>();
        if (name == null || name.isBlank()) return List.of("name.empty");
        String n = name.strip();
        int length = n.codePointCount(0, n.length());
        if (length < min) errors.add("name.too_short");
        if (length > max) errors.add("name.too_long");
        if (!Character.isLetter(n.codePointAt(0))) errors.add("name.start_with_letter");
        boolean lastSpace = false;
        for (int i = 0; i < n.length(); ) {
            int cp = n.codePointAt(i);
            i += Character.charCount(cp);
            boolean space = cp == ' ';
            if (!(Character.isLetter(cp) || Character.getType(cp) == Character.NON_SPACING_MARK || space || cp == '\'' || cp == '-')) {
                errors.add("name.bad_character");
                break;
            }
            if (space && lastSpace) { errors.add("name.double_space"); break; }
            lastSpace = space;
        }
        return errors;
    }

    /** The family name a new player carries: the clan's name, or the chosen pool name, or the {@code names} stream's roll. */
    public static String family(CreatorRules rules, String origin, String chosen, long saveSeed) {
        var pool = rules.familyNames(origin);
        if (rules.isClan(origin)) return pool.get(0);
        if (chosen != null && pool.contains(chosen)) return chosen;
        if (chosen != null) throw new IllegalArgumentException("family name " + chosen + " is not in the pool");
        return Seeds.stream(saveSeed, "names", "player").pick(pool);
    }

    /**
     * The player's tokens, as dialogue and quest text use them: {@code {player}} the given name, {@code {player_family}},
     * {@code {player_full}}, and {@code {player_clan}} (the clan's name, empty for the clanless).
     */
    public static Map<String, String> tokens(PlayerName name, String clanName) {
        var m = new LinkedHashMap<String, String>();
        m.put("player", name.given());
        m.put("player_family", name.family());
        m.put("player_full", name.full());
        m.put("player_clan", clanName == null ? "" : clanName);
        return m;
    }

    private Names() {}
}
