package dev.shinobi.life.home;

import dev.shinobi.life.home.Piece.Category;
import dev.shinobi.life.home.Piece.Source;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * The furniture, sets and keepsakes of the home (docs/HOME.md, "Furniture" and "Keepsakes"). Ids are bare here; the
 * item registry namespaces them ({@code shinobi_life:<id>}) and tags them {@code shinobi_life:furniture}. Prices are
 * the furniture shop's in ryo (the items session sets the final numbers in {@code economy.json}); slices are
 * {@code b1}, {@code b2}, {@code b2.5}, {@code b3} or {@code later}.
 */
public final class Catalog {

    /** The 25 clans of CLANS.md, in welcome-wave order: wave 1 (Beta 2), then wave 2 (Beta 2.5). */
    public static final List<String> CLANS_WAVE_1 = List.of("senju", "uzumaki", "uchiha", "hyuga", "nara", "akimichi", "yamanaka", "inuzuka");
    public static final List<String> CLANS_WAVE_2 = List.of("sarutobi", "aburame", "hatake", "kurama", "shimura", "yuhi", "gekko",
            "shiranui", "morino", "umino", "haruno", "namiashi", "hagane", "kinoshita", "tsuchigumo", "suzuran", "tobari");

    public static final Map<String, Piece> PIECES;
    public static final Map<String, FurnitureSet> SETS;
    public static final Map<String, Keepsake> KEEPSAKES;
    /** What every Academy flat starts with, besides its fixtures (the item registry's {@code kit:start}; the wardrobe cabinet is built in). */
    public static final List<String> STARTER = List.of("futon", "low_table", "cupboard", "storage_chest", "cooking_pot");

    private static final List<Piece> pieces = new ArrayList<>();
    private static Piece p(String id, Category c, int comfort, int style, int cells, int price, String set, String slice, Source src, String... tags) {
        var x = new Piece(id, c, comfort, style, cells, price, set, slice, src, 0, Set.of(tags));
        pieces.add(x); return x;
    }
    private static void shelf(String id, Category c, int style, int cells, int price, String slice, int displays, String... tags) {
        pieces.add(new Piece(id, c, 0, style, cells, price, "", slice, Source.SHOP, displays, Set.of(tags)));
    }
    /** Chests and barrels: plain Minecraft storage, {@code slots:27} each. */
    private static void chest(String id, int comfort, int style, int cells, int price, String slice, Source src) {
        pieces.add(new Piece(id, Category.STORAGE, comfort, style, cells, price, "", slice, src, 0, Set.of("chest", "slots:27")));
    }

