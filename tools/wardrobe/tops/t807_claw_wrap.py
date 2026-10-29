"""Claw Wrap: a sleeveless fighting top wrapped tight across the chest, three red claw slashes raked
across the front, a red sash knotted at the side and bandaged forearms: the clan's taijutsu dress."""
from kit import belt
from kit_inuzuka import claw_marks
from kit_shinobi import bandage
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Claw Wrap",
    "gender": "unisex",
    "description": "Tight sleeveless wrapped top raked with red claw slashes, a knotted red sash, bandaged forearms.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 8630, 2, 0, 9)
    fabric(body.top, "P", "weave", 8630, 3)
    f = body.front
    for i in range(7):
        f.set(7 - i, i, "P1"), f.set(6 - i, i, "P3")
    claw_marks(f, 1, 2, "A2", length=5)
    claw_marks(body.back, 2, 2, "A1", length=4)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 8631, 2, 0, 1)
        fabric(arm.top, "P", "weave", 8631, 3)
        arm.strip.hline(0, arm.strip.w - 1, 1, "P1")
        bandage(arm.strip, 0, 5, arm.strip.w - 1, 10)
        arm.strip.hline(0, arm.strip.w - 1, 5, "S2")
    sash = belt(g, "sash", y=9.2, role="A", buckle=None)
    sash.front.hline(0, sash.front.w - 1, 1, "A1")
    knot = g.piece("sash_knot", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(-3.6, 9.2, -3.1))
    solid(knot, "A", "weave", 8632, 3, edge=False)
    for i, x in enumerate((-3.5, -2.5)):
        tail = g.piece(f"sash_tail_{i}", "TORSO", (0, 0, 0), (1, 4 - i, 1), pivot=(x, 11.0, -3.0),
                       rotation=(0, 0, -6 + 14 * i), motion="flap_front")
        solid(tail, "A", "weave", 8633 + i, 2)
