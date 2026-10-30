package dev.shinobi.village.mixin;

import dev.shinobi.village.LeafNames;
import dev.villagefriends.VillageFriends;
import net.minecraft.world.entity.npc.villager.Villager;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/** Use the Leaf save's names after VF creates the resident's profile, before it records the resident in its ledger. */
@Mixin(VillageFriends.class)
abstract class NamesMixin {
    @Inject(method = "ensureIdentity", at = @At("TAIL"))
    private static void narutominecraft$name(Villager resident, CallbackInfo ci) {
        LeafNames.ensure(resident);
    }
}
