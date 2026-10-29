"""Foundation Vest: a Root agent's close sleeveless tunic, fastened down the right side with steel
studs under a high collar, the left forearm bound in bandages and the right in a black guard, a
dark-red sash knotted at the hip and short split tails."""
from kit import belt, flaps
from kit_shinobi import bandage
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Foundation Vest",
    "gender": "unisex",
    "description": "Sleeveless high-collared tunic fastened at the side, a bandaged forearm and a black guard, a red sash.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 13680, 2)
    cap(body, "P", seed=13680)
    strip_fabric(jacket, "P", "weave", 13681, 2, 0, 8)
    fabric(jacket.top, "P", "weave", 13681, 3)
    f = jacket.front
    f.vline(2, 0, 8, "P1")
    for y in (1, 3, 5, 7):
        f.set(1, y, "M3")
    for face in (jacket.right, jacket.left):
        face.vline(0, 0, 8, "P1")
    neck = g.piece("high_collar", "TORSO", (-4.5, -1.8, -2.6), (9, 2, 5), inflate=.08)
    solid(neck, "P", "weave", 13682, 2)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "P3")
    neck.front.vline(2, 0, 1, "P0")
    left, right = g.part("left_arm"), g.part("right_arm")
    bandage(left.strip, 0, 5, left.strip.w - 1, 10)
    left.strip.hline(0, left.strip.w - 1, 5, "S1")
    strip_fabric(right, "K", "smooth", 13683, 2, 6, 11)
    fabric(right.bottom, "K", "smooth", 13683, 1)
    right.strip.hline(0, right.strip.w - 1, 6, "K3")
    sash = belt(g, "sash", y=8.6, role="A", height=2, buckle=None, inflate=.14)
    sash.front.hline(0, 7, 1, "A1")
    for i, (x, rz) in enumerate(((2.6, 6), (3.4, -10))):
        end = g.piece(f"sash_end_{i}", "TORSO", (-.5, 0, -.5), (1, 4 - i, 1), pivot=(x, 10.4, -2.85), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "A", "weave", 13684 + i, 2)
    flaps(g, "tails", 4, "P", "weave", 13686, width=9, top=10.8, slit=True, hem="P1")
