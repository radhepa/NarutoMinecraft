"""Attendant Kimono Skirt: the long skirt of the attendant kimono, falling straight to the ankles
with the overlap down the front and a narrow hem band, over white tabi and straw sandals."""
from kit import flaps, side_panels
from kit_hyuga import tabi
from paint import fabric, strip_fabric

META = {"name": "Attendant Kimono Skirt", "gender": "unisex",
        "description": "The ankle-length skirt of the attendant kimono, white tabi, straw sandals.",
        "tags": ["hyuga", "kimono"], "locked_to": "t407_attendant_kimono"}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 4941, 2, 9, 11)
    fabric(body.bottom, "P", "velvet", 4941, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "velvet", 4942, 1, 0, 8)
    tabi(g)
    for face in flaps(g, "skirt", 11, "P", "velvet", 4943, width=9, hem="S3", top=11.0, front_z=-2.75, back_z=1.75):
        if face.name == "front":
            face.vline(6, 0, 10, "P1"), face.vline(7, 0, 10, "S3")
    side_panels(g, "skirt_side", 10, "P", "velvet", hem="S3", top=11.0)
