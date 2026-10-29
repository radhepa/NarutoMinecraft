package dev.shinobi.life.roster;

import java.util.ArrayList;
import java.util.List;

/**
 * A technique someone learns where the player can see it: at a story beat ({@code beat}, e.g. {@code ch12.natures})
 * or in training with the player ({@link #TRAINING}), once they reach {@code minLevel}. A technique whose beat
 * passed before they were ready, or passed while they were away on their own squad, shows at the next beat or
 * training where the player sees them: never off-screen. The
 * ids are placeholders the combat kits bind ({@code niche.genjutsu.1} is that peer's first genjutsu).
 */
public record Technique(String id, int minLevel, String beat) {
    public static final String TRAINING = "training";

    /** The usual kit of a classmate: the Academy three, their niche, a nature, a clan technique, the exam reward, and the later arcs. */
    public static List<Technique> kit(Niche niche, String clan) {
        var k = new ArrayList<Technique>();
        k.add(new Technique("academy.clone", 1, "ch6.exam_eve"));
        k.add(new Technique("academy.transformation", 2, "ch6.exam_eve"));
        k.add(new Technique("academy.substitution", 3, "ch7.graduation"));
        k.add(new Technique("niche." + niche.id() + ".1", 8, TRAINING));
        k.add(new Technique("nature.first", 10, "ch12.natures"));
        if (clan != null && !clan.isEmpty()) k.add(new Technique("clan." + clan + ".1", 11, "ch12.natures"));
        k.add(new Technique("niche." + niche.id() + ".2", 14, TRAINING));
        k.add(new Technique("exam.reward", 16, "ch18.training_break"));
        k.add(new Technique("niche." + niche.id() + ".3", 22, "arc.chunin"));
        k.add(new Technique("nature.second", 26, "arc.chunin.natures"));
        if (clan != null && !clan.isEmpty()) k.add(new Technique("clan." + clan + ".2", 28, TRAINING));
        k.add(new Technique("niche." + niche.id() + ".4", 34, "arc.jonin"));
        k.add(new Technique("nature.third", 38, "arc.jonin.natures"));
        k.add(new Technique("signature", 44, "arc.road"));
        return k;
    }
}
