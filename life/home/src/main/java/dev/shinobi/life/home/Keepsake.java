package dev.shinobi.life.home;

/**
 * Something kept and shown: a quest's or a clan welcome's reward, a story moment's token, a gift a friend gave you, or
 * a curio (charming, useless loot). They are ordinary items: they live in chests, and the ones you choose stand on
 * their own on a surface or go on display shelves, cases, cabinets and wall mounts; each one shown adds a little
 * style. A displayed gift is noticed by its giver, once (the bond engine's {@code Gifts.seenDisplayed}). {@code from}
 * is the quest, story hook or loot table it came from; {@code giver} is a role or resident id, or empty.
 */
public record Keepsake(String id, Kind kind, String from, String giver, String slice) {

    public enum Kind { QUEST, CLAN, STORY, GIFT, FESTIVAL, CURIO }

    public Keepsake {
        giver = giver == null ? "" : giver;
    }
    public boolean gift() { return !giver.isEmpty(); }

    /** A gift a friend gave the player (the bond engine's {@code Gifts.Received} id), kept for display. */
    public static Keepsake gift(int giftId, String item, String giver) { return new Keepsake("gift:" + giftId, Kind.GIFT, item, giver, "b1"); }
    /** A curio from a loot table (the item registry's {@code curio_*} items). */
    public static Keepsake curio(String item, String lootTable) { return new Keepsake(item, Kind.CURIO, lootTable, "", "b1"); }
    /** The bond engine's gift id, or -1 for anything that is not a gift. */
    public int giftId() {
        if (kind != Kind.GIFT || !id.startsWith("gift:")) return -1;
        try { return Integer.parseInt(id.substring(5)); } catch (NumberFormatException e) { return -1; }
    }
    /** A story moment's keepsake, by the story's hook id; its name and meaning live with the story. */
    public static Keepsake story(String hook, String slice) { return new Keepsake("story:" + hook, Kind.STORY, hook, "", slice); }
}
