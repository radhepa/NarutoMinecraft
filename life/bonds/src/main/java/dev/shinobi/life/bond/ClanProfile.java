package dev.shinobi.life.bond;

import dev.shinobi.life.bond.Personality.Value;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * A clan as a social structure: how strict it is about marrying in, the values its upbringing instills, how it
 * nudges its members' temperaments, its customs (dialogue and quest ids), and the shape of its households (a main
 * and branch house where the clan has one). Flavor follows CLANS.md and the clan files; numbers are tuning.
 *
 * <p>{@code strictness} (0 to 1) is the pressure to marry within the clan: a cross-clan match is
 * {@code (1 - strictness)} as likely on each side, and a strict clan frowns on it ({@code forbidden_match} hooks).
 * {@code traits} adds to a rolled member's axes (warmth, boldness, pride, discipline, openness).
 */
public record ClanProfile(String id, boolean noble, double strictness, Set<Value> values, double[] traits, List<String> customs,
        boolean branchHouse, int elders) {

    public static final String CIVILIAN = "group:civilian", CLANLESS = "group:clanless";

    public static ClanProfile of(String id) {
        var p = PROFILES.get(id);
        if (p == null) throw new IllegalArgumentException("unknown clan " + id);
        return p;
    }
    public static boolean known(String id) { return PROFILES.containsKey(id); }
    public static Set<String> ids() { return PROFILES.keySet(); }

    /** A member's personality shaped by their upbringing: the clan's trait bias, and its values on top of their own. */
    public Personality shape(Personality p) {
        var values = new java.util.HashSet<>(p.values());
        values.addAll(this.values);
        while (values.size() > 3) values.remove(values.stream().filter(v -> !this.values.contains(v)).findFirst().orElse(values.iterator().next()));
        return p.withTraits(p.warmth() + traits[0], p.boldness() + traits[1], p.pride() + traits[2], p.discipline() + traits[3], p.openness() + traits[4])
                .withValues(values);
    }

    private static ClanProfile c(String id, boolean noble, double strict, Set<Value> values, double w, double b, double p, double d, double o,
            List<String> customs, boolean branch, int elders) {
        return new ClanProfile(id, noble, strict, values, new double[]{w, b, p, d, o}, customs, branch, elders);
    }
    private static final Map<String, ClanProfile> PROFILES = Map.ofEntries(
            Map.entry("senju", c("senju", true, .2, Set.of(Value.FAMILY, Value.DUTY), .2, .1, .1, .1, .2, List.of("founders_shrine", "living_tree"), false, 3)),
            Map.entry("uzumaki", c("uzumaki", true, .2, Set.of(Value.LOYALTY, Value.FAMILY), .3, .2, 0, -.1, .3, List.of("memorial_vigil", "sealing_masks"), false, 1)),
            Map.entry("uchiha", c("uchiha", true, .7, Set.of(Value.STRENGTH, Value.FAMILY), -.2, .2, .4, .2, -.3, List.of("fan_crest", "police_duty"), false, 3)),
            Map.entry("hyuga", c("hyuga", true, .85, Set.of(Value.DUTY, Value.FAMILY), -.1, -.1, .3, .4, -.3, List.of("bow_to_the_main_house", "dojo_forms"), true, 3)),
            Map.entry("nara", c("nara", true, .3, Set.of(Value.KNOWLEDGE, Value.LOYALTY), 0, -.2, -.1, -.1, -.1, List.of("deer_count", "shogi"), false, 2)),
            Map.entry("akimichi", c("akimichi", true, .3, Set.of(Value.FAMILY, Value.KINDNESS), .3, .1, 0, 0, .2, List.of("share_the_feast", "harvest_feast"), false, 2)),
            Map.entry("yamanaka", c("yamanaka", true, .3, Set.of(Value.LOYALTY, Value.KINDNESS), .2, 0, .1, 0, .3, List.of("flower_language", "quiet_hall"), false, 2)),
            Map.entry("inuzuka", c("inuzuka", true, .3, Set.of(Value.LOYALTY, Value.COURAGE), .2, .3, .1, -.3, .3, List.of("ninken_pairing", "respect_the_pack"), false, 2)),
            Map.entry("sarutobi", c("sarutobi", true, .3, Set.of(Value.DUTY, Value.LOYALTY), .2, .1, 0, .1, .1, List.of("lantern_walk", "will_of_fire"), false, 2)),
            Map.entry("aburame", c("aburame", true, .5, Set.of(Value.KNOWLEDGE, Value.LOYALTY), -.1, -.2, 0, .3, -.4, List.of("insect_night", "never_harm_insects"), false, 2)),
            Map.entry("hatake", c("hatake", true, .1, Set.of(Value.LOYALTY, Value.DUTY), 0, .1, 0, .1, -.2, List.of("memorial_stone_visit"), false, 0)),
            Map.entry("kurama", c("kurama", true, .5, Set.of(Value.CREATIVITY, Value.FAMILY), .1, -.2, .1, 0, -.1, List.of("painting_exhibition"), false, 1)),
            Map.entry("shimura", c("shimura", true, .6, Set.of(Value.DUTY, Value.STRENGTH), -.3, 0, .2, .4, -.4, List.of("silence_in_the_house"), false, 1)),
            Map.entry("yuhi", c("yuhi", true, .3, Set.of(Value.CREATIVITY, Value.LOYALTY), .1, 0, 0, .1, 0, List.of("grove_viewing"), false, 1)),
            Map.entry("gekko", c("gekko", true, .4, Set.of(Value.DUTY, Value.STRENGTH), 0, .1, .1, .3, -.1, List.of("moon_viewing_duels", "bow_before_the_blade"), false, 1)),
            Map.entry("shiranui", c("shiranui", false, .1, Set.of(Value.COURAGE), 0, .2, .1, 0, .1, List.of("senbon_wall"), false, 1)),
            Map.entry("morino", c("morino", false, .2, Set.of(Value.DUTY, Value.HONESTY), -.2, .1, .1, .3, -.2, List.of("barred_windows"), false, 1)),
            Map.entry("umino", c("umino", false, .1, Set.of(Value.KINDNESS, Value.KNOWLEDGE), .3, 0, -.1, .1, .2, List.of("teachers_table"), false, 1)),
            Map.entry("haruno", c("haruno", false, .1, Set.of(Value.FAMILY, Value.KNOWLEDGE), .1, 0, 0, .1, .1, List.of("tidy_garden"), false, 1)),
            Map.entry("namiashi", c("namiashi", false, .1, Set.of(Value.STRENGTH), 0, .1, 0, .2, 0, List.of("footwork_dojo"), false, 1)),
            Map.entry("hagane", c("hagane", false, .1, Set.of(Value.HONESTY, Value.CREATIVITY), 0, 0, .1, .2, .1, List.of("forge_oath"), false, 1)),
            Map.entry("kinoshita", c("kinoshita", false, .1, Set.of(Value.CREATIVITY, Value.FAMILY), .2, 0, 0, .1, .1, List.of("builders_yard"), false, 1)),
            Map.entry("tsuchigumo", c("tsuchigumo", false, .4, Set.of(Value.FAMILY, Value.DUTY), -.1, 0, .1, .2, -.2, List.of("quarry_rites"), false, 1)),
            Map.entry("suzuran", c("suzuran", false, .2, Set.of(Value.KINDNESS, Value.KNOWLEDGE), .3, -.2, 0, .1, .1, List.of("herb_racks"), false, 1)),
            Map.entry("tobari", c("tobari", false, .5, Set.of(Value.DUTY, Value.LOYALTY), -.1, 0, 0, .2, -.4, List.of("lanterns_at_nightfall", "never_speak_of_the_watch"), false, 1)));
}
