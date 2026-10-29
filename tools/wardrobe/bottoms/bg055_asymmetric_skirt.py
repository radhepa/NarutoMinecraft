"""Asymmetric Skirt: a skirt short on the right and falling long over the left leg, its hem cut on
a diagonal, over fitted shorts, with a mesh stocking on the left leg and sandals."""
from kit import belt
from kit_shinobi import mesh, sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Asymmetric Skirt", "gender": "female",
        "description": "Skirt short on the right and long over the left leg, shorts, one mesh stocking.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 33680, 2, 9, 11)
    fabric(body.bottom, "P", "smooth", 33680, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 33681, 2, 0, 1)
        fabric(leg.top, "K", "plain", 33681, 2)
    left = g.part("left_leg")
    strip_fabric(left, "K", "plain", 33682, 1, 2, 9)
    mesh(left.strip, 0, 2, 15, 9, "K3")
    sandals(g)
    belt(g, "waist_band", y=9.3, role="A", height=1, buckle=None, inflate=.15)
    # Front and back panels stepped longer toward the left (+x).
    for name, z, motion in (("front", -2.9, "flap_front"), ("back", 1.9, "flap_back")):
        for i, (x, length) in enumerate(((-4.5, 3), (-1.5, 5), (1.5, 8))):
            panel = g.piece(f"waist_skirt_{name}_{i}", "TORSO", (0, 0, 0), (3, length, 1), pivot=(x, 10.2, z), motion=motion)
            solid(panel, "P", "smooth", 33683 + i, 2)
            for face in (panel.front, panel.back):
                face.hline(0, 2, length - 1, "P1")
    side = g.piece("waist_skirt_left", "TORSO", (0, 0, -2), (1, 8, 4), pivot=(4.0, 10.2, 0))
    solid(side, "P", "smooth", 33687, 2)
