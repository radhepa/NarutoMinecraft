"""Ceremonial Kimono Skirt: the floor-length lower half of the Mito ceremonial kimono, its hem
patterned in red waves, over white tabi and dark zori. Worn only with its kimono."""
from kit import flaps, side_panels
from kit_uzumaki import waves
from paint import fabric, strip_fabric

META = {"name": "Ceremonial Kimono Skirt", "gender": "unisex",
        "description": "Floor-length kimono skirt with a red wave hem, white tabi and dark zori.",
        "tags": ["ceremonial"], "locked_to": "t210_mito_ceremonial_kimono"}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 2440, 2, 9, 11)
    fabric(body.bottom, "P", "velvet", 2440, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "velvet", 2441, 1, 0, 10)
        fabric(leg.top, "P", "velvet", 2441, 1)
        leg.strip.hline(0, leg.strip.w - 1, 10, "S3")
        leg.strip.hline(0, leg.strip.w - 1, 11, "K1")
        leg.bottom.fill("K0")
    for face in flaps(g, "kimono", 12, "P", "velvet", 2442, width=9, hem="A1", top=11.2, front_z=-2.8, back_z=1.8):
        waves(face, 9, "A", 2)
        face.vline(5, 1, 11, "P1")
    side_panels(g, "kimono_side", 12, "P", "velvet", hem="A1", top=11.2)
