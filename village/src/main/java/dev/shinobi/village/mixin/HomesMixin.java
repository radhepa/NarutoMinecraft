package dev.shinobi.village.mixin;

import com.llamalad7.mixinextras.injector.wrapmethod.WrapMethod;
import com.llamalad7.mixinextras.injector.wrapoperation.Operation;
import dev.villagefriends.CompanionController;
import dev.villagefriends.home.Homes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.npc.villager.Villager;
import org.spongepowered.asm.mixin.Mixin;

import java.util.List;

/** VF notes each resident's current bed only every twenty ticks; note them all before beds are handed out (see AssignmentsMixin). */
@Mixin(Homes.class)
abstract class HomesMixin {
    @WrapMethod(method = "assign")
    private static void narutominecraft$noteBeds(ServerLevel level, String village, Operation<Void> original) {
        for (Villager v : List.copyOf(CompanionController.loaded)) if (v.level() == level) Homes.keep(v, level);
        original.call(level, village);
    }
}
