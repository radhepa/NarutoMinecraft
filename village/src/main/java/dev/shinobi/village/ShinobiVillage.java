package dev.shinobi.village;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.minecraft.commands.Commands;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/** Shinobi Village's entrypoint: the Konoha blocks and the builder's test-street command. */
public final class ShinobiVillage implements ModInitializer {
    public static final Logger LOG = LoggerFactory.getLogger("Shinobi Village");

    @Override
    public void onInitialize() {
        KonohaBlocks.register();
        // `/narutominecraft street` builds the P03 test street with its ground layer under the operator's feet.
        CommandRegistrationCallback.EVENT.register((dispatcher, registry, env) -> dispatcher.register(
                Commands.literal("narutominecraft").requires(Commands.hasPermission(Commands.LEVEL_GAMEMASTERS))
                        .then(Commands.literal("street").executes(ctx -> {
                            var src = ctx.getSource();
                            TestStreet.Built built;
                            try {
                                built = TestStreet.build(src.getLevel(), BlockPos.containing(src.getPosition()).below());
                            } catch (IllegalStateException e) {
                                src.sendFailure(Component.literal(e.getMessage()));
                                return 0;
                            }
                            src.sendSuccess(() -> Component.literal("Leaf test street: " + built.residents().size() + " residents, "
                                    + built.plaques().size() + " plaques"), true);
                            return built.residents().size();
                        }))));
    }
}
