"""Root Tunic: the dark field tunic of the ANBU's hidden Root division: a high wrapped collar,
long sleeves into black gloves, a black belt with a steel ring, slit tails to mid-thigh, an ink
scroll at the hip and a tanto hung straight down the back."""
from kit import belt, collar, flaps, sleeves
from kit_shinobi import tanto
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Root Tunic",
    "gender": "unisex",
    "description": "Dark high-collared tunic with slit tails, black gloves and belt, an ink scroll, a tanto.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 251, 2)
    cap(body, "P", seed=251)
    strip_fabric(jacket, "P", "weave", 252, 2)
    cap(jacket, "P", seed=252)
    # A crossed front: the left panel over the right, one shade lighter along its edge.
    for y in range(9):
        jacket.front.set(min(7, 2 + y // 2), y, "P3")
        jacket.front.set(min(7, 1 + y // 2), y, "P1")
    for side in ("right", "left"):
        jacket.right.vline(1, 0, 11, "P1") if side == "right" else jacket.left.vline(2, 0, 11, "P1")
    for arm in sleeves(g, "P", "weave", 253, 2, rows=(0, 8)):
        arm.strip.hline(0, arm.strip.w - 1, 8, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "smooth", 254, 2, 9, 11)
        fabric(arm.bottom, "K", "smooth", 254, 1)
        fabric(arm.top, "P", "weave", 253, 3)
    high = collar(g, "collar", "P", "weave", 2, height=2, y=-1.6, inflate=.1)
    high.front.vline(4, 0, 2, "P0")
    belt(g, "belt", y=9.4, role="K", buckle=None, height=1, inflate=.12)
    ring = g.piece("belt_ring", "TORSO", (-1, -1, -.5), (2, 2, 1), pivot=(0, 9.9, -2.95))
    solid(ring, "M", "plain", 255, 3, edge=False)
    ring.front.set(0, 0, "M4"), ring.front.set(1, 1, "M1")
    flaps(g, "tails", 6, "P", "weave", 256, width=9, top=11.0, slit=True, hem="P1")
    # The ink scroll tucked through the belt at the front of the right hip, red-capped at both ends.
    scroll = g.piece("ink_scroll", "TORSO", (-2.5, -1, -1), (5, 2, 2), pivot=(-2.4, 10.0, -3.1), rotation=(0, 0, -8))
    solid(scroll, "S", "plain", 257, 2, edge=False)
    for face in (scroll.front, scroll.back, scroll.top, scroll.bottom):
        face.vline(0, 0, face.h - 1, "A2"), face.vline(face.w - 1, 0, face.h - 1, "A2")
    scroll.right.fill("A1"), scroll.left.fill("A1")
    tanto(g, pivot=(-.6, 2.0, 2.85), rotation=(0, 0, -10), length=9)
