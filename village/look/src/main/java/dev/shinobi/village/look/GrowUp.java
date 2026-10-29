package dev.shinobi.village.look;

import java.util.ArrayList;

/**
 * Carrying a look into the next age stage at a time skip. Hair grows into the suggested style (the Years Later
 * mirror preselects it and the player may pick again); an outfit that the new stage no longer offers becomes the
 * stage's first outfit of the player's current rank, keeping the palette when it can; marks the new stage opens
 * stay as they are; nothing locked changes.
 */
public final class GrowUp {
    private final CreatorRules rules;

    public GrowUp(CreatorRules rules) { this.rules = rules; }

    /** The hairstyle a style grows into at a stage, or the same style. */
    public String hairAt(String hair, AgeStage stage) {
        var row = CreatorRules.map(CreatorRules.map(rules.data.get("grows_into")).get(hair));
        if (row == null) return hair;
        Object to = row.get(stage.id());
        if (to == null && stage == AgeStage.ADULT) to = row.get(AgeStage.TEEN.id());
        return to == null ? hair : (String) to;
    }

    /** The look carried to {@code to}, for a player of {@code rank} (academy, genin, chunin...). */
    public Look grow(Look look, String origin, AgeStage to, String rank) {
        var c = rules.choices(origin, to);
        String hair = hairAt(look.hair(), to);
        if (!c.hair().contains(hair)) hair = look.hair();
        var next = look.withHair(hair);
        var outfit = c.outfit(look.body(), look.outfit());
        if (outfit == null) {
            var options = c.outfits().get(look.body());
            var pick = options.stream().filter(o -> o.rank().equals(rank)).findFirst().orElse(options.get(0));
            next = next.withOutfit(pick.id(), pick.palettes().contains(look.palette()) ? look.palette() : pick.palettes().get(0));
        }
        var marks = new ArrayList<>(next.marks());
        marks.removeIf(m -> !c.marks().contains(m));
        next = next.withMarks(marks);
        if (!c.headwear().contains(next.headwear())) next = next.withHeadwear(null);
        return next;
    }
}
