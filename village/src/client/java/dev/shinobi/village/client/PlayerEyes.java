package dev.shinobi.village.client;

import com.mojang.blaze3d.vertex.PoseStack;
import dev.shinobi.village.PlayerLooks;
import dev.shinobi.village.mixin.client.ResidentModelAccess;
import dev.villagefriends.ResidentMotion;
import dev.villagefriends.client.ResidentModel;
import dev.villagefriends.client.ResidentRenderState;
import dev.villagefriends.client.ResidentSkins;
import dev.villagefriends.outfit.Outfit;
import net.minecraft.client.Minecraft;
import net.minecraft.client.model.player.PlayerModel;
import net.minecraft.client.player.AbstractClientPlayer;
import net.minecraft.client.renderer.SubmitNodeCollector;
import net.minecraft.client.renderer.entity.LivingEntityRenderer;
import net.minecraft.client.renderer.entity.RenderLayerParent;
import net.minecraft.client.renderer.entity.layers.RenderLayer;
import net.minecraft.client.renderer.entity.state.AvatarRenderState;
import net.minecraft.client.renderer.rendertype.RenderTypes;
import net.minecraft.resources.Identifier;

import java.util.HashMap;
import java.util.Map;

/**
 * The player's face as a resident's: Village Friends' eye, brow, blush and mouth planes on the player's head, from the
 * same baked outfit texture, blinking and styled as VF animates a resident's face. Draws for any player with a look,
 * and in the creator's preview.
 * shortcut: one face model per layer, so players drawn in one frame share the last one's blink, until a server has
 * several players with looks in view.
 */
public final class PlayerEyes extends RenderLayer<AvatarRenderState, PlayerModel> {
    private static final String[] FACE = {"eye0", "eye1", "brow0", "brow1", "browTail0", "browTail1", "blush0", "blush1", "mouth", "lips"};
    private record Face(Outfit outfit, Identifier texture) {}
    private static final Map<String, Face> FACES = new HashMap<>();
    private final ResidentModel face = new ResidentModel(false);
    private final ResidentRenderState state = new ResidentRenderState();

    public PlayerEyes(RenderLayerParent<AvatarRenderState, PlayerModel> parent) { super(parent); }

    @Override
    public void submit(PoseStack pose, SubmitNodeCollector out, int light, AvatarRenderState s, float yRot, float xRot) {
        if (s.isInvisible || !(Minecraft.getInstance().level != null && Minecraft.getInstance().level.getEntity(s.id) instanceof AbstractClientPlayer player)) return;
        String look = PlayerSkins.look(player);
        if (look == null) return;
        if (FACES.size() > 64) FACES.clear();   // creator previews make one look per step
        var f = FACES.computeIfAbsent(look, json -> {
            try {
                var l = PlayerLooks.parse(json);
                var outfit = PlayerLooks.outfit(l);
                return new Face(outfit, ResidentSkins.texture(outfit, l.complexion()));
            } catch (RuntimeException e) {
                return new Face(null, null);
            }
        });
        if (f.outfit == null) return;
        state.outfit = f.outfit;
        state.motionSeed = ResidentMotion.seed(player.getUUID());
        state.ageInTicks = s.ageInTicks;
        ((ResidentModelAccess) (Object) face).narutominecraft$animateFace(state);
        pose.pushPose();
        getParentModel().head.translateAndRotate(pose);
        var type = RenderTypes.entityTranslucent(f.texture);
        int overlay = LivingEntityRenderer.getOverlayCoords(s, 0);
        for (String part : FACE) out.submitModelPart(face.head.getChild(part), pose, type, light, overlay, null);
        pose.popPose();
    }
}
