"""Forest Mantle: a short shoulder cape in forest cloth over a loose long-sleeved shirt, closed at the
throat by a crest clasp, the back of the cape bearing the crest. For walks in the Nara woods."""
from kit_nara import back_crest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Forest Mantle",
    "gender": "unisex",
    "description": "Short shoulder cape with a crest clasp over a loose long-sleeved shirt.",
    "tags": ["shinobi", "nara", "cloak"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 5551, 2)
    cap(body, "S", seed=5551)
    body.front.vline(3, 5, 11, "S1"), body.front.set(4, 6, "S1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 5552 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "S", "weave", 5552, 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "S1"), arm.strip.hline(0, arm.strip.w - 1, 10, "K2")
    # The mantle: a shell over the shoulders and upper arms, flaring a little.
    cape = g.piece("mantle", "TORSO", (-6, 0, -3), (12, 6, 6), pivot=(0, -.6, 0), inflate=.1)
    solid(cape, "P", "weave", 5554, 2)
    for face in cape.sides:
        face.hline(0, face.w - 1, 5, "P1")
        face.hline(0, face.w - 1, 0, "P3")
    cape.top.fill("P3")
    for x in (2, 9):
        cape.front.vline(x, 1, 5, "P1")
    back = g.piece("mantle_back", "TORSO", (-6, 0, 0), (12, 4, 1), pivot=(0, 5.2, 2.6), motion="flap_back")
    solid(back, "P", "weave", 5555, 2)
    back.back.hline(0, 11, 3, "P1")
    back_crest(g, "P", "K1", 5556, y=.4, z=3.15)
    clasp = g.piece("clasp", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(0, .2, -3.4))
    solid(clasp, "M", "plain", 5557, 3, edge=False)
    clasp.front.set(0, 0, "M4"), clasp.front.set(1, 1, "M1")
