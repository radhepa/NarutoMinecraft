package dev.shinobi.combat.runtime.client;

import com.mojang.blaze3d.platform.InputConstants;
import dev.shinobi.combat.HandSign;
import dev.shinobi.combat.runtime.Fighter;
import dev.shinobi.combat.runtime.ShinobiCombat;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.fabric.api.client.event.lifecycle.v1.ClientTickEvents;
import net.fabricmc.fabric.api.client.keymapping.v1.KeyMappingHelper;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayNetworking;
import net.fabricmc.fabric.api.client.rendering.v1.RenderStateDataKey;
import net.fabricmc.fabric.api.client.rendering.v1.hud.HudElementRegistry;
import net.fabricmc.fabric.api.client.rendering.v1.hud.VanillaHudElements;
import net.minecraft.client.DeltaTracker;
import net.minecraft.client.KeyMapping;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;

import java.util.stream.Collectors;

/**
 * Shinobi Combat's client (P06-2): the Shinobi keys (Options > Controls, rebindable), sent to the server as actions; the
 * chakra and stamina bars, the signs woven and the hint on the HUD; and every player's synced clip on its model.
 * shortcut: Weave is held (no toggle) and there are no quick slots or auto-sign, until the settings screen.
 */
public final class ShinobiCombatClient implements ClientModInitializer {
    static final KeyMapping.Category SHINOBI = KeyMapping.Category.register(Identifier.fromNamespaceAndPath(ShinobiCombat.MOD_ID, "shinobi"));
    // COMBAT.md: Weave R, the signs 1 to 0, - and =, Dodge Left Alt, block with right click, the wheel J and substitution N (keys vanilla leaves free).
    public static final KeyMapping WEAVE = key("weave", InputConstants.KEY_R), RADIAL = key("radial", InputConstants.KEY_J),
            GUARD = KeyMappingHelper.registerKeyMapping(new KeyMapping("key.shinobi_combat.guard", InputConstants.Type.MOUSE, InputConstants.MOUSE_BUTTON_RIGHT, SHINOBI)),
            DODGE = key("dodge", InputConstants.KEY_LALT), SUBSTITUTE = key("substitute", InputConstants.KEY_N);
    /** The twelve sign keys, read while Weave is held; signs 1 to 9 share the hotbar keys, which do not switch slots while weaving. */
    public static final KeyMapping[] SIGNS = new KeyMapping[12];
    static {
        int[] keys = {InputConstants.KEY_1, InputConstants.KEY_2, InputConstants.KEY_3, InputConstants.KEY_4, InputConstants.KEY_5, InputConstants.KEY_6,
                InputConstants.KEY_7, InputConstants.KEY_8, InputConstants.KEY_9, InputConstants.KEY_0, InputConstants.KEY_MINUS, InputConstants.KEY_EQUALS};
        for (int i = 0; i < 12; i++) SIGNS[i] = key("sign_" + (i + 1), keys[i]);
    }
    /** The clip an avatar plays (Fighter.Stance) and how many ticks in. */
    public static final RenderStateDataKey<String> CLIP = RenderStateDataKey.create(() -> "shinobi_combat:clip");
    public static final RenderStateDataKey<Float> AGE = RenderStateDataKey.create(() -> "shinobi_combat:age");
    static boolean weaving, guarding;

    private static KeyMapping key(String name, int key) {
        return KeyMappingHelper.registerKeyMapping(new KeyMapping("key.shinobi_combat." + name, key, SHINOBI));
    }

    @Override
    public void onInitializeClient() {
        // At the start of the tick, before the hotbar keys are read: while weaving they are signs.
        ClientTickEvents.START_CLIENT_TICK.register(ShinobiCombatClient::tick);
        HudElementRegistry.attachElementAfter(VanillaHudElements.HOTBAR, Identifier.fromNamespaceAndPath(ShinobiCombat.MOD_ID, "hud"), ShinobiCombatClient::hud);
    }

    static void send(int action, int arg) { if (ClientPlayNetworking.canSend(Fighter.Act.TYPE)) ClientPlayNetworking.send(new Fighter.Act(action, arg)); }

    private static void tick(Minecraft mc) {
        if (mc.player == null || !ClientPlayNetworking.canSend(Fighter.Act.TYPE)) { weaving = guarding = false; return; }
        if (mc.gui.screen() instanceof RadialScreen) return;
        // On the Use button (the default) only an empty hand guards, so a held kunai still throws and food still eats.
        boolean free = mc.gui.screen() == null, hold = free && WEAVE.isDown(),
                guard = free && GUARD.isDown() && !(GUARD.same(mc.options.keyUse) && !mc.player.getMainHandItem().isEmpty());
        // Letting go of Weave casts; a screen opening mid-weave (a menu, death) drops it.
        if (hold != weaving) send(hold ? Fighter.Act.BEGIN : free ? Fighter.Act.RELEASE : Fighter.Act.CANCEL, 0);
        weaving = hold;
        for (int i = 0; i < 12; i++) {
            while (SIGNS[i].consumeClick()) if (weaving) send(Fighter.Act.SIGN, i);
            if (weaving && i < 9) while (mc.options.keyHotbarSlots[i].consumeClick()) {}
        }
        if (guard != guarding) send(Fighter.Act.GUARD, guard ? 1 : 0);
        guarding = guard;
        while (DODGE.consumeClick()) send(Fighter.Act.DODGE, 0);
        while (SUBSTITUTE.consumeClick()) send(Fighter.Act.SUBSTITUTE, 0);
        while (RADIAL.consumeClick()) mc.setScreenAndShow(new RadialScreen());
    }

    /** The chakra and stamina bars at the top left, and while weaving the signs so far and what they could become. */
    private static void hud(GuiGraphicsExtractor g, DeltaTracker delta) {
        var mc = Minecraft.getInstance();
        if (mc.player == null) return;
        var s = mc.player.getAttached(ShinobiCombat.STATE);
        if (s == null) return;
        bar(g, 8, 8, s.chakra() / Fighter.CHAKRA, 0xFF3A7BD5);
        bar(g, 8, 18, s.stamina() / Fighter.STAMINA, 0xFF5FA55A);
        g.text(mc.font, Component.translatable("shinobi_combat.hud.chakra", (int) s.chakra()), 94, 7, 0xFFFFFFFF);
        g.text(mc.font, Component.translatable("shinobi_combat.hud.stamina", (int) s.stamina()), 94, 17, 0xFFFFFFFF);
        var st = mc.player.getAttached(ShinobiCombat.STANCE);
        if (st == null || st.pose() != Fighter.Stance.WEAVING) return;
        var woven = HandSign.sequence(st.signs());
        g.text(mc.font, woven.stream().map(h -> Component.translatable("shinobi_combat.sign." + h.id()).getString()).collect(Collectors.joining(" - ", "> ", "")), 8, 30, 0xFFFFD257);
        var hint = Fighter.book(s.learned()).candidates(woven);
        if (!hint.isEmpty())
            g.text(mc.font, Component.translatable("shinobi_combat.hud.hint", hint.stream().map(id -> ShinobiCombat.data.technique(id).name()).collect(Collectors.joining(", "))), 8, 41, 0xFFD0D0D0);
    }

    private static void bar(GuiGraphicsExtractor g, int x, int y, double fraction, int color) {
        g.fill(x - 1, y - 1, x + 81, y + 6, 0xA0000000);
        g.fill(x, y, x + (int) Math.round(80 * Math.clamp(fraction, 0, 1)), y + 5, color);
    }
}
