package dev.shinobi.village;

import com.mojang.serialization.Codec;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerLifecycleEvents;
import net.minecraft.commands.Commands;
import net.minecraft.core.BlockPos;
import net.minecraft.core.UUIDUtil;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Map;
import java.util.UUID;

/** Shinobi Village's entrypoint: the Konoha blocks, the street's protection and the builder's commands. */
public final class ShinobiVillage implements ModInitializer {
    public static final Logger LOG = LoggerFactory.getLogger("Shinobi Village");
    /** The map's named anchors (marker type to position), saved with the level: quests find their places here. */
    public static final AttachmentType<Map<String, BlockPos>> ANCHORS = AttachmentRegistry.create(
            Identifier.fromNamespaceAndPath("narutominecraft", "anchors"), b -> b.persistent(Codec.unboundedMap(Codec.STRING, BlockPos.CODEC)));
    /**
     * The residents quests can name, saved with the level: {@code role:<name>} for a marker's bound role and
     * {@code job:<name>} for its job. shortcut: one resident per role or job (the last placed), until the cast's
     * role identities (P03 queue, item 3).
     */
    public static final AttachmentType<Map<String, UUID>> ROLES = AttachmentRegistry.create(
            Identifier.fromNamespaceAndPath("narutominecraft", "roles"), b -> b.persistent(Codec.unboundedMap(Codec.STRING, UUIDUtil.CODEC)));

    @Override
    public void onInitialize() {
        KonohaBlocks.register();
        StreetGuard.register();
        PlayerLooks.register();
        ServerLifecycleEvents.SERVER_STARTED.register(TestStreet::firstStart);
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
