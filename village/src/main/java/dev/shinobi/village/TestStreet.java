package dev.shinobi.village;

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
import java.util.Set;
import java.util.UUID;

/**
 * The Leaf map from tools/konoha/layout.json: its streets and built plots in a marked VF village, House Plaques hung
 * and residents at their markers, each with the bed of the house it stands in. The test street (the Leaf apartment
 * block, a tea house, a training yard with the notice board, Sakura Lane's homes) comes first in the layout, so its
 * residents keep their UUIDs as the map grows. Flat 3a stays unplaqued for the player.
 */
public final class TestStreet {
    // shortcut: Varied keeps flat 3a too, until homes.json ships with the map and the apartment stream picks a candidate flat.
    public static final String BUILDING = "leaf_block", PLAYER_FLAT = "flat.leaf_block.3a", VILLAGE = "Leaf Test Street";
    /** The Hidden Leaf world preset (data/narutominecraft/worldgen/world_preset/leaf.json): void, no structures or features. */
    public static final ResourceKey<WorldPreset> PRESET = ResourceKey.create(Registries.WORLD_PRESET, Identifier.fromNamespaceAndPath("narutominecraft", "leaf"));
    public static final Layout LAYOUT = Layout.leaf();
    /** A new world's map: the apartment block's [0, 0, 0], and the spawn on the path under the block's front eave, just north of Leaf Street. */
    public static final BlockPos MAP = LAYOUT.map(), SPAWN = MAP.offset(LAYOUT.spawn());
    /** The border's centre (x, z, in the world) and side: the whole Beta 1 village, its planned plots included. */
    public static final double BORDER_X = MAP.getX() + LAYOUT.borderX(), BORDER_Z = MAP.getZ() + LAYOUT.borderZ(), BORDER = LAYOUT.border();
    /** Classic's cast seed, whatever the world seed: the street's first cast (P03). */
    static final long CLASSIC_CAST = 26;
    /** The quest places the map saves as anchors (layout.py ANCHORS): the board, the yard, the Academy, the Hokage's office. */
    static final Set<String> PLACES = Set.of("notice_board", "anchor:training", "anchor:hokage_office", "anchor:academy.grounds", "anchor:academy.yard", "anchor:academy.library");
    /**
     * The Leaf map's rules, all off: no monsters, raiders or traders wander in, and TNT and arrows leave the street alone.
     * Mob griefing stays on: VF's farmers harvest and residents pick up items through it.
     */
    public static final List<GameRule<Boolean>> OFF = List.of(GameRules.SPAWN_MONSTERS, GameRules.SPAWN_PATROLS, GameRules.SPAWN_PHANTOMS,
            GameRules.SPAWN_WANDERING_TRADERS, GameRules.RAIDS, GameRules.TNT_EXPLODES, GameRules.PROJECTILES_CAN_BREAK_BLOCKS);

    /**
     * The player flat's main room from the apartment block's [0, 0, 0], 6 by 3 by 6 (tools/konoha/blueprints/leaf_block.homes.json).
     * shortcut: one room of the one player flat, kept as an anchor, until P05's home claims a flat with all its rooms.
     */
    static final Vec3i ROOM = new Vec3i(1, 10, 3);
    public static final Vec3i ROOM_SIZE = new Vec3i(5, 2, 5);
    /** The flat's chest and crafting table from the room's corner (the bed's head). */
    public static final Vec3i FLAT_CHEST = new Vec3i(5, 0, 0), FLAT_TABLE = new Vec3i(4, 0, 0);

    private TestStreet() {}

    /** Whether {@code pos} lies in the main room of the street's player flat. */
    public static boolean inPlayerRoom(Level level, BlockPos pos) {
        var at = level instanceof ServerLevel server ? server.getAttachedOrElse(ShinobiVillage.ANCHORS, Map.of()).get(PLAYER_FLAT) : null;
        return at != null && BoundingBox.fromCorners(at, at.offset(ROOM_SIZE)).isInside(pos);
    }

    /**
     * A world's first start pastes the map: the street at {@link #MAP}, grass on the rest of the bordered square, the
     * border, and the spawn by the street facing the block. A world with anchors has its map already, and a world not
     * on the Leaf's void generator keeps its terrain (so does `/narutominecraft street`). The ground,
     * border and spawn are laid even if the street fails, so the player never starts over the void; the save is written at
     * once, so a crash before the first autosave never pastes the map twice.
     * shortcut: a dedicated server's default level-type is vanilla's, so it gets no map, until server.properties defaults to the Leaf.
     */
    public static void firstStart(MinecraftServer server) {
        var level = server.overworld();
        if (level.getAttached(ShinobiVillage.ANCHORS) != null || !leafVoid(level)) return;
        Built built = null;
        long start = System.nanoTime();
        try {
            built = build(level, MAP);
        } catch (RuntimeException e) {
            ShinobiVillage.LOG.error("No Leaf map in this world", e);
        }
        var grass = Blocks.GRASS_BLOCK.defaultBlockState();
        // shortcut: one block at a time over the whole border on the server thread (about 20 s on first start), until the terrain pass fills by chunk section.
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
        ShinobiVillage.LOG.info("Leaf map pasted in {} ms: {} residents, {} plaques", (System.nanoTime() - start) / 1_000_000, built.residents().size(), built.plaques().size());
    }

