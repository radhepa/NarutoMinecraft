package dev.shinobi.village;

import dev.villagefriends.NoticeBoardBlock;
import dev.villagefriends.VillageSettlements;
import dev.villagefriends.home.HousePlaqueBlock;
import net.fabricmc.fabric.api.event.player.PlayerBlockBreakEvents;
import net.fabricmc.fabric.api.event.player.UseBlockCallback;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.tags.BlockTags;
import net.minecraft.tags.ItemTags;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.state.BlockState;

/**
 * Adventure protection: nobody breaks or builds on the Leaf map except in builder mode, which an operator
 * switches on deliberately with `/narutominecraft builder`. Doors, beds, plaques and the board still work.
 * Monster spawns, fire spread, TNT and arrows are handled by the map's rules ({@link TestStreet#OFF}).
 * shortcut: protects the test street's village by name and only blocks breaking, block placement, lighting fires, the
 * tools that reshape blocks and making a flat private (not buckets or explosions of placed mobs), until the master
 * map's layout names its protected regions (Phase 0, Map).
 */
public final class StreetGuard {
    public static final String BUILDER = "narutominecraft.builder";

    private StreetGuard() {}

    static void register() {
        PlayerBlockBreakEvents.BEFORE.register((level, player, pos, state, entity) -> allowed(level, player, pos));
        UseBlockCallback.EVENT.register((player, level, hand, hit) -> {
            var pos = hit.getBlockPos();
            var target = level.getBlockState(pos);
            var stack = player.getItemInHand(hand);
            boolean sneak = player.isSecondaryUseActive();
            // Sneak-using a plaque makes the house private, which turns its resident out.
            if (sneak && target.getBlock() instanceof HousePlaqueBlock) return allowed(level, player, pos) ? InteractionResult.PASS : InteractionResult.FAIL;
            if (!sneak && usable(target)) return InteractionResult.PASS;
            BlockPos changed = stack.getItem() instanceof BlockItem || stack.is(Items.FLINT_AND_STEEL) || stack.is(Items.FIRE_CHARGE) ? pos.relative(hit.getDirection())
                    : stack.is(ItemTags.HOES) || stack.is(ItemTags.SHOVELS) || stack.is(ItemTags.AXES) || stack.is(Items.BONE_MEAL) ? pos : null;
            return changed != null && !allowed(level, player, changed) ? InteractionResult.FAIL : InteractionResult.PASS;
        });
    }

    /** Blocks a player uses rather than changes. */
    static boolean usable(BlockState s) {
        return s.is(BlockTags.DOORS) || s.is(BlockTags.TRAPDOORS) || s.is(BlockTags.FENCE_GATES) || s.is(BlockTags.BEDS)
                || s.getBlock() instanceof HousePlaqueBlock || s.getBlock() instanceof NoticeBoardBlock;
    }

    /** Whether {@code player} may change the block at {@code pos}. */
    public static boolean allowed(Level level, Player player, BlockPos pos) {
        if (!(level instanceof ServerLevel server) || player.entityTags().contains(BUILDER)) return true;
        // Every village holding the spot, not just the nearest: a marker placed beside the street must not unprotect it.
        return VillageSettlements.book(server).villages().values().stream().noneMatch(v -> v.contains(pos) && TestStreet.VILLAGE.equals(v.name()));
    }
}
