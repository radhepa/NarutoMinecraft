package dev.shinobi.life.home;

import dev.shinobi.life.home.Piece.Category;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 * One player's home: the flat, the furniture placed in it, the keepsakes and photos on show, the mess, the plant, the
 * cupboard, the mailbox, and who holds a spare key. One home per player (in multiplayer too: each player gets their
 * own flat in the block, and only its owner, and later a spouse, furnishes it). The world glue keeps the blocks; this
 * keeps the meaning, and is what the save stores ({@code shinobi_life:home}, format 1).
 */
public final class Home {
    /** The most mess that piles up: the floor is covered, and it goes no further. Tidy, lived-in, messy. */
    public static final int MAX_MESS = 12, LIVED_IN = 4, MESSY = 8, KEY_LEVEL = 6;
    /** Keepsakes that can stand on their own (the sill, the table, the tops of things) before display furniture is needed. */
    public static final int FREE_STANDING = 6;
    /** The orphan's stipend, in the mailbox every morning for the whole game. There is no rent. */
    public static final int STIPEND = 30;

    public enum Tidiness { TIDY, LIVED_IN, MESSY }

    public final String owner;
    private Flat flat;
    private final List<String> placed = new ArrayList<>();
    private final List<String> crates = new ArrayList<>();
    private final List<Keepsake> owned = new ArrayList<>(), displayed = new ArrayList<>();
    private final Map<String, List<Photo>> photos = new LinkedHashMap<>();
    private final Map<String, Long> keys = new TreeMap<>();
    private final TreeSet<String> noticed = new TreeSet<>();
    private final List<String> residents = new ArrayList<>();
    final Map<String, Long> lastVisit = new TreeMap<>();
    private int mess, ramenCups, cleanings;
    private String pet = "";
    public final Plant plant = new Plant();
    public final Pantry pantry = new Pantry();
    public final Mailbox mailbox = new Mailbox();

    public Home(String owner, Flat flat) {
        this.owner = owner; this.flat = flat;
        residents.add(owner);
        placed.addAll(Catalog.STARTER);
    }
    public static Home starting(String owner, long seed, boolean classic) { return new Home(owner, Flat.starting(seed, classic)); }

    public Flat flat() { return flat; }
    public List<String> placed() { return List.copyOf(placed); }
    public List<String> crates() { return List.copyOf(crates); }
    public boolean has(String piece) { return placed.contains(piece); }
    public boolean hasTag(String tag) { return placed.stream().anyMatch(id -> Catalog.piece(id).tags().contains(tag)); }
    public int cellsUsed() { return placed.stream().mapToInt(id -> Catalog.piece(id).cells()).sum(); }
    public int cellsFree() { return flat.cells() - cellsUsed(); }
    public long beds() { return placed.stream().filter(id -> Catalog.piece(id).category() == Category.BED && !Catalog.piece(id).tags().contains("camp")).count(); }

    // -- furnish mode --------------------------------------------------------------------------------

    /** Places a piece: "ok", "no_room", "too_many_beds" or "balcony" (a balcony piece in a flat without one). */
    public String place(String id) {
        var p = Catalog.piece(id);
        if (p.category() == Category.FIXTURE) return "fixed";
        if (p.cells() > cellsFree()) return "no_room";
        if (p.category() == Category.BED && !p.tags().contains("camp") && beds() >= flat.tier().beds) return "too_many_beds";
        if (p.tags().contains("balcony") && !flat.balcony()) return "balcony";
        placed.add(id);
        if (p.tags().contains("fresh")) pantry.icebox(true);
        return "ok";
    }
    /** Picks a piece back up: "ok", "not_here", "fixed" or "last_bed" (every home keeps one bed). */
    public String remove(String id) {
        var p = Catalog.piece(id);
        if (p.category() == Category.FIXTURE) return "fixed";
        if (!placed.contains(id)) return "not_here";
        if (p.category() == Category.BED && !p.tags().contains("camp") && beds() <= 1) return "last_bed";
        placed.remove(id);
        if (p.tags().contains("fresh") && !hasTag("fresh")) pantry.icebox(false);
        int keep = slots("keepsake"), frames = slots("photo");
        while (displayed.size() > keep) displayed.removeLast();
        while (hung() > frames) unhangOne();
        return "ok";
    }

    // -- keepsakes and photos ------------------------------------------------------------------------

    int slots(String tag) {
        int furniture = placed.stream().map(Catalog::piece).filter(p -> p.category() == Category.DISPLAY && p.tags().contains(tag)).mapToInt(Piece::displays).sum();
        return tag.equals("keepsake") ? furniture + FREE_STANDING : furniture;
    }
    /** Chest slots at home: plain Minecraft chests and barrels, 27 each. More come with every chest you buy. */
    public int storageSlots() {
        return placed.stream().map(Catalog::piece).flatMap(p -> p.tags().stream()).filter(t -> t.startsWith("slots:"))
                .mapToInt(t -> Integer.parseInt(t.substring(6))).sum();
    }
    public void keep(Keepsake k) { if (owned.stream().noneMatch(o -> o.id().equals(k.id()))) owned.add(k); }
    public List<Keepsake> owned() { return List.copyOf(owned); }
    public List<Keepsake> displayed() { return List.copyOf(displayed); }
    /** Puts a keepsake you own on show: "ok", "no_space", "not_owned" or "already". */
    public String display(String keepsakeId) {
        var k = owned.stream().filter(o -> o.id().equals(keepsakeId)).findFirst().orElse(null);
        if (k == null) return "not_owned";
        if (displayed.contains(k)) return "already";
        if (displayed.size() >= slots("keepsake")) return "no_space";
        displayed.add(k);
        return "ok";
    }
    public void undisplay(String keepsakeId) { displayed.removeIf(k -> k.id().equals(keepsakeId)); }

