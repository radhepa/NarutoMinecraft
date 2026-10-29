package dev.shinobi.life.bond;

import java.util.List;
import java.util.Map;

/**
 * The player's family in the post-game: a married player can have children. A child is a VF resident born into
 * the household (VF records parents, households and surnames); here they are a {@link Person} whose personality
 * takes after the spouse, rolled from the save seed, and whose bond starts where VF's families start. Rules:
 * married, both adults, the post-game flag set, and at least {@link #SPACING} days since the last child.
 */
public final class Household {
    public static final String POSTGAME_FLAG = "story.postgame";
    public static final int SPACING = 112;

    /** "" when a child can be born now, else why not. */
    public static String refuse(BondWorld w, long lastChildDay) {
        String spouse = w.spouse();
        if (spouse.isEmpty()) return "not_married";
        if (!w.flag(POSTGAME_FLAG)) return "not_postgame";
        if (w.playerStage() != Person.Stage.ADULT || w.person(spouse).stage() != Person.Stage.ADULT) return "not_adults";
        if (lastChildDay >= 0 && w.day() - lastChildDay < SPACING) return "too_soon";
        return "";
    }
    /** The child: the spouse's archetype, traits halfway between the spouse's and the archetype's own, a birthday today. */
    public static Person child(BondWorld w, String id, String gender) {
        var spouse = w.person(w.spouse());
        var rng = Seeds.stream(w.seed(), "household", id);
        var sp = spouse.personality();
        var own = Personality.rolled(sp.archetype(), rng, .3);
        var mixed = own.withTraits((own.warmth() + sp.warmth()) / 2, (own.boldness() + sp.boldness()) / 2, (own.pride() + sp.pride()) / 2,
                (own.discipline() + sp.discipline()) / 2, (own.openness() + sp.openness()) / 2);
        return new Person(id, w.playerClan().isEmpty() ? spouse.clan() : w.playerClan(), spouse.district(), Person.CIVILIAN,
                Person.Stage.CHILD, mixed, gender, "NONE", BondWorld.dayOfYear(w.day()),
                Map.of(BondWorld.PLAYER, "parent", spouse.id(), "parent"), List.of("household:" + spouse.id()));
    }
    /** Born: added to the world, the household's child, with a first big memory. */
    public static Person born(BondWorld w, String id, String gender) {
        var kid = child(w, id, gender);
        w.add(kid);
        w.act(w.spouse(), Act.CHILD_BORN);
        w.bond(id).meet(w.day());
        return kid;
    }

    private Household() {}
}
