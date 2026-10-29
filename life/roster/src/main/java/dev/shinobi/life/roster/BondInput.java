package dev.shinobi.life.roster;

/**
 * What the bond engine (life:bonds) tells the roster about one person today, filled by the Life mod's glue from
 * {@code BondWorld}: the level they act on toward the player, how many times they trained or sparred with the player,
 * whether a quarrel is going on (a permanent falling-out counts: {@code conflict().active() || conflict().broken()}), and the Kindling tier ({@code none}, {@code nature}, {@code technique}, {@code full}).
 */
public record BondInput(int level, int trainedTogether, boolean quarrel, String kindling) {
    public static final BondInput NONE = new BondInput(0, 0, false, "none");
    public BondInput { if (kindling == null) kindling = "none"; }
    public static BondInput of(int level) { return new BondInput(level, 0, false, "none"); }
    public BondInput training(int times) { return new BondInput(level, times, quarrel, kindling); }
    public BondInput quarrelling(boolean q) { return new BondInput(level, trainedTogether, q, kindling); }
    public BondInput kindled(String tier) { return new BondInput(level, trainedTogether, quarrel, tier); }
}
