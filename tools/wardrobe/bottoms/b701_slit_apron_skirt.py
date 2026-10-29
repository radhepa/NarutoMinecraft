"""Slit Apron Skirt: a purple wrap skirt split high at the sides over dark shorts, both legs wound
in bandages from thigh to knee, the forehead protector worn as a belt, and navy open-toe sandals."""
from kit import belt, flaps
from kit_shinobi import protector_plate, sandals
from kit_yamanaka import wrapped
from paint import fabric, strip_fabric

META = {"name": "Slit Apron Skirt", "gender": "unisex",
        "description": "Purple side-slit skirt over shorts, bandaged thighs, protector worn as a belt, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 7170, 2, 9, 11)
    fabric(body.bottom, "K", "plain", 7170, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 7171, 2, 0, 1)
        fabric(leg.top, "K", "plain", 7171, 2)
        wrapped(leg.strip, 0, 2, leg.strip.w - 1, 6)
    sandals(g)
    belt(g, "waist_band", y=9.2, role="D", height=1, buckle=None, inflate=.2)
    plate = g.piece("waist_plate", "TORSO", (-9, -4, -2), (18, 8, 2), pivot=(0, 9.7, -2.85), scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 7172, 2)
    protector_plate(plate.front)
    for face in flaps(g, "waist_skirt", 6, "P", "plain", 7173, width=9, hem="P1", top=10.2, front_z=-2.9, back_z=1.9):
        face.vline(0, 1, 5, "P1"), face.vline(8, 1, 5, "P3")
