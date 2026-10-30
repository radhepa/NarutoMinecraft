package dev.shinobi.combat.runtime;

import dev.shinobi.combat.HandSign;
import dev.shinobi.combat.runtime.client.ShinobiCombatClient;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext;
import net.fabricmc.fabric.api.client.gametest.v1.world.TestWorldSave;
import com.mojang.blaze3d.platform.InputConstants;
import net.minecraft.client.CameraType;
import net.minecraft.client.KeyMapping;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.screens.options.controls.KeyBindsScreen;
import net.minecraft.client.gui.screens.worldselection.WorldCreationUiState;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.Identifier;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.entity.Display;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.Mob;
import net.minecraft.world.entity.decoration.Mannequin;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.levelgen.presets.WorldPresets;
import net.minecraft.world.phys.AABB;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.phys.Vec3;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * P06-2: a player taught the three Academy techniques weaves Clone with the real keys (Weave held, the hotbar keys as
 * signs): three decoys stand and chakra drops. Transformation (with the 0, - and = sign keys) hides the player as a log
 * until a hit. Substitution armed by its key takes a hit, blinks the player back short of a wall behind them and leaves
 * a log. A held guard takes 60% off a melee hit, a hit inside the hurt cooldown costs it nothing, a dodge costs stamina,
 * a thrown practice kunai deals its damage, dying mid-guard drops the guard, and reopening keeps what was learned.
 * P06 controls: every key is in the Shinobi category of Options > Controls, and a sign rebound there (and saved) is
 * woven by its new key and no longer by its old one. Each pose is the synced clip of animations.json.
 * Screenshots: controls-shinobi, academy-weaving (the HUD, its hint and the hands in a sign), academy-cast, academy-clones, academy-guard, academy-dodge,
 * academy-ready, academy-ninja-run, academy-meditate (the keyed ready stance, run and meditation).
 */
@SuppressWarnings("UnstableApiUsage")
public final class AcademyGameTest implements FabricClientGameTest {
    @Override
    public void runTest(ClientGameTestContext c) {
        var casts = new CopyOnWriteArrayList<String>();
        ShinobiCombat.CAST.register((p, id) -> casts.add(id));
        TestWorldSave save;
        var keys = new ArrayList<>(List.of(ShinobiCombatClient.WEAVE, ShinobiCombatClient.RADIAL, ShinobiCombatClient.GUARD, ShinobiCombatClient.DODGE, ShinobiCombatClient.SUBSTITUTE));
        keys.addAll(List.of(ShinobiCombatClient.SIGNS));
        // The run folder's options.txt keeps the bindings of earlier runs: start from the defaults.
        c.runOnClient(mc -> { keys.forEach(k -> k.setKey(k.getDefaultKey())); KeyMapping.resetMapping(); });
        check(c.computeOnClient(mc -> keys.stream().allMatch(k -> Arrays.asList(mc.options.keyMappings).contains(k)
                && k.getCategory().label().getString().equals("Shinobi") && k.getCategory() == ShinobiCombatClient.WEAVE.getCategory())), "every combat key is in Controls under Shinobi");
        check(ShinobiCombatClient.GUARD.getDefaultKey().getType() == InputConstants.Type.MOUSE && ShinobiCombatClient.SIGNS[11].getDefaultKey().getValue() == InputConstants.KEY_EQUALS,
                "the documented defaults: guard on right click, the twelfth sign on =");
        int scale = c.computeOnClient(mc -> mc.options.guiScale().get());
        c.runOnClient(mc -> { mc.options.guiScale().set(1); mc.resizeGui(); });   // small enough for the whole category
        c.setScreen(() -> new KeyBindsScreen(null, Minecraft.getInstance().options));
        c.getInput().setCursorPos(200, 200);
        c.getInput().scroll(-500);   // the Shinobi category is the last
        c.waitTicks(2);
        c.takeScreenshot("controls-shinobi");
        c.setScreen(() -> null);
        c.runOnClient(mc -> { mc.options.guiScale().set(scale); mc.resizeGui(); });
        try (var w = c.worldBuilder().adjustSettings(ui -> {
            var flat = ui.getSettings().worldgenLoadContext().lookupOrThrow(Registries.WORLD_PRESET).getOrThrow(WorldPresets.FLAT);
            ui.setWorldType(new WorldCreationUiState.WorldTypeEntry(flat));
            ui.setGenerateStructures(false);
        }).create()) {
            w.getConnection().waitForChunksRender();
            for (String cmd : List.of("gamerule spawn_mobs false", "time set noon", "difficulty normal", "gamemode survival @a")) w.getServer().runCommand(cmd);
            BlockPos at = w.getServer().computeOnServer(s -> player(w).blockPosition());
            w.getServer().runCommand("tp @p " + (at.getX() + .5) + " " + at.getY() + " " + (at.getZ() + .5) + " 0 0");
            w.getServer().runCommand("summon pig " + (at.getX() + .5) + " " + at.getY() + " " + (at.getZ() + 3.5) + " {NoAI:1b,Tags:[\"academy_target\"]}");
            check(w.getServer().computeOnServer(s -> ShinobiCombat.teach(player(w), Fighter.CLONE) && ShinobiCombat.teach(player(w), Fighter.TRANSFORMATION)
                    && ShinobiCombat.teach(player(w), Fighter.SUBSTITUTION) && !ShinobiCombat.teach(player(w), Fighter.CLONE)
                    && !ShinobiCombat.teach(player(w), "combat:nin.none") && ShinobiCombat.knows(player(w), Fighter.SUBSTITUTION)), "the three techniques are taught once each");
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.THIRD_PERSON_FRONT));
            c.waitTicks(60);   // past the joining player's spawn invulnerability
            check(c.computeOnClient(mc -> mc.player.getAttached(ShinobiCombat.STATE).learned().size() == 3), "the learned set syncs to the client");

