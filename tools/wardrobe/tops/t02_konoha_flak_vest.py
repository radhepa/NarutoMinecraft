"""Konoha Flak Vest: the green padded vest of chunin and jonin, scroll pockets on the chest, a high
collar and the red Uzumaki swirl on the back and both shoulders, over a navy long-sleeved shirt."""
from glyphs import SWIRL, SWIRL_SMALL, stamp
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Konoha Flak Vest",
    "gender": "unisex",
    "description": "Padded green vest with scroll pockets, high collar and red swirls, over a navy shirt.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 51, 2)
    cap(body, "D", seed=51)
    # The vest: padded ribs every three rows, a zip down the middle, shading toward the sides.
    strip_fabric(jacket, "P", "plain", 52, 2, 0, 11)
    cap(jacket, "P", texture="plain", seed=52)
    for y in (2, 5, 8):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P1")
    for y in (1, 4, 7):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P0")
    jacket.front.vline(3, 0, 10, "P0"), jacket.front.vline(4, 0, 10, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 11, "P1")
    back = g.piece("back_swirl", "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(0, 2.2, 2.3), scale=(.5, .5, .5))
    fabric(back.back, "P", "plain", 53, 2)
    stamp(back.back, SWIRL, 0, 0, {"#": "A2"})
    for face in (back.top, back.bottom, back.right, back.left, back.front):
        face.fill("P2")
    # Navy sleeves to the wrist, the swirl patch on each shoulder.
    for side, bone, x in (("right", "RIGHT_ARM", -3.05), ("left", "LEFT_ARM", 3.05)):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 54 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "D", "weave", 54, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
        patch = g.piece(f"{side}_swirl", bone, (0, 0, -3), (1, 6, 6), pivot=(x - (.5 if side == "right" else 0), .6, 0),
                        scale=(.5, .5, .5))
        outer = patch.right if side == "right" else patch.left
        for face in patch.faces:
            face.fill("D2")
        rows = SWIRL_SMALL if side == "left" else [r[::-1] for r in SWIRL_SMALL]
        stamp(outer, rows, 0, 0, {"#": "A2"})
    # High padded collar.
    collar = g.piece("collar", "TORSO", (-4.5, -1.6, -2.7), (9, 2, 5), inflate=.08)
    solid(collar, "P", "plain", 56, 2)
    collar.front.hline(3, 5, 0, "P0"), collar.front.set(4, 1, "P0")
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "P3")
    # Two scroll pockets on each side of the chest.
    for i, x in enumerate((-3.7, -2.1, .6, 2.2)):
        pocket = g.piece(f"scroll_pocket_{i}", "TORSO", (0, 0, -1), (3, 6, 1), pivot=(x, 3.4, -2.3), scale=(.5, .5, .5))
        solid(pocket, "P", "plain", 57 + i, 2)
        pocket.front.hline(0, 2, 0, "P3"), pocket.front.hline(0, 2, 1, "P1")
        pocket.front.vline(2, 2, 5, "P1")
