package dev.shinobi.life.bond;

import dev.shinobi.life.bond.Personality.Peeve;
import dev.shinobi.life.bond.Personality.Trait;
import dev.shinobi.life.bond.Personality.Value;
import java.util.EnumSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;

/**
 * Everything that can happen between you and someone, with what it does to their {@link Meter}s before their
 * personality has its say ({@link Reaction}). An act the person lives through becomes a {@link Memory}; small and
 * notable memories fade by half every {@code halfLife} days, big ones are permanent. Some acts are shared
 * experiences (counted for the story gates), some are moments (a level gate wants a real one), some are deeds the
 * village talks about ({@code worth}, spread by {@link Gossip}), and some start a quarrel ({@link Conflict}).
 * Professional acts (orders, missions, training) cost trust and respect but never start a quarrel by themselves.
 * Quest data names acts by lower-case id ({@code "camp_night"}).
 */
public enum Act {
    // Talk, gifts and favors go into warmth, not memories (see Bond.warm); listed so data can name them.
    TALK(def(Size.SMALL, 0).warmth(1)),
    GIFT_LOVED(def(Size.SMALL, 30).meters(1, 0.5, 0, 0).warmth(3.5)),
    GIFT_LIKED(def(Size.SMALL, 0).warmth(2)),
    GIFT_PLAIN(def(Size.SMALL, 0).warmth(.6)),
    GIFT_DISLIKED(def(Size.SMALL, 20).meters(-1, 0, 0, 0).warmth(-1)),
    GIFT_HATED(def(Size.SMALL, 30).meters(-3.5, -0.5, 0, 0).peeve(Peeve.RUDENESS)),
    FAVOR(def(Size.SMALL, 0).warmth(.8)),

    // Shared experiences: they count most.
    STUDIED_TOGETHER(def(Size.SMALL, 30).meters(1, 0.5, 0.5, 0).exp(Experience.STUDY).honors(Value.KNOWLEDGE)),
    TRAINED_TOGETHER(def(Size.SMALL, 30).meters(0.5, 0.5, 0.5, 0.5).exp(Experience.TRAINING).honors(Value.STRENGTH)
            .lean(Trait.DISCIPLINE, Meter.RESPECT, 0.5)),
    MEAL_TOGETHER(def(Size.SMALL, 30).meters(2, 0.5, 0, 0).exp(Experience.MEAL).honors(Value.FAMILY)),
    SPAR_WON(def(Size.SMALL, 40).meters(-0.5, 0.5, 3, 3.5).exp(Experience.SPAR).honors(Value.STRENGTH)
            .lean(Trait.PRIDE, Meter.AFFECTION, -2).lean(Trait.PRIDE, Meter.RIVALRY, 3).lean(Trait.PRIDE, Meter.RESPECT, 0.5)),
    SPAR_LOST(def(Size.SMALL, 40).meters(1, 0.5, 0.5, 2).exp(Experience.SPAR)
            .lean(Trait.PRIDE, Meter.RESPECT, -1).lean(Trait.WARMTH, Meter.AFFECTION, 0.5)),
    MISSION_TOGETHER(def(Size.NOTABLE, 60).meters(1.5, 2.5, 1, 0).exp(Experience.MISSION).honors(Value.DUTY)),
    CAMP_NIGHT(def(Size.NOTABLE, 90).meters(3, 2.5, 0, 0).exp(Experience.CAMP).lean(Trait.OPENNESS, Meter.AFFECTION, 1)),
    FESTIVAL_TOGETHER(def(Size.NOTABLE, 90).meters(3, 0.5, 0, 0).romance(4).exp(Experience.FESTIVAL).lean(Trait.OPENNESS, Meter.AFFECTION, 1)),
    HUNG_OUT(def(Size.SMALL, 45).meters(2, 1, 0, 0).exp(Experience.HANGOUT).lean(Trait.OPENNESS, Meter.AFFECTION, 0.5)),
    HIGHLIGHT(def(Size.NOTABLE, 150).meters(2.5, 1.5, 0, 0)),
    SAW_GIFT_DISPLAYED(def(Size.NOTABLE, 120).meters(2.5, 1, 0, 0).lean(Trait.WARMTH, Meter.AFFECTION, 1)),
    VISITED_HOME(def(Size.SMALL, 45).meters(2, 1.5, 0, 0).exp(Experience.HANGOUT).honors(Value.FAMILY).lean(Trait.OPENNESS, Meter.AFFECTION, 0.5)),
    SAW_PHOTO_TOGETHER(def(Size.NOTABLE, 120).meters(2.5, 1, 0, 0).lean(Trait.WARMTH, Meter.AFFECTION, 1)),
    AWKWARD_HANGOUT(def(Size.SMALL, 20).meters(-1, 0, 0, 0)),
    CELEBRATED_WITH_THEM(def(Size.SMALL, 60).meters(2, 1, 0, 0).honors(Value.FAMILY)),
    COMFORTED(def(Size.NOTABLE, 120).meters(3, 4, 0, 0).honors(Value.KINDNESS).lean(Trait.WARMTH, Meter.AFFECTION, 1)),
    ASKED_AFTER_THEM(def(Size.SMALL, 30).meters(1, 1, 0, 0).honors(Value.KINDNESS)),
    ASKED_ADVICE(def(Size.SMALL, 30).meters(1, 1, 0.5, 0).honors(Value.KNOWLEDGE).lean(Trait.PRIDE, Meter.AFFECTION, 1)),
    DATE(def(Size.NOTABLE, 90).meters(2.5, 1, 0, 0).romance(8).exp(Experience.DATE).romantic()),

