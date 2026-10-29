"""Chest Wraps: the whole torso bound tight in bandage cloth, a broad belly band of rough cloth at
the waist, a crossing carry strap and a single leather pauldron on the left shoulder; upper arms
and fists wound to match. A wanderer who fights bare-handed."""
from kit_shinobi import bandage
from paint import fabric, solid, strip_fabric, strip_line

META = {
    "name": "Chest Wraps",
    "gender": "unisex",
    "description": "Torso bound in bandages, a rough belly band, a crossing strap, one leather pauldron, wound fists.",
    "tags": ["shinobi", "genin", "wrap", "taijutsu"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    bandage(body.strip, 0, 1, body.strip.w - 1, 8)
    bandage(body.top, 0, 0, body.top.w - 1, body.top.h - 1)
    body.strip.hline(0, body.strip.w - 1, 1, "S2")
    # A rough belly band of cloth from the ribs to the hips.
    strip_fabric(jacket, "P", "weave", 35020, 2, 8, 10)
    jacket.strip.hline(0, jacket.strip.w - 1, 8, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1")
    strip_fabric(body, "P", "weave", 35021, 1, 9, 10)
    # A leather carry strap from the left shoulder to the right hip, front and back.
    strip_line(jacket, [(11, 0), (5, 7)], "L2"), strip_line(jacket, [(10, 0), (4, 7)], "L1")
    strip_line(jacket, [(18, 0), (23, 6)], "L2"), strip_line(jacket, [(18, 1), (23, 7)], "L1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        bandage(arm.strip, 0, 1, arm.strip.w - 1, 2)
        bandage(arm.strip, 0, 7, arm.strip.w - 1, 11)
        arm.strip.hline(0, arm.strip.w - 1, 7, "S2")
        fabric(arm.bottom, "S", "plain", 35022, 2)
    # One leather pauldron on the left shoulder, laced with two cords.
    pad = g.piece("left_pauldron", "LEFT_ARM", (-1.3, -2.5, -2.5), (5, 3, 5), rotation=(0, 0, -6), inflate=.05)
    solid(pad, "L", "leather", 35023, 2)
    for face in pad.sides:
        face.hline(0, face.w - 1, 0, "L3"), face.hline(0, face.w - 1, 2, "L1")
    pad.left.set(1, 1, "S3"), pad.left.set(3, 1, "S3")
    knot = g.piece("band_knot", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(2.0, 8.6, -2.9))
    solid(knot, "P", "weave", 35024, 2, edge=False)
