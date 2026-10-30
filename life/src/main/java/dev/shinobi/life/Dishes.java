package dev.shinobi.life;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import dev.shinobi.life.economy.Catalogue;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.component.Consumables;
import net.minecraft.world.level.Level;

/**
 * The Leaf dishes (ITEMS.md, "Leaf dishes"): every Beta 1 food of the item data, edible, with its hunger values and
 * its short buff. Ramen ({@code chakra+N%}) and dango ({@code regen+N%}) speed chakra regen for the dish's {@code time}
 * seconds; tea ({@code fatigue-60m}) puts tonight's fatigue off an hour; a proper meal halves fatigue's slowdown for an hour.
 * shortcut: ramen speeds regen rather than restoring chakra at once, no VF Well Fed tier, and dishes without an authored
 * sprite show their tint's base sprite or a vanilla food, until tools/items/sprites.py draws them.
 */
public final class Dishes {
    /** What the last dish gave, in game ticks: a chakra regen bonus until one tick, a meal's halved slowdown until another. */
    public record Fed(double regen, long until, long meal) {
        static final Codec<Fed> CODEC = RecordCodecBuilder.create(i -> i.group(Codec.DOUBLE.fieldOf("regen").forGetter(Fed::regen),
                Codec.LONG.fieldOf("until").forGetter(Fed::until), Codec.LONG.fieldOf("meal").forGetter(Fed::meal)).apply(i, Fed::new));
    }
    /** A dish's buff, read once from its {@code buff}, {@code time} and {@code meal} props. */
    record Buff(double regen, int seconds, boolean tea, boolean meal) {}

    public static final AttachmentType<Fed> FED = AttachmentRegistry.create(Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, "fed"),
            b -> b.persistent(Fed.CODEC).initializer(() -> new Fed(0, 0, 0)));
    /** A game hour, how long a meal halves the slowdown. */
    static final int HOUR = 1000;
    private Dishes() {}

    /** Registers each Beta 1 food; an unknown buff stops the load, naming the dish. */
    static void register(Catalogue catalogue) {
        for (var dish : catalogue.items.values()) {
            if (!"food".equals(dish.category()) || !"beta1".equals(dish.slice())) continue;
            var buff = buff(dish);
            boolean tea = "tea".equals(dish.group());
            var food = new FoodProperties.Builder().nutrition(Integer.parseInt(dish.prop("food"))).saturationModifier(Float.parseFloat(dish.prop("sat")));
            if (tea) food.alwaysEdible();
            var id = Identifier.fromNamespaceAndPath(ShinobiLife.MOD_ID, dish.id());
            Registry.register(BuiltInRegistries.ITEM, id, new Item(new Item.Properties().setId(ResourceKey.create(Registries.ITEM, id)).stacksTo(dish.stack())
                    .food(food.build(), tea ? Consumables.DEFAULT_DRINK : Consumables.DEFAULT_FOOD)) {
                @Override
                public ItemStack finishUsingItem(ItemStack stack, Level level, LivingEntity user) {
                    if (user instanceof ServerPlayer p) eaten(p, buff, stack.getHoverName());
                    return super.finishUsingItem(stack, level, user);
                }
            });
        }
    }

    static Buff buff(Catalogue.Item dish) {
        double regen = 0;
        boolean tea = false;
        for (String b : dish.prop("buff").split(",")) {
            if (b.isEmpty()) continue;
            if (b.equals("fatigue-60m")) tea = true;
            else if ((b.startsWith("chakra+") || b.startsWith("regen+")) && b.endsWith("%")) regen += Integer.parseInt(b.substring(b.indexOf('+') + 1, b.length() - 1)) / 100.0;
            else throw new IllegalStateException("Dish " + dish.id() + ": unknown buff " + b);
        }
        return new Buff(regen, dish.has("time") ? Integer.parseInt(dish.prop("time")) : 0, tea, dish.has("meal"));
    }

    /** The newest dish's regen bonus replaces the last one's; tea and a meal add theirs. */
    static void eaten(ServerPlayer p, Buff buff, Component name) {
        long now = p.level().getGameTime();
        var fed = p.getAttachedOrCreate(FED);
        if (buff.tea()) Daily.tea(p);
        boolean regen = buff.regen() > 0 && buff.seconds() > 0;
        p.setAttached(FED, new Fed(regen ? buff.regen() : fed.regen(), regen ? now + buff.seconds() * 20L : fed.until(), buff.meal() ? now + HOUR : fed.meal()));
        if (regen) p.sendSystemMessage(Component.translatable("shinobi_life.fed", name, Math.round(buff.regen() * 100), buff.seconds()));
    }

    /** The chakra regen bonus of the last dish still working (0.10 for +10%). */
    static double regen(ServerPlayer p) {
        var fed = p.getAttachedOrCreate(FED);
        return p.level().getGameTime() < fed.until() ? fed.regen() : 0;
    }

    /** Whether a proper meal in the last hour halves fatigue's slowdown. */
    static boolean meal(ServerPlayer p) { return p.level().getGameTime() < p.getAttachedOrCreate(FED).meal(); }
}
