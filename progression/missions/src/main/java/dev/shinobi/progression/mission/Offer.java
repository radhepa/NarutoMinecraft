package dev.shinobi.progression.mission;

import java.util.Map;

/**
 * A mission on the board: a template with its slots filled, its twist rolled (or none), its pay and XP, and how long
 * it stays up. Saves store offers by template id plus rolled slots (ROADMAP.md, "Versioning and migrations"), so a
 * template edit never corrupts a save. {@code requestedBy} is the client who asked for the player by name;
 * {@code chain} the recurring client's chain; {@code contest} marks a race against the rival squad.
 */
public record Offer(String id, String template, Rank rank, Map<String, String> slots, String twist, boolean harder,
                    int pay, int xp, int posted, int expires, String requestedBy, String chain, boolean contest) {
    public String client() { return slots.get("client"); }
    public boolean requested() { return requestedBy != null; }
}
