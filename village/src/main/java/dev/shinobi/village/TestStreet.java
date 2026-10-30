package dev.shinobi.village;

import com.google.gson.JsonArray;
import dev.shinobi.core.SaveSeed;
import dev.villagefriends.HousePlaqueBlockEntity;
import dev.villagefriends.VillageSettlements;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.minecraft.core.BlockPos;
import net.minecraft.core.GlobalPos;
import net.minecraft.core.Vec3i;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityTypes;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.levelgen.structure.BoundingBox;
import net.minecraft.world.entity.ai.memory.MemoryModuleType;
import net.minecraft.world.entity.npc.villager.Villager;
import net.minecraft.world.level.block.BedBlock;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.gamerules.GameRule;
import net.minecraft.world.level.gamerules.GameRules;
import net.minecraft.world.level.block.state.properties.BedPart;
import net.minecraft.world.level.biome.Biomes;
import net.minecraft.world.level.levelgen.FlatLevelSource;
import net.minecraft.world.level.levelgen.presets.WorldPreset;
import net.minecraft.world.level.storage.LevelData;

import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/**
 * The P03 test street: the Leaf apartment block, a tea house and a training yard with the notice board in a marked VF
 * village, House Plaques hung and residents at their markers, each with the bed of the house it stands in.
 * Flat 3a stays unplaqued for the player.
 * shortcut: three plots pasted by code, until the master map's paste tool and layout.json (Phase 0, Map).
 */
public final class TestStreet {
    // shortcut: Varied keeps flat 3a too, until homes.json ships with the map and the apartment stream picks a candidate flat.
    public static final String BUILDING = "leaf_block", PLAYER_FLAT = "flat.leaf_block.3a", VILLAGE = "Leaf Test Street";
    /** The Hidden Leaf world preset (data/narutominecraft/worldgen/world_preset/leaf.json): void, no structures or features. */
    public static final ResourceKey<WorldPreset> PRESET = ResourceKey.create(Registries.WORLD_PRESET, Identifier.fromNamespaceAndPath("narutominecraft", "leaf"));
    /** A new world's map: the apartment block's [0, 0, 0], and the spawn on the path under the block's front eave. */
    public static final BlockPos MAP = new BlockPos(0, 64, 0), SPAWN = MAP.offset(17, 1, 14);
    /** The border's centre (x, z) and side: the three plots and the street, with a margin of at least nine blocks. */
    public static final double BORDER_X = 18.5, BORDER_Z = 12.5, BORDER = 80;
    /** Classic's cast seed, whatever the world seed: the street's first cast (P03). */
    static final long CLASSIC_CAST = 26;
    /**
     * The Leaf map's rules, all off: no monsters, raiders or traders wander in, and TNT and arrows leave the street alone.
     * Mob griefing stays on: VF's farmers harvest and residents pick up items through it.
     */
    public static final List<GameRule<Boolean>> OFF = List.of(GameRules.SPAWN_MONSTERS, GameRules.SPAWN_PATROLS, GameRules.SPAWN_PHANTOMS,
            GameRules.SPAWN_WANDERING_TRADERS, GameRules.RAIDS, GameRules.TNT_EXPLODES, GameRules.PROJECTILES_CAN_BREAK_BLOCKS);
    /** Each plot and where its [0, 0, 0] sits from the apartment block's: the shop west, the yard east, street fronts in line. */
    static final List<Map.Entry<String, Vec3i>> PLOTS = List.of(Map.entry(BUILDING, Vec3i.ZERO),
            Map.entry("shop_tea_house", new Vec3i(-12, 0, 4)), Map.entry("training_yard", new Vec3i(36, 0, 4)));

    /**
     * The player flat's main room from the apartment block's [0, 0, 0], 6 by 3 by 6 (tools/konoha/blueprints/leaf_block.homes.json).
     * shortcut: one room of the one player flat, kept as an anchor, until P05's home claims a flat with all its rooms.
     */
    static final Vec3i ROOM = new Vec3i(1, 10, 3), ROOM_SIZE = new Vec3i(5, 2, 5);

    private TestStreet() {}

