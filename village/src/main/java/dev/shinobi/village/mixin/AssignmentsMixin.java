package dev.shinobi.village.mixin;

import com.llamalad7.mixinextras.injector.wrapmethod.WrapMethod;
import com.llamalad7.mixinextras.injector.wrapoperation.Operation;
import dev.shinobi.village.LeafFlats;
import dev.villagefriends.home.Assignments;
import dev.villagefriends.home.HousingIndex;
import dev.villagefriends.social.Townsfolk;
import net.minecraft.core.BlockPos;
import org.spongepowered.asm.mixin.Mixin;

import java.util.Collection;
import java.util.Map;
import java.util.Set;

/** VF keeps residents in the bed they sleep in only for generated houses; Leaf flats are plaqued, so seed those first. */
@Mixin(Assignments.class)
abstract class AssignmentsMixin {
    @WrapMethod(method = "assign")
    private static HousingIndex narutominecraft$ownFlat(HousingIndex previous, Collection<Townsfolk> folk, Map<String, BlockPos> anchors,
            Set<String> noticed, long today, Operation<HousingIndex> original) {
        return original.call(LeafFlats.seed(previous, folk, anchors), folk, anchors, noticed, today);
    }
}
