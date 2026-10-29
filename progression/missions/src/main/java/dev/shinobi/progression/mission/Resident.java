package dev.shinobi.progression.mission;

import java.util.Map;

/**
 * What the slot filler needs to know about a resident: a profile matched against a slot's {@code where}. Phase 0
 * builds these from Shinobi Village's markers and VF's census; the simulation builds a sample village.
 *
 * @param traveller someone passing through or living in a far region; only slots that say
 *                  {@code "resident_of": "any"} may pick them
 * @param parentOf  the resident id of their child, or null
 */
public record Resident(String id, String job, String district, String age, String group, String clan, String rank,
                       boolean hasPet, boolean household, boolean children, boolean traveller, String parentOf) {

    /** Whether this resident fits a slot's {@code where}; {@code filled} holds the slots already filled. */
    public boolean matches(Map<String, Object> where, Map<String, String> filled, Map<String, Resident> byId) {
        boolean anywhere = "any".equals(where.get("resident_of"));
        if (traveller && !anywhere) return false;
        for (var e : where.entrySet()) {
            Object v = e.getValue();
            boolean ok = switch (e.getKey()) {
                case "resident_of" -> true;
                case "has_pet" -> hasPet == Boolean.TRUE.equals(v);
                case "household" -> household == Boolean.TRUE.equals(v);
                case "household_children" -> children == Boolean.TRUE.equals(v);
                case "job" -> v.equals(job);
                case "age" -> v.equals(age);
                case "group" -> v.equals(group);
                case "clan" -> v.equals(clan);
                case "rank" -> v.equals(rank);
                case "district" -> {
                    String d = (String) v;
                    if (!d.startsWith("same:")) yield d.equals(district);
                    Resident other = byId.get(filled.get(d.substring(5)));
                    yield other != null && other.district().equals(district) && !other.id().equals(id);
                }
                case "parent_of" -> {
                    String child = filled.get((String) v);
                    yield child != null && child.equals(parentOf);
                }
                default -> false;
            };
            if (!ok) return false;
        }
        return true;
    }
}
