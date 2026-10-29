"""Tasuki Kimono: an everyday kimono for spring cleaning and the kitchen, its sleeves hitched up out
of the way by a cord that crosses in an X over the back, so the forearms are bare and the sleeves
bunch at the shoulders; a small checked tenugui is tucked into the obi."""
from kit_household import checks, overlap, sash, trim
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Tasuki Kimono",
    "gender": "unisex",
    "description": "Kimono with the sleeves tied back by a cord crossing over the back, bare forearms, tenugui at the obi.",
    "tags": ["civilian", "kimono", "wrap", "work"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 37380, 2)
    cap(body, "P", texture="weave", seed=37380)
    overlap(body.front, "D2", "P1", rows=8, under="S3")
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 37381, 2, 0, 3)
        fabric(arm.top, "P", "weave", 37381, 3)
        bunch = g.piece(f"{side}_bunch", bone, (ox - .5, -1.6, -2.5), (5, 4, 5), inflate=.12)
        solid(bunch, "P", "weave", 37382 + (side == "left"), 2)
        for face in bunch.sides:
            face.vline(1, 0, 3, "P1"), face.vline(3, 0, 3, "P1")
        trim(bunch, 1, "A2")
    for i, rz in enumerate((38, -38)):
        cord = g.piece(f"tasuki_{i}", "TORSO", (-.5, -6, -.5), (1, 12, 1), pivot=(0, 4.4, 2.35), rotation=(0, 0, rz))
        solid(cord, "A", "weave", 37385 + i, 2, edge=False)
    sash(g, "obi", "D", y=7.6, height=2, knot="back", seed=37387)
    towel = g.piece("tenugui", "TORSO", (0, 0, 0), (2, 4, 1), pivot=(1.4, 8.4, -3.0), rotation=(0, 0, -6), motion="sway")
    solid(towel, "S", "plain", 37391, 3)
    checks(towel.front, "D2", every=2)
