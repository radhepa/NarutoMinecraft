"""Sealer Hakama: wide pleated hakama with a band of paper seal tags sewn round the hem, a stiff back
panel at the waist, over split-toe socks and straw sandals."""
from kit import flaps
from kit_hyuga import hakama_legs, tabi
from kit_specialist import seal_trim
from paint import fabric, k, solid, strip_fabric

META = {"name": "Sealer Hakama", "gender": "unisex",
        "description": "Wide pleated hakama hemmed with seal tags, stiff back panel, tabi and sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 34440, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 34440, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 34441, 2, 0, 8)
        fabric(leg.top, "D", "twill", 34441, 2)
    tabi(g)
    for box in hakama_legs(g, "hakama", "D", 34442, flare=5, length=9, top=.6):
        for face in box.sides:
            seal_trim(face, 6, 3, every=2, seed=34444, start=face.x0 % 2)
            face.hline(0, face.w - 1, 8, k("D", 0))
    for face in flaps(g, "waist_hakama", 4, "D", "twill", 34446, width=9, top=10.8, front_z=-2.8, back_z=1.8):
        for x in range(1, 9, 2):
            face.vline(x, 1, 3, k("D", 1))
    koshi = g.piece("waist_koshi_ita", "TORSO", (-2.5, 0, 0), (5, 3, 1), pivot=(0, 9.0, 2.05))
    solid(koshi, "D", "twill", 34448, 3)
    koshi.back.hline(0, 4, 0, k("D", 4))
