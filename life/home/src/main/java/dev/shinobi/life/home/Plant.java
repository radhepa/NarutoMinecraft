package dev.shinobi.life.home;

/**
 * The houseplant: a sprout that grows over the seasons if you water it. Each day it was watered within the last three
 * days it grows (faster in spring, slower in winter, a quarter faster with the whole balcony set). Forgotten for a
 * while it droops, and after ten days it wilts; it never dies, and one watering perks it up again. From
 * {@code FLOWERING} it flowers in spring and summer, and visitors notice.
 */
public final class Plant {
    public enum Stage { SPROUT, SEEDLING, LEAFY, FLOWERING, GRAND }
    public enum Look { HEALTHY, DROOPING, WILTED }
    /** Growth needed for each stage: about two seasons of care from sprout to grand. */
    static final int[] GROWTH = {0, 8, 20, 36, 56};
    public static final int THIRSTY = 3, WILTS = 10;

    private double growth;
    private long watered = Long.MIN_VALUE / 2;

    public void water(long day) { watered = day; }
    public long lastWatered() { return watered; }

    /** End of day: grows if it was watered recently. Seasons are VF's (0 spring to 3 winter). */
    public void endDay(long day, int season, boolean morningAir) {
        if (day - watered > THIRSTY) return;
        double rate = switch (season) { case 0 -> 1.5; case 3 -> .5; default -> 1; };
        growth += rate * (morningAir ? 1.25 : 1);
    }
    public Stage stage() {
        int s = 0;
        for (int i = 0; i < GROWTH.length; i++) if (growth >= GROWTH[i]) s = i;
        return Stage.values()[s];
    }
    public Look look(long day) {
        long dry = day - watered;
        return dry > WILTS ? Look.WILTED : dry > THIRSTY ? Look.DROOPING : Look.HEALTHY;
    }
    public boolean flowering(long day, int season) {
        return stage().compareTo(Stage.FLOWERING) >= 0 && season <= 1 && look(day) == Look.HEALTHY;
    }
    /** What it adds to the home's comfort: a cared-for plant 1 to 3 by stage, a drooping one nothing. */
    public int comfort(long day) {
        if (look(day) != Look.HEALTHY) return 0;
        return 1 + stage().ordinal() / 2;
    }
    double growth() { return growth; }
    void restore(double g, long w) { growth = g; watered = w; }
}
