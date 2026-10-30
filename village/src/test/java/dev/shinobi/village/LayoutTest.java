package dev.shinobi.village;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.core.Vec3i;
import net.minecraft.world.level.block.Mirror;
import net.minecraft.world.level.block.Rotation;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class LayoutTest {
    @Test
    void theShippedLayoutStartsWithTheTestStreet() {
        var leaf = Layout.leaf();
        assertEquals(new BlockPos(0, 64, 0), leaf.map());
        assertEquals("leaf_block", leaf.plots().getFirst().id());
        assertEquals(leaf.plots().subList(0, leaf.district("leaf_street").size()), leaf.district("leaf_street"));
    }

    /** The same corners as layout.py's local(): mirror east-west first, then the clockwise turn. */
    @Test
    void turnsMatchLayoutPy() {
        var size = new JsonArray();
        for (int n : new int[]{11, 14, 5}) size.add(n);
        var json = new JsonObject();
        json.add("size", size);
        var bp = new Blueprint("t", json);
        assertEquals(new Vec3i(4, 0, 0), bp.local(0, 0, 0, Rotation.CLOCKWISE_90, Mirror.NONE));
        assertEquals(new Vec3i(0, 2, 10), bp.local(10, 2, 4, Rotation.CLOCKWISE_90, Mirror.NONE));
        assertEquals(new Vec3i(10, 0, 4), bp.local(0, 0, 0, Rotation.CLOCKWISE_180, Mirror.NONE));
        assertEquals(new Vec3i(0, 0, 0), bp.local(0, 0, 0, Rotation.COUNTERCLOCKWISE_90, Mirror.FRONT_BACK));
        // a street side south faces west after a quarter turn, north after a half
        assertEquals(Direction.WEST, Rotation.CLOCKWISE_90.rotate(Direction.SOUTH));
        assertEquals(Direction.WEST, Mirror.FRONT_BACK.mirror(Direction.EAST));
        var marker = new JsonObject();
        marker.addProperty("facing", "north");
        assertEquals("east", Blueprint.facing(new Layout.Plot("p", "d", Vec3i.ZERO, Rotation.CLOCKWISE_90, Mirror.NONE, "x", "P"), marker));
        marker.addProperty("facing", "east");
        assertEquals("north", Blueprint.facing(new Layout.Plot("p", "d", Vec3i.ZERO, Rotation.CLOCKWISE_90, Mirror.FRONT_BACK, "x", "P"), marker));
    }
}