    static {
        // The flat's fixtures: built in, never moved. The mailbox, mirror and closet are where the day starts.
        p("window", Category.FIXTURE, 0, 1, 0, 0, "", "b1", Source.FIXED, "view");
        p("mailbox", Category.FIXTURE, 0, 0, 0, 0, "", "b1", Source.FIXED, "mail");
        p("mirror", Category.FIXTURE, 0, 0, 0, 0, "", "b1", Source.FIXED, "wardrobe");
        p("sink", Category.FIXTURE, 0, 0, 0, 0, "", "b1", Source.FIXED, "clean");
        p("stove", Category.FIXTURE, 0, 0, 0, 0, "", "b1", Source.FIXED, "heat");
        p("bathtub", Category.FIXTURE, 0, 1, 0, 0, "", "b1", Source.FIXED, "bath");

        // The Leaf set: the first proper set, about an in-game week of savings (ROADMAP.md, "Ryo").
        p("futon", Category.BED, 4, 1, 2, 0, "", "b1", Source.STARTER, "bed");
        p("low_table", Category.TABLE, 2, 1, 1, 0, "", "b1", Source.STARTER, "meal");
        p("zabuton", Category.SEATING, 2, 1, 1, 15, "leaf", "b1", Source.SHOP);
        p("tatami", Category.FLOOR, 3, 1, 0, 40, "leaf", "b1", Source.SHOP);
        p("andon_lamp", Category.LIGHT, 2, 2, 1, 35, "leaf", "b1", Source.SHOP);
        p("scroll_shelf", Category.STORAGE, 1, 2, 1, 60, "leaf", "b1", Source.SHOP, "study");
        p("shoji_screen", Category.DECOR, 1, 2, 1, 80, "leaf", "b1", Source.SHOP);
        p("leaf_banner", Category.WALL, 0, 3, 0, 50, "leaf", "b1", Source.SHOP);

        // The ramen corner: a little shrine to Ichiraku.
        p("ramen_cup_tower", Category.DECOR, 0, 2, 1, 15, "ramen", "b1", Source.SHOP);
        p("noren", Category.WALL, 1, 2, 0, 35, "ramen", "b1", Source.SHOP);
        p("poster", Category.WALL, 0, 2, 0, 20, "ramen", "b1", Source.SHOP);
        p("bowl_shelf", Category.STORAGE, 0, 2, 1, 40, "ramen", "b1", Source.SHOP);
        p("ichiraku_stool", Category.SEATING, 2, 2, 1, 0, "ramen", "b1", Source.QUEST, "from:filler.ramen_thief.3");

        // The balcony: plants, a bench and the view of the Rock.
        p("balcony_planter", Category.PLANT, 1, 2, 1, 40, "balcony", "b1", Source.SHOP, "balcony", "plant");
        p("wind_chime", Category.WALL, 1, 2, 0, 20, "balcony", "b1", Source.SHOP, "balcony");
        p("balcony_bench", Category.SEATING, 2, 1, 1, 70, "balcony", "b1", Source.SHOP, "balcony");
        p("laundry_line", Category.DECOR, 1, 1, 0, 15, "balcony", "b1", Source.SHOP, "balcony");
        p("potted_bonsai", Category.PLANT, 1, 3, 1, 120, "balcony", "b2", Source.SHOP, "plant");

        // The training corner: short practice at home, capped (Practice).
        p("training_dummy", Category.TRAINING, 0, 1, 1, 160, "training", "b1", Source.SHOP, "practice");
        p("meditation_mat", Category.TRAINING, 1, 1, 1, 30, "training", "b1", Source.SHOP, "practice", "meditate");
        p("weight_rack", Category.TRAINING, 0, 1, 1, 120, "training", "b2", Source.SHOP, "practice");
        p("weapon_rack", Category.TRAINING, 0, 2, 0, 140, "training", "b2", Source.SHOP, "practice");
        p("target_board", Category.TRAINING, 0, 1, 0, 70, "training", "b2", Source.SHOP, "practice");

        // The tea corner, around the tea master's gift.
        p("tea_set", Category.TABLE, 1, 2, 0, 0, "tea", "b2", Source.QUEST, "from:side.b2.tea_master");
        p("tea_table", Category.TABLE, 2, 2, 1, 90, "tea", "b2", Source.SHOP);
        p("hanging_scroll", Category.WALL, 0, 3, 0, 80, "tea", "b2", Source.SHOP);
        p("ikebana", Category.DECOR, 1, 2, 1, 45, "tea", "b2", Source.SHOP);

        // Festival pieces, from the Leaf Festival's stalls and games.
        p("lantern_string", Category.LIGHT, 1, 3, 0, 40, "festival", "b2", Source.EVENT);
        p("festival_mask", Category.WALL, 0, 2, 0, 25, "festival", "b2", Source.EVENT);
        p("goldfish_bowl", Category.DECOR, 1, 2, 1, 0, "festival", "b2", Source.EVENT, "from:goldfish_scooping");
        p("fan_display", Category.WALL, 0, 2, 0, 20, "festival", "b2", Source.EVENT);
        p("festival_drum", Category.DECOR, 0, 2, 1, 80, "festival", "b2", Source.EVENT);

        // Everything else in the Academy flat and after.
        p("cupboard", Category.KITCHEN, 1, 0, 1, 0, "", "b1", Source.STARTER, "pantry");
        p("wardrobe_cabinet", Category.FIXTURE, 0, 1, 0, 0, "", "b1", Source.FIXED, "wardrobe");
        p("futon_deluxe", Category.BED, 7, 2, 2, 220, "", "b1", Source.SHOP, "bed");
        p("low_desk", Category.TABLE, 1, 1, 1, 70, "", "b1", Source.SHOP, "journal", "study");
        p("cooking_pot", Category.KITCHEN, 1, 1, 0, 0, "", "b1", Source.STARTER, "cook", "vf:hearth_pot");
        p("prep_table", Category.KITCHEN, 1, 1, 1, 90, "", "b1", Source.SHOP, "cook", "vf:hearth_prep");
        p("icebox", Category.KITCHEN, 1, 0, 1, 160, "", "b1", Source.SHOP, "pantry", "fresh");
        p("tea_kettle", Category.KITCHEN, 1, 1, 0, 25, "", "b1", Source.SHOP, "tea");
        p("clay_oven", Category.KITCHEN, 1, 1, 1, 150, "", "b2", Source.SHOP, "cook", "vf:hearth_oven");
        p("rug", Category.FLOOR, 2, 1, 0, 25, "", "b1", Source.SHOP);
        p("curtains", Category.WALL, 1, 1, 0, 25, "", "b1", Source.SHOP);
        p("wall_clock", Category.WALL, 0, 1, 0, 60, "", "b1", Source.SHOP);
        p("calendar_scroll", Category.WALL, 0, 1, 0, 10, "", "b1", Source.SHOP, "events");
        p("alarm_clock", Category.DECOR, 0, 1, 0, 15, "", "b1", Source.SHOP, "alarm");
        p("shoe_rack", Category.STORAGE, 0, 1, 1, 20, "", "b1", Source.SHOP, "genkan");
        p("umbrella_stand", Category.DECOR, 0, 1, 1, 15, "", "b1", Source.SHOP, "genkan");
        p("bath_mat", Category.BATH, 1, 1, 0, 10, "", "b1", Source.SHOP);
        p("towel_rack", Category.BATH, 1, 1, 0, 15, "", "b1", Source.SHOP);
        p("potted_fern", Category.PLANT, 1, 2, 1, 25, "", "b1", Source.SHOP, "plant", "waterable");
        p("pet_bed", Category.PET, 1, 1, 1, 40, "", "b1", Source.SHOP, "pet");
        p("pet_bowl", Category.PET, 0, 0, 1, 10, "", "b1", Source.SHOP, "pet");
        chest("storage_chest", 0, 0, 1, 10, "b1", Source.STARTER);
        chest("barrel", 0, 1, 1, 15, "b1", Source.SHOP);
        chest("tansu_chest", 1, 3, 1, 180, "b1", Source.SHOP);
        chest("step_tansu", 1, 3, 2, 320, "b2", Source.SHOP);
        p("workbench", Category.STATION, 0, 0, 2, 250, "", "b1", Source.SHOP, "craft");
        p("small_forge", Category.STATION, 0, 0, 2, 900, "", "b2", Source.SHOP, "smith");
        p("folding_screen", Category.DECOR, 1, 3, 1, 220, "", "b2", Source.SHOP);
        p("kotatsu", Category.TABLE, 6, 2, 2, 280, "", "b2", Source.SHOP, "winter", "meal");
        p("bedroll", Category.BED, 1, 0, 1, 80, "", "b3", Source.SHOP, "camp");
        shelf("display_shelf", Category.DISPLAY, 1, 0, 75, "b1", 6, "keepsake");
        shelf("wall_mount", Category.DISPLAY, 1, 0, 45, "b1", 1, "keepsake");
        shelf("photo_frame", Category.DISPLAY, 1, 0, 15, "b1", 1, "photo");
        shelf("display_case", Category.DISPLAY, 2, 1, 130, "b2", 4, "keepsake");
        shelf("curio_cabinet", Category.DISPLAY, 2, 1, 220, "b2", 12, "keepsake");

        // Later homes (designed now, built after the beta): a bigger bed, a hearth, a partner's and a child's things.
        p("wooden_bed", Category.BED, 9, 3, 3, 600, "", "later", Source.SHOP, "bed");
        p("double_futon", Category.BED, 8, 2, 3, 500, "", "later", Source.SHOP, "bed", "two");
        p("child_futon", Category.BED, 4, 1, 1, 150, "", "later", Source.SHOP, "bed", "child");
        p("pinboard", Category.WALL, 0, 1, 0, 0, "", "later", Source.QUEST, "from:story.home.case_board");
        p("irori_hearth", Category.KITCHEN, 5, 3, 4, 1200, "", "later", Source.SHOP, "heat", "meal");
        p("engawa_bench", Category.SEATING, 3, 2, 2, 250, "", "later", Source.SHOP);
        p("stone_lantern", Category.LIGHT, 1, 3, 1, 200, "", "later", Source.SHOP, "garden");

        // Clan pieces: a banner, a screen and a lantern in each clan's colours, sold in its quarter (one registry item each, variant clan:<id>).
        for (var wave : List.of(CLANS_WAVE_1, CLANS_WAVE_2)) for (String clan : wave) {
            String slice = wave == CLANS_WAVE_1 ? "b2" : "b2.5", set = "clan." + clan;
            p("clan_banner@" + clan, Category.WALL, 0, 3, 0, 60, set, slice, Source.CLAN);
            p("clan_screen@" + clan, Category.DECOR, 1, 2, 1, 120, set, slice, Source.CLAN);
            p("clan_lantern@" + clan, Category.LIGHT, 2, 2, 1, 70, set, slice, Source.CLAN);
        }

        var all = new LinkedHashMap<String, Piece>();
        for (var x : pieces) if (all.put(x.id(), x) != null) throw new IllegalStateException("duplicate piece " + x.id());
        PIECES = Collections.unmodifiableMap(all);

        var sets = new LinkedHashMap<String, FurnitureSet>();
        set(sets, "leaf", FurnitureSet.HOME_SWEET_HOME, Set.of("warmhearted", "steadfast", "gentle"), "");
        set(sets, "ramen", FurnitureSet.RAMEN_AT_HOME, Set.of("fiery", "playful", "warmhearted", "adventurous"), "");
        set(sets, "balcony", FurnitureSet.MORNING_AIR, Set.of("gentle", "imaginative", "shy", "reserved"), "");
        set(sets, "training", FurnitureSet.DOJO, Set.of("proud", "stern", "fiery", "protective", "meticulous"), "");
        set(sets, "tea", FurnitureSet.TEA_TIME, Set.of("thoughtful", "stern", "gentle", "meticulous", "pragmatic"), "");
        set(sets, "festival", FurnitureSet.FESTIVE, Set.of("playful", "curious", "imaginative", "warmhearted"), "");
        for (var wave : List.of(CLANS_WAVE_1, CLANS_WAVE_2)) for (String clan : wave) set(sets, "clan." + clan, FurnitureSet.CLAN_COLOURS, Set.of(), clan);
        SETS = Collections.unmodifiableMap(sets);

        var ks = new LinkedHashMap<String, Keepsake>();
        // Beta 1 (SIDE_QUESTS.md, "Beta catalogue"), by the item registry's ids.
        k(ks, "keepsake_shogi_set", Keepsake.Kind.QUEST, "side.b1.shogi", "", "b1");
        k(ks, "keepsake_cat_figurine", Keepsake.Kind.QUEST, "district.b1.neighbours.3", "", "b1");
        k(ks, "keepsake_framed_ladle", Keepsake.Kind.QUEST, "filler.ramen_thief.3", "", "b1");
        k(ks, "keepsake_bond_teammate_a_1", Keepsake.Kind.GIFT, "bond.b1.classmate_a", "role:teammate_a", "b1");
        k(ks, "keepsake_bond_teammate_b_1", Keepsake.Kind.GIFT, "bond.b1.classmate_b", "role:teammate_b", "b1");
        // Beta 2.
        k(ks, "keepsake_race_ribbon", Keepsake.Kind.QUEST, "side.b2.rooftop_race", "", "b2");
        k(ks, "keepsake_price_war", Keepsake.Kind.QUEST, "district.b2.price_war.4", "", "b2");
        k(ks, "keepsake_ferry_lantern", Keepsake.Kind.QUEST, "district.b2.ferryman.3", "", "b2");
        k(ks, "keepsake_post_splinter", Keepsake.Kind.QUEST, "district.b2.unbeatable_post", "", "b2");
        k(ks, "keepsake_lake_lantern", Keepsake.Kind.QUEST, "filler.lake_lanterns.4", "", "b2");
        k(ks, "keepsake_peace_offering", Keepsake.Kind.QUEST, "filler.dogs_and_bugs.3", "", "b2");
        k(ks, "keepsake_bond_teammate_a_2", Keepsake.Kind.GIFT, "bond.b2.teammate_a.2", "role:teammate_a", "b2");
        k(ks, "keepsake_bond_teammate_b_2", Keepsake.Kind.GIFT, "bond.b2.teammate_b.2", "role:teammate_b", "b2");
        // The story's keepsakes are kept by hook id in the story's files; Keepsake.story(<hook>) makes one at run time.
        // The item registry's 20 mission keepsakes (keepsake_<name>) are kept and shown the same way.
        // The clan welcomes (SIDE_QUESTS.md section 4): one keepsake each.
        for (String clan : CLANS_WAVE_1) k(ks, "keepsake_clan_" + clan, Keepsake.Kind.CLAN, "clan." + clan + ".1", "", "b2");
        for (String clan : CLANS_WAVE_2) k(ks, "keepsake_clan_" + clan, Keepsake.Kind.CLAN, "clan." + clan + ".1", "", "b2.5");
        KEEPSAKES = Collections.unmodifiableMap(ks);
    }
    private static void set(Map<String, FurnitureSet> sets, String id, String perk, Set<String> lovedBy, String clan) {
        var members = pieces.stream().filter(x -> x.set().equals(id)).map(Piece::id).toList();
        sets.put(id, new FurnitureSet(id, members, perk, lovedBy, clan));
    }
    private static void k(Map<String, Keepsake> ks, String id, Keepsake.Kind kind, String from, String giver, String slice) {
        ks.put(id, new Keepsake(id, kind, from, giver, slice));
    }

    public static Piece piece(String id) {
        var x = PIECES.get(id);
        if (x == null) throw new IllegalArgumentException("unknown piece " + id);
        return x;
    }
    public static FurnitureSet set(String id) { return SETS.get(id); }

    private Catalog() {}
}
