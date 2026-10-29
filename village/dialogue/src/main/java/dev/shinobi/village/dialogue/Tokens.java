package dev.shinobi.village.dialogue;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Fills a line's tokens: {@code {player}} and its forms, {@code {name:<ref>}}, {@code {given:<ref>}},
 * {@code {family:<ref>}}, {@code {hokage:<n>}}, pronouns {@code {they:<ref>}}..., {@code {twist:<slot>}}, and
 * situational values from the context ({@code {item}}, {@code {place}}, {@code {friend}}...). Returns null when a
 * token has no value here, so the selector moves on to a line it can say.
 */
public final class Tokens {
    private static final Pattern TOKEN = Pattern.compile("\\{([a-z_]+)(?::([^{}]+))?}");

    public static String fill(String text, Context c, Names names) {
        if (text == null) return null;
        Matcher m = TOKEN.matcher(text);
        var out = new StringBuilder();
        while (m.find()) {
            String value = value(m.group(1), m.group(2), c, names);
            if (value == null || value.isBlank()) return null;
            m.appendReplacement(out, Matcher.quoteReplacement(value));
        }
        m.appendTail(out);
        String s = out.toString();
        return s.isEmpty() ? s : Character.toUpperCase(s.charAt(0)) + s.substring(1);
    }

    private static String value(String token, String arg, Context c, Names names) {
        if (arg != null) return switch (token) {
            case "name", "given", "family" -> names.name(arg, token);
            case "they", "them", "their", "theirs" -> names.pronoun(arg, token);
            case "twist" -> names.name("twist:" + arg, "name");
            case "hokage" -> { try { yield names.hokage(Integer.parseInt(arg)); } catch (NumberFormatException e) { yield null; } }
            default -> null;
        };
        return switch (token) {
            case "player" -> names.player("given");
            case "player_family" -> names.player("family");
            case "player_full" -> names.player("full");
            case "player_rank" -> names.player("rank");
            case "player_clan" -> names.player("clan");
            default -> c.filled(token);
        };
    }

    private Tokens() {}
}
