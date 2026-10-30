package dev.shinobi.village.client;

import dev.villagefriends.client.FriendshipScreen;
import dev.villagefriends.client.JournalScreen;
import dev.villagefriends.client.LedgerScreen;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import net.minecraft.client.gui.screens.ChatScreen;
import net.minecraft.client.gui.screens.inventory.ContainerScreen;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.contents.TranslatableContents;

import java.util.HashMap;
import java.util.Map;

/**
 * The Hidden Leaf look of the screens a player meets with residents: Village Friends' conversation window (its journal
 * tab too), village ledger and angler's journal, and the shop. VF's screens keep their layout and behaviour; every
 * colour they draw is swapped for washi paper, sumi ink, Konoha green and orange, and the mixins add scroll rods and
 * the leaf crest. The chat is LeafChat's own message scroll.
 * shortcut: VF's layout recoloured (no brush font is installed), until our own screens replace VF's.
 */
public final class LeafUi {
    public static final int PAPER = 0xFFF1E2BF, SHADE = 0xFFDCC594, WOOD = 0xFF4A2F1A, GREEN = 0xFF35582A, DEEP = 0xFF24391B,
            LEAF = 0xFF5E9A35, ORANGE = 0xFFE07A1F, ORANGE_LIGHT = 0xFFF2A65A, INK = 0xFF2A2017, FADED = 0xFF77654A, CHAT = 0x1C2E14;
    /** VF's palette (FriendshipScreen, LedgerScreen, JournalScreen) and the container label, to the Leaf's. */
    private static final Map<Integer, Integer> MAP = new HashMap<>();

    static {
        int[][] pairs = {
                {0xFF4E382B, INK}, {0xFF8B765C, FADED}, {0xFFFFF8E9, PAPER}, {0xFFF2E4C9, SHADE}, {0xFF5B3A29, GREEN},
                {0xFFB98A5E, ORANGE}, {0xFF55753F, 0xFF3F7A26}, {0xFFE0567A, ORANGE}, {0xFFFF9DB4, ORANGE_LIGHT},
                {0xFFE6D7C0, 0xFFD3BF91}, {0xFFFFF1F4, PAPER}, {0xFF2F8F3A, LEAF},
                // ledger: leather cover, row highlights, meters
                {0xFF5A2E1E, DEEP}, {0xFF7A3A26, GREEN}, {0xFFFBE3B2, 0xFFF5C98A}, {0xFFF6ECD8, 0xFFEAD7AE},
                {0xFFE3D6C0, SHADE}, {0xFFB8A58A, FADED}, {0xFFE3789E, ORANGE}, {0xFF6DB56A, LEAF}, {0xFF9DBF7C, 0xFF8DB05A},
                // angler's journal
                {0xFF3B2A1A, INK}, {0xFF7A6448, FADED}, {0xFF9A6A10, 0xFFB85E12},
                // container labels
                {0xFF404040, INK},
                // name ribbons and badges, one per personality or job, to dyed-cloth tones
                {0xFFE88A6E, 0xFFC8602A}, {0xFF7C9CCF, 0xFF4D6E8A}, {0xFFF0B84A, 0xFFD49A2A}, {0xFF5FAE8B, 0xFF3F7A56},
                {0xFFB08ACF, 0xFF7A5A8A}, {0xFF8DB062, 0xFF5E8A35}, {0xFF6E8E9E, 0xFF56707A}, {0xFFE07FA8, 0xFFB0505A},
                {0xFFB48A5F, 0xFF8A6238}, {0xFF5DA9C9, 0xFF3E7C8C}, {0xFFC96A5A, 0xFFA8452E}, {0xFFE3A1C0, 0xFFB8786A}};
        for (int[] p : pairs) {
            MAP.put(p[0], p[1]);
            MAP.putIfAbsent(darker(p[0]), darker(p[1]));   // VF shades ribbons and pills with its own darker()
        }
    }

