package dev.shinobi.life.roster;

/**
 * Something the game can show or say: {@code level} (they reached a whole level), {@code technique} (learned where the
 * player saw it), {@code caught_up} (they trained hard on their own and closed the gap; dialogue mentions it),
 * {@code plateau} (they hit the top of the band and wait for the player), {@code kindled}, {@code promoted}.
 */
public record GrowthEvent(long day, String who, String kind, String detail) {}
