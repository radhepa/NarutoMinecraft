"""Kappogi Apron: the white smock-apron of the kitchen and the wash-house, worn over a kimono to
keep it clean: full sleeves gathered at the wrist, a square patch pocket, the kimono's collar
showing at the throat and the skirt falling past the hips, tied with cords at the back."""
from kit_household import arm_cloth, robe_skirt
from paint import cap, solid, strip_fabric

META = {
    "name": "Kappogi Apron",
    "gender": "unisex",
    "description": "White sleeved smock-apron over a kimono: gathered wrists, patch pocket, kimono collar at the throat.",
    "tags": ["civilian", "work", "robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "plain", 37220, 3)
    cap(body, "S", seed=37220, base=3)
    f = body.front
    for x, y in ((2, 0), (3, 0), (4, 0), (5, 0), (3, 1), (4, 1)):
        f.set(x, y, "P2")
    f.set(3, 0, "S4"), f.set(5, 0, "P1")
    f.rect(4, 7, 3, 3, "S4"), f.hline(4, 6, 7, "S2")
    for face in (body.right, body.left):
        face.vline(2, 2, 11, "S2")
    robe_skirt(g, "apron", 4, "S", "plain", 37221, hem="S2")
    for arm in arm_cloth(g, "S", "plain", 37223, rows=(0, 9), base=3):
        arm.strip.hline(0, arm.strip.w - 1, 9, "S2")
        for x in range(0, arm.strip.w, 2):
            arm.strip.set(x, 9, "S1")
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        cuff = g.piece(f"{side}_gather", bone, (ox - .3, 7.6, -2.3), (5, 1, 5))
        solid(cuff, "S", "plain", 37226, 3, edge=False)
    for i, x in enumerate((-.8, .4)):
        cord = g.piece(f"back_cord_{i}", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(x, 7.6, 2.3), motion="sway")
        solid(cord, "S", "weave", 37228 + i, 2)
