package dev.shinobi.life.bond;

import static dev.shinobi.life.bond.Leaf.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class SaveFormatTest {
    static BondWorld lived(long seed) {
        var w = Leaf.classic(seed, 12);
        w.formSquad("squad:7", SENSEI, TEAMMATES, List.of(CLASSMATE_C));
        for (int d = 0; d < 30; d++) {
            w.talk(TEAMMATE_A); w.gift(TEAMMATE_B, "food:ramen"); w.favor(TEAMMATE_A, 2);
            w.experience(Act.MISSION_TOGETHER, w.squad().members());
            if (d == 5) w.act(TEAMMATE_B, Act.SAVED_LIFE, List.of(TEAMMATE_A, SENSEI));
            if (d == 9) w.quarrel(RIVAL, Act.QUARREL);
            if (d == 12) w.moment(TEAMMATE_A, "bond.teammate_a.1");
            w.endDay();
        }
        w.setFlag(Kindling.UNLOCK_FLAG, true);
        w.reveal(RIVAL, "dream");
        return w;
    }
    static String snapshot(BondWorld w) {
        var sb = new StringBuilder();
        for (var b : w.bonds()) sb.append(b.from()).append('>').append(b.to()).append(' ').append(w.meters(b.from(), b.to())).append(" L").append(b.level())
                .append(' ').append(b.conflict()).append(' ').append(b.memories().size()).append(' ').append(b.moments()).append('\n');
        sb.append(w.squad().teammates()).append(w.squad().attention(TEAMMATE_A)).append(w.cohesion()).append(w.flags()).append(w.deeds().size());
        return sb.toString();
    }

    @Test void aSaveRoundTripsExactlyAndPlaysOnTheSame() {
        var w = lived(77);
        var saved = SaveFormat.write(w);
        assertEquals(SaveFormat.FORMAT, saved.get("format"));
        var back = SaveFormat.read(saved, 77, new ArrayList<>(w.people()));
        assertEquals(snapshot(w), snapshot(back));
        w.advance(20); back.advance(20);
        assertEquals(snapshot(w), snapshot(back), "and the future plays out the same");
    }
    @Test void theSameSeedAndActsGiveTheSameSave() {
        assertEquals(SaveFormat.write(lived(5)).toString(), SaveFormat.write(lived(5)).toString());
        assertNotEquals(snapshot(lived(5)), snapshot(lived(6)), "another seed, another village");
    }
    @Test void peopleGoneFromThePackAreSkippedAndNewerFormatsRefused() {
        var w = lived(77);
        var people = new ArrayList<>(w.people());
        people.removeIf(p -> p.id().equals(RIVAL));
        var back = SaveFormat.read(SaveFormat.write(w), 77, people);
        assertTrue(back.bonds().stream().noneMatch(b -> b.from().equals(RIVAL)));
        var future = new java.util.LinkedHashMap<>(SaveFormat.write(w));
        future.put("format", SaveFormat.FORMAT + 1);
        var e = assertThrows(IllegalStateException.class, () -> SaveFormat.read(future, 77, people));
        assertTrue(e.getMessage().contains("newer"));
    }
    @Test void villageFriendsFriendshipsCarryOver() {
        Map<String, Object> vf = Map.of("format", 0, "day", 40, "friendships", Map.of(
                COOK, Map.of("points", 120, "trust", 70, "level", 7),
                MERCHANT, Map.of("points", 10)));
        var w = SaveFormat.read(vf, 1, new ArrayList<>(Leaf.classic(1, 0).people()));
        assertEquals(7, w.level(COOK), "nobody loses a level they earned");
        assertTrue(w.meters(COOK).trust() > w.meters(MERCHANT).trust());
        assertTrue(w.bond(COOK).warmth() > w.bond(MERCHANT).warmth());
        assertEquals(40, w.day());
        w.advance(3);
        assertEquals(7, w.level(COOK), "and it holds");
    }
}
