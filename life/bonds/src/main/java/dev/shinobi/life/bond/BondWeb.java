package dev.shinobi.life.bond;

/**
 * Everyone you are close to, as one number: how many bonds the player has at level 6 or more, and how deep. Level 6
 * counts 1, 7 counts 2, 8 counts 3, 9 counts 4 and 10 counts 6; and each community (a clan, a district, a rank)
 * holding at least one such bond adds 1, so a web that reaches across the village counts for more than a deep
 * circle in one corner. Quests read it with {@code bond_web}.
 */
public final class BondWeb {
    private static final int[] WEIGHT = {0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 6};

    public static int score(BondWorld w) {
        int sum = 0;
        var reached = new java.util.TreeSet<String>();
        for (String who : w.bonded()) {
            int level = w.effectiveLevel(who);
            if (level < 6) continue;
            sum += WEIGHT[Math.min(10, level)];
            for (String c : w.person(who).communities()) if (!c.equals("village")) reached.add(c);
        }
        return sum + reached.size();
    }
    private BondWeb() {}
}
