"""Hatake Clan Coat: the clan's formal coat, slate to the knee and open over a navy shirt, white edging
down the front, a standing collar and the white fang crest large across the back."""
from kit import flaps
from kit_hatake import CREST, decal
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Hatake Clan Coat",
    "gender": "unisex",
    "description": "Knee-length slate coat with white edging and the fang crest on the back, open over a navy shirt.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 11901, 2)
    cap(body, "D", seed=11901)
    strip_fabric(jacket, "P", "weave", 11902, 2)
    cap(jacket, "P", seed=11902)
    f = jacket.front
    for y in range(12):
        for x in (3, 4):
            f.clear(x, y)
        f.set(2, y, "S3"), f.set(5, y, "S3")
    jacket.strip.hline(0, jacket.strip.w - 1, 9, "K1")
    decal(g, "back_crest", CREST, {"o": "S3", "f": "S4"}, "P2", (0, .8, 2.3), pad=2)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 11903 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "P", "weave", 11903, 3)
        strip_fabric(sleeve, "P", "weave", 11905, 2, 0, 9)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "S3")
        arm.strip.hline(0, arm.strip.w - 1, 9, "S3")
    neck = g.piece("collar", "TORSO", (-4.5, -1.8, -2.6), (9, 2, 5), inflate=.08)
    solid(neck, "P", "weave", 11906, 2)
    neck.front.vline(4, 0, 1, "D1"), neck.front.vline(3, 0, 1, "S3"), neck.front.vline(5, 0, 1, "S3")
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "P3")
    for face in flaps(g, "skirt", 8, "P", "weave", 11907, slit=True):
        face.hline(0, face.w - 1, 7, "S3")