    // Moments: the story gates want these (bond quests, heart-to-hearts, a life saved, a secret kept).
    BOND_MOMENT(def(Size.BIG, 0).meters(2, 2.5, 0.5, 0).moment()),
    HEART_TO_HEART(def(Size.NOTABLE, 120).meters(2.5, 3, 0, 0).lean(Trait.OPENNESS, Meter.AFFECTION, 1)),
    SAVED_LIFE(def(Size.BIG, 0).meters(9, 11, 5, 0).moment().honors(Value.COURAGE, Value.LOYALTY).deed(20)),
    SAVED_BY_THEM(def(Size.BIG, 0).meters(5, 3.5, 0, 0).moment().lean(Trait.WARMTH, Meter.AFFECTION, 2)),
    KEPT_SECRET(def(Size.BIG, 0).meters(2.5, 8.5, 1, 0).moment().honors(Value.LOYALTY, Value.HONESTY)),
    SUPPORTED_DREAM(def(Size.BIG, 0).meters(3.5, 3, 2, 0).moment()),
    OFFERED_FLAME(def(Size.BIG, 0).meters(3, 4, 1, 0).moment()),
    GAVE_FLAME(def(Size.BIG, 0).meters(4, 3.5, 1, 0).moment()),
    RECONCILED(def(Size.BIG, 0).meters(2.5, 3.5, 0.5, 0).moment()),
    YEARS_TOGETHER(def(Size.BIG, 0).meters(2.5, 3, 1, 0)),

    // Notable good turns.
    PROTECTED_THEM(def(Size.NOTABLE, 120).meters(2.5, 5, 2, 0).honors(Value.LOYALTY, Value.COURAGE).deed(6)),
    STOOD_BY_THEM(def(Size.NOTABLE, 120).meters(2, 3, 0.5, 0).honors(Value.LOYALTY)),
    KEPT_PROMISE(def(Size.NOTABLE, 90).meters(1, 4, 0.5, 0).honors(Value.HONESTY)),
    BIRTHDAY_REMEMBERED(def(Size.NOTABLE, 90).meters(3, 1, 0, 0).honors(Value.FAMILY)),
    MISSION_SUCCESS(def(Size.NOTABLE, 45).meters(0.5, 1, 2, 0).honors(Value.DUTY).lean(Trait.DISCIPLINE, Meter.RESPECT, 0.5)),
    FOLLOWED_ORDERS(def(Size.SMALL, 45).meters(0, 2, 0.5, 0).honors(Value.DUTY).lean(Trait.DISCIPLINE, Meter.TRUST, 1)),
    RANK_UP(def(Size.BIG, 0).meters(0.5, 0, 3.5, 0).deed(8).lean(Trait.PRIDE, Meter.RIVALRY, 2.5)),
    HELPED_RESIDENT(def(Size.SMALL, 60).meters(2, 2, 0.5, 0).honors(Value.KINDNESS).deed(5)),
    DEFENDED_VILLAGE(def(Size.NOTABLE, 120).meters(2.5, 2.5, 3.5, 0).honors(Value.COURAGE, Value.DUTY).deed(12)),
    APOLOGIZED(def(Size.SMALL, 30).meters(1, 1, 0, 0)),
    ANSWERED(def(Size.NOTABLE, 120).meters(0.5, 0.5, 0, 0)),
    STATED(def(Size.SMALL, 30)),
    MEDIATED(def(Size.NOTABLE, 90).meters(2, 3, 2, 0).honors(Value.KINDNESS).deed(4)),
    HONORED_CUSTOM(def(Size.NOTABLE, 90).meters(2, 2, 1.5, 0).honors(Value.FAMILY, Value.DUTY).deed(4)),
    GUEST_IN_QUARTER(def(Size.SMALL, 60).meters(1, 1, 0, 0).deed(1)),

