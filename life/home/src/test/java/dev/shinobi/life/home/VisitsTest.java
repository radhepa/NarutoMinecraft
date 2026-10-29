package dev.shinobi.life.home;

import static org.junit.jupiter.api.Assertions.*;

import dev.shinobi.life.bond.BondWorld;
import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.Test;

/** Visits through the real bond engine. */
class VisitsTest {
    static final long SEED = 20261029;

    static List<Visits.Visit> run(long seed, Home h, BondFriends f, int days, int rank) {
        var all = new ArrayList<Visits.Visit>();
        for (int d = 0; d < days; d++) {
            long day = f.world().day();
            for (String who : Cast.CLASSMATES) f.world().talk(who);
            all.addAll(Visits.daily(seed, h, f, Cast.day(day, rank, 17, day % 4 == 0)));
            h.clean();
            f.world().endDay();
        }
        return all;
    }

    @Test void strangersDoNotDropBy() {
        var w = Cast.world(SEED); var f = new BondFriends(w); var h = new Home(BondWorld.PLAYER, Flat.CLASSIC);
        var visits = run(SEED, h, f, 30, 0);
        assertTrue(visits.stream().noneMatch(v -> v.kind().startsWith("drop_in") || v.kind().startsWith("squad_crash")), visits.toString());
    }
    @Test void friendsDoAndTheSameSeedGivesTheSameVisits() {
        var a = friendsWorld(); var b = friendsWorld();
        var va = run(SEED, a.h, a.f, 60, 1); var vb = run(SEED, b.h, b.f, 60, 1);
        assertEquals(va, vb);
        assertTrue(va.stream().anyMatch(v -> v.kind().startsWith("drop_in")), va.toString());
        assertTrue(va.stream().anyMatch(v -> v.kind().startsWith("sensei_check")));
        assertTrue(va.stream().anyMatch(v -> v.kind().startsWith("neighbour.")));
        assertNotEquals(va, run(SEED + 1, friendsWorld().h, friendsWorld().f, 60, 1));
    }
    record Setup(Home h, BondFriends f) {}
    static Setup friendsWorld() {
        var w = Cast.world(SEED);
        for (String who : Cast.CLASSMATES) Cast.befriend(w, who, 4);
        Cast.befriend(w, Cast.SENSEI, 3);
        return new Setup(new Home(BondWorld.PLAYER, Flat.CLASSIC), new BondFriends(w));
    }

