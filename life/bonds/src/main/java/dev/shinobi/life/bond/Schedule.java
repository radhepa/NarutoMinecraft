package dev.shinobi.life.bond;

/**
 * When someone is free, in hours of the in-game day, matching VF's routines: everyone sleeps from 23:00 to 6:00;
 * Academy children have lessons 9 to 12 on weekdays; civilians with a workplace work 9 to 17 on weekdays; shinobi are
 * away on duty some days (8 to 18), more often the higher their rank, rolled from the save seed per person and day.
 * The world glue can override with VF's actual routine block; the engine uses this to decline or suggest a time.
 */
public final class Schedule {
    /** Market Day is the seventh day of VF's week; the weekdays are the first five. */
    public static int weekday(long day) { return (int) Math.floorMod(day, 7); }
    public static boolean weekend(long day) { return weekday(day) >= 5; }

    public static double dutyChance(Person p) {
        return switch (Person.seniority(p.rank())) { case 1 -> .35; case 2 -> .45; case 3 -> .55; case 4 -> .6; default -> 0; };
    }
    /** What someone is doing at that hour: "free", "asleep", "lessons", "work" or "duty". */
    public static String doing(long seed, Person p, long day, int hour) {
        if (hour >= 23 || hour < 6) return "asleep";
        if (p.stage() == Person.Stage.CHILD && p.rank() <= 0 && !weekend(day) && hour >= 9 && hour < 12) return "lessons";
        if (!p.shinobi() && p.stage() != Person.Stage.CHILD && !weekend(day) && hour >= 9 && hour < 17
                && p.circles().stream().anyMatch(c -> c.startsWith("work:"))) return "work";
        if (p.shinobi() && p.rank() >= 1 && hour >= 8 && hour < 18 && Seeds.roll(seed, "duty", p.id(), Long.toString(day)) < dutyChance(p)) return "duty";
        return "free";
    }
    public static boolean free(long seed, Person p, long day, int hour) { return doing(seed, p, day, hour).equals("free"); }

    /** The first hour within the next {@code days} days when everyone is free and the activity is open, or null. */
    public static long[] nextFree(long seed, java.util.List<Person> people, Activity a, long from, int fromHour, int days) {
        for (long d = from; d < from + days; d++)
            for (int h = d == from ? fromHour : 6; h < 24; h++) {
                if (!a.open(d, h)) continue;
                final long dd = d; final int hh = h;
                if (people.stream().allMatch(p -> free(seed, p, dd, hh))) return new long[]{d, h};
            }
        return null;
    }
    private Schedule() {}
}
