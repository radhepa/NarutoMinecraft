package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;

/**
 * A question a resident can ask the player, as the dialogue data writes it (one JSON object; the engine reads it
 * parsed into maps, {@link #parse}). See BONDS.md, "Questions and choices".
 *
 * <pre>
 * {"format": 1, "id": "q.dilemma.found_wallet", "kind": "dilemma", "level": 3, "depth": 1,
 *  "follow_up_of": "", "min_gap_days": 0, "about": "value:honesty", "public": false,
 *  "audience": {"archetypes": [], "values": [], "roles": [], "min_stage": "child", "clan": ""},
 *  "answers": [{"id": "return_it", "tags": ["honest", "kind"], "stance": "honest",
 *               "sets": "", "nudge": {"trait": "", "amount": 0}, "deed": ""}]}
 * </pre>
 */
public record Question(String id, Kind kind, int level, int depth, String followUpOf, int minGapDays, String about, boolean isPublic,
        Set<String> archetypes, Set<Personality.Value> values, Set<String> roles, Person.Stage minStage, String clan, List<Answer> answers) {

    public enum Kind {
        OPINION, DILEMMA, ADVICE, PREFERENCE, PLAYER_PAST, PLAYER_PLANS, CONFESSION;
        public String id() { return name().toLowerCase(Locale.ROOT); }
        public static Kind of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
        /** How much a kind of question weighs: confessions and dilemmas are heavier than a preference. */
        public double weight() {
            return switch (this) { case CONFESSION -> 1.3; case DILEMMA, ADVICE -> 1.15; case PREFERENCE -> .7; default -> 1; };
        }
    }
    /** One answer: what it says about the player (tags), where it stands on the question's axis, and what it can change. */
    public record Answer(String id, List<AnswerTag> tags, String stance, String sets, Personality.Trait nudgeTrait, double nudge, Act deed) {}

    public Question {
        answers = List.copyOf(answers); archetypes = Set.copyOf(archetypes); values = Set.copyOf(values); roles = Set.copyOf(roles);
        followUpOf = followUpOf == null ? "" : followUpOf; about = about == null ? "" : about; clan = clan == null ? "" : clan;
        if (answers.size() < 2 || answers.size() > 4) throw new IllegalArgumentException(id + ": a question has 2 to 4 answers");
    }
    public Answer answer(String answerId) {
        return answers.stream().filter(a -> a.id().equals(answerId)).findFirst().orElseThrow(() -> new IllegalArgumentException(id + " has no answer " + answerId));
    }
    /** Whether this question suits someone: their personality, values, role, stage and clan. */
    public boolean suits(Person p) {
        if (!archetypes.isEmpty() && !archetypes.contains(p.personality().archetype())) return false;
        if (!values.isEmpty() && values.stream().noneMatch(p.personality()::holds)) return false;
        if (!roles.isEmpty() && !roles.contains(p.id())) return false;
        if (!clan.isEmpty() && !clan.equals(p.clan())) return false;
        return p.stage().compareTo(minStage) >= 0;
    }

    @SuppressWarnings("unchecked")
    public static Question parse(Map<String, Object> m) {
        var aud = (Map<String, Object>) m.getOrDefault("audience", Map.of());
        var answers = new ArrayList<Answer>();
        for (Object o : (List<Object>) m.get("answers")) {
            var a = (Map<String, Object>) o;
            var tags = ((List<Object>) a.getOrDefault("tags", List.of())).stream().map(t -> AnswerTag.of((String) t)).toList();
            var nudge = (Map<String, Object>) a.getOrDefault("nudge", Map.of());
            String trait = (String) nudge.getOrDefault("trait", "");
            String deed = (String) a.getOrDefault("deed", "");
            answers.add(new Answer((String) a.get("id"), tags, (String) a.getOrDefault("stance", a.get("id")), (String) a.getOrDefault("sets", ""),
                    trait.isEmpty() ? null : Personality.Trait.valueOf(trait.toUpperCase(Locale.ROOT)),
                    Math.clamp(SaveFormat.dbl(nudge.getOrDefault("amount", 0)), -.1, .1), deed.isEmpty() ? null : Act.of(deed)));
        }
        return new Question((String) m.get("id"), Kind.of((String) m.get("kind")), (int) SaveFormat.lng(m.getOrDefault("level", 0)),
                (int) SaveFormat.lng(m.getOrDefault("depth", 1)), (String) m.getOrDefault("follow_up_of", ""), (int) SaveFormat.lng(m.getOrDefault("min_gap_days", 0)),
                (String) m.getOrDefault("about", ""), Boolean.TRUE.equals(m.get("public")),
                Set.copyOf((List<String>) aud.getOrDefault("archetypes", List.of())),
                Set.copyOf(((List<String>) aud.getOrDefault("values", List.of())).stream().map(v -> Personality.Value.valueOf(v.toUpperCase(Locale.ROOT))).toList()),
                Set.copyOf((List<String>) aud.getOrDefault("roles", List.of())),
                Person.Stage.valueOf(((String) aud.getOrDefault("min_stage", "child")).toUpperCase(Locale.ROOT)), (String) aud.getOrDefault("clan", ""), answers);
    }
}
