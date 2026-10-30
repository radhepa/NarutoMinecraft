package dev.shinobi.village;

import com.google.gson.Gson;
import com.mojang.serialization.Codec;
import dev.shinobi.village.look.AgeStage;
import dev.shinobi.village.look.CreatorRules;
import dev.shinobi.village.look.Json;
import dev.shinobi.village.look.Look;
import dev.villagefriends.outfit.Gender;
import dev.villagefriends.outfit.MasterPalettes;
import dev.villagefriends.outfit.Outfit;
import dev.villagefriends.outfit.PaletteID;
import dev.villagefriends.outfit.Profession;
import dev.villagefriends.outfit.Wardrobe;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentSyncPredicate;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.fabricmc.fabric.api.networking.v1.PayloadTypeRegistry;
import net.fabricmc.fabric.api.networking.v1.ServerPlayNetworking;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.common.custom.CustomPacketPayload;
import net.minecraft.resources.Identifier;
import net.minecraft.server.level.ServerPlayer;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/**
 * The player's look (P05-1): picked once in the creator from the clanless child choices, checked by the server against
 * the creator rules, kept on the player and synced so every client draws it as the player's skin.
 * shortcut: the look only, with default Roots and no restyle, until the full creator flow of CHARACTER_CREATION.md.
 */
public final class PlayerLooks {
    /** The chosen look as JSON (Look.toMap); absent until the player has made a character. */
    public static final AttachmentType<String> LOOK = AttachmentRegistry.create(Identifier.fromNamespaceAndPath("narutominecraft", "look"),
            b -> b.persistent(Codec.STRING).copyOnDeath().syncWith(ByteBufCodecs.STRING_UTF8, AttachmentSyncPredicate.all()));
    public static CreatorRules rules;

    /** The creator's submission: one look as JSON. */
    public record SetLook(String look) implements CustomPacketPayload {
        public static final Type<SetLook> TYPE = new Type<>(Identifier.fromNamespaceAndPath("narutominecraft", "set_look"));
        public static final StreamCodec<FriendlyByteBuf, SetLook> CODEC = StreamCodec.of(
                (buf, value) -> buf.writeUtf(value.look, 2048), buf -> new SetLook(buf.readUtf(2048)));
        @Override public Type<? extends CustomPacketPayload> type() { return TYPE; }
    }

    private PlayerLooks() {}

    static void register() {
        try {
            rules = CreatorRules.load(FabricLoader.getInstance().getModContainer("narutominecraft").orElseThrow()
                    .findPath("data/narutominecraft/creator/creator.json").orElseThrow());
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
        PayloadTypeRegistry.serverboundPlay().register(SetLook.TYPE, SetLook.CODEC);
        ServerPlayNetworking.registerGlobalReceiver(SetLook.TYPE, (payload, context) -> choose(context.player(), payload.look()));
    }

    /** Keeps a look the player has not yet chosen one and the rules allow; false otherwise. */
    public static boolean choose(ServerPlayer player, String json) {
        if (player.hasAttached(LOOK)) return false;
        Look look;
        try {
            // A client's JSON may hold wrong types (marks of numbers) that fail only while the rules read them.
            look = parse(json);
            if (!allowed(look)) return false;
        } catch (RuntimeException e) {
            return false;
        }
        player.setAttached(LOOK, json(look));
        return true;
    }

    /** The creator rules for a clanless child, plus the colours and pieces Village Friends can draw. */
    public static boolean allowed(Look look) {
        if (!rules.validate(CreatorRules.CLANLESS, AgeStage.CHILD, look).isEmpty() || !drawn(look.hairColor())) return false;
        try {
            outfit(look);
            return true;
        } catch (RuntimeException e) {
            return false;
        }
    }

    /** Whether Village Friends has the hair colour. shortcut: VF's ten colours only, until the Leaf hair colours reach VF. */
    public static boolean drawn(String hairColor) {
        return Wardrobe.HAIR_COLORS.stream().anyMatch(c -> c.id().equals(hairColor));
    }

    /**
     * The look as a Village Friends outfit, for baking the skin.
     * shortcut: the Leaf palette picks one of VF's ten master palettes by its name's hash, until the Leaf palettes reach VF.
     */
    public static Outfit outfit(Look look) {
        var o = rules.outfit(look.outfit());
        var palettes = PaletteID.values();
        return new Outfit(Gender.valueOf(look.body().toUpperCase(Locale.ROOT)), Profession.NONE,
                MasterPalettes.get(palettes[Math.floorMod(look.palette().hashCode(), palettes.length)]), Wardrobe.get(look.hair()),
                Wardrobe.hairColor(look.hairColor()), Wardrobe.get(o.top()), Wardrobe.get(o.bottom()),
                Wardrobe.template(look.outfit().replace('.', '/')));
    }

    @SuppressWarnings("unchecked")
    public static Look parse(String json) { return Look.fromMap((Map<String, Object>) Json.parse(json)); }

    public static String json(Look look) { return new Gson().toJson(look.toMap()); }

    /** The creator's opening look, as tests choose it to skip the screen. */
    public static String defaultLook() { return json(rules.defaults(CreatorRules.CLANLESS, rules.bodies.getFirst())); }

    /** The hair colours the creator offers for the clanless child. */
    public static List<String> hairColors() {
        return rules.choices(CreatorRules.CLANLESS, AgeStage.CHILD).hairColors().stream().filter(PlayerLooks::drawn).toList();
    }
}
