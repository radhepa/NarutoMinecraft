package dev.shinobi.life.bond;

import dev.shinobi.life.bond.Personality.Peeve;
import dev.shinobi.life.bond.Personality.Trait;
import dev.shinobi.life.bond.Personality.Value;
import java.util.List;
import java.util.Locale;
import java.util.Set;

/**
 * What an answer says about the player, as the asker hears it. Each tag has an effect (affection / trust / respect /
 * rivalry), values it honors or violates, maybe a pet peeve, and leans on the asker's traits, resolved like an act
 * ({@link Reaction}): a blunt answer earns trust and costs warmth, more so with the warm and the proud; an ambitious
 * one impresses the proud; a playful one charms the open and grates on the disciplined.
 */
public enum AnswerTag {
    KIND(Meters.of(2, 1, 0, 0), Set.of(Value.KINDNESS), Set.of(), null, List.of(new Act.Lean(Trait.WARMTH, Meter.AFFECTION, 1))),
    BLUNT(Meters.of(-1.5, 2, 1, 0), Set.of(Value.HONESTY), Set.of(), null,
            List.of(new Act.Lean(Trait.WARMTH, Meter.AFFECTION, -1), new Act.Lean(Trait.PRIDE, Meter.AFFECTION, -1))),
    HONEST(Meters.of(0.5, 2, 0.5, 0), Set.of(Value.HONESTY), Set.of(), null, List.of()),
    LOYAL(Meters.of(1.5, 2, 0, 0), Set.of(Value.LOYALTY, Value.FAMILY), Set.of(), null, List.of()),
    AMBITIOUS(Meters.of(0, 0, 2, 1), Set.of(Value.STRENGTH, Value.COURAGE), Set.of(), null,
            List.of(new Act.Lean(Trait.PRIDE, Meter.RIVALRY, 1.5), new Act.Lean(Trait.PRIDE, Meter.AFFECTION, 1))),
    PLAYFUL(Meters.of(1.5, 0, -0.5, 0), Set.of(Value.FREEDOM), Set.of(), null,
            List.of(new Act.Lean(Trait.DISCIPLINE, Meter.AFFECTION, -1.5), new Act.Lean(Trait.OPENNESS, Meter.AFFECTION, 1))),
    CAUTIOUS(Meters.of(0, 1.5, -0.5, 0), Set.of(Value.DUTY), Set.of(), null, List.of(new Act.Lean(Trait.BOLDNESS, Meter.RESPECT, -2))),
    BOLD(Meters.of(0.5, -0.5, 1.5, 0.5), Set.of(Value.COURAGE), Set.of(), null,
            List.of(new Act.Lean(Trait.BOLDNESS, Meter.RESPECT, 1.5), new Act.Lean(Trait.DISCIPLINE, Meter.TRUST, -1))),
    HUMBLE(Meters.of(1, 0.5, 0.5, -0.5), Set.of(Value.KINDNESS), Set.of(), null, List.of(new Act.Lean(Trait.PRIDE, Meter.RESPECT, -1))),
    PROUD(Meters.of(-0.5, 0, 1, 1), Set.of(Value.STRENGTH), Set.of(), Peeve.BRAGGING,
            List.of(new Act.Lean(Trait.PRIDE, Meter.AFFECTION, 1), new Act.Lean(Trait.WARMTH, Meter.AFFECTION, -1))),
    DUTIFUL(Meters.of(0, 1.5, 1, 0), Set.of(Value.DUTY), Set.of(Value.FREEDOM), null, List.of(new Act.Lean(Trait.DISCIPLINE, Meter.TRUST, 1.5))),
    FREE(Meters.of(1, 0, 0, 0), Set.of(Value.FREEDOM, Value.CREATIVITY), Set.of(Value.DUTY), null, List.of()),
    EVASIVE(Meters.of(-1, -1.5, 0, 0), Set.of(), Set.of(Value.HONESTY), null, List.of(new Act.Lean(Trait.OPENNESS, Meter.AFFECTION, -1))),
    RUDE(Meters.of(-3, -1, 0, 0), Set.of(), Set.of(Value.KINDNESS), Peeve.RUDENESS, List.of()),
    CURIOUS(Meters.of(1, 0.5, 0, 0), Set.of(Value.KNOWLEDGE), Set.of(), null, List.of(new Act.Lean(Trait.OPENNESS, Meter.AFFECTION, 0.5))),
    FAMILY(Meters.of(1, 1, 0, 0), Set.of(Value.FAMILY), Set.of(), null, List.of());

    public final Meters base;
    public final Set<Value> honors, violates;
    public final Peeve peeve;
    public final List<Act.Lean> leans;
    AnswerTag(Meters base, Set<Value> honors, Set<Value> violates, Peeve peeve, List<Act.Lean> leans) {
        this.base = base; this.honors = honors; this.violates = violates; this.peeve = peeve; this.leans = leans;
    }
    public String id() { return name().toLowerCase(Locale.ROOT); }
    public static AnswerTag of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
    public Meters react(Personality p) { return Reaction.react(p, base, leans, honors, violates, peeve); }
}
