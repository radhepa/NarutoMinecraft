package dev.shinobi.life.home;

import dev.shinobi.life.bond.Act;
import dev.shinobi.life.bond.BondWorld;
import dev.shinobi.life.bond.Gifts;
import dev.shinobi.life.bond.Schedule;
import dev.shinobi.life.bond.Together;
import java.util.List;

/**
 * {@link Friends} over the bond engine, by its own verbs: a visit is talk and contact, a good one the
 * {@code visited_home} act, a very good one a little more warmth; something of theirs on show is
 * {@code Gifts.noticed} (their gift: {@code saw_gift_displayed}; a photo they are in: {@code saw_photo_together}, once
 * each); a spare key is the bond flag {@code home.key} (never a moment, so it opens no story gate) and, the first time
 * only, a little warmth; home hangouts are the engine's activities ({@code home_dinner}, {@code study_night},
 * {@code cook_together}, {@code balcony_stargazing}, {@code squad_crash}, {@code tea_at_home}), asked and held through
 * {@code Together}.
 */
public final class BondFriends implements Friends {
    /** The bond flag a key holder carries (quests read it with {@code bond_flag}); a key is not a moment, so it opens no gate. */
    public static final String KEY_FLAG = "home.key", KEY_EVER = "home.key.given", NOTICED = "home.noticed:";
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
        if (quality >= .4) { w.together(who); w.act(who, Act.VISITED_HOME); }
        if (quality >= .65) w.addFriendship(who, 1);
    }
    @Override public boolean noticed(String who, String what, boolean photo) {
        if (w.person(who) == null) return false;
        if (what.startsWith("gift:")) {
            int id;
            try { id = Integer.parseInt(what.substring(5)); } catch (NumberFormatException e) { return false; }
            var gift = Gifts.gift(w, id).orElse(null);
            return gift != null && gift.from().equals(who) && !gift.seen() && Gifts.noticed(w, who, gift.item(), false);
        }
        return Gifts.noticed(w, who, what, photo);
    }
    @Override public void keyGiven(String who) {
        w.setBondFlag(who, KEY_FLAG);
        if (!w.bond(who).has(KEY_EVER)) { w.setBondFlag(who, KEY_EVER); w.addFriendship(who, 1); }
    }
    @Override public void keyTaken(String who) { w.clearBondFlag(who, KEY_FLAG); }

    @Override public String host(List<String> who, String activity, long day, int hour) {
        var answer = Together.invite(w, who, activity, day, hour);
        if (answer.plan() == null) return answer.answers().values().stream().findFirst().orElse("not_today");
        var out = Together.go(w, answer.plan().id(), true);
        return out == null ? "fine" : out.band();
    }
}