    private LeafUi() {}

    /** VF's darker(): three quarters of each channel. */
    private static int darker(int c) { return 0xFF000000 | (c >> 16 & 255) * 3 / 4 << 16 | (c >> 8 & 255) * 3 / 4 << 8 | (c & 255) * 3 / 4; }

    /** Whether the shop window has this title: ShopMenu titles it with shinobi_life.shop.title. */
    public static boolean shop(Component title) {
        return title.getContents() instanceof TranslatableContents t && t.getKey().equals("shinobi_life.shop.title");
    }

    private static boolean skinned() {
        var s = Minecraft.getInstance().gui.screen();
        return s instanceof FriendshipScreen || s instanceof LedgerScreen || s instanceof JournalScreen || s instanceof ContainerScreen c && shop(c.getTitle());
    }

    private static boolean chatting() { return Minecraft.getInstance().gui.screen() instanceof ChatScreen; }

    /** A fill colour: the chat screen's black input box turns leaf green (alpha kept); VF's palette turns the Leaf's. */
    public static int fill(int argb) {
        if ((argb & 0xFFFFFF) == 0 && argb != 0 && chatting()) return argb & 0xFF000000 | CHAT;
        return text(argb);
    }

    public static int text(int argb) {
        if (!MAP.containsKey(argb) || !skinned()) return argb;
        return MAP.get(argb);
    }

    /** The Konoha leaf crest, 9 pixels square: an orange swirl outlined in green. */
    private static final String[] CREST = {
            "..GGGGG..",
            ".GOOOOOG.",
            "GOOGGGOOG",
            "GOG...GOG",
            "GOG.G.GOG",
            "GOG..GGOG",
            "GOOG...G.",
            ".GOOGGG..",
            "..GGG.GOG"};

    public static void crest(GuiGraphicsExtractor g, int x, int y) {
        for (int row = 0; row < CREST.length; row++) for (int col = 0; col < 9; col++) {
            char c = CREST[row].charAt(col);
            if (c != '.') g.fill(x + col, y + row, x + col + 1, y + row + 1, c == 'G' ? DEEP : ORANGE);
        }
    }

    /** A scroll's wooden roller standing beside a panel, with orange end caps. */
    public static void rod(GuiGraphicsExtractor g, int x, int y, int h) {
        g.fill(x + 1, y - 3, x + 5, y, ORANGE);
        g.fill(x + 1, y + h, x + 5, y + h + 3, ORANGE);
        g.fill(x, y, x + 6, y + h, WOOD);
        g.fill(x + 1, y, x + 2, y + h, 0xFF7A5434);
        g.fill(x + 4, y, x + 6, y + h, 0xFF33200F);
    }

    /** The shop counter: paper on a green frame, sunken wells under the slots, a rope between shelf and pack, the crest. */
    public static void counter(GuiGraphicsExtractor g, int left, int top, int w, int h, int shelfBottom, Iterable<int[]> slots) {
        g.fill(left - 2, top - 2, left + w + 2, top + h + 2, DEEP);
        g.fill(left, top, left + w, top + h, GREEN);
        g.fill(left + 3, top + 3, left + w - 3, top + h - 3, PAPER);
        g.fill(left + 3, top + 3, left + w - 3, top + 14, SHADE);
        g.fill(left + 3, top + 14, left + w - 3, top + 15, ORANGE);
        for (int[] s : slots) {
            g.fill(left + s[0] - 1, top + s[1] - 1, left + s[0] + 17, top + s[1] + 17, 0xFFB89C66);
            g.fill(left + s[0], top + s[1], left + s[0] + 16, top + s[1] + 16, 0xFFE9D4A4);
        }
        for (int x = left + 6; x < left + w - 6; x += 4) g.fill(x, top + shelfBottom, x + 3, top + shelfBottom + 1, ORANGE);
        crest(g, left + w - 14, top + 4);
    }
}
