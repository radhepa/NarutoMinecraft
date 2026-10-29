package dev.shinobi.village.look;

/**
 * The player's age stages (ROADMAP.md, "Growing up"). The model is scaled, never swapped, so every wardrobe piece fits
 * every stage: vanilla's {@code scale} attribute carries the hitbox, eye height and reach, and the player poser draws a
 * child's head 10% larger. There is no old age: adult is for good.
 */
public enum AgeStage {
    CHILD("child", 11, 12, 0.78, 1.1),
    TEEN("teen", 13, 17, 0.9, 1.0),
    ADULT("adult", 18, Integer.MAX_VALUE, 1.0, 1.0);

    /** Vanilla's player eye height at scale 1, in blocks. */
    public static final double EYE_HEIGHT = 1.62;
    /** Vanilla's player height at scale 1, in blocks. */
    public static final double HEIGHT = 1.8;

    private final String id;
    public final int fromAge, toAge;
    /** The {@code scale} attribute's value. */
    public final double scale;
    /** The player poser's extra head scale, on top of {@link #scale}. */
    public final double head;

    AgeStage(String id, int fromAge, int toAge, double scale, double head) {
        this.id = id; this.fromAge = fromAge; this.toAge = toAge; this.scale = scale; this.head = head;
    }

    public String id() { return id; }
    public double eyeHeight() { return EYE_HEIGHT * scale; }
    public double height() { return HEIGHT * scale; }

    /** The next stage, or this one if it is the last. */
    public AgeStage next() { return this == ADULT ? ADULT : values()[ordinal() + 1]; }

    /** The stage after a number of the story's time skips: none in the beta, one opens the Chunin arc, two the Jonin trial. */
    public static AgeStage afterTimeSkips(int skips) { return values()[Math.max(0, Math.min(skips, 2))]; }

    public static AgeStage of(String id) {
        for (var s : values()) if (s.id.equals(id)) return s;
        throw new IllegalArgumentException("unknown age stage " + id);
    }

    public boolean atLeast(AgeStage other) { return ordinal() >= other.ordinal(); }
}
