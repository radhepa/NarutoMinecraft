"""Kurama Genin Tunic: the practical look of the clan's young shinobi. A short-sleeved wrap tunic in
the clan color over a chain-mesh undershirt to the elbow, a narrow sash with a brush tucked through
it, bandaged forearms and a scroll pouch at the back of the hip."""
from kit import belt, pouch
from kit_kurama import wrap_front
from kit_shinobi import bandage, mesh
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Kurama Genin Tunic",
    "gender": "unisex",
    "description": "Short-sleeved wrap tunic over a mesh undershirt, a sash with a tucked brush, bandaged forearms.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 12775, 2)
    cap(body, "P", seed=12775)
    f = body.front
    for x, y in [(2, 0), (3, 0), (3, 1)]:
        f.clear(x, y)
    mesh(f, 2, 0, 3, 1, "K2")
    wrap_front(f, "A2", "P1", rows=7, start=3)
    sash = belt(g, "sash", y=8.4, role="A", height=2, buckle=None, inflate=.1)
    for face in sash.sides:
        face.hline(0, face.w - 1, 1, "A1")
    brush = g.piece("tucked_brush", "TORSO", (-.5, -4, -.5), (1, 6, 1), pivot=(2.4, 9.4, -2.75), rotation=(0, 0, 18),
                    scale=(.5, 1, .5))
    solid(brush, "L", "smooth", 12776, 3)
    brush.top.fill("K1")
    for face in brush.sides:
        face.set(0, 0, "K2"), face.set(0, 1, "M3")
    pouch(g, "scroll_pouch", (2.4, 10.4, 2.3), size=(3, 2, 1), role="L", flap="M3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 12777, 2, 0, 2)
        fabric(arm.top, "P", "weave", 12777, 3)
        mesh(arm.strip, 0, 3, arm.strip.w - 1, 5, "K2")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
        strip_fabric(sleeve, "P", "weave", 12778, 2, 0, 3)
        fabric(sleeve.top, "P", "weave", 12778, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "A2")
