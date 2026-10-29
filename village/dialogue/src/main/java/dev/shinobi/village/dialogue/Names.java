package dev.shinobi.village.dialogue;

import java.util.Map;

/**
 * Where names come from: text never holds a name, only tokens (ROADMAP.md, "Names rolled per save"). Shinobi Village
 * implements this from the save's bound cast and rolled names; tests use {@link #of}. A null answer means the token
 * cannot be filled here, and a line that needs it is skipped.
 */
public interface Names {
    /** The player: {@code given}, {@code family}, {@code full}, {@code rank} (a title) or {@code clan} (display name). */
    String player(String form);
    /** Someone by reference ({@code role:sensei}, {@code resident:41}, {@code twist:<slot>}): {@code name}, {@code given} or {@code family}. */
    String name(String ref, String form);
    /** Their pronoun ({@code they}, {@code them}, {@code their}, {@code theirs}), from how they are recorded. */
    String pronoun(String ref, String form);
    /** The given name of the Nth Hokage (rolled per save). */
    String hokage(int n);

    /**
     * Names from a flat map: {@code player.given}, {@code role:sensei.name}, {@code role:sensei.they}, {@code hokage.4}...
     * Pronouns default to they/them/their/theirs.
     */
    static Names of(Map<String, String> m) {
        return new Names() {
            public String player(String form) { return m.get("player." + form); }
            public String name(String ref, String form) { return m.get(ref + "." + form); }
            public String pronoun(String ref, String form) {
                String v = m.get(ref + "." + form);
                return v != null ? v : form;
            }
            public String hokage(int n) { return m.get("hokage." + n); }
        };
    }
}
