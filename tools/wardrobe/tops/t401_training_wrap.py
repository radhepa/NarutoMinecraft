"""Training Wrap: the courtyard sparring top, a short-sleeved cream wrap crossed left over right
with a lavender edge, belted with a knotted sash, the forearms bound in white tape for palm strikes."""
from kit_hyuga import obi, wrap_front
from kit_shinobi import bandage
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Training Wrap",
    "gender": "unisex",
    "description": "Short-sleeved cream wrap top with a lavender edge, a knotted sash and taped forearms.",
    "tags": ["shinobi", "hyuga", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 4631, 2)
    cap(body, "P", texture="velvet", seed=4631)
    wrap_front(body.front, trim="A2", rows=8)
    body.back.vline(3, 1, 7, "P1")
    obi(g, "sash", "D", y=7.6, height=2, knot="side", seed=4633)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 4636, 2, 0, 3)
        fabric(arm.top, "P", "velvet", 4636, 3)
        strip_fabric(sleeve, "P", "velvet", 4637, 2, 0, 3)
        fabric(sleeve.top, "P", "velvet", 4637, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "A2")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.06)
    solid(collar, "P", "velvet", 4639, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "A2")
