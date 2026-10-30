package dev.shinobi.village.mixin.client;

import dev.shinobi.village.TestStreet;
import net.minecraft.client.gui.screens.worldselection.WorldCreationContext;
import net.minecraft.client.gui.screens.worldselection.WorldCreationUiState;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceKey;
import net.minecraft.world.level.levelgen.presets.WorldPreset;
import net.minecraft.world.level.levelgen.presets.WorldPresets;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

import java.nio.file.Path;
import java.util.Optional;
import java.util.OptionalLong;

/** A fresh Create World screen starts on the Hidden Leaf preset where vanilla picks Default; More World Options can still change it. */
@Mixin(WorldCreationUiState.class)
abstract class WorldCreationUiStateMixin {
    @Inject(method = "<init>", at = @At("TAIL"))
    private void narutominecraft$leaf(Path saves, WorldCreationContext settings, Optional<ResourceKey<WorldPreset>> preset, OptionalLong seed, CallbackInfo ci) {
        // Only a fresh world asks for Default; re-creating a world and the debug test world ask for their own preset.
        if (preset.equals(Optional.of(WorldPresets.NORMAL)))
            settings.worldgenLoadContext().lookupOrThrow(Registries.WORLD_PRESET).get(TestStreet.PRESET)
                    .ifPresent(leaf -> ((WorldCreationUiState) (Object) this).setWorldType(new WorldCreationUiState.WorldTypeEntry(leaf)));
    }
}
