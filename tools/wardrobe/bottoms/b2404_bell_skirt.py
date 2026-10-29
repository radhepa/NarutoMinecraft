"""Bell Skirt: a knee-length skirt cut to flare out from the hip like an upturned lily-of-the-valley
bell, its hem scalloped into points, over dark leggings and sandals."""
from kit import flaps, side_panels
from kit_shinobi import sandals
from paint import fabric, k, strip_fabric

META = {"name": "Bell Skirt", "gender": "female",
        "description": "Knee-length flared skirt with a scalloped hem like a lily bell, dark leggings, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 24731, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 24731, 1)
    body.strip.hline(0, body.strip.w - 1, 9, "D2")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "knit", 24732, 2, 0, 9)
        fabric(leg.top, "K", "knit", 24732, 2)
    for face in flaps(g, "skirt", 6, "P", "weave", 24733, width=10, top=11.6, front_z=-2.9, back_z=1.9):
        # The scalloped hem: a white bell lip every third texel between shaded dips.
        for x in range(face.w):
            face.set(x, 5, "S4" if x % 3 == 1 else k("P", 0))
            face.set(x, 4, "S3" if x % 3 == 1 else k("P", 1))
        for x in range(0, face.w, 3):
            face.vline(x, 1, 4, "P1")
    side_panels(g, "skirt_side", 6, "P", "weave", hem="S4", top=11.6)
    sandals(g)
