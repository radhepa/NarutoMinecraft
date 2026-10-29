package dev.shinobi.life.home;

import dev.shinobi.life.bond.Act;
import dev.shinobi.life.bond.Activity;
import dev.shinobi.life.bond.BondWorld;
import dev.shinobi.life.bond.Gifts;
import dev.shinobi.life.bond.Schedule;
import dev.shinobi.life.bond.Together;
import java.util.ArrayList;
import java.util.List;

/**
 * {@link Friends} over the bond engine. Visits use the engine's own verbs: a good visit is the {@code hung_out}
 * shared experience, any visit is contact and warmth; a gift on show is the engine's {@code Gifts.seenDisplayed} (the
 * giver remembers it once); a photo they are in is warmth and a bond flag ({@code home.noticed:<what>}); a spare
 * key is a moment ({@code home.spare_key}).
 * Home hangouts are the engine's activities when it has them ({@code home_dinner} today), so asking, tastes,
 * highlights and rituals all work; the proposed home activities ({@link HomeHangout}) fall back to a plain shared
 * experience until the engine's catalog carries them.
 */
public final class BondFriends implements Friends {
    public static final String KEY_MOMENT = "home.spare_key", NOTICED = "home.noticed:";
    private final BondWorld w;

    public BondFriends(BondWorld w) { this.w = w; }
    public BondWorld world() { return w; }

    @Override public List<String> known() { return w.bonded(); }
    @Override public int level(String who) { return w.effectiveLevel(who); }
    @Override public boolean cold(String who) { var c = w.bond(who).conflict(); return c.active() || c.broken(); }
    @Override public boolean free(String who, long day, int hour) { var p = w.person(who); return p != null && Schedule.free(w.seed(), p, day, hour); }
    @Override public String archetype(String who) { var p = w.person(who); return p == null ? "" : p.personality().archetype(); }
    @Override public double warmth(String who) { var p = w.person(who); return p == null ? 0 : p.personality().warmth(); }
    @Override public double openness(String who) { var p = w.person(who); return p == null ? 0 : p.personality().openness(); }
    @Override public String clan(String who) { var p = w.person(who); return p == null ? "" : p.clan(); }

    @Override public void visited(String who, String kind, double quality) {
        if (w.person(who) == null) return;
        w.talk(who);
        if (quality >= .4) { w.together(who); w.act(who, Act.HUNG_OUT); }
        if (quality >= .65) w.addFriendship(who, 1);
    }
    @Override public boolean noticed(String who, String what) {
        if (w.person(who) == null) return false;
        if (what.startsWith("gift:")) {
            try { return Gifts.seenDisplayed(w, Integer.parseInt(what.substring(5))); } catch (NumberFormatException e) { return false; }
        }
        if (w.bond(who).has(NOTICED + what)) return false;
        w.addFriendship(who, 1);
        w.setBondFlag(who, NOTICED + what);
        return true;
    }
    @Override public void keyGiven(String who) { w.moment(who, KEY_MOMENT); }

    @Override public String host(List<String> who, String activity, long day, int hour) {
        if (Activity.CATALOG.containsKey(activity)) {
            var answer = Together.invite(w, who, activity, day, hour);
            if (answer.plan() == null) return answer.answers().values().stream().findFirst().orElse("not_today");
            var out = Together.go(w, answer.plan().id(), true);
            return out == null ? "fine" : out.band();
        }
        var h = HomeHangout.of(activity);
        var came = new ArrayList<String>();
        String why = "not_today";
        for (String id : who) {
            if (level(id) < h.minLevel()) { why = "not_close_enough"; continue; }
            if (hour < h.from() || hour >= h.to()) { why = "closed"; continue; }
            if (!free(id, day, hour)) { why = "busy"; continue; }
            came.add(id);
        }
        if (came.isEmpty()) return why;
        w.experience(h.act(), came);
        return "good";
    }
}
