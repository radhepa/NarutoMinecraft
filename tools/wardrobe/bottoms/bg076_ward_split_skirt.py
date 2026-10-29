"""Ward Split Skirt: the medic's long skirt to the shin, split at the front to the knee over pale
leggings, banded in the corps colour at the hem, with split-toe socks and straw sandals."""
from kit import flaps, side_panels
from kit_hyuga import tabi
from paint import fabric, strip_fabric

META = {"name": "Ward Split Skirt", "gender": "unisex",
        "description": "Shin-length skirt split at the front over pale leggings, banded hem, tabi and sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 34700, 2, 9, 11)
    fabric(body.bottom, "P", "smooth", 34700, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "plain", 34701, 3, 0, 8)
        fabric(leg.top, "S", "plain", 34701, 3)
    tabi(g, "S", "K1", "A2")
    for face in flaps(g, "waist_skirt", 10, "P", "smooth", 34702, width=9, hem="A2", top=10.0, front_z=-2.9,
                      back_z=1.9, slit=True):
        face.hline(0, 8, 8, "S3")
    side_panels(g, "waist_skirt_side", 9, "P", "smooth", hem="A2", top=10.0)
