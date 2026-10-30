package dev.shinobi.village;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.minecraft.commands.Commands;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/** Shinobi Village's entrypoint: the Konoha blocks, the street's protection and the builder's commands. */
public final class ShinobiVillage implements ModInitializer {
    public static final Logger LOG = LoggerFactory.getLogger("Shinobi Village");

    @Override
    public void onInitialize() {
        KonohaBlocks.register();
        StreetGuard.register();
        // `/narutominecraft street` builds the P03 test street with its ground layer under the operator's feet;
        // `/narutominecraft builder` switches the operator's builder mode, the only way to change the street.
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
                        }))
                        .then(Commands.literal("builder").executes(ctx -> {
                            var player = ctx.getSource().getPlayerOrException();
                            boolean on = player.entityTags().contains(StreetGuard.BUILDER) ? !player.removeTag(StreetGuard.BUILDER) : player.addTag(StreetGuard.BUILDER);
                            ctx.getSource().sendSuccess(() -> Component.literal("Builder mode " + (on ? "on" : "off")), true);
                            return on ? 1 : 0;
                        }))));
    }
}
