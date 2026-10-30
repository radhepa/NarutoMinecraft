package dev.shinobi.life;

import dev.shinobi.life.economy.Catalogue;
import net.minecraft.ChatFormatting;
import net.minecraft.core.Holder;
import net.minecraft.core.component.DataComponents;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.SimpleContainer;
import net.minecraft.world.SimpleMenuProvider;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.inventory.ChestMenu;
import net.minecraft.world.inventory.ContainerInput;
import net.minecraft.world.inventory.MenuType;
import net.minecraft.world.inventory.Slot;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.SpawnEggItem;
import net.minecraft.world.item.component.ItemLore;

import java.util.ArrayList;
import java.util.List;

/**
 * The shop screen (ITEMS.md, How buying works): the shelves of a keeper's shops that are open now, each line with its
 * price, what is left and its shop, and the player's purse in the corner. Clicking a line buys one; the server checks
 * the hours, the shelf, the stock, the wallet and room in the pack ({@link ShinobiLife#buy}). Nothing in it can be taken
 * or put in, and it closes when the player walks away from the keeper.
 * shortcut: a vanilla chest window, buying only, at most 45 lines, until the shop counter block and Shinobi Life's own
 * screen with sell and order buttons.
 */
public final class ShopMenu extends ChestMenu {
    /** One line of the window: its shop, an item or service id, and the shelf line (null for a service). */
    public record Offer(String shop, String id, Catalogue.Line line) {}
    static final int ROWS = 6, LINES = 45, PURSE = ROWS * 9 - 1;
    private final ServerPlayer player;
    private final Entity keeper;
    private final List<Offer> offers;

    private ShopMenu(int id, ServerPlayer player, Entity keeper, List<Offer> offers) {
        super(MenuType.GENERIC_9x6, id, player.getInventory(), new SimpleContainer(ROWS * 9), ROWS);
        this.player = player;
        this.keeper = keeper;
        this.offers = offers;
        refresh();
    }

    /**
     * Opens the window, titled with the keeper's own shop (the first), on the keeper's shops that are open now; with all
     * of them shut, says so politely and opens nothing.
     */
    public static boolean open(ServerPlayer player, Entity keeper, List<String> shops) {
        var open = shops.stream().filter(s -> ShinobiLife.open(player.level(), s)).toList();
        if (open.isEmpty()) {
            if (!shops.isEmpty()) player.sendSystemMessage(ShinobiLife.shut(player.level(), shops.getFirst()));
            return false;
        }
        var offers = new ArrayList<Offer>();
        for (String shop : open) {
            // A line two shops sell is bought from the first.
            for (var line : ShinobiLife.shelf(player, shop))
                if (offers.stream().noneMatch(o -> o.id().equals(line.item()))) offers.add(new Offer(shop, line.item(), line));
            for (var service : ShinobiLife.services(shop)) offers.add(new Offer(shop, service.id(), null));
        }
        var lines = List.copyOf(offers.subList(0, Math.min(LINES, offers.size())));
        player.openMenu(new SimpleMenuProvider((id, inv, p) -> new ShopMenu(id, player, keeper, lines), Component.translatable("shinobi_life.shop.title", ShinobiLife.catalogue.shops.get(shops.getFirst()).name())));
        return true;
    }

    public List<Offer> offers() { return offers; }

    /** Draws each line with its price, what is left and its shop, and the purse. */
    void refresh() {
        var box = getContainer();
        for (int i = 0; i < offers.size(); i++) {
            var o = offers.get(i);
            var shop = ShinobiLife.catalogue.shops.get(o.shop());
            ItemStack stack;
            int price, left;
            if (o.line() == null) {
                var service = ShinobiLife.catalogue.services.get(o.id());
                stack = new ItemStack(SpawnEggItem.byId(ShinobiLife.PETS.get(o.id())).map(Holder::value).orElse(Items.EGG));
                stack.set(DataComponents.CUSTOM_NAME, Component.literal(service.effect()));
                price = service.price();
                left = Integer.MAX_VALUE;
            } else {
                stack = new ItemStack(ShinobiLife.item(o.id()));
                price = ShinobiLife.price(o.shop(), o.id());
                left = ShinobiLife.left(player.level(), o.shop(), o.line());
            }
            stack.set(DataComponents.LORE, new ItemLore(List.of(
                    Component.translatable("shinobi_life.shop.price", price).withStyle(ChatFormatting.GOLD),
                    (left == Integer.MAX_VALUE ? Component.translatable("shinobi_life.shop.plenty")
                            : left > 0 ? Component.translatable("shinobi_life.shop.left", left) : Component.translatable("shinobi_life.shop.none_left"))
                            .withStyle(left > 0 ? ChatFormatting.GREEN : ChatFormatting.RED),
                    Component.literal(shop.name()).withStyle(ChatFormatting.GRAY))));
            box.setItem(i, stack);
        }
        var purse = new ItemStack(Items.GOLD_NUGGET);
        purse.set(DataComponents.CUSTOM_NAME, Component.translatable("shinobi_life.shop.purse", ShinobiLife.ryo(player)).withStyle(ChatFormatting.YELLOW));
        box.setItem(PURSE, purse);
    }

    /** A click on a line buys one and redraws the window, bought or not; any other click in it does nothing. The pack below works as usual. */
    @Override
    public void clicked(int slot, int button, ContainerInput input, Player who) {
        if (slot >= 0 && slot < ROWS * 9) {
            if (input == ContainerInput.PICKUP && slot < offers.size()) {
                ShinobiLife.buy(player, offers.get(slot).shop(), offers.get(slot).id());
                refresh();
            }
            return;
        }
        super.clicked(slot, button, input, who);
    }

    @Override
    public ItemStack quickMoveStack(Player who, int slot) { return ItemStack.EMPTY; }

    @Override
    public boolean canTakeItemForPickAll(ItemStack stack, Slot slot) { return slot.container != getContainer() && super.canTakeItemForPickAll(stack, slot); }

    @Override
    public boolean stillValid(Player who) { return keeper.isAlive() && who.closerThan(keeper, 8); }
}
