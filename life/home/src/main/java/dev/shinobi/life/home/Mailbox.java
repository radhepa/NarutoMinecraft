package dev.shinobi.life.home;

import java.util.ArrayList;
import java.util.List;

/**
 * The mailbox by the door, checked each morning. Letters are dialogue keys with who sent them: the stipend envelope
 * (Academy years), notes from friends who dropped by while you were out, invitations slipped under the door (the bond
 * engine's), clan summons, the landlady's notes, gifts, and story letters by hook id. The world glue turns a letter
 * into VF's Sealed Letter item when you take it out.
 */
public final class Mailbox {
    public enum Kind { STIPEND, NOTE, INVITATION, CLAN_SUMMONS, GIFT, LANDLADY, NEIGHBOUR, STORY }
    public record Letter(Kind kind, String from, long day, String key, String attachment) {}
    public static final int HOLDS = 12;

    private final List<Letter> letters = new ArrayList<>();
    private int dropped;

    /** Posts a letter; a full mailbox keeps the newest twelve (old notes fall behind the box, nothing important). */
    public void post(Kind kind, String from, long day, String key, String attachment) {
        letters.add(new Letter(kind, from, day, key, attachment == null ? "" : attachment));
        while (letters.size() > HOLDS) {
            var oldest = letters.stream().filter(l -> l.kind() == Kind.NOTE || l.kind() == Kind.NEIGHBOUR).findFirst().orElse(letters.getFirst());
            letters.remove(oldest); dropped++;
        }
    }
    public List<Letter> peek() { return List.copyOf(letters); }
    /** Takes everything out: the morning check. */
    public List<Letter> collect() { var out = List.copyOf(letters); letters.clear(); return out; }
    public int size() { return letters.size(); }
    public int dropped() { return dropped; }
}
