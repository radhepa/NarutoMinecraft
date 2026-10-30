package dev.shinobi.village;

import dev.villagefriends.home.House;
import dev.villagefriends.home.HousingIndex;
import dev.villagefriends.social.Townsfolk;
import net.minecraft.core.BlockPos;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Leaf flats and shops are plaqued houses, which VF fills in its own order: a resident placed in one would get a
 * flat on another floor it cannot path to. A resident already sleeping in a free bed of a Leaf house keeps it (AssignmentsMixin),
 * and a map resident gets back the bed it was placed beside even if VF handed out beds before it noted that bed.
 */
public final class LeafFlats {
    /** The plaque name that marks a Leaf flat; VF keeps it as the house's custom name. */
    public static final String NAME = "Flat ", TEA_HOUSE = "Tea House";

    /** The bed head each map resident was placed beside (VF's id), noted by TestStreet until a hand-out gives it to them. */
    // shortcut: kept in memory only, so a restart before the first hand-out falls back to VF's anchors; persist it if that bites.
    static final Map<String, BlockPos> CLAIMS = new ConcurrentHashMap<>();

    private LeafFlats() {}

    /** Whether a plaque name marks a Leaf house: a flat, or a plot of the map's layout. */
    static boolean leaf(String name) { return name.startsWith(NAME) || name.equals(TEA_HOUSE) || Layout.leaf().names().contains(name); }

    /** {@code previous} with each resident at home who claims or sleeps in a free Leaf house bed ({@code anchors}: VF's id to bed head) holding it. */
    public static HousingIndex seed(HousingIndex previous, Collection<Townsfolk> folk, Map<String, BlockPos> anchors) {
        var beds = new HashMap<>(previous.beds());
        var holder = new HashMap<BlockPos, String>();
        for (var e : beds.entrySet()) holder.put(e.getValue().head(), e.getKey());
        for (var t : folk) {
            var claim = CLAIMS.get(t.id());
            var head = claim != null ? claim : anchors.get(t.id());
            if (!t.home() || head == null || claim == null && beds.containsKey(t.id())) continue;
            // A claimed bed is taken back once from anyone who does not claim it themselves; the claim is then spent, so VF may move them on.
            var held = holder.get(head);
            if (t.id().equals(held)) { CLAIMS.remove(t.id()); continue; }
            if (held != null && (claim == null || head.equals(CLAIMS.get(held)))) continue;
            for (var h : previous.houses()) {
                var bed = h.bed(head);
                if (h.kind() == House.Kind.PLAYER && leaf(h.customName()) && !h.privateHome() && bed != null && bed.present()) {
                    if (held != null) beds.remove(held);
                    var old = beds.put(t.id(), new HousingIndex.BedKey(h.id(), head));
                    if (old != null) holder.remove(old.head());
                    holder.put(head, t.id());
                    CLAIMS.remove(t.id());
                    break;
                }
            }
        }
        return new HousingIndex(previous.village(), previous.houses(), beds, previous.homeless(), previous.needs(), previous.vacated(),
                previous.moved(), previous.cursed(), previous.stamp(), previous.surveyed());
    }
}
