"""Ninken Handler: the Hatake who runs with the ninja hounds, a slate shirt under a navy hound vest
like Pakkun's with the scarecrow face on the back, white paw prints on the shoulders, black gloves
and a summoning scroll at the hip."""
from kit_hatake import PAW, SCARECROW, decal, shoulder_decal
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Ninken Handler",
    "gender": "unisex",
    "description": "Navy hound vest with the scarecrow face on the back over a slate shirt, paw prints, a summoning scroll.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 11601, 2)
    cap(body, "P", seed=11601)
    # The vest: navy over the chest and back, open at the sides of the waist.
    strip_fabric(jacket, "D", "weave", 11602, 2, 0, 9)
    cap(jacket, "D", seed=11602)
    jacket.strip.hline(0, jacket.strip.w - 1, 9, "D1"), jacket.strip.hline(0, jacket.strip.w - 1, 0, "D3")
    jacket.front.vline(3, 0, 8, "D0"), jacket.front.vline(4, 0, 8, "D3")
    for face in (jacket.right, jacket.left):
        for y in range(4, 10):
            face.set(1, y, None), face.set(2, y, None)
    decal(g, "back_scarecrow", SCARECROW, {"#": "S3"}, "D2", (0, 1.4, 2.3))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 11603 + (side == "left"), 2, 0, 8)
        fabric(arm.top, "P", "weave", 11603, 3)
        arm.strip.hline(0, arm.strip.w - 1, 4, "P1")
        strip_fabric(arm, "K", "smooth", 11605, 2, 9, 11)
        arm.strip.hline(0, arm.strip.w - 1, 9, "K3")
        arm.bottom.fill("K1")
    shoulder_decal(g, "paw", PAW, {"o": "S3"}, "P2")
    # The summoning scroll tucked at the left hip, red caps on both ends.
    scroll = g.piece("summon_scroll", "TORSO", (-1, -3, -1), (2, 6, 2), pivot=(4.6, 9.2, -.4), rotation=(0, 0, 14))
    solid(scroll, "S", "weave", 11606, 3)
    for face in scroll.sides:
        face.hline(0, 1, 0, "A2"), face.hline(0, 1, 5, "A2"), face.set(0, 3, "S1")
    scroll.top.fill("A3"), scroll.bottom.fill("A1")
    belt = g.piece("belt", "TORSO", (-4.6, 9.4, -2.6), (9, 1, 5), inflate=.05)
    solid(belt, "L", "leather", 11607, 2, edge=False)
