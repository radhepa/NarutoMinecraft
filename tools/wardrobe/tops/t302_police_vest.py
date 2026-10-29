"""Police Vest: the Konoha Military Police uniform, a dark long-sleeved shirt under a padded vest
with a high collar, the Uchiha crest on its back and the force's badge, a four-point shuriken star with
the crest at its heart, on both shoulders."""
from kit import arm_bone, arm_x, belt
from kit_uchiha import back_crest, police_badge
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Police Vest",
    "gender": "unisex",
    "description": "Military Police vest over a dark long-sleeved shirt, crest on the back, shuriken-star badges on the shoulders.",
    "tags": ["shinobi", "vest", "uchiha"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 3815, 2)
    cap(body, "D", seed=3815)
    # The vest: padded panels in two tiers, a centre closure and open sides under the arms.
    strip_fabric(jacket, "P", "plain", 3816, 2, 0, 10)
    cap(jacket, "P", texture="plain", seed=3816)
    for y in (4, 8):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P1")
        jacket.strip.hline(0, jacket.strip.w - 1, y - 1, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P0")
    jacket.front.vline(3, 0, 10, "P0"), jacket.front.vline(4, 0, 10, "P3")
    for face in (jacket.right, jacket.left):
        for y in range(1, 9):
            face.clear(1, y), face.clear(2, y)
    # Chest pockets with steel snaps.
    for i, x in enumerate((-3.4, 1.4)):
        pocket = g.piece(f"chest_pocket_{i}", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(x, 4.4, -2.75))
        solid(pocket, "P", "plain", 3817 + i, 2)
        pocket.front.hline(0, 1, 0, "P3"), pocket.front.set(1, 0, "M3")
    back_crest(g, "P", pivot=(0, 1.2, 2.35), texture="plain", seed=3819)
    collar = g.piece("collar", "TORSO", (-4.5, -1.8, -2.7), (9, 2, 5), inflate=.08)
    solid(collar, "P", "plain", 3820, 2)
    collar.front.hline(3, 5, 0, "P0"), collar.front.hline(3, 5, 1, "P0")
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "P3")
    belt(g, "duty_belt", y=10.0, role="L", height=1, buckle="M", inflate=.3)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 3821 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "D", "weave", 3821, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
        cuff = g.piece(f"{side}_cuff", arm_bone(side), (arm_x(side) - .3, 8.6, -2.3), (4, 1, 4), inflate=.12)
        solid(cuff, "D", "weave", 3823, 3)
    for side in ("right", "left"):
        police_badge(g, side, "D", seed=3824)
