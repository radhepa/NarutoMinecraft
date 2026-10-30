package dev.shinobi.combat.runtime.client;

import dev.shinobi.combat.HandSign;
import dev.shinobi.combat.runtime.Fighter;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.client.input.MouseButtonEvent;
import net.minecraft.network.chat.Component;

/** The sign wheel: Rat at the top and clockwise (HandSign.radial); a click weaves the sign under the mouse, closing casts. */
final class RadialScreen extends Screen {
    static final int RADIUS = 70;

    RadialScreen() { super(Component.translatable("shinobi_combat.radial")); }

    @Override
    protected void init() {
        if (!ShinobiCombatClient.weaving) ShinobiCombatClient.send(Fighter.Act.BEGIN, 0);
        ShinobiCombatClient.weaving = true;
    }

    private HandSign at(double x, double y) { return HandSign.radial((x - width / 2.0) / RADIUS, (height / 2.0 - y) / RADIUS); }

    @Override
    public boolean mouseClicked(MouseButtonEvent e, boolean doubleClick) {
        if (e.button() == 1) { onClose(); return true; }
        var s = at(e.x(), e.y());
        if (s != null) ShinobiCombatClient.send(Fighter.Act.SIGN, s.ordinal());
        return true;
    }

    @Override
    public void extractRenderState(GuiGraphicsExtractor g, int mouseX, int mouseY, float delta) {
        super.extractRenderState(g, mouseX, mouseY, delta);
        var hover = at(mouseX, mouseY);
        for (var s : HandSign.values()) {
            double a = Math.toRadians(30 * s.ordinal());
            g.centeredText(font, Component.translatable("shinobi_combat.sign." + s.id()), width / 2 + (int) (Math.sin(a) * RADIUS),
                    height / 2 - (int) (Math.cos(a) * RADIUS) - 4, s == hover ? 0xFFFFD257 : 0xFFFFFFFF);
        }
        g.centeredText(font, title, width / 2, height / 2 + RADIUS + 16, 0xFFD0D0D0);
    }

    @Override public boolean isPauseScreen() { return false; }

    @Override
    public void removed() {
        ShinobiCombatClient.send(Fighter.Act.RELEASE, 0);
        ShinobiCombatClient.weaving = false;
    }
}