    /** Whether {@code pos} lies in the main room of the street's player flat. */
    public static boolean inPlayerRoom(Level level, BlockPos pos) {
        var at = level instanceof ServerLevel server ? server.getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).get(PLAYER_FLAT) : null;
        return at != null && BoundingBox.fromCorners(at, at.offset(ROOM_SIZE)).isInside(pos);
    }

    /**
     * A world's first start pastes the map: the street at {@link #MAP}, grass on the rest of the bordered square, the
     * border, and the spawn on the street facing the block. A world with anchors has its map already, and a world not
     * on the Leaf's void generator keeps its terrain (an operator can still run `/narutominecraft street`). The ground,
     * border and spawn are laid even if the street fails, so the player never starts over the void; the save is written at
     * once, so a crash before the first autosave never pastes the map twice.
     * shortcut: a dedicated server's default level-type is vanilla's, so it gets no map, until server.properties defaults to the Leaf.
     */
    public static void firstStart(MinecraftServer server) {
        var level = server.overworld();
        if (level.getAttached(ShinobiVillage.ANCHORS) != null || !leafVoid(level)) return;
        Built built = null;
        try {
            built = build(level, MAP);
        } catch (RuntimeException e) {
            ShinobiVillage.LOG.error("No Leaf map in this world", e);
        }
        var grass = Blocks.GRASS_BLOCK.defaultBlockState();
        for (int x = (int) Math.floor(BORDER_X - BORDER / 2); x < BORDER_X + BORDER / 2; x++)
            for (int z = (int) Math.floor(BORDER_Z - BORDER / 2); z < BORDER_Z + BORDER / 2; z++) {
                var at = new BlockPos(x, MAP.getY(), z);
                if (level.getBlockState(at).isAir()) level.setBlock(at, grass, Block.UPDATE_CLIENTS);
            }
        level.getWorldBorder().setCenter(BORDER_X, BORDER_Z);
        level.getWorldBorder().setSize(BORDER);
        server.setRespawnData(LevelData.RespawnData.of(level.dimension(), SPAWN, 180, 0));
        level.getGameRules().set(GameRules.RESPAWN_RADIUS, 0, server);
        if (built == null) return;
        server.saveEverything(true, true, false);
        ShinobiVillage.LOG.info("Leaf map pasted: {} residents, {} plaques", built.residents().size(), built.plaques().size());
    }

    /**
     * Whether the overworld generates the Leaf preset's void: flat, all air, the void biome.
     * shortcut: vanilla's The Void superflat matches too (it has no terrain to lose), until the save records its preset.
     */
    static boolean leafVoid(ServerLevel level) {
        return level.getChunkSource().getGenerator() instanceof FlatLevelSource flat && flat.settings().getBiome().is(Biomes.THE_VOID)
                && flat.settings().getLayers().stream().allMatch(s -> s == null || s.isAir());   // an air layer is null
    }

    /** Builds the street with the apartment block's [0, 0, 0] (its ground layer) at {@code origin}, on ground no village holds yet. */
    public static Built build(ServerLevel level, BlockPos origin) {
        var here = VillageSettlements.discover(level, origin);
        if (here != null) throw new IllegalStateException("The test street needs empty ground; " + here.name() + " is already here");
        // shortcut: world-wide rules set by the street command, until the master map ships its own level settings (Phase 0, Map).
        var rules = level.getGameRules();
        for (var rule : OFF) rules.set(rule, false, level.getServer());
        // No fire spreads or burns blocks; a fire, once lit, also never goes out, so StreetGuard stops players lighting one.
        rules.set(GameRules.FIRE_SPREAD_RADIUS_AROUND_PLAYER, 0, level.getServer());
        long cast = castSeed(level);
        var plots = new ArrayList<Map.Entry<BlockPos, JsonArray>>();
        for (var plot : PLOTS) {
            var at = origin.offset(plot.getValue());
            plots.add(Map.entry(at, Blueprint.load(plot.getKey()).paste(level, at)));
        }
        String village = VillageSettlements.mark(level, origin, VILLAGE).id();
        var plaques = new ArrayList<String>();
        var residents = new ArrayList<Villager>();
        var anchors = new HashMap<String, BlockPos>();
        var roles = new HashMap<String, UUID>();
        for (var plot : plots) {
            var beds = new ArrayList<BlockPos>();
            for (var m : plot.getValue()) if ("bed".equals(m.getAsJsonObject().get("type").getAsString())) beds.add(bedHead(level, Blueprint.at(plot.getKey(), m.getAsJsonObject())));
            for (var m : plot.getValue()) {
                var marker = m.getAsJsonObject();
                var pos = Blueprint.at(plot.getKey(), marker);
                switch (marker.get("type").getAsString()) {
                    case "house_plaque" -> {
                        // Flats name their home; the tea house's plaque has none.
                        String home = marker.has("home") ? marker.get("home").getAsString() : null;
                        if (PLAYER_FLAT.equals(home)) continue;
                        level.setBlock(pos, Blueprint.state(level, "villagefriends:house_plaque[facing=" + marker.get("facing").getAsString() + ",mount=wall]"), 3);
                        if (!(level.getBlockEntity(pos) instanceof HousePlaqueBlockEntity plaque)) throw new IllegalStateException("No room for a House Plaque at " + pos.toShortString());
                        plaque.name(home == null ? LeafFlats.TEA_HOUSE : LeafFlats.NAME + home.substring(home.lastIndexOf('.') + 1));
                        plaques.add(plaque.scanForBeds());
                    }
                    case "resident" -> {
                        var v = new Villager(EntityTypes.VILLAGER, level);
                        // VF draws a resident's profile, look and name from its UUID.
                        v.setUUID(resident(cast, residents.size()));
                        v.setPos(pos.getX() + .5, pos.getY(), pos.getZ() + .5);
                        // The nearest bed of its house is its own: VF keeps the bed a resident already sleeps in when it hands beds out.
                        beds.stream().min(Comparator.comparingInt(b -> b.distManhattan(pos)))
                                .ifPresent(bed -> v.getBrain().setMemory(MemoryModuleType.HOME, GlobalPos.of(level.dimension(), bed)));
                        if (!level.addFreshEntity(v)) throw new IllegalStateException("Resident " + v.getUUID() + " already lives in this world");
                        residents.add(v);
                        if (marker.has("role")) roles.put("role:" + marker.get("role").getAsString(), v.getUUID());
                        if (marker.has("job") && !"any".equals(marker.get("job").getAsString())) roles.put("job:" + marker.get("job").getAsString(), v.getUUID());
                    }
                    case "notice_board", "anchor:training" -> anchors.put(marker.get("type").getAsString(), pos);
                    default -> {}
                }
            }
        }
        anchors.put(PLAYER_FLAT, origin.offset(ROOM));
        save(level, ShinobiVillage.ANCHORS, anchors);
        save(level, ShinobiVillage.ROLES, roles);
        return new Built(village, List.copyOf(plaques), List.copyOf(residents), Map.copyOf(anchors));
    }

    /** Adds {@code found} to what the level already holds under {@code type}. */
    private static <V> void save(ServerLevel level, AttachmentType<Map<String, V>> type, Map<String, V> found) {
        var saved = new HashMap<>(level.getAttachedOrElse(type, Map.of()));
        saved.putAll(found);
        level.setAttached(type, Map.copyOf(saved));
    }

    private static BlockPos bedHead(ServerLevel level, BlockPos pos) {
        var state = level.getBlockState(pos);
        if (!(state.getBlock() instanceof BedBlock) || state.getValue(BedBlock.PART) != BedPart.HEAD) throw new IllegalStateException("No bed head at bed marker " + pos.toShortString());
        return pos;
    }

    /** The seed of this save's cast: {@link #CLASSIC_CAST} in Classic, the save seed in Varied. */
    public static long castSeed(ServerLevel level) {
        var save = SaveSeed.of(level.getServer());
        return "varied".equals(save.mode()) ? save.seed() : CLASSIC_CAST;
    }

    /** The UUID of the resident at the building's {@code marker}th resident marker: the same cast in every world with this cast seed. */
    public static UUID resident(long seed, int marker) {
        return UUID.nameUUIDFromBytes((BUILDING + ":" + seed + ":" + marker).getBytes(StandardCharsets.UTF_8));
    }

    /** The VF village id, each plaque's scan readout, the residents spawned, and the notice board and training anchors. */
    public record Built(String village, List<String> plaques, List<Villager> residents, Map<String, BlockPos> anchors) {}
}
