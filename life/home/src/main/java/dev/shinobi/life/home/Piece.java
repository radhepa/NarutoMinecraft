package dev.shinobi.life.home;

import java.util.Set;

/**
 * One piece of furniture as data: what it is for ({@link Category}), the comfort and style it adds, how many floor
 * cells it takes, its price at the furniture shop (0 for a piece you are given or earn), the set it belongs to (or
 * none), the beta slice that brings it, and where it comes from. Keepsake displays hold {@code displays} keepsakes.
 * The item registry (Shinobi Life's furniture items) registers one block per piece under the same id.
 */
public record Piece(String id, Category category, int comfort, int style, int cells, int price, String set, String slice,
        Source source, int displays, Set<String> tags) {

    /** What a piece is for. Some categories have a job at home beyond comfort (a bed clears fatigue; a stove cooks). */
    public enum Category {
        BED, TABLE, SEATING, STORAGE, LIGHT, FLOOR, WALL, DECOR, PLANT, KITCHEN, BATH, STATION, TRAINING, PET, DISPLAY, FIXTURE;
        public String id() { return name().toLowerCase(java.util.Locale.ROOT); }
    }
    /** Where a piece comes from: the furniture shop, the workbench, a quest or event reward, or the flat itself. */
    public enum Source { STARTER, SHOP, CRAFT, QUEST, EVENT, CLAN, FIXED }

    public Piece {
        set = set == null ? "" : set;
        tags = Set.copyOf(tags);
        if (cells < 0 || comfort < 0 || style < 0 || price < 0) throw new IllegalArgumentException("negative value on " + id);
    }
    public boolean inSet() { return !set.isEmpty(); }
    /** Half price back at the shop (ROADMAP.md, "Ryo"); fixed and starter pieces are not sold. */
    public int resale() { return source == Source.FIXED || source == Source.STARTER ? 0 : price / 2; }
}
