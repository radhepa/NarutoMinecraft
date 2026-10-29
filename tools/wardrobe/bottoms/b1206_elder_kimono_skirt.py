"""Elder's Kimono Skirt: the lower half of the Elder's Layered Kimono, falling straight to the ankle
with the front panels overlapping, wisteria hanging from the waist, cream tabi and lacquered geta."""
from kit import flaps, side_panels
from kit_kurama import wisteria_hem
from paint import fabric, k, strip_fabric

META = {"name": "Elder's Kimono Skirt", "gender": "unisex",
        "description": "Ankle-length kimono skirt with overlapping front panels, wisteria from the waist, tabi and geta.",
        "tags": ["robe"], "locked_to": "t1210_elder_kimono"}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 12940, 2, 9, 11)
    fabric(body.bottom, "P", "velvet", 12940, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "velvet", 12941, 2, 0, 10)
        fabric(leg.top, "P", "velvet", 12941, 2)
        leg.strip.hline(0, leg.strip.w - 1, 11, "S3")
        leg.bottom.fill("K1")
        pants = g.part(f"{side}_pants")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "K2")
        pants.bottom.fill("K0")
    for face in flaps(g, "kimono", 11, "P", "velvet", 12942, width=9, hem="S3", top=11.2, front_z=-2.75, back_z=1.75):
        wisteria_hem(face, 12943, light="A3", dark="A2", stem="P1", step=2, y0=1)
        if face.name == "front":
            face.vline(5, 1, 10, "S3"), face.vline(6, 1, 10, k("P", 1))
    side_panels(g, "kimono_side", 11, "P", "velvet", hem="S3", top=11.2)