            double chakra = state(w).chakra();
            weave(c, HandSign.RAM, HandSign.SNAKE);
            check(c.computeOnClient(mc -> mc.player.getAttached(ShinobiCombat.STANCE).signs().equals(List.of("ram", "snake"))
                    && clip(mc).equals("combat.sign.snake")), "the woven signs and the last sign's clip reach the client");
            c.takeScreenshot("academy-weaving");
            weave(c, HandSign.TIGER);
            c.getInput().releaseKey(ShinobiCombatClient.WEAVE);
            c.waitTicks(3);
            check(c.computeOnClient(mc -> clip(mc).equals("combat.cast.push_palms")), "a cast plays the release");
            c.takeScreenshot("academy-cast");
            c.waitTicks(2);
            int decoys = w.getServer().computeOnServer(s -> near(w, Mannequin.class, 6, m -> m.entityTags().contains(Jutsu.DECOY)).size());
            check(decoys == 3 && state(w).chakra() < chakra - 4 && casts.contains(Fighter.CLONE), "Clone stands three decoys for its chakra: " + decoys + ", " + state(w));
            c.takeScreenshot("academy-clones");

            // Rat rebound from 1 to K as the Controls screen does it: K weaves Rat, 1 (still the first hotbar slot) does not, and the binding is saved.
            var rat = ShinobiCombatClient.SIGNS[0];
            c.runOnClient(mc -> { rat.setKey(InputConstants.getKey("key.keyboard.k")); KeyMapping.resetMapping(); mc.options.save(); });
            c.getInput().holdKey(ShinobiCombatClient.WEAVE);
            c.waitTicks(2);
            c.getInput().pressKey(InputConstants.KEY_1);
            c.waitTicks(5);
            c.getInput().pressKey(InputConstants.KEY_K);
            c.waitTicks(5);
            c.getInput().pressKey(InputConstants.KEY_2);
            c.waitTicks(5);
            check(c.computeOnClient(mc -> mc.player.getAttached(ShinobiCombat.STANCE).signs().equals(List.of("rat", "ox")) && mc.player.getInventory().getSelectedSlot() == 0),
                    "the rebound key weaves Rat, the old one nothing, and the hotbar keys do not switch slots while weaving");
            check(c.computeOnClient(mc -> {
                try { return Files.readString(mc.gameDirectory.toPath().resolve("options.txt")).contains("key_key.shinobi_combat.sign_1:key.keyboard.k"); }
                catch (IOException e) { throw new UncheckedIOException(e); }
            }), "the new binding is saved");
            c.getInput().releaseKey(ShinobiCombatClient.WEAVE);
            c.waitTicks(2);
            check(c.computeOnClient(mc -> clip(mc).equals("combat.sign.fizzle")), "a wrong sequence fizzles");
            c.getInput().pressKey(InputConstants.KEY_2);
            c.waitTicks(2);
            check(c.computeOnClient(mc -> mc.player.getInventory().getSelectedSlot() == 1), "outside a weave the hotbar keys switch slots");
            c.getInput().pressKey(InputConstants.KEY_1);
            c.runOnClient(mc -> { rat.setKey(rat.getDefaultKey()); KeyMapping.resetMapping(); mc.options.save(); });
            c.waitTicks(10);

