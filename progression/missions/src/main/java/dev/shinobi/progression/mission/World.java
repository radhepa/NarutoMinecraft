package dev.shinobi.progression.mission;

import java.util.List;

/**
 * The village as the Mission Desk sees it: residents to cast as clients and bystanders, the map's anchors by tag
 * ({@code districts.json}, owned by the Konoha build), and the save's bound roles. Phase 0 implements it over the
 * world; tests and the simulation use a sample village.
 */
public interface World {
    List<Resident> residents();
    /** Every anchor id with this tag, in a stable order. */
    List<String> anchors(String tag);
    /** The resident a role is bound to in this save, or null if the role is not bound (yet). */
    String role(String role);
    /** The player's squad and sensei, who are never cast as clients. */
    default List<String> squad() { return List.of(); }
}