    /**
     * Whether the overworld generates the Leaf preset's void: flat, all air, the void biome.
     * shortcut: vanilla's The Void superflat matches too (it has no terrain to lose), until the save records its preset.
     */
    static boolean leafVoid(ServerLevel level) {
        return level.getChunkSource().getGenerator() instanceof FlatLevelSource flat && flat.settings().getBiome().is(Biomes.THE_VOID)
                && flat.settings().getLayers().stream().allMatch(s -> s == null || s.isAir());   // an air layer is null
    }

    /** Builds the map with its origin (the apartment block's [0, 0, 0], its ground layer) at {@code origin}, on ground no village holds yet. */
    public static Built build(ServerLevel level, BlockPos origin) {
        var here = VillageSettlements.discover(level, origin);
        if (here != null) throw new IllegalStateException("The test street needs empty ground; " + here.name() + " is already here");
        // shortcut: world-wide rules set by the street command, until the master map ships its own level settings (Phase 0, Map).
        var rules = level.getGameRules();
        for (var rule : OFF) rules.set(rule, false, level.getServer());
        // No fire spreads or burns blocks; a fire, once lit, also never goes out, so StreetGuard stops players lighting one.
        rules.set(GameRules.FIRE_SPREAD_RADIUS_AROUND_PLAYER, 0, level.getServer());
        // A defeat costs the thrown tools only, not the pack (ROADMAP.md, Death).
        rules.set(GameRules.KEEP_INVENTORY, true, level.getServer());
        long cast = castSeed(level);
        for (var street : LAYOUT.streets()) Blueprint.load(street.design()).paste(level, street.origin(origin));
        var plots = new ArrayList<Map.Entry<Layout.Plot, Blueprint>>();
        for (var plot : LAYOUT.plots()) {
            var bp = Blueprint.load(plot.design());
            bp.paste(level, plot.origin(origin), plot.rotation(), plot.mirror());
            plots.add(Map.entry(plot, bp));
        }
        String village = VillageSettlements.mark(level, origin, VILLAGE).id();
        var plaques = new ArrayList<String>();
        var residents = new ArrayList<Villager>();
        var anchors = new HashMap<String, BlockPos>();
        var roles = new HashMap<String, UUID>();
        for (var plot : plots) {
            var bp = plot.getValue();
            var markers = bp.json().getAsJsonArray("markers");
            var beds = new ArrayList<BlockPos>();
            for (var m : markers) if ("bed".equals(m.getAsJsonObject().get("type").getAsString())) beds.add(bedHead(level, bp.at(origin, plot.getKey(), m.getAsJsonObject())));
            for (var m : markers) {
                var marker = m.getAsJsonObject();
                var pos = bp.at(origin, plot.getKey(), marker);
                switch (marker.get("type").getAsString()) {
                    case "house_plaque" -> {
                        // Flats name their home; a house's plaque carries its plot's name.
                        String home = marker.has("home") ? marker.get("home").getAsString() : null;
                        if (PLAYER_FLAT.equals(home)) continue;
                        level.setBlock(pos, Blueprint.state(level, "villagefriends:house_plaque[facing=" + Blueprint.facing(plot.getKey(), marker) + ",mount=wall]"), 3);
                        if (!(level.getBlockEntity(pos) instanceof HousePlaqueBlockEntity plaque)) throw new IllegalStateException("No room for a House Plaque at " + pos.toShortString());
                        plaque.name(home == null ? plot.getKey().name() : LeafFlats.NAME + home.substring(home.lastIndexOf('.') + 1));
                        plaques.add(plaque.scanForBeds());
                    }
                    case "resident" -> {
                        var v = new Villager(EntityTypes.VILLAGER, level);
                        // VF draws a resident's profile, look and name from its UUID.
                        v.setUUID(resident(cast, residents.size()));
                        v.setPos(pos.getX() + .5, pos.getY(), pos.getZ() + .5);
                        // The nearest bed marker is its own (a plot places each resident beside its bed): VF keeps the bed a resident already sleeps in when it hands beds out.
                        beds.stream().min(Comparator.comparingInt(b -> b.distManhattan(pos))).ifPresent(bed -> {
                            v.getBrain().setMemory(MemoryModuleType.HOME, GlobalPos.of(level.dimension(), bed));
                            LeafFlats.CLAIMS.put(v.getUUID().toString(), bed);
                        });
                        if (!level.addFreshEntity(v)) throw new IllegalStateException("Resident " + v.getUUID() + " already lives in this world");
                        residents.add(v);
                        if (marker.has("role")) roles.put("role:" + marker.get("role").getAsString(), v.getUUID());
                        if (marker.has("job") && !"any".equals(marker.get("job").getAsString())) roles.put("job:" + marker.get("job").getAsString(), v.getUUID());
                    }
                    case String type when PLACES.contains(type) -> anchors.put(type, pos);
                    default -> {}
                }
            }
        }
        anchors.put(PLAYER_FLAT, origin.offset(ROOM));
        // The flat's storage and workbench, on the mat across the room from the bed (ROADMAP.md, P05: vanilla chests).
        // shortcut: placed by the paste, not the blueprint, until the home session's furnishing rows ship with the map.
        level.setBlock(origin.offset(ROOM).offset(FLAT_CHEST), Blueprint.state(level, "minecraft:chest[facing=south]"), Block.UPDATE_CLIENTS);
        level.setBlock(origin.offset(ROOM).offset(FLAT_TABLE), Blocks.CRAFTING_TABLE.defaultBlockState(), Block.UPDATE_CLIENTS);
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
