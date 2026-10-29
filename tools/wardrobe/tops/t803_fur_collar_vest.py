"""Fur Collar Vest: a sleeveless padded vest with a big fur collar, worn open over a chain-mesh shirt,
bare arms with bandaged forearms and red claw slashes across the back: for running and brawling
beside the pack."""
from kit_inuzuka import claw_marks, fur_box
from kit_shinobi import bandage, mesh
from paint import fabric, solid, strip_fabric

META = {
    "name": "Fur Collar Vest",
    "gender": "unisex",
    "description": "Open sleeveless vest with a big fur collar over mesh, bandaged forearms, claw slashes on the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    mesh(body.strip, 0, 0, body.strip.w - 1, 9)
    mesh(body.top, 0, 0, body.top.w - 1, body.top.h - 1)
    strip_fabric(jacket, "P", "quilt", 8510, 2, 0, 10)
    fabric(jacket.top, "P", "quilt", 8510, 3)
    f = jacket.front
    for y in range(11):
        f.set(3, y, None), f.set(4, y, None)
    f.vline(2, 0, 10, "P0"), f.vline(5, 0, 10, "P0")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1")
    claw_marks(jacket.back, 1, 3, "A2", length=5)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "S2")
    collar = g.piece("fur_collar", "TORSO", (-5, -1.2, -3), (10, 3, 6), inflate=.05)
    fur_box(collar, "S", 8512, 2)
    for side, x in (("right", -3.2), ("left", 3.2)):
        lapel = g.piece(f"fur_lapel_{side}", "TORSO", (-1, 0, 0), (2, 4, 1), pivot=(x * .55, 1.6, -2.75))
        fur_box(lapel, "S", 8514 + (side == "left"), 2)
