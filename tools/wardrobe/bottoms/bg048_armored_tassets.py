"""Armored Tassets: overlapping lacquered tassets hung from a belt like a short armored skirt, front,
back and over each hip, over fitted leggings and leather boots with steel toecaps."""
from kit import belt, footwear
from paint import fabric, solid, strip_fabric

META = {"name": "Armored Tassets", "gender": "unisex",
        "description": "Short skirt of lacquered tassets on a belt, fitted leggings, steel-toed boots.",
        "tags": ["shinobi", "skirt", "armor"]}

PLATES = [("front", (-4.5, 0, 0), (9, 4, 1), (0, 10.4, -2.95), "flap_front"),
          ("back", (-4.5, 0, 0), (9, 4, 1), (0, 10.4, 1.95), "flap_back"),
          ("right", (0, 0, -2.5), (1, 4, 5), (-5.0, 10.4, 0), "none"),
          ("left", (0, 0, -2.5), (1, 4, 5), (4.0, 10.4, 0), "none")]


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 33540, 2, 9, 11)
    fabric(body.bottom, "K", "plain", 33540, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 33541, 2, 0, 11)
        fabric(leg.top, "K", "plain", 33541, 2)
    footwear(g, "boot", top=7, role="L", base=2, toe="M3")
    belt(g, "waist_belt", y=9.4, role="L", height=1, buckle="M")
    for name, origin, size, pivot, motion in PLATES:
        plate = g.piece(f"waist_tasset_{name}", "TORSO", origin, size, pivot=pivot, motion=motion)
        solid(plate, "P", "smooth", 33542, 2)
        for face in plate.sides:
            face.hline(0, face.w - 1, 1, "P1"), face.hline(0, face.w - 1, 2, "P3")
            face.hline(0, face.w - 1, 3, "A2")
