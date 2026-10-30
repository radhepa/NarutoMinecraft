package dev.shinobi.village;

import dev.villagefriends.HousePlaqueBlockEntity;
import dev.villagefriends.VillageSettlements;
import net.minecraft.core.BlockPos;
import net.minecraft.core.GlobalPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.entity.ai.memory.MemoryModuleType;
import net.minecraft.world.entity.npc.villager.Villager;
import net.minecraft.world.level.block.BedBlock;
import net.minecraft.world.level.block.state.properties.BedPart;

import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.UUID;

/**
 * The P03 test street: the Leaf apartment block in a marked VF village, its House Plaques hung and ten
 * residents at its markers, each with the bed of the flat it stands in. Flat 3a stays unplaqued for the player.
 * shortcut: one building pasted by code, until the master map's paste tool and layout.json (Phase 0, Map).
 */
public final class TestStreet {
    public static final String BUILDING = "leaf_block", PLAYER_FLAT = "flat.leaf_block.3a";

    private TestStreet() {}

    /** Builds the street with the blueprint's [0, 0, 0] (its ground layer) at {@code origin}, on ground no village holds yet. */
    public static Built build(ServerLevel level, BlockPos origin) {
        var here = VillageSettlements.discover(level, origin);
        if (here != null) throw new IllegalStateException("The test street needs empty ground; " + here.name() + " is already here");
        var markers = Blueprint.load(BUILDING).paste(level, origin);
        String village = VillageSettlements.mark(level, origin, "Leaf Test Street").id();
        var plaques = new ArrayList<String>();
        var residents = new ArrayList<Villager>();
        for (var m : markers) {
            var marker = m.getAsJsonObject();
            var pos = Blueprint.at(origin, marker);
            switch (marker.get("type").getAsString()) {
                case "house_plaque" -> {
                    String home = marker.get("home").getAsString();
                    if (PLAYER_FLAT.equals(home)) continue;
                    level.setBlock(pos, Blueprint.state(level, "villagefriends:house_plaque[facing=" + marker.get("facing").getAsString() + ",mount=wall]"), 3);
                    if (!(level.getBlockEntity(pos) instanceof HousePlaqueBlockEntity plaque)) throw new IllegalStateException("No room for a House Plaque at " + pos.toShortString());
                    plaque.name(LeafFlats.NAME + home.substring(home.lastIndexOf('.') + 1));
                    plaques.add(plaque.scanForBeds());
                }
                case "resident" -> {
                    var v = new Villager(EntityTypes.VILLAGER, level);
                    // VF draws a resident's profile, look and name from its UUID.
                    v.setUUID(resident(level.getSeed(), residents.size()));
                    v.setPos(pos.getX() + .5, pos.getY(), pos.getZ() + .5);
                    // The nearest bed on its floor is its own: VF keeps the bed a resident already sleeps in when it hands beds out.
                    BlockPos.betweenClosedStream(pos.offset(-8, 0, -8), pos.offset(8, 0, 8)).map(BlockPos::immutable)
                            .filter(p -> level.getBlockState(p).getBlock() instanceof BedBlock && level.getBlockState(p).getValue(BedBlock.PART) == BedPart.HEAD)
                            .min(Comparator.comparingInt(p -> p.distManhattan(pos))).ifPresent(bed -> v.getBrain().setMemory(MemoryModuleType.HOME, GlobalPos.of(level.dimension(), bed)));
                    if (!level.addFreshEntity(v)) throw new IllegalStateException("Resident " + v.getUUID() + " already lives in this world");
                    residents.add(v);
                }
                default -> {}
            }
        }
        return new Built(village, List.copyOf(plaques), List.copyOf(residents));
    }

    /**
     * The UUID of the resident at the building's {@code marker}th resident marker: the same cast in every world with this seed.
     * shortcut: the world seed, until Shinobi Core's save seed and its Classic/Varied mode choose the cast (P03 queue, item 3).
     */
    public static UUID resident(long seed, int marker) {
        return UUID.nameUUIDFromBytes((BUILDING + ":" + seed + ":" + marker).getBytes(StandardCharsets.UTF_8));
    }

    /** The VF village id, each plaque's scan readout, and the residents spawned. */
    public record Built(String village, List<String> plaques, List<Villager> residents) {}
}