    // Notable wrongs.
    RECKLESS_CHARGE(def(Size.SMALL, 30).professional().meters(0, -2, 1, 0).honors(Value.COURAGE).peeve(Peeve.RECKLESSNESS)
            .lean(Trait.BOLDNESS, Meter.RESPECT, 2).lean(Trait.BOLDNESS, Meter.TRUST, 2)),
    DISOBEYED_ORDERS(def(Size.NOTABLE, 45).professional().meters(-0.5, -3.5, -0.5, 0).violates(Value.DUTY).peeve(Peeve.RECKLESSNESS)
            .lean(Trait.BOLDNESS, Meter.RESPECT, 2).lean(Trait.DISCIPLINE, Meter.TRUST, -2)),
    MISSION_FAILED(def(Size.NOTABLE, 30).professional().meters(-0.5, -1, -1, 0).violates(Value.DUTY)),
    BRAGGED(def(Size.SMALL, 20).meters(-1, 0, -0.5, 1).peeve(Peeve.BRAGGING).lean(Trait.PRIDE, Meter.RIVALRY, 2)),
    RUDE(def(Size.SMALL, 20).meters(-2.5, -0.5, 0, 0).peeve(Peeve.RUDENESS).lean(Trait.WARMTH, Meter.AFFECTION, -0.5)),
    SKIPPED_TRAINING(def(Size.SMALL, 20).professional().meters(-0.5, -0.5, -1, 0).violates(Value.DUTY).peeve(Peeve.LAZINESS)),
    PRIED(def(Size.SMALL, 30).meters(-2, -2, 0, 0).peeve(Peeve.NOSINESS).lean(Trait.OPENNESS, Meter.AFFECTION, 1)),
    MISSED_BIRTHDAY(def(Size.NOTABLE, 30).meters(-2.5, -0.5, 0, 0).peeve(Peeve.NEGLECT).violates(Value.FAMILY)),
    FELT_OVERLOOKED(def(Size.SMALL, 30).meters(-2, -0.5, 0, 1).peeve(Peeve.NEGLECT).lean(Trait.PRIDE, Meter.RIVALRY, 2)),
    STOOD_UP(def(Size.NOTABLE, 60).meters(-3, -5, 0, 0).violates(Value.HONESTY).peeve(Peeve.LATENESS)),
    CAUGHT_CONTRADICTION(def(Size.SMALL, 60).meters(-0.5, -1.5, 0, 0).violates(Value.HONESTY).peeve(Peeve.DISHONESTY)),
    BROKE_PROMISE(def(Size.NOTABLE, 60).meters(-2.5, -6, -0.5, 0).violates(Value.HONESTY).peeve(Peeve.LATENESS)),
    WENT_OVER_THEIR_HEAD(def(Size.NOTABLE, 60).meters(-2, -5, 0, 0.5).violates(Value.LOYALTY).lean(Trait.DISCIPLINE, Meter.TRUST, 2.5)),
    SIDED_AGAINST(def(Size.NOTABLE, 60).meters(-3, -3, 0, 1).violates(Value.LOYALTY)),
    INSULTED_CLAN(def(Size.NOTABLE, 60).meters(-5, -3, -1, 0).violates(Value.FAMILY).peeve(Peeve.RUDENESS).deed(-8)),
    FAILED_CLIENT(def(Size.NOTABLE, 60).professional().meters(-2, -3, -1, 0).violates(Value.DUTY).deed(-4)),
    HURT_RESIDENT(def(Size.NOTABLE, 60).meters(-7, -7, -1, 0).violates(Value.KINDNESS).peeve(Peeve.CRUELTY).deed(-15)),
    QUARREL(def(Size.NOTABLE, 45).meters(-6, -2.5, 0, 2).quarrel().spreads().lean(Trait.PRIDE, Meter.AFFECTION, -2)),

