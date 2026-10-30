package dev.shinobi.combat.runtime.mixin;

import dev.shinobi.combat.runtime.Tools;
import net.minecraft.core.BlockPos;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.InsideBlockEffectApplier;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.TripWireBlock;
import net.minecraft.world.level.block.state.BlockState;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** A mob walking into a wire is tripped (Tools.trip). */
@Mixin(TripWireBlock.class)
abstract class TripWireBlockMixin {
    @Inject(method = "entityInside", at = @At("HEAD"))
    private void shinobi_combat$trip(BlockState state, Level level, BlockPos pos, Entity entity, InsideBlockEffectApplier effects, boolean moved, CallbackInfo ci) {
        Tools.trip(level, entity);
    }
}