            weave(c, HandSign.DOG, HandSign.BOAR, HandSign.RAM);
            c.getInput().releaseKey(ShinobiCombatClient.WEAVE);
            c.waitTicks(5);
            check(w.getServer().computeOnServer(s -> player(w).isInvisible() && Jutsu.disguised(player(w))), "Transformation hides the player as a log");
            check(drop(w, 1) > 0 && !w.getServer().computeOnServer(s -> Jutsu.disguised(player(w))), "a hit ends the disguise");

            // A one-block wall four blocks behind the player, inside the five-block blink.
            String wall = (at.getX() - 2) + " " + at.getY() + " " + (at.getZ() - 4) + " " + (at.getX() + 2) + " " + (at.getY() + 1) + " " + (at.getZ() - 4);
            w.getServer().runCommand("tp @p " + (at.getX() + .5) + " " + at.getY() + " " + (at.getZ() + .5) + " 0 0");
            w.getServer().runCommand("fill " + wall + " stone");
            c.waitTicks(2);
            c.getInput().pressKey(ShinobiCombatClient.SUBSTITUTE);
            c.waitTicks(2);
            Vec3 from = w.getServer().computeOnServer(s -> player(w).position());
            check(drop(w, 4) == 0, "Substitution takes the hit");
            c.waitTicks(2);
            Vec3 to = w.getServer().computeOnServer(s -> player(w).position());
            check(to.distanceTo(from) >= 2.5 && to.z - .3 >= at.getZ() - 3 && w.getServer().computeOnServer(s -> !near(w, Display.ItemDisplay.class, 8, d -> d.entityTags().contains(Jutsu.PROP)).isEmpty())
                    && casts.contains(Fighter.SUBSTITUTION), "the player blinks back short of the wall, to " + to + ", and a log stands where they were");
            w.getServer().runCommand("fill " + wall + " air");

            c.waitTicks(15);
            c.getInput().holdKey(ShinobiCombatClient.GUARD);
            c.waitTicks(3);
            double stamina = state(w).stamina();
            float guarded = drop(w, 5);
            check(state(w).stamina() < stamina, "a guarded hit costs stamina");
            check(w.getServer().computeOnServer(s -> {
                double before = Fighter.of(player(w)).stamina.value();
                return drop(w, 5) == 0 && Fighter.of(player(w)).stamina.value() == before;
            }), "a hit inside the hurt cooldown costs the guard nothing");
            c.getInput().releaseKey(ShinobiCombatClient.GUARD);
            c.waitTicks(12);   // past the guarded hit's invulnerability
            float open = drop(w, 5);
            check(guarded > 0 && Math.abs(guarded - open * 0.4F) < 0.01F, "the guard takes 60% off: " + guarded + " of " + open);

            stamina = state(w).stamina();
            c.getInput().pressKey(ShinobiCombatClient.DODGE);
            c.waitTicks(3);
            check(state(w).stamina() < stamina - 15, "a dodge costs stamina: " + stamina + " to " + state(w).stamina());
            check(c.computeOnClient(mc -> clip(mc).equals("combat.def.dodge_back")), "a dodge with no direction held plays the back dodge");
            c.takeScreenshot("academy-dodge");

            c.waitTicks(10);   // past the dodge's clip
            var partner = w.getServer().computeOnServer(s -> Spar.partnerAt(player(w).level(), player(w).blockPosition().offset(3, 0, 0)));
            check(partner != null, "a spar partner stands by the player");
            try {
                w.getServer().runOnServer(s -> Spar.attack(player(w), partner));   // a first light press starts the jab
                c.waitTicks(2);
                check(c.computeOnClient(mc -> clip(mc).equals("combat.tai.academy.jab")), "a spar hit plays its combo clip");
                c.takeScreenshot("academy-jab");
                check(w.getServer().computeOnServer(s -> partner.getAttached(ShinobiCombat.STANCE).clip()).equals("combat.res.spar_bow"), "the partner bows as the bout starts");
            } finally {
                w.getServer().runOnServer(s -> { Spar.end(player(w)); partner.discard(); });
            }