    /** A photo taken at a milestone; a retake after a time skip is the next version and hangs in its place. */
    public Photo photo(String milestone, long day, List<String> people, String stage) {
        var versions = photos.computeIfAbsent(milestone, k -> new ArrayList<>());
        var p = new Photo(milestone, day, people, stage, versions.size() + 1);
        versions.add(p);
        return p;
    }
    public Map<String, List<Photo>> album() { var m = new LinkedHashMap<String, List<Photo>>(); photos.forEach((k, v) -> m.put(k, List.copyOf(v))); return m; }
    private final List<String> wall = new ArrayList<>();
    /** Hangs a milestone's newest photo: "ok", "no_frame", "no_photo" or "already". */
    public String hang(String milestone) {
        if (!photos.containsKey(milestone)) return "no_photo";
        if (wall.contains(milestone)) return "already";
        if (wall.size() >= slots("photo")) return "no_frame";
        wall.add(milestone);
        return "ok";
    }
    public List<Photo> wall() { return wall.stream().map(m -> photos.get(m).getLast()).toList(); }
    int hung() { return wall.size(); }
    private void unhangOne() { wall.removeLast(); }

    // -- mess ----------------------------------------------------------------------------------------

    /** Mess from living: a meal's dishes, a ramen cup, cooking, guests, mud from a mission. Capped, never worse. */
    public void mess(int amount, String why) {
        mess = Math.min(MAX_MESS, mess + Math.max(0, amount));
        if (why.equals("ramen_cup")) ramenCups = Math.min(6, ramenCups + 1);
    }
    /** A quick clean at the sink: everything put away in one go. */
    public void clean() { if (mess > 0) cleanings++; mess = 0; ramenCups = 0; }
    public int mess() { return mess; }
    /** How many empty ramen cups are on show (the world glue renders up to six). */
    public int ramenCups() { return ramenCups; }
    public int cleanings() { return cleanings; }
    public Tidiness tidiness() { return mess >= MESSY ? Tidiness.MESSY : mess >= LIVED_IN ? Tidiness.LIVED_IN : Tidiness.TIDY; }

    // -- the day -------------------------------------------------------------------------------------

    /** Morning: the stipend envelope is in the mailbox, every day of the game. Returns the ryo in it. */
    public int morning(long day) {
        mailbox.post(Mailbox.Kind.STIPEND, "office:hokage", day, "home.mail.stipend", STIPEND + " ryo");
        return STIPEND;
    }
    /** End of day: the plant grows if it was watered (only a houseplant or bonsai that is actually placed). */
    public void endDay(long day, int season, Comfort.Score score) {
        if (hasTag("plant")) plant.endDay(day, season, score.perk(FurnitureSet.MORNING_AIR));
    }

    // -- people --------------------------------------------------------------------------------------

    /** Gives a spare key: "ok", "not_close_enough" (bond level 6 needed), "no_keys_left" or "already". */
    public String giveKey(String who, int level, long day) {
        if (keys.containsKey(who)) return "already";
        if (level < KEY_LEVEL) return "not_close_enough";
        if (keys.size() >= flat.keys()) return "no_keys_left";
        keys.put(who, day);
        return "ok";
    }
    public void takeKeyBack(String who) { keys.remove(who); }
    /** Key holders by id, in that fixed order (visits walk it, so a seed always gives the same day). */
    public Map<String, Long> keys() { return Collections.unmodifiableMap(new TreeMap<>(keys)); }
    public boolean keyHolder(String who) { return keys.containsKey(who); }

    public void pet(String kind) { pet = kind == null ? "" : kind; }
    public String pet() { return pet; }
    public boolean petAtHome() { return !pet.isEmpty() && has("pet_bed"); }

    /** Someone moves in (a spouse, later a child): they need a bed of their own, or a double futon to share. */
    public String moveIn(String who) {
        if (residents.contains(who)) return "already";
        long sleepers = residents.size() + 1, room = placed.stream().map(Catalog::piece)
                .filter(p -> p.category() == Category.BED && !p.tags().contains("camp")).mapToLong(p -> p.tags().contains("two") ? 2 : 1).sum();
        if (room < sleepers) return "needs_bed";
        residents.add(who);
        return "ok";
    }
    public List<String> residents() { return List.copyOf(residents); }

    /** Whether {@code who} has already remarked on {@code what} (a kept gift, a photo they are in): once each. */
    public boolean noticed(String who, String what) { return noticed.contains(who + "|" + what); }
    void notice(String who, String what) { noticed.add(who + "|" + what); }

    // -- moving --------------------------------------------------------------------------------------

    /**
     * Moves to another home: everything is packed into moving crates and set out again in the new place, in the order
     * it was placed; what does not fit stays in its crate. Keepsakes, photos, the plant, the pet, the keys' holders
     * (they get a new key) and the people who live here all come along.
     */
    public void moveTo(Flat next) {
        var packed = new ArrayList<>(placed); packed.addAll(crates);
        placed.clear(); crates.clear();
        flat = next;
        for (String id : packed) if (!place(id).equals("ok")) crates.add(id);
        int keep = slots("keepsake"), frames = slots("photo");
        while (displayed.size() > keep) displayed.removeLast();
        while (hung() > frames) unhangOne();
        while (keys.size() > flat.keys()) keys.remove(keys.keySet().iterator().next());
    }
    /** Unpacks a crate into the home, when room has been made. */
    public String unpack(String id) {
        if (!crates.contains(id)) return "not_packed";
        String r = place(id);
        if (r.equals("ok")) crates.remove(id);
        return r;
    }
}