    // Big wrongs: permanent, and most start a quarrel.
    MOCKED_DREAM(def(Size.BIG, 0).meters(-6, -3.5, 0, 2).quarrel().peeve(Peeve.RUDENESS)),
    BROKE_SECRET(def(Size.BIG, 0).meters(-7, -18, -1, 0).quarrel().violates(Value.LOYALTY, Value.HONESTY).peeve(Peeve.DISHONESTY)),
    ABANDONED_MISSION(def(Size.BIG, 0).meters(-3.5, -12, -6, 0).violates(Value.DUTY, Value.LOYALTY).peeve(Peeve.COWARDICE).deed(-15)),
    LEFT_THEM_BEHIND(def(Size.BIG, 0).meters(-8.5, -17, -3.5, 0).quarrel().violates(Value.LOYALTY).peeve(Peeve.COWARDICE).deed(-10)),

    // Romance and family: teen stage and up only (Courtship).
    CONFESSION_ACCEPTED(def(Size.BIG, 0).meters(3.5, 2.5, 0, 0).romance(15).moment().romantic()),
    PROPOSAL_ACCEPTED(def(Size.BIG, 0).meters(3.5, 3.5, 0, 0).romance(10).moment().romantic()),
    WEDDING(def(Size.BIG, 0).meters(6, 6, 1, 0).romance(10).moment().romantic().deed(10)),
    CHILD_BORN(def(Size.BIG, 0).meters(6, 3.5, 0, 0).romance(4).moment().deed(6));

    public enum Size { SMALL, NOTABLE, BIG }
    /** The kinds of shared experience the gates count. */
    public enum Experience { STUDY, TRAINING, MEAL, SPAR, MISSION, CAMP, FESTIVAL, DATE, HANGOUT }
    public record Lean(Trait trait, Meter meter, double amount) {}

    public final Size size;
    /** Days for a memory of it to fade by half; 0 for a permanent memory. */
    public final int halfLife;
    public final Meters base;
    public final double warmth;
    public final Experience experience;
    public final boolean moment, quarrel, romantic, spreads, professional;
    /** Standing it is worth to the communities that hear of it; 0 for a private act. */
    public final int worth;
    public final Set<Value> honors, violates;
    public final Peeve peeve;
    public final List<Lean> leans;

    Act(Def d) {
        size = d.size; halfLife = d.size == Size.BIG ? 0 : d.halfLife; base = d.base; warmth = d.warmth; experience = d.exp;
        moment = d.moment; quarrel = d.quarrel; romantic = d.romantic; professional = d.professional; worth = d.worth; spreads = d.spreads || d.worth != 0;
        honors = Set.copyOf(d.honors); violates = Set.copyOf(d.violates); peeve = d.peeve; leans = List.copyOf(d.leans);
    }
    public String id() { return name().toLowerCase(Locale.ROOT); }
    public static Act of(String id) { return valueOf(id.toUpperCase(Locale.ROOT)); }
    public boolean permanent() { return halfLife == 0 && size == Size.BIG; }
    /** Talk, gifts and favors: they add warmth rather than a memory of their own. */
    public boolean warms() { return warmth != 0; }
    public boolean remembered() { return !base.isZero(); }

    private static Def def(Size size, int halfLife) { return new Def(size, halfLife); }
    private static final class Def {
        final Size size; final int halfLife; Meters base = Meters.ZERO; double warmth; Experience exp; boolean moment, quarrel, romantic, spreads, professional;
        int worth; final EnumSet<Value> honors = EnumSet.noneOf(Value.class), violates = EnumSet.noneOf(Value.class);
        Peeve peeve; final java.util.ArrayList<Lean> leans = new java.util.ArrayList<>();
        Def(Size size, int halfLife) { this.size = size; this.halfLife = halfLife; }
        Def meters(double a, double t, double r, double v) { base = new Meters(a, t, r, v, base.romance()); return this; }
        Def romance(double r) { base = base.with(Meter.ROMANCE, r); return this; }
        Def warmth(double w) { warmth = w; return this; }
        Def exp(Experience e) { exp = e; return this; }
        Def moment() { moment = true; return this; }
        Def quarrel() { quarrel = true; return this; }
        Def professional() { professional = true; return this; }
        Def romantic() { romantic = true; return this; }
        Def spreads() { spreads = true; return this; }
        Def deed(int w) { worth = w; return this; }
        Def honors(Value... v) { honors.addAll(List.of(v)); return this; }
        Def violates(Value... v) { violates.addAll(List.of(v)); return this; }
        Def peeve(Peeve p) { peeve = p; return this; }
        Def lean(Trait t, Meter m, double amount) { leans.add(new Lean(t, m, amount)); return this; }
    }
}
