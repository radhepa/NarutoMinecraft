"""White Fang Vest: Sakumo's uniform, the flak vest over a navy shirt, a short white sleeve on the left
arm trimmed in red with the swirl crest, a bandaged right forearm, black gloves, and the white-hilted
chakra sabre slung across the back on a strap over the chest."""
from glyphs import SWIRL_SMALL, stamp
from kit_hatake import white_fang_tanto
from kit_shinobi import bandage, flak_vest
from paint import fabric, k, line, solid, strip_fabric

META = {
    "name": "White Fang Vest",
    "gender": "unisex",
    "description": "Flak vest, a red-trimmed white sleeve on one arm, a bandaged forearm, a white-hilted tanto across the back.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 11101, 2)
    fabric(body.top, "D", "weave", 11101, 3), fabric(body.bottom, "D", "weave", 11102, 1)
    flak_vest(g, shoulder_swirls=False, seed=11103)
    # The sabre's strap from the right shoulder down to the left hip, over the vest.
    jacket = g.part("jacket")
    line(jacket.front, 0, 0, 7, 9, "L1"), line(jacket.front, 1, 0, 7, 8, "L2")
    line(jacket.back, 0, 9, 7, 0, "L1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 11110 + (side == "left"), 2, 0, 8)
        fabric(arm.top, "D", "weave", 11110, 3)
        strip_fabric(arm, "K", "smooth", 11112, 2, 9, 11)
        arm.strip.hline(0, arm.strip.w - 1, 9, "K3")
        arm.bottom.fill("K1")
    # Bandages wound round the right forearm.
    right = g.part("right_arm")
    for face in right.sides:
        bandage(face, 0, 5, face.w - 1, 8)
    # The white sleeve on the left upper arm: red trim and the red swirl on the outside.
    sleeve = g.piece("left_white_sleeve", "LEFT_ARM", (-1.4, -2.4, -2.4), (5, 5, 5))
    solid(sleeve, "S", "weave", 11115, 3)
    fabric(sleeve.top, "S", "weave", 11115, 4)
    for face in sleeve.sides:
        face.hline(0, face.w - 1, 4, "A2"), face.hline(0, face.w - 1, 3, "A1")
    patch = g.piece("left_sleeve_swirl", "LEFT_ARM", (0, 0, -3), (1, 6, 6), pivot=(3.65, -1.8, 0), scale=(.5, .5, .5))
    for face in patch.faces:
        face.fill("S3")
    stamp(patch.left, SWIRL_SMALL, 0, 0, {"#": "A2"})
    white_fang_tanto(g, "sabre", pivot=(-2.2, 2.6, 2.9), rotation=(0, 0, 36), length=9)
