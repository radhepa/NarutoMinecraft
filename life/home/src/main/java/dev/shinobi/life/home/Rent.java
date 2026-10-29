package dev.shinobi.life.home;

/**
 * Money for the home. The orphan's stipend (30 ryo a day, in the mailbox each morning) covers the Academy years, rent
 * included. <b>Rent from Genin is an open question</b> (docs/HOME.md, "Money"): off by default; when on, a small weekly
 * rent is due to the landlady on Market Day. She forgives one late week a season; after that it simply carries over,
 * with a note under the door. Nothing is ever taken, and nobody is ever put out.
 */
public final class Rent {
    public static final int STIPEND = 30, GENIN_WEEKLY = 50, CHUNIN_FLAT_WEEKLY = 300, MARKET_DAY = 6;

    /** What a week's rent day did. */
    public record Due(int asked, int paid, int owed, boolean forgiven, String note) {}

    private final boolean on;
    private int owed, forgivenSeason = -1, paidTotal, lateWeeks;

    public Rent(boolean on) { this.on = on; }
    public boolean on() { return on; }
    public int owed() { return owed; }
    public int paidTotal() { return paidTotal; }
    public int lateWeeks() { return lateWeeks; }

    /** The stipend for the day: Academy years only. */
    public static int stipend(int rank) { return rank <= 0 ? STIPEND : 0; }
    /** What a week costs at this rank in this home. */
    public int weekly(int rank, Flat flat) {
        if (!on && flat.tier() == Flat.Tier.ACADEMY_FLAT) return 0;
        if (flat.tier() == Flat.Tier.TWO_ROOM_FLAT) return CHUNIN_FLAT_WEEKLY;
        return flat.tier() == Flat.Tier.ACADEMY_FLAT && rank >= 1 ? GENIN_WEEKLY : 0;
    }

    /** Market Day: pay what is due from {@code purse} (what you can), and the landlady answers. */
    public Due weekDue(int rank, Flat flat, int season, int purse) {
        int asked = weekly(rank, flat) + owed;
        if (asked == 0) return new Due(0, 0, 0, false, "");
        int paid = Math.min(asked, Math.max(0, purse));
        paidTotal += paid;
        int left = asked - paid;
        if (left == 0) { owed = 0; return new Due(asked, paid, 0, false, "home.landlady.thanks"); }
        lateWeeks++;
        if (forgivenSeason != season) {
            forgivenSeason = season; owed = 0;
            return new Due(asked, paid, 0, true, "home.landlady.forgiven");
        }
        owed = left;
        return new Due(asked, paid, left, false, "home.landlady.reminder");
    }
}
