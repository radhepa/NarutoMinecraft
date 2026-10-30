package dev.shinobi.village;

import net.minecraft.core.BlockPos;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.util.StringRepresentable;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.core.Direction;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Mirror;
import net.minecraft.world.level.block.Rotation;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.BlockStateProperties;
import net.minecraft.world.level.block.state.properties.EnumProperty;
import net.minecraft.world.level.block.state.properties.IntegerProperty;
import net.minecraft.world.level.block.state.properties.Property;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.Shapes;
import net.minecraft.world.phys.shapes.VoxelShape;

import java.util.Locale;

/**
 * The Konoha decor blocks, as authored in tools/konoha/blocks.py (models and blockstates in the root resources).
 * They are placed by blueprints and builders; their states are set by the paste, not worked out on placement.
 * shortcut: shapes are a full cube, a 2 px mat or none, until a block needs its exact outline (players or residents snag on it).
 */
public final class KonohaBlocks {
    public enum PolePart implements StringRepresentable {
        POLE, TOP, TRANSFORMER;
        @Override public String getSerializedName() { return name().toLowerCase(Locale.ROOT); }
    }
    public enum TankPart implements StringRepresentable {
        BOTTOM, MIDDLE, SINGLE, TOP;
        @Override public String getSerializedName() { return name().toLowerCase(Locale.ROOT); }
    }
    static final EnumProperty<PolePart> POLE_PART = EnumProperty.create("part", PolePart.class);
    static final EnumProperty<TankPart> TANK_PART = EnumProperty.create("part", TankPart.class);
    static final IntegerProperty SAG = IntegerProperty.create("sag", 0, 2);

    static final VoxelShape FULL = Shapes.block(), MAT = Block.box(0, 0, 0, 16, 2, 16), NONE = Shapes.empty();

    private KonohaBlocks() {}

    public static void register() {
        var axis = BlockStateProperties.HORIZONTAL_AXIS;
        var facing = BlockStateProperties.HORIZONTAL_FACING;
        var half = BlockStateProperties.DOUBLE_BLOCK_HALF;
        for (String n : new String[]{"tatami", "aged_tatami"}) add(n, SoundType.WOOL, 0, MAT, axis);
        for (String n : new String[]{"shoji_screen", "dark_shoji_screen"}) add(n, SoundType.BAMBOO_WOOD, 0, FULL, facing, half);
        for (String n : new String[]{"stone_lantern", "mossy_stone_lantern"}) add(n, SoundType.STONE, 12, FULL, facing, half);
        for (String n : new String[]{"red_paper_lantern", "white_paper_lantern"}) add(n, SoundType.WOOL, 13, FULL);
        for (String n : new String[]{"grey_kawara_ridge", "green_kawara_ridge", "orange_kawara_ridge"}) add(n, SoundType.DECORATED_POT, 0, FULL, axis);
        for (String n : new String[]{"red_awning", "green_awning", "indigo_awning", "red_noren", "indigo_noren", "ramen_noren", "tea_noren"})
            add(n, SoundType.WOOL, 0, NONE, facing);
        add("power_wire", SoundType.WOOL, 0, NONE, axis, SAG);
        add("utility_pole", SoundType.WOOD, 0, FULL, axis, POLE_PART);
        add("water_tank", SoundType.METAL, 0, FULL, TANK_PART);
    }

    private static void add(String name, SoundType sound, int light, VoxelShape shape, Property<?>... props) {
        var id = Identifier.fromNamespaceAndPath("narutominecraft", name);
        var p = BlockBehaviour.Properties.of().setId(ResourceKey.create(Registries.BLOCK, id))
                .strength(1.5F).sound(sound).noOcclusion().lightLevel(s -> light);
        if (shape == NONE) p.noCollision();
        Block block = new Block(p) {
            @Override protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> b) { b.add(props); }
            @Override protected VoxelShape getShape(BlockState s, BlockGetter level, BlockPos pos, CollisionContext c) { return shape == NONE ? FULL : shape; }
            // A turned or mirrored paste turns facings and swaps horizontal axes, as vanilla blocks do.
            @Override protected BlockState rotate(BlockState s, Rotation r) {
                if (s.hasProperty(BlockStateProperties.HORIZONTAL_FACING)) return s.setValue(BlockStateProperties.HORIZONTAL_FACING, r.rotate(s.getValue(BlockStateProperties.HORIZONTAL_FACING)));
                if (s.hasProperty(BlockStateProperties.HORIZONTAL_AXIS) && (r == Rotation.CLOCKWISE_90 || r == Rotation.COUNTERCLOCKWISE_90))
                    return s.setValue(BlockStateProperties.HORIZONTAL_AXIS, s.getValue(BlockStateProperties.HORIZONTAL_AXIS) == Direction.Axis.X ? Direction.Axis.Z : Direction.Axis.X);
                return s;
            }
            @Override protected BlockState mirror(BlockState s, Mirror m) {
                return s.hasProperty(BlockStateProperties.HORIZONTAL_FACING) ? s.setValue(BlockStateProperties.HORIZONTAL_FACING, m.mirror(s.getValue(BlockStateProperties.HORIZONTAL_FACING))) : s;
            }
        };
        Registry.register(BuiltInRegistries.BLOCK, id, block);
        Registry.register(BuiltInRegistries.ITEM, id, new BlockItem(block,
                new Item.Properties().setId(ResourceKey.create(Registries.ITEM, id)).useBlockDescriptionPrefix()));
    }
}
