"""Kimono Trim Blouse: a rose blouse cut like a short kimono, its crossed collar banded in cream, wide
elbow sleeves edged in the same band, and a broad accent sash knotted in a bow at the back."""
from kit import arm_bone, arm_x, belt
from kit_haruno import kimono_trim
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Kimono Trim Blouse",
    "gender": "unisex",
    "description": "Short kimono-cut blouse with a cream-banded crossed collar, wide banded elbow sleeves, a sash with a back bow.",
    "tags": ["shinobi", "wrap"],
}

# The crossed collar: the wearer's left panel laps over the right, meeting low on the chest.
COLLAR = [(0, 5), (1, 4), (2, 4), (3, 3), (4, 3), (5, 2)]


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 19540, 2)
    cap(body, "P", texture="weave", seed=19540)
    kimono_trim(body.front, COLLAR, "S")
    body.front.set(1, 0, k("S", 4)), body.front.set(2, 0, k("S", 3))
    for y in range(1, 6):
        body.front.set(6 - y // 2, y, k("P", 1)) if y > 2 else None
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 19541 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 19541, 3)
        sleeve = g.piece(f"{side}_wide_sleeve", arm_bone(side), (arm_x(side) - .5, 1.0, -2.5), (5, 4, 5), motion="sway")
        solid(sleeve, "P", "weave", 19543 + (side == "left"), 2)
        for face in sleeve.sides:
            face.hline(0, face.w - 1, 3, k("S", 3))
        sleeve.bottom.fill(k("P", 0))
    sash = belt(g, "sash", y=7.4, role="A", height=3, buckle=None, inflate=.2)
    for face in sash.sides:
        face.hline(0, face.w - 1, 1, k("A", 3)), face.hline(0, face.w - 1, 2, k("A", 1))
    for i, rz in enumerate((-30, 30)):
        loop = g.piece(f"bow_{i}", "TORSO", (-3 + 3 * i, -1, 0), (3, 2, 1), pivot=(0, 8.4, 2.6), rotation=(0, 0, rz))
        solid(loop, "A", "weave", 19545 + i, 3, edge=False)
    knot = g.piece("bow_knot", "TORSO", (-1, -1, 0), (2, 2, 1), pivot=(0, 8.6, 2.9))
    solid(knot, "A", "weave", 19547, 2, edge=False)
