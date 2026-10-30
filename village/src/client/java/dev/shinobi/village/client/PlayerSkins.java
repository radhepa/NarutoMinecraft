package dev.shinobi.village.client;

import com.mojang.blaze3d.platform.NativeImage;
import dev.shinobi.village.PlayerLooks;
import dev.villagefriends.client.ResidentSkins;
import net.minecraft.client.Minecraft;
import net.minecraft.client.player.AbstractClientPlayer;
import net.minecraft.client.renderer.texture.DynamicTexture;
import net.minecraft.core.ClientAsset;
import net.minecraft.resources.Identifier;
import net.minecraft.world.entity.player.PlayerModelType;
import net.minecraft.world.entity.player.PlayerSkin;

import java.util.HashMap;
import java.util.Map;

/**
 * The player's skin from their look: Village Friends bakes the outfit as it does a resident's, and the player wears the
 * baked 64x64 skin at the atlas origin.
 * shortcut: the flat skin only, without VF's 3D garment pieces and eye planes, until a player model renders them.
 */
public final class PlayerSkins {
    private static final Map<String, Identifier> TEXTURES = new HashMap<>();
    /** Marks a look that does not bake (data changed between versions), so it is not retried every frame. */
    private static final Identifier BROKEN = Identifier.fromNamespaceAndPath("narutominecraft", "player_skin/broken");
    private static int next;

    private PlayerSkins() {}

    /** The skin for the player's look (or the creator's preview), or null to keep the account skin. */
    public static PlayerSkin skin(AbstractClientPlayer player, PlayerSkin account) {
        var mc = Minecraft.getInstance();
        String look = player == mc.player && CreatorScreen.preview != null ? CreatorScreen.preview : player.getAttached(PlayerLooks.LOOK);
        if (look == null) return null;
        var texture = TEXTURES.get(look);
        if (texture == BROKEN) return null;
        if (texture == null) {
            try {
                var l = PlayerLooks.parse(look);
                if (!(mc.getTextureManager().getTexture(ResidentSkins.texture(PlayerLooks.outfit(l), l.complexion())) instanceof DynamicTexture baked)
                        || baked.getPixels() == null) return null;   // VF's bodies are not loaded yet
                var image = new NativeImage(64, 64, true);
                for (int y = 0; y < 64; y++) for (int x = 0; x < 64; x++) image.setPixel(x, y, baked.getPixels().getPixel(x, y));
                // Creator previews make one texture per step; drop them all now and then.
                if (TEXTURES.size() > 64) clear();
                texture = Identifier.fromNamespaceAndPath("narutominecraft", "player_skin/" + Integer.toString(next++));
                Identifier id = texture;
                mc.getTextureManager().register(id, new DynamicTexture(() -> "Player look " + id, image));
                TEXTURES.put(look, id);
            } catch (RuntimeException e) {
                TEXTURES.put(look, BROKEN);
                return null;
            }
        }
        return new PlayerSkin(new ClientAsset.ResourceTexture(texture, texture), account.cape(), account.elytra(), PlayerModelType.WIDE, account.secure());
    }

    static void clear() {
        TEXTURES.values().stream().filter(id -> id != BROKEN).forEach(Minecraft.getInstance().getTextureManager()::release);
        TEXTURES.clear();
    }
}