    @Test void aGiftOnShowIsNoticedOnceAndWarmsTheBond() {
        var s = friendsWorld(); var w = s.f.world();
        s.h.place("keepsake_shelf");
        s.h.keep(Catalog.KEEPSAKES.get("village_painting"));
        s.h.display("village_painting");
        double before = w.closeness(Cast.TEAMMATE_A);
        var d = Cast.day(w.day(), 1, 17, false);
        var first = Visits.meet(s.h, s.f, d, List.of(Cast.TEAMMATE_A), "drop_in", 19);
        assertTrue(first.reactions().contains("home.visit.kept_gift"), first.toString());
        assertTrue(w.bond(Cast.TEAMMATE_A).has(BondFriends.NOTICED + "village_painting"));
        assertTrue(w.closeness(Cast.TEAMMATE_A) > before);
        var second = Visits.meet(s.h, s.f, d, List.of(Cast.TEAMMATE_A), "drop_in", 20);
        assertFalse(second.reactions().contains("home.visit.kept_gift"));
        assertFalse(Visits.meet(s.h, s.f, d, List.of(Cast.TEAMMATE_B), "drop_in", 20).reactions().contains("home.visit.kept_gift"),
                "only the giver remarks on it");
    }
    @Test void aMessIsCommentedOnNeverHeldAgainstYou() {
        var s = friendsWorld(); var w = s.f.world();
        s.h.mess(Home.MAX_MESS, "meal");
        double before = w.closeness(Cast.RIVAL);
        var v = Visits.meet(s.h, s.f, Cast.day(w.day(), 1, 17, false), List.of(Cast.RIVAL), "drop_in", 19);
        assertTrue(v.reactions().contains("home.visit.mess.fussy"), v.toString());
        assertTrue(w.closeness(Cast.RIVAL) >= before);
        var easy = Visits.meet(s.h, s.f, Cast.day(w.day(), 1, 17, false), List.of(Cast.TEAMMATE_B), "drop_in", 19);
        assertTrue(easy.reactions().contains("home.visit.mess.dont_mind"));
    }
    @Test void aSpareKeyIsForCloseFriendsAndIsAMoment() {
        var s = friendsWorld(); var w = s.f.world();
        assertEquals("not_close_enough", Visits.giveKey(s.h, s.f, Cast.TEAMMATE_B, w.day()));
        Cast.befriend(w, Cast.TEAMMATE_B, 6);
        assertEquals("ok", Visits.giveKey(s.h, s.f, Cast.TEAMMATE_B, w.day()));
        assertTrue(w.bond(Cast.TEAMMATE_B).moments().contains(BondFriends.KEY_MOMENT));
        assertEquals("already", Visits.giveKey(s.h, s.f, Cast.TEAMMATE_B, w.day()));
    }
    @Test void whileYouAreOutTheyLeaveANoteOrWaitInside() {
        var s = friendsWorld(); var w = s.f.world();
        Cast.befriend(w, Cast.TEAMMATE_B, 6);
        Visits.giveKey(s.h, s.f, Cast.TEAMMATE_B, w.day());
        var nobodyHome = Cast.day(w.day(), 1, 23, false);
        s.h.mailbox.collect();
        var hours = nobodyHome.atHome().clone();
        var waited = new Visits.Day(w.day(), 0, 1, "", backAt(18), false, Cast.SQUAD, Cast.SENSEI, Cast.INSTRUCTOR, Cast.NEIGHBOURS);
        // Drive the private knock through daily() until both outcomes have happened.
        boolean note = false, inside = false;
        for (int i = 0; i < 400 && !(note && inside); i++) {
            var d = i % 2 == 0 ? nobodyHome : waited;
            var dd = new Visits.Day(w.day() + i, d.season(), d.rank(), d.clan(), d.atHome(), false, d.squad(), d.sensei(), d.instructor(), List.of());
            for (var v : Visits.daily(SEED, s.h, s.f, dd)) {
                if (!v.met() && v.kind().equals("drop_in")) note = true;
                if (v.kind().endsWith(".waited_inside")) inside = true;
            }
        }
        assertTrue(note, "a note in the mailbox"); assertTrue(inside, "a key holder waiting inside");
        assertTrue(s.h.mailbox.peek().stream().anyMatch(l -> l.key().equals("home.note.drop_in")));
        assertNotNull(hours);
    }
    static boolean[] backAt(int hour) { var a = new boolean[24]; for (int h = 0; h < 24; h++) a[h] = h < 8 || h >= hour; return a; }

    @Test void keyHoldersLookAfterThePlaceWhileYouAreAway() {
        var s = friendsWorld(); var w = s.f.world();
        Cast.befriend(w, Cast.CLASSMATE_D, 6);
        Visits.giveKey(s.h, s.f, Cast.CLASSMATE_D, w.day());
        boolean fed = false;
        for (int i = 0; i < 60 && !fed; i++) fed = Visits.daily(SEED, s.h, s.f, Cast.away(w.day() + i, 1)).stream().anyMatch(v -> v.kind().equals("left_food"));
        assertTrue(fed);
        assertFalse(s.h.pantry.empty());
    }
    @Test void hostingDinnerGoesThroughTheBondEngine() {
        var s = friendsWorld(); var w = s.f.world();
        Cast.befriend(w, Cast.TEAMMATE_A, 5);
        String result = "";
        for (int i = 0; i < 30 && !result.startsWith("hosted.home_dinner") || result.contains(".not_") || result.contains(".busy"); i++) {
            var v = Visits.host(s.h, s.f, Cast.day(w.day(), 1, 17, false), List.of(Cast.TEAMMATE_A), "home_dinner", 19);
            result = v.kind();
            w.endDay();
            if (v.met()) break;
        }
        assertEquals("hosted.home_dinner", result);
        assertFalse(w.bond(Cast.TEAMMATE_A).flags().isEmpty() && s.h.mess() == 0, "a dinner leaves dishes");
        var study = Visits.host(s.h, s.f, Cast.day(w.day(), 1, 17, false), List.of(Cast.CLASSMATE_C), "study_night", 19);
        assertTrue(study.met() || study.kind().endsWith(".busy"), study.toString());
    }
}
