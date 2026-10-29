package dev.shinobi.life.home;

/**
 * Something kept for what it means: a quest's or a clan welcome's reward, a story moment's token, or a gift a friend
 * gave you. Keepsakes go on shelves, in display cases and in wall frames; each one shown adds a little style. A
 * displayed gift is noticed by its giver ("You kept it!"), once. {@code from} is the quest or story hook id that gives
 * it (or {@code gift:<item>}); {@code giver} is a role or resident id, or empty.
 */
public record Keepsake(String id, Kind kind, String from, String giver, String slice) {

    public enum Kind { QUEST, CLAN, STORY, GIFT, FESTIVAL }

    public Keepsake {
        giver = giver == null ? "" : giver;
    }
    public boolean gift() { return !giver.isEmpty(); }

    /** A gift a friend gave the player, kept for display. Any giftable item can be one. */
    public static Keepsake gift(String item, String giver) { return new Keepsake("gift:" + item, Kind.GIFT, "gift:" + item, giver, "b1"); }
    /** A story moment's keepsake, by the story's hook id; its name and meaning live with the story. */
    public static Keepsake story(String hook, String slice) { return new Keepsake("story:" + hook, Kind.STORY, hook, "", slice); }
}
