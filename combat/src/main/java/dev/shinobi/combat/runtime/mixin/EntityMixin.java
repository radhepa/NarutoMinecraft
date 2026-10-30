package dev.shinobi.combat.runtime.mixin;

import dev.shinobi.combat.runtime.Fighter;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.phys.Vec3;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.ModifyVariable;

/** Rope Escape loosens a cobweb's hold on a player who knows it, on both sides so the client's movement agrees (Fighter.unstuck). */
@Mixin(Entity.class)
abstract class EntityMixin {
    @ModifyVariable(method = "makeStuckInBlock", at = @At("HEAD"), argsOnly = true)
    private Vec3 shinobi_combat$ropeEscape(Vec3 multiplier, BlockState state) {
        return Fighter.unstuck((Entity) (Object) this, state, multiplier);
    }
}
