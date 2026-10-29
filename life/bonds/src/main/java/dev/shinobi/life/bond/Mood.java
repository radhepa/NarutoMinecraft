package dev.shinobi.life.bond;

import java.util.Locale;

/**
 * How a community feels after what has happened: cheer (-1 grief to 1 celebration) and tension (0 calm to 1 on edge),
 * pushed by deeds, clan incidents and events, easing by {@link #EASE} a day. Tension makes quarrels likelier and
 * news travel faster; cheer makes good news travel faster. Dialogue reads the label ({@code village.mood.<label>}).
 */
public record Mood(double cheer, double tension) {
    public static final Mood CALM = new Mood(0, 0);
    public static final double EASE = .9;

    public enum Label {
        FESTIVE, PROUD, CALM, UNEASY, TENSE, GRIEVING;
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Label of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
    }
    public Mood { cheer = Math.clamp(cheer, -1, 1); tension = Math.clamp(tension, 0, 1); }
    public Mood push(double c, double t) { return new Mood(cheer + c, tension + t); }
    public Mood eased() { return new Mood(cheer * EASE, tension * EASE); }
    public boolean settled() { return Math.abs(cheer) < .02 && tension < .02; }
    public Label label() {
        if (cheer <= -.4) return Label.GRIEVING;
        if (tension >= .6) return Label.TENSE;
        if (tension >= .3) return Label.UNEASY;
        if (cheer >= .5) return Label.FESTIVE;
        if (cheer >= .2) return Label.PROUD;
        return Label.CALM;
    }
}
