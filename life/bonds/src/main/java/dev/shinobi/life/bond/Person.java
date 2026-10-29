package dev.shinobi.life.bond;

import java.util.List;
import java.util.Locale;
import java.util.Map;

/**
 * Someone the player can bond with, as the bond engine sees them. {@code id} is the role id for cast characters
 * ({@code role:teammate_a}) or the resident id; the engine never stores a name (text uses name tokens).
 * {@code clan} is a clan id or "" for the clanless; {@code district} the civilian district or quarter they live in;
 * {@code rank} is {@link #CIVILIAN} or a ladder index ({@link #rankIndex}); {@code family} maps a relative's id to
 * what they are to this person ("parent", "sibling"...), like VF's {@code Townsfolk.kin}.
 * {@code gender} and {@code attraction} follow VF's {@code Chemistry}: attraction is "FEMALE", "MALE" or "ANY",
 * "NONE" for someone who is not romantic.
 */
public record Person(String id, String clan, String district, int rank, Stage stage, Personality personality, String gender,
        String attraction, int birthday, Map<String, String> family, List<String> circles) {
    public static final int CIVILIAN = -1;
    public static final List<String> RANKS = List.of("academy", "genin", "chunin", "jonin", "anbu", "hokage");

    /** Child (the whole beta), teen (from the first time skip) and adult (from the second). Mirrors Core's age stage. */
    public enum Stage {
        CHILD, TEEN, ADULT;
        public String id() { return name().toLowerCase(Locale.ROOT); }
    }

    public Person {
        clan = clan == null ? "" : clan; district = district == null ? "" : district;
        gender = gender == null ? "NON_BINARY" : gender; attraction = attraction == null ? "ANY" : attraction;
        family = Map.copyOf(family); circles = List.copyOf(circles);
    }
    public static int rankIndex(String rank) {
        if (rank == null || rank.isEmpty() || rank.equals("civilian")) return CIVILIAN;
        int i = RANKS.indexOf(rank.toLowerCase(Locale.ROOT));
        if (i < 0) throw new IllegalArgumentException("unknown rank " + rank);
        return i;
    }
    /** How senior a rank is on the ladder (ANBU sits beside Jonin). */
    public static int seniority(int rank) { return rank == CIVILIAN ? 0 : rank >= 4 ? rank - 1 : rank; }
    public boolean shinobi() { return rank != CIVILIAN; }
    public boolean clanless() { return clan.isEmpty(); }
    public boolean romantic() { return !attraction.equals("NONE"); }
    public boolean attractedTo(String otherGender) { return attraction.equals("ANY") || attraction.equals(otherGender); }
    /** The communities whose standing this person's opinion counts toward: clan (or clanless), district, rank. */
    public List<String> communities() {
        var list = new java.util.ArrayList<String>();
        list.add(clan.isEmpty() ? (shinobi() ? "group:clanless" : "group:civilian") : "clan:" + clan);
        if (!district.isEmpty()) list.add("district:" + district);
        list.add(shinobi() ? "rank:" + RANKS.get(rank) : "rank:civilian");
        list.add("village");
        return list;
    }
    public Person withStage(Stage next) { return new Person(id, clan, district, rank, next, personality, gender, attraction, birthday, family, circles); }
    public Person withRank(int next) { return new Person(id, clan, district, next, stage, personality, gender, attraction, birthday, family, circles); }
    public Person withPersonality(Personality next) { return new Person(id, clan, district, rank, stage, next, gender, attraction, birthday, family, circles); }
    public Person withClan(String next) { return new Person(id, next, district, rank, stage, personality, gender, attraction, birthday, family, circles); }
}
