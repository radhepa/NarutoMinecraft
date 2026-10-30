package dev.shinobi.combat.runtime.mixin.client;

import dev.shinobi.combat.runtime.ShinobiCombat;
import dev.shinobi.combat.runtime.client.ShinobiCombatClient;
import net.minecraft.client.renderer.entity.LivingEntityRenderer;
import net.minecraft.client.renderer.entity.state.LivingEntityRenderState;
import net.minecraft.world.entity.Avatar;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.npc.villager.Villager;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Carries an entity's synced clip, and the ticks since it started, into its render state for HumanoidModelMixin: a
 * player's, or a resident's (the spar partner's bow, stance and victory). A resident's one-shot ends with its clip, and a
 * resident running flat out takes the ninja run.
 * shortcut: the run is read from the client's movement (over 0.15 blocks a tick), until residents sync a gait of their own.
 */
@Mixin(LivingEntityRenderer.class)
abstract class LivingEntityRendererMixin {
    private static final double RUN = .15;

    @Inject(method = "extractRenderState(Lnet/minecraft/world/entity/LivingEntity;Lnet/minecraft/client/renderer/entity/state/LivingEntityRenderState;F)V", at = @At("TAIL"))
    private void shinobi_combat$stance(LivingEntity entity, LivingEntityRenderState state, float partialTick, CallbackInfo ci) {
        var stance = entity.getAttached(ShinobiCombat.STANCE);
        String clip = stance == null ? "" : stance.clip();
        float age = stance == null ? 0F : entity.level().getGameTime() - stance.since() + partialTick;
        if (!(entity instanceof Avatar)) {
            var c = ShinobiCombat.data.clips.get(clip);
            if (c != null && !c.loop() && age > c.ticks()) clip = "";
            if (clip.isEmpty() && entity instanceof Villager && Math.hypot(entity.getX() - entity.xo, entity.getZ() - entity.zo) > RUN) {
                clip = "combat.move.ninja_run";
                age = entity.tickCount + partialTick;
            }
        }
        state.setData(ShinobiCombatClient.CLIP, clip);
        state.setData(ShinobiCombatClient.AGE, age);
    }
}
