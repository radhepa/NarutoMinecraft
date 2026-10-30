package dev.shinobi.village;

import com.google.gson.JsonObject;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Vec3i;
import net.minecraft.world.level.block.Mirror;
import net.minecraft.world.level.block.Rotation;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * The Hidden Leaf's map, tools/konoha/layout.json (shipped as data/narutominecraft/layout.json): the origin, spawn and
 * border, and the plots to paste, streets first. `python tools/konoha/layout.py --check` holds it to its rules.
 */
public record Layout(BlockPos map, Vec3i spawn, double borderX, double borderZ, double border, List<Plot> streets, List<Plot> plots) {
    /**
     * A blueprint placed with its footprint's north-west corner at {@code at} from the map's origin, mirrored east-west
     * and then turned clockwise, as layout.py places it.
     */
    public record Plot(String id, String design, Vec3i at, Rotation rotation, Mirror mirror, String district, String name) {
        public BlockPos origin(BlockPos map) { return map.offset(at); }
    }

    private static final Layout LEAF = parse(LeafWardrobe.read("/data/narutominecraft/layout.json"));

    /** The shipped layout. */
    public static Layout leaf() { return LEAF; }

    static Layout parse(JsonObject json) {
        if (!"konoha-layout/1".equals(json.get("format").getAsString())) throw new IllegalArgumentException("Not a konoha-layout/1");
        var b = json.getAsJsonObject("border");
        var streets = new ArrayList<Plot>();
        for (var e : json.getAsJsonArray("streets")) {
            var s = e.getAsJsonObject();
            var from = s.getAsJsonArray("from");
            var to = s.getAsJsonArray("to");
            int ax = from.get(0).getAsInt(), az = from.get(1).getAsInt(), bx = to.get(0).getAsInt(), bz = to.get(1).getAsInt(), h = s.get("width").getAsInt() / 2;
            // A street's blueprint starts at the north-west corner of its run (layout.street_rect).
            var at = az == bz ? new Vec3i(Math.min(ax, bx), 0, az - h) : new Vec3i(ax - h, 0, Math.min(az, bz));
            String id = s.get("id").getAsString();
            streets.add(new Plot(id, "street." + id, at, Rotation.NONE, Mirror.NONE, null, s.get("name").getAsString()));
        }
        var plots = new ArrayList<Plot>();
        for (var e : json.getAsJsonArray("plots")) {
            var p = e.getAsJsonObject();
            if (p.has("planned") && p.get("planned").getAsBoolean()) continue;
            int rot = p.has("rot") ? p.get("rot").getAsInt() : 0;
            var rotation = switch (rot) {
                case 0 -> Rotation.NONE;
                case 90 -> Rotation.CLOCKWISE_90;
                case 180 -> Rotation.CLOCKWISE_180;
                case 270 -> Rotation.COUNTERCLOCKWISE_90;
                default -> throw new IllegalArgumentException("plot " + p.get("id").getAsString() + ": rot " + rot);
            };
            var mirror = p.has("mirror") && p.get("mirror").getAsBoolean() ? Mirror.FRONT_BACK : Mirror.NONE;
            plots.add(new Plot(p.get("id").getAsString(), p.get("design").getAsString(), vec(p.getAsJsonArray("at")), rotation, mirror,
                    p.get("district").getAsString(), p.get("name").getAsString()));
        }
        return new Layout(BlockPos.ZERO.offset(vec(json.getAsJsonArray("map"))), vec(json.getAsJsonArray("spawn")), b.get("x").getAsDouble(), b.get("z").getAsDouble(),
                b.get("size").getAsDouble(), List.copyOf(streets), List.copyOf(plots));
    }

    /** The built plots of one district, in layout order. */
    public List<Plot> district(String id) { return plots.stream().filter(p -> id.equals(p.district())).toList(); }

    /** Every built plot's name: the names its House Plaques carry. */
    public Set<String> names() { return plots.stream().map(Plot::name).collect(Collectors.toSet()); }

    private static Vec3i vec(com.google.gson.JsonArray a) { return new Vec3i(a.get(0).getAsInt(), a.get(1).getAsInt(), a.get(2).getAsInt()); }
}
