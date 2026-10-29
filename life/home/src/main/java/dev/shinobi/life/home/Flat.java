package dev.shinobi.life.home;

import dev.shinobi.life.bond.Seeds;
import java.util.List;

/**
 * A home's shape, as {@code homes.json} lists it (the Konoha build session owns the blocks and the file): its rooms in
 * blocks, the floor cells furniture may use, the comfort it can hold at most, and its view. The Academy flats are the
 * beta's; the later tiers are designed now and built after it. Classic saves always get {@link #CLASSIC}; Varied
 * saves roll one of the Academy candidates from the save seed.
 */
public record Flat(String id, Tier tier, List<Room> rooms, int cells, int keys, String view, boolean balcony) {

    /** A room inside the home's bounds: width (x) and depth (z) of open floor, and ceiling height, in blocks. */
    public record Room(String id, int w, int d, int h) {
        public int floor() { return w * d; }
    }

    /** The homes of a life, in order. {@code cap} is the most comfort the home holds; {@code beds} the most beds. */
    public enum Tier {
        ACADEMY_FLAT(60, 1), TWO_ROOM_FLAT(80, 2), HOUSE(95, 4), CLAN_ESTATE(110, 8), HOKAGE_QUARTERS(110, 6);
        public final int cap, beds;
        Tier(int cap, int beds) { this.cap = cap; this.beds = beds; }
        public String id() { return name().toLowerCase(java.util.Locale.ROOT); }
    }

    public Flat {
        rooms = List.copyOf(rooms);
    }
    public int floor() { return rooms.stream().mapToInt(Room::floor).sum(); }

    /** The Classic flat: one room, a kitchenette, a bathroom and a little balcony facing the Hokage Rock. */
    public static final Flat CLASSIC = new Flat("flat.leaf_block.3a", Tier.ACADEMY_FLAT, List.of(
            new Room("main", 6, 6, 3), new Room("kitchenette", 3, 4, 3), new Room("bathroom", 3, 3, 3),
            new Room("genkan", 2, 1, 3), new Room("balcony", 4, 2, 0)), 22, 3, "hokage_rock", true);

    /** The Academy candidates a Varied save rolls from (the Classic flat among them). */
    public static final List<Flat> ACADEMY = List.of(CLASSIC,
            new Flat("flat.leaf_block.2c", Tier.ACADEMY_FLAT, List.of(new Room("main", 7, 5, 3), new Room("kitchenette", 3, 3, 3),
                    new Room("bathroom", 2, 3, 3), new Room("genkan", 2, 1, 3), new Room("balcony", 3, 2, 0)), 22, 3, "hokage_rock", true),
            new Flat("flat.riverside_row.1b", Tier.ACADEMY_FLAT, List.of(new Room("main", 6, 6, 3), new Room("kitchenette", 4, 3, 3),
                    new Room("bathroom", 3, 2, 3), new Room("genkan", 2, 1, 3), new Room("yard", 4, 3, 0)), 23, 3, "river", true),
            new Flat("flat.market_loft.4", Tier.ACADEMY_FLAT, List.of(new Room("main", 7, 6, 2), new Room("kitchenette", 3, 3, 2),
                    new Room("bathroom", 2, 3, 2), new Room("genkan", 2, 1, 3)), 21, 3, "rooftops", false));

    /** Later homes (designed now, built after the beta). */
    public static final List<Flat> LATER = List.of(
            new Flat("flat.leaf_block.5b", Tier.TWO_ROOM_FLAT, List.of(new Room("main", 7, 6, 3), new Room("bedroom", 5, 4, 3),
                    new Room("kitchen", 4, 3, 3), new Room("bathroom", 3, 3, 3), new Room("genkan", 2, 2, 3), new Room("balcony", 5, 2, 0)), 34, 4, "hokage_rock", true),
            new Flat("house.residential.small", Tier.HOUSE, List.of(new Room("living", 8, 7, 3), new Room("bedroom", 5, 5, 3),
                    new Room("second_bedroom", 4, 4, 3), new Room("kitchen", 5, 4, 3), new Room("bathroom", 3, 4, 3),
                    new Room("genkan", 3, 2, 3), new Room("garden", 8, 5, 0)), 56, 5, "garden", true));

    /** The flat a save starts in: the Classic flat, or one rolled from the save seed in Varied. */
    public static Flat starting(long seed, boolean classic) {
        if (classic) return CLASSIC;
        return ACADEMY.get((int) (Seeds.roll(seed, "home", "academy_flat") * ACADEMY.size()));
    }
    public static Flat of(String id) {
        for (var f : ACADEMY) if (f.id.equals(id)) return f;
        for (var f : LATER) if (f.id.equals(id)) return f;
        throw new IllegalArgumentException("unknown flat " + id);
    }
}
