package dev.shinobi.village.client;

import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.components.ChatComponent;
import net.minecraft.client.multiplayer.chat.GuiMessage;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.Style;
import net.minecraft.util.FormattedCharSequence;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.function.Predicate;
import java.util.regex.Pattern;

/**
 * The Hidden Leaf message scroll that replaces Minecraft's chat: each message is a card on a lacquered panel framed in
 * wood, a speaker's line carries an orange name plate and writes itself out letter by letter, and a line of answers
 * (clickable text) sits on its own orange-edged card. It draws through the chat's own graphics access, so links, hover
 * and the chat screen's clicks still land on the right text.
 * shortcut: no tag icons, queue or restricted-chat prompt, scrolling counts whole messages and each frame lays the cards
 * out again, until players need them or a profile shows the chat.
 */
public final class LeafChat {
    /** "Name: rest" at the start of a plain line: the speaker of a story or resident line. */
    private static final Pattern SPEAKER = Pattern.compile("^([^:\"§\\[<>]{1,32}): (.+)$", Pattern.DOTALL);
    private static final int LINE = 9, PAD = 4, PLATE = 11, GAP = 3, LACQUER = 0x1A2614, CARD = 0x2A3A1F, FADE_TICKS = 200;

    private LeafChat() {}

    /** One message laid out: its name plate (or null), wrapped lines, whether it is an answer card, its fade and height. */
    private record Card(String speaker, List<FormattedCharSequence> lines, boolean answers, float alpha, int height) {}

    public static void draw(ChatComponent.ChatGraphicsAccess g, int guiHeight, int tick, ChatComponent.DisplayMode mode, List<GuiMessage> messages,
                            Predicate<GuiMessage> visible, int scroll, float scale, int width, int linesPerPage) {
        var font = Minecraft.getInstance().font;
        int inner = width - 2 * PAD - 4, bottom = (int) Math.floor((guiHeight - 40) / scale), room = (linesPerPage + 2) * LINE;
        var cards = new ArrayList<Card>();
        int used = 0, skipped = 0;
        for (var m : messages) {   // newest first
            if (!visible.test(m)) continue;
            if (skipped++ < scroll) continue;
            float alpha = mode.foreground ? 1 : fade(tick - m.addedTime());
            if (alpha <= 0.01f) break;
            String speaker = null;
            Component body = m.content();
            boolean answers = clickable(body);
            var who = SPEAKER.matcher(body.getString());
            if (!answers && body.getSiblings().isEmpty() && who.matches()) {   // one plain style, so retyping it loses nothing
                speaker = who.group(1);
                String said = who.group(2);
                int age = tick - m.addedTime();
                if (age >= 0 && age * 2 < said.length()) said = said.substring(0, age * 2);   // writes itself out, two letters a tick
                body = Component.literal(said).withStyle(body.getStyle());
            }
            var lines = font.split(body, inner);
            int h = lines.size() * LINE + 2 * GAP + (speaker == null ? 0 : PLATE - 2);
            if (used + h > room && !cards.isEmpty()) break;
            cards.add(new Card(speaker, lines, answers, alpha, h));
            used += h + 2;
            if (!mode.foreground && cards.size() >= 4) break;
        }
        if (cards.isEmpty()) return;
        g.updatePose(p -> p.scale(scale, scale));
        float top = 0;
        for (var c : cards) top = Math.max(top, c.alpha);
        int y = bottom - used - PAD;
        // the panel: a wood frame, orange corner bands and dark lacquer
        int a = (int) (top * 255) << 24, frame = a | (LeafUi.WOOD & 0xFFFFFF);
        g.fill(-2, y - 2, width + 2, bottom + 2, frame);
        g.fill(0, y, width, bottom, (int) (top * 0.85f * 255) << 24 | LACQUER);
        g.fill(-2, y - 2, 10, y - 1, a | (LeafUi.ORANGE & 0xFFFFFF));
        g.fill(width - 10, bottom + 1, width + 2, bottom + 2, a | (LeafUi.ORANGE & 0xFFFFFF));
        int cy = bottom - PAD;
        for (var c : cards) {
            cy -= c.height;
            int ca = (int) (c.alpha * 255) << 24;
            g.fill(PAD, cy, width - PAD, cy + c.height, ca | (c.answers ? 0x3A2A12 : CARD));
            g.fill(PAD, cy, PAD + 2, cy + c.height, ca | ((c.answers ? LeafUi.ORANGE : LeafUi.LEAF) & 0xFFFFFF));
            int ty = cy + GAP;
            if (c.speaker != null) {
                int w = font.width(c.speaker) + 8;
                g.fill(PAD + 4, cy - 3, PAD + 4 + w, cy + PLATE - 4, ca | (LeafUi.ORANGE & 0xFFFFFF));
                g.fill(PAD + 4, cy + PLATE - 4, PAD + 4 + w, cy + PLATE - 3, ca | (LeafUi.DEEP & 0xFFFFFF));
                text(g, PAD + 8, cy - 2, c.alpha, Component.literal(c.speaker).withColor(LeafUi.INK & 0xFFFFFF).getVisualOrderText());
                ty += PLATE - 2;
            }
            for (var line : c.lines) {
                text(g, PAD + 6, ty, c.alpha, line);
                ty += LINE;
            }
            cy -= 2;
        }
    }

    /** handleMessage draws at x 0, so the pose moves over for it and back. */
    private static void text(ChatComponent.ChatGraphicsAccess g, int x, int y, float alpha, FormattedCharSequence line) {
        g.updatePose(p -> p.translate(x, 0));
        g.handleMessage(y, alpha, line);
        g.updatePose(p -> p.translate(-x, 0));
    }

    /** Vanilla's fade: full for 8 seconds, then out over the last 2. */
    private static float fade(int age) {
        double t = Math.clamp((1 - age / (double) FADE_TICKS) * 10, 0, 1);
        return (float) (t * t * (Minecraft.getInstance().options.chatOpacity().get() * .9 + .1));
    }

    private static boolean clickable(Component c) {
        return c.visit((Style s, String text) -> s.getClickEvent() != null ? Optional.of(true) : Optional.empty(), Style.EMPTY).orElse(false);
    }
}