            w.getServer().runCommand("tp @p " + (at.getX() + .5) + " " + at.getY() + " " + (at.getZ() + .5) + " 0 15");   // facing the pig, a little down
            w.getServer().runOnServer(s -> player(w).setItemInHand(InteractionHand.MAIN_HAND,
                    new ItemStack(BuiltInRegistries.ITEM.getValue(Identifier.fromNamespaceAndPath(ShinobiCombat.MOD_ID, "practice_kunai")), 4)));
            c.waitTicks(15);
            awaitClip(c, "combat.stance.idle", "standing still with a kunai is the ready stance");
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.THIRD_PERSON_BACK));   // the pig stands where the front camera goes
            c.waitTicks(1);
            c.takeScreenshot("academy-ready");
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.THIRD_PERSON_FRONT));
            float pig = w.getServer().computeOnServer(s -> target(w).getHealth());
            c.getInput().pressKey(o -> o.keyUse);
            c.waitTicks(11);
            float hit = pig - w.getServer().computeOnServer(s -> target(w).getHealth());
            check(Math.abs(hit - 1) < 0.01F, "a practice kunai hits for 1: " + hit);

            int kunai = w.getServer().computeOnServer(s -> player(w).getMainHandItem().getCount());
            c.getInput().holdKey(ShinobiCombatClient.GUARD);
            c.waitTicks(3);
            check(w.getServer().computeOnServer(s -> !Fighter.of(player(w)).guarding && player(w).getMainHandItem().getCount() < kunai),
                    "right click with a kunai in hand throws and does not guard");
            c.getInput().releaseKey(ShinobiCombatClient.GUARD);
            w.getServer().runOnServer(s -> player(w).setItemInHand(InteractionHand.MAIN_HAND, ItemStack.EMPTY));

            // Ninja wire strung at your feet; step back and a mob standing in it is tripped.
            Item wire = BuiltInRegistries.ITEM.getValue(Identifier.fromNamespaceAndPath(ShinobiCombat.MOD_ID, "ninja_wire"));
            w.getServer().runOnServer(s -> player(w).setItemInHand(InteractionHand.MAIN_HAND, new ItemStack(wire, 2)));
            w.getServer().runCommand("tp @p ~ ~ ~ 0 90");
            c.waitTicks(3);
            c.getInput().pressKey(o -> o.keyUse);
            c.waitTicks(3);
            check(w.getServer().computeOnServer(s -> s.overworld().getBlockState(at).is(Blocks.TRIPWIRE) && player(w).getMainHandItem().getCount() == 1),
                    "ninja wire strings a tripwire");
            w.getServer().runCommand("tp @p " + (at.getX() + 3.5) + " " + at.getY() + " " + (at.getZ() + .5) + " 90 30");
            w.getServer().runCommand("summon husk " + (at.getX() + .5) + " " + at.getY() + " " + (at.getZ() + .5) + " {NoAI:1b,Tags:[\"academy_tool\"]}");
            c.waitTicks(5);
            check(w.getServer().computeOnServer(s -> tool(w).hasEffect(MobEffects.SLOWNESS)), "a mob in the wire is tripped");

            // A smoke bomb at your feet: the husk hunting you loses you, and you leave its tracking.
            w.getServer().runOnServer(s -> { tool(w).removeAllEffects(); tool(w).setTarget(player(w)); player(w).setItemInHand(InteractionHand.MAIN_HAND, new ItemStack(ShinobiCombat.SMOKE_BOMB, 2)); });
            w.getServer().runCommand("tp @p ~ ~ ~ 0 90");
            c.waitTicks(3);
            c.getInput().pressKey(o -> o.keyUse);
            c.waitTicks(5);
            check(w.getServer().computeOnServer(s -> tool(w).getTarget() == null && player(w).hasEffect(MobEffects.INVISIBILITY)),
                    "a smoke bomb loses the hunter and hides its thrower");
            w.getServer().runCommand("tp @p ~ ~ ~ 90 20");
            c.waitTicks(2);
            c.takeScreenshot("academy-smoke");
            w.getServer().runOnServer(s -> { tool(w).discard(); player(w).removeAllEffects(); player(w).setItemInHand(InteractionHand.MAIN_HAND, ItemStack.EMPTY); });
            w.getServer().runCommand("setblock " + at.getX() + " " + at.getY() + " " + at.getZ() + " air");

            // A sprint jump off a log beam pushes on and costs chakra.
            String beam = (at.getX() + 2) + " " + (at.getY() - 1) + " " + at.getZ() + " " + (at.getX() - 12) + " " + (at.getY() - 1) + " " + at.getZ();
            w.getServer().runCommand("fill " + beam + " oak_log");
            w.getServer().runCommand("tp @p " + (at.getX() + 2.5) + " " + at.getY() + " " + (at.getZ() + .5) + " 90 0");   // facing west, along the beam
            c.waitTicks(5);
            c.getInput().holdKey(o -> o.keyUp);
            c.getInput().holdKey(o -> o.keySprint);
            c.waitTicks(8);
            awaitClip(c, "combat.move.ninja_run", "sprinting is the ninja run");
            c.takeScreenshot("academy-ninja-run");
            double hopFrom = state(w).chakra();
            String before = c.computeOnClient(mc -> "sprinting " + mc.player.isSprinting() + ", food " + mc.player.getFoodData().getFoodLevel()
                    + ", on " + mc.player.level().getBlockState(mc.player.getOnPos()).getBlock() + ", ground " + mc.player.onGround());
            c.getInput().holdKey(o -> o.keyJump);   // jump reads isDown each tick, which a press-and-release in one tick misses
            c.waitTicks(1);
            c.getInput().releaseKey(o -> o.keyJump);
            c.waitTicks(2);   // the server's push reaches the client
            double speed = c.computeOnClient(mc -> mc.player.getDeltaMovement().horizontalDistance());
            check(speed > .4 && hopFrom - state(w).chakra() > .5 && c.computeOnClient(mc -> clip(mc).equals("combat.move.roof_hop")),
                    "a sprint jump off a log is a roof hop: " + speed + " (" + before + ", chakra " + hopFrom + " to " + state(w).chakra() + ")");
            c.getInput().releaseKey(o -> o.keySprint);
            c.getInput().releaseKey(o -> o.keyUp);
            c.waitTicks(20);
            w.getServer().runCommand("fill " + beam + " grass_block");
            w.getServer().runCommand("tp @p " + (at.getX() + .5) + " " + at.getY() + " " + (at.getZ() + .5) + " 0 15");

            check(w.getServer().computeOnServer(s -> ShinobiCombat.teach(player(w), Fighter.RELEASE) && ShinobiCombat.teach(player(w), Fighter.ROPE_ESCAPE)
                    && ShinobiCombat.teach(player(w), Fighter.FIRST_AID)), "Release, Rope Escape and First Aid are taught");
            w.getServer().runCommand("effect give @p nausea 30");
            c.waitTicks(5);
            weave(c, HandSign.RAM);
            c.getInput().releaseKey(ShinobiCombatClient.WEAVE);
            c.waitTicks(3);
            check(c.computeOnClient(mc -> clip(mc).equals("combat.sign.release_ram")) && casts.contains(Fighter.RELEASE)
                    && !w.getServer().computeOnServer(s -> player(w).hasEffect(MobEffects.NAUSEA)), "Release on Ram breaks the illusion");
            var web = Blocks.COBWEB.defaultBlockState();
            var held = new Vec3(.25, .05, .25);
            check(w.getServer().computeOnServer(s -> Fighter.unstuck(player(w), web, held)).equals(held.scale(1.4))
                    && c.computeOnClient(mc -> Fighter.unstuck(mc.player, web, held)).equals(held.scale(1.4)), "Rope Escape loosens a cobweb on both sides");

            w.getServer().runOnServer(s -> target(w).setHealth(7));   // hurt by no more than First Aid's heal
            w.getServer().runCommand("tp @p " + (at.getX() + .5) + " " + at.getY() + " " + (at.getZ() + 1.8) + " 0 40");   // crouched over the hurt pig
            c.getInput().holdKey(o -> o.keyShift);
            c.waitTicks(3);
            c.getInput().pressKey(o -> o.keyUse);
            c.waitTicks(3);
            check(w.getServer().computeOnServer(s -> Fighter.of(player(w)).aiding != null) && c.computeOnClient(mc -> clip(mc).equals("combat.cast.first_aid")),
                    "a crouched use with an empty hand on a hurt ally starts First Aid");
            c.takeScreenshot("academy-first-aid");
            c.waitTicks(62);
            check(w.getServer().computeOnServer(s -> target(w).getHealth() == target(w).getMaxHealth() && Fighter.of(player(w)).aiding == null)
                    && casts.contains(Fighter.FIRST_AID), "First Aid heals the ally after its 3 s");
            c.waitTicks(45);
            awaitClip(c, "combat.pose.meditate", "two seconds crouched still is meditation");
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.THIRD_PERSON_BACK));   // the pig stands where the front camera goes
            c.waitTicks(1);
            c.takeScreenshot("academy-meditate");
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.THIRD_PERSON_FRONT));
            c.getInput().releaseKey(o -> o.keyShift);
            w.getServer().runCommand("tp @p ~ ~ ~ 180 0");   // back to the pig, so the front camera is clear of it
            w.getServer().runCommand("item replace entity @p armor.chest with iron_chestplate");   // the armour follows the guard pose
            w.getServer().runCommand("item replace entity @p armor.legs with iron_leggings");
            c.waitTicks(5);
            c.getInput().holdKey(ShinobiCombatClient.GUARD);
            c.waitTicks(3);
            check(w.getServer().computeOnServer(s -> Fighter.of(player(w)).guarding), "the guard is up");
            c.takeScreenshot("academy-guard");   // here, clear of the substitution's smoke
            w.getServer().runCommand("kill @p");
            c.waitTicks(5);   // the death screen is up: the guard's release reaches a dead player, who cannot act
            c.getInput().releaseKey(ShinobiCombatClient.GUARD);
            c.runOnClient(mc -> mc.player.respawn());
            c.waitTicks(10);
            check(w.getServer().computeOnServer(s -> !Fighter.of(player(w)).guarding), "dying mid-guard drops the guard");
            c.runOnClient(mc -> mc.options.setCameraType(CameraType.FIRST_PERSON));
            save = w.getWorldSave();
        }
        try (var w = save.open()) {
            w.getConnection().waitForChunksRender();
            c.waitTicks(20);
            check(w.getServer().computeOnServer(s -> ShinobiCombat.knows(player(w), Fighter.CLONE) && state(w).learned().size() == 6), "reopening keeps the learned techniques");
            check(w.getServer().computeOnServer(s -> near(w, Mannequin.class, 16, m -> true).isEmpty()), "no decoy outlives the session");
        }
    }

    /** Holds Weave and presses each sign's key, a little slower than a sign takes. */
    static void weave(ClientGameTestContext c, HandSign... signs) {
        var in = c.getInput();
        in.holdKey(ShinobiCombatClient.WEAVE);
        c.waitTicks(2);
        for (var s : signs) {
            int i = s.ordinal();
            in.pressKey(ShinobiCombatClient.SIGNS[i]);
            c.waitTicks(5);
        }
    }

    /** The health a melee hit from the target pig takes off the player (over 10 ticks after the last), measured within one server tick. */
    static float drop(TestSingleplayerContext w, float amount) {
        return w.getServer().computeOnServer(s -> {
            var p = player(w);
            float before = p.getHealth();
            p.hurtServer(p.level(), p.level().damageSources().mobAttack(target(w)), amount);
            return before - p.getHealth();
        });
    }

    static String clip(Minecraft mc) { return mc.player.getAttached(ShinobiCombat.STANCE).clip(); }

    /** Waits up to 3 s for the player's clip, as the server sets it a tick or more after the action. */
    static void awaitClip(ClientGameTestContext c, String want, String what) {
        for (int i = 0; i < 60 && !want.equals(c.computeOnClient(AcademyGameTest::clipOrNone)); i++) c.waitTick();
        String got = c.computeOnClient(AcademyGameTest::clipOrNone);
        check(want.equals(got), what + ": " + got);
    }

    static String clipOrNone(Minecraft mc) { var s = mc.player.getAttached(ShinobiCombat.STANCE); return s == null ? "none" : s.clip(); }

    static ServerPlayer player(TestSingleplayerContext w) { return w.getConnection().getServerPlayer(); }

    static Fighter.State state(TestSingleplayerContext w) { return w.getServer().computeOnServer(s -> player(w).getAttached(ShinobiCombat.STATE)); }

    static Mob tool(TestSingleplayerContext w) {
        return near(w, Mob.class, 16, e -> e.entityTags().contains("academy_tool")).getFirst();
    }

    static LivingEntity target(TestSingleplayerContext w) {
        return near(w, LivingEntity.class, 16, e -> e.entityTags().contains("academy_target")).getFirst();
    }

    static <T extends net.minecraft.world.entity.Entity> List<T> near(TestSingleplayerContext w, Class<T> type, double r, java.util.function.Predicate<T> test) {
        return w.getConnection().getServerLevel().getEntitiesOfClass(type, new AABB(player(w).blockPosition()).inflate(r), test);
    }

    static void check(boolean ok, String what) {
        if (!ok) throw new AssertionError("Failed: " + what);
    }
}
