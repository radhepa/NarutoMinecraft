package dev.shinobi.combat;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/**
 * The twelve hand signs. Typed input maps them to {@code 1} to {@code 0}, {@code -} and {@code =} by default; the
 * radial wheel puts Rat at the top and goes clockwise, 30 degrees a sign.
 */
public enum HandSign {
    RAT, OX, TIGER, HARE, DRAGON, SNAKE, HORSE, RAM, MONKEY, BIRD, DOG, BOAR;

    public static final String[] DEFAULT_KEYS = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="};
    public static final double DEADZONE = 0.25;

    public String id() { return name().toLowerCase(Locale.ROOT); }
    public static HandSign of(String id) { return valueOf(id.trim().toUpperCase(Locale.ROOT)); }

    public static HandSign byKey(String key) {
        for (int i = 0; i < DEFAULT_KEYS.length; i++) if (DEFAULT_KEYS[i].equals(key)) return values()[i];
        return null;
    }
    /**
     * The sign under a radial stick or mouse offset ({@code x} right, {@code y} up, each -1..1), or null inside the
     * dead zone. Each sign owns the 30 degrees centred on its spoke.
     */
    public static HandSign radial(double x, double y) {
        if (Math.hypot(x, y) < DEADZONE) return null;
        double deg = Math.toDegrees(Math.atan2(x, y));
        if (deg < 0) deg += 360;
        return values()[(int) Math.floor((deg + 15) / 30) % 12];
    }

    /** "snake ram monkey" to signs; an empty string is a signless technique. */
    public static List<HandSign> sequence(String text) {
        var out = new ArrayList<HandSign>();
        for (String p : text.trim().split("\\s+")) if (!p.isEmpty()) out.add(of(p));
        return out;
    }
    public static List<HandSign> sequence(List<String> ids) {
        var out = new ArrayList<HandSign>();
        for (String s : ids) out.add(of(s));
        return out;
    }
}
