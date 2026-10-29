"""Avenger Open Shirt: a white high-collared shirt worn open to the waist, the fan crest on the back,
elbow sleeves over dark forearm guards and a thick rope belt knotted at the front."""
from kit import arm_bone, arm_x, belt
from kit_uchiha import back_crest, high_collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Avenger Open Shirt",
    "gender": "unisex",
    "description": "White high-collared shirt open to the waist, crest on the back, rope belt, dark forearm guards.",
    "tags": ["shinobi", "uchiha"],
}

# The open front: texels cleared on the shirt so the chest shows, a deep V to the belt.
OPEN = {0: (2, 5), 1: (2, 5), 2: (3, 4), 3: (3, 4), 4: (3, 4), 5: (3, 4), 6: (3, 4)}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 3801, 2)
    cap(body, "S", seed=3801)
    f = body.front
    for y, (x0, x1) in OPEN.items():
        for x in range(x0, x1 + 1):
            f.clear(x, y)
        f.set(x0 - 1, y, "S1"), f.set(x1 + 1, y, "S3")
    f.vline(1, 3, 11, "S1"), f.vline(6, 3, 11, "S1")
    back_crest(g, "S", texture="weave", seed=3802)
    high_collar(g, "S", seed=3803, height=3, trim="S4")
    # The rope belt: a thick twisted cord and a knot with two hanging ends.
    rope = belt(g, "rope", y=8.2, role="D", height=2, buckle=None, inflate=.25)
    for face in rope.sides:
        for x in range(face.w):
            face.set(x, 0, "D3" if x % 2 else "D2"), face.set(x, 1, "D1" if x % 2 else "D2")
    knot = g.piece("rope_knot", "TORSO", (-1, 0, -1), (2, 2, 1), pivot=(-1.2, 8.4, -2.9))
    solid(knot, "D", "weave", 3804, 3)
    for i, (x, rz) in enumerate(((-1.6, 6), (-.8, -6))):
        end = g.piece(f"rope_end_{i}", "TORSO", (-.5, 0, -.5), (1, 4 - i, 1), pivot=(x, 10.2, -2.9), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "D", "weave", 3805 + i, 2)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 3807, 2, 0, 5)
        fabric(arm.top, "S", "weave", 3807, 3)
        strip_fabric(sleeve, "S", "weave", 3808, 3, 0, 4)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "S1")
        fabric(sleeve.top, "S", "weave", 3808, 4)
        # Dark guards from the elbow to the wrist.
        strip_fabric(arm, "K", "leather", 3809, 2, 6, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "K3")
        band = g.piece(f"{side}_guard_band", arm_bone(side), (arm_x(side) - .3, 9.4, -2.3), (4, 1, 4), inflate=.1)
        solid(band, "K", "leather", 3810, 3)
