"""Fan Wrap Top: a crossed wrap top with a red-lined collar, elbow sleeves flared at the hem, white
arm warmers beneath, a wide sash tied in a bow at the back and the crest above it."""
from kit import arm_bone, arm_x, belt
from kit_uchiha import arm_warmers, back_crest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Fan Wrap Top",
    "gender": "unisex",
    "description": "Crossed wrap top with a red-lined collar, flared elbow sleeves, warmers, a sash bowed at the back.",
    "tags": ["shinobi", "uchiha"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 3940, 2)
    cap(body, "P", seed=3940)
    f = body.front
    # The crossed collar: a white edge lined in red from each shoulder to the waist.
    for i in range(6):
        f.set(1 + i, i, "S3"), f.set(2 + i, i, "A2")
        if i < 4:
            f.set(6 - i, i, "S2")
    back_crest(g, "P", pivot=(0, .6, 2.05), seed=3941)
    sash = belt(g, "sash", y=7.8, role="S", height=2, buckle=None, inflate=.15)
    for face in sash.sides:
        face.hline(0, face.w - 1, 1, "A2")
    for i, (x, rz) in enumerate(((-1.4, 30), (1.4, -30))):
        loop = g.piece(f"sash_bow_{i}", "TORSO", (-1, -1, 0), (2, 2, 1), pivot=(x, 8.8, 2.75), rotation=(0, 0, rz))
        solid(loop, "S", "weave", 3942 + i, 3, edge=False)
    knot = g.piece("sash_knot", "TORSO", (-.5, -.5, 0), (1, 1, 1), pivot=(0, 8.8, 2.8))
    solid(knot, "A", "weave", 3944, 2)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 3945, 2, 0, 5)
        fabric(arm.top, "P", "weave", 3945, 3)
        flare = g.piece(f"{side}_sleeve_flare", arm_bone(side), (arm_x(side) - .5, 3.0, -2.5), (5, 2, 5), inflate=.05)
        solid(flare, "P", "weave", 3946, 2, edge=False)
        for face in flare.sides:
            face.hline(0, face.w - 1, 1, "A2")
    arm_warmers(g, rows=(6, 10), role="S", seed=3947)
