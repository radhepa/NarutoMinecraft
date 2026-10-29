"""Kurama Chunin Vest: the Konoha flak vest over the clan's dark shirt with a soft kimono collar,
accent cuffs at the wrists and a lacquered brush case slung across the back like a short sword: a
genjutsu painter on duty."""
from kit_shinobi import flak_vest
from paint import fabric, solid, strip_fabric

META = {
    "name": "Kurama Chunin Vest",
    "gender": "unisex",
    "description": "Flak vest over a dark kimono-collared shirt, accent cuffs, a brush case across the back.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 12800, 2)
    fabric(body.top, "D", "weave", 12800, 3)
    flak_vest(g, seed=12801)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 12806, 2, 0, 10)
        fabric(arm.top, "D", "weave", 12806, 3)
        strip_fabric(sleeve, "D", "weave", 12807, 2, 8, 9)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "A2")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "A1")
    # The kimono collar of the shirt, crossing at the throat above the vest collar.
    for i, (x, rz) in enumerate(((-1.0, -24), (1.0, 24))):
        lap = g.piece(f"shirt_collar_{i}", "TORSO", (-.5, 0, 0), (1, 3, 1), pivot=(x, -2.0, -2.9), rotation=(0, 0, rz))
        solid(lap, "S", "weave", 12808, 3)
    case = g.piece("brush_case", "TORSO", (-1, -5, -1), (2, 11, 2), pivot=(0, 5.4, 3.3), rotation=(0, 0, 40))
    solid(case, "K", "smooth", 12809, 2)
    for face in case.sides:
        face.hline(0, 1, 0, "A2"), face.hline(0, 1, 10, "A2"), face.hline(0, 1, 5, "M3")
    strap = g.piece("case_strap", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.4, 2.65), rotation=(0, 0, -42))
    solid(strap, "L", "leather", 12810, 2)
