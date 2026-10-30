package dev.shinobi.village.client;

import dev.shinobi.village.PlayerLooks;
import dev.shinobi.village.look.AgeStage;
import dev.shinobi.village.look.CreatorRules;
import dev.shinobi.village.look.Look;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayNetworking;
import net.minecraft.client.gui.GuiGraphicsExtractor;
import net.minecraft.client.gui.components.Button;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.client.gui.screens.inventory.InventoryScreen;
import net.minecraft.network.chat.Component;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.function.Function;
import java.util.function.UnaryOperator;

/**
 * The character creator a new player meets on first join: each button steps one choice of the clanless child look,
 * the player beside the buttons wears the look as it changes, and Done sends it to the server.
 */
public final class CreatorScreen extends Screen {
    /** The look the local player wears while the creator is open. */
    static volatile String preview;
    private Look look = PlayerLooks.rules.defaults(CreatorRules.CLANLESS, PlayerLooks.rules.bodies.getFirst());
    private final List<Runnable> relabel = new ArrayList<>();

    public CreatorScreen() {
        super(Component.translatable("narutominecraft.creator.title"));
        preview = PlayerLooks.json(look);
    }

    @Override
    protected void init() {
        relabel.clear();
        int x = width / 2 - 170, y = height / 2 - 75;
        var r = PlayerLooks.rules;
        row(x, y, "body", Look::body, l -> r.defaults(CreatorRules.CLANLESS, next(r.bodies, l.body())).withComplexion(l.complexion()));
        row(x, y += 24, "complexion", l -> String.valueOf(l.complexion() + 1), l -> l.withComplexion(next(r.complexions, l.complexion())));
        row(x, y += 24, "hair", Look::hair, l -> l.withHair(next(choices().hair(), l.hair())));
        row(x, y += 24, "hair_color", Look::hairColor, l -> l.withHairColor(next(PlayerLooks.hairColors(), l.hairColor())));
        row(x, y += 24, "outfit", Look::outfit, l -> {
            String o = next(choices().outfits().get(l.body()).stream().map(CreatorRules.Outfit::id).toList(), l.outfit());
            return l.withOutfit(o, choices().outfit(l.body(), o).palettes().getFirst());
        });
        row(x, y += 24, "palette", Look::palette, l -> l.withOutfit(l.outfit(), next(choices().outfit(l.body(), l.outfit()).palettes(), l.palette())));
        addRenderableWidget(Button.builder(Component.translatable("narutominecraft.creator.done"), b -> {
            ClientPlayNetworking.send(new PlayerLooks.SetLook(PlayerLooks.json(look)));
            onClose();
        }).bounds(x, y + 34, 180, 20).build());
    }

    private void row(int x, int y, String key, Function<Look, String> value, UnaryOperator<Look> step) {
        var button = addRenderableWidget(Button.builder(Component.empty(), b -> {
            look = step.apply(look);
            preview = PlayerLooks.json(look);
            relabel.forEach(Runnable::run);
        }).bounds(x, y, 180, 20).build());
        Runnable label = () -> button.setMessage(Component.translatable("narutominecraft.creator." + key, words(value.apply(look))));
        label.run();
        relabel.add(label);
    }

    private static CreatorRules.Choices choices() { return PlayerLooks.rules.choices(CreatorRules.CLANLESS, AgeStage.CHILD); }

    private static <T> T next(List<T> options, T current) { return options.get((options.indexOf(current) + 1) % options.size()); }

    /** A data id as words: "hg001_messy_mop" and "academy_genin.first_day" read "Messy mop" and "First day". */
    static String words(String id) {
        String s = id.substring(id.lastIndexOf('.') + 1).replaceFirst("^h[a-z]?\\d+_", "").replace('_', ' ').toLowerCase(Locale.ROOT);
        return s.isEmpty() ? id : Character.toUpperCase(s.charAt(0)) + s.substring(1);
    }

    @Override
    public void extractRenderState(GuiGraphicsExtractor g, int mouseX, int mouseY, float delta) {
        super.extractRenderState(g, mouseX, mouseY, delta);
        g.centeredText(font, title, width / 2, height / 2 - 100, 0xFFFFFFFF);
        if (minecraft.player != null)
            InventoryScreen.extractEntityInInventoryFollowsMouse(g, width / 2 + 40, height / 2 - 90, width / 2 + 170, height / 2 + 90,
                    70, 0.0625F, mouseX, mouseY, minecraft.player);
    }

    // A new player must pick; Done always sends an allowed look.
    @Override public boolean shouldCloseOnEsc() { return false; }
    @Override public boolean isPauseScreen() { return false; }

    @Override
    public void removed() { preview = null; }

    // The look may sync after the creator opened, or arrive from elsewhere: then there is nothing to create.
    @Override
    public void tick() { if (minecraft.player == null || minecraft.player.hasAttached(PlayerLooks.LOOK)) onClose(); }
}
