package dev.shinobi.village;

import dev.villagefriends.home.House;
import dev.villagefriends.home.HousingIndex;
import dev.villagefriends.social.Townsfolk;
import net.minecraft.core.BlockPos;

import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

/**
 * Leaf flats are plaqued houses, which VF fills in its own order: a resident placed in one would get a flat on
 * another floor it cannot path to. A resident already sleeping in a free bed of a Leaf flat keeps it (AssignmentsMixin).
 */
public final class LeafFlats {
    /** The plaque name that marks a Leaf flat; VF keeps it as the house's custom name. */
    public static final String NAME = "Flat ";

    private LeafFlats() {}

    /** {@code previous} with each resident at home who sleeps in a free Leaf flat bed ({@code anchors}: VF's id to bed head) holding it. */
    public static HousingIndex seed(HousingIndex previous, Collection<Townsfolk> folk, Map<String, BlockPos> anchors) {
        var beds = new HashMap<>(previous.beds());
        var taken = new HashSet<BlockPos>();
        for (var key : beds.values()) taken.add(key.head());
        for (var t : folk) {
            var head = anchors.get(t.id());
            if (!t.home() || head == null || beds.containsKey(t.id()) || taken.contains(head)) continue;
            for (var h : previous.houses()) {
                var bed = h.bed(head);
                if (h.kind() == House.Kind.PLAYER && h.customName().startsWith(NAME) && !h.privateHome() && bed != null && bed.present()) {
                    beds.put(t.id(), new HousingIndex.BedKey(h.id(), head));
                    taken.add(head);
                    break;
                }
            }
        }
        return new HousingIndex(previous.village(), previous.houses(), beds, previous.homeless(), previous.needs(), previous.vacated(),
                previous.moved(), previous.cursed(), previous.stamp(), previous.surveyed());
    }
}
