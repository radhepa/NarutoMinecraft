package dev.shinobi.village;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import net.minecraft.commands.arguments.blocks.BlockStateParser;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.Registries;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockState;

import java.util.HashMap;

/** A konoha-blueprint/1 building from tools/konoha/blueprints, shipped as data/narutominecraft/blueprints. */
public record Blueprint(String id, JsonObject json) {
    public static Blueprint load(String id) {
        var json = LeafWardrobe.read("/data/narutominecraft/blueprints/" + id + ".json");
        if (!"konoha-blueprint/1".equals(json.get("format").getAsString())) throw new IllegalArgumentException("Not a konoha-blueprint/1: " + id);
        return new Blueprint(id, json);
    }

    /** Places every block with {@code origin} at the blueprint's [0, 0, 0]; '.' is air. Returns the markers. */
    public JsonArray paste(ServerLevel level, BlockPos origin) {
        var states = new HashMap<Character, BlockState>();
        states.put('.', Blocks.AIR.defaultBlockState());
        for (var e : json.getAsJsonObject("palette").entrySet()) {
            if (e.getKey().length() != 1) throw new IllegalArgumentException(id + ": palette key '" + e.getKey() + "' is not one character");
            states.put(e.getKey().charAt(0), state(level, e.getValue().getAsString()));
        }
        var layers = json.getAsJsonArray("layers");
        for (int y = 0; y < layers.size(); y++) {
            var rows = layers.get(y).getAsJsonArray();
            for (int z = 0; z < rows.size(); z++) {
                String row = rows.get(z).getAsString();
                for (int x = 0; x < row.length(); x++) {
                    var s = states.get(row.charAt(x));
                    if (s == null) throw new IllegalArgumentException(id + ": no palette entry for '" + row.charAt(x) + "'");
                    // No neighbour updates: the blueprint already holds each block's final state (doors, beds, fences).
                    level.setBlock(origin.offset(x, y, z), s, Block.UPDATE_CLIENTS | Block.UPDATE_KNOWN_SHAPE);
                }
            }
        }
        return json.getAsJsonArray("markers");
    }

    static BlockState state(ServerLevel level, String text) {
        try {
            return BlockStateParser.parseForBlock(level.registryAccess().lookupOrThrow(Registries.BLOCK), text, false).blockState();
        } catch (CommandSyntaxException e) {
            throw new IllegalArgumentException("Bad block state " + text, e);
        }
    }

    static BlockPos at(BlockPos origin, JsonObject marker) {
        var p = marker.getAsJsonArray("pos");
        return origin.offset(p.get(0).getAsInt(), p.get(1).getAsInt(), p.get(2).getAsInt());
    }
}
