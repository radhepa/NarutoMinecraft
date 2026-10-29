"""Teacher Cardigan: a soft sand cardigan buttoned over a warm navy shirt for the classroom, two
patch pockets with a stub of chalk in one, sea-blue ribbing at the hem and cuffs."""
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Teacher Cardigan",
    "gender": "unisex",
    "description": "Sand knit cardigan buttoned over a navy shirt, patch pockets with chalk, sea-blue ribbing.",
    "tags": ["shinobi", "casual"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 18501, 2)
    cap(body, "D", seed=18501)
    strip_fabric(jacket, "S", "weave", 18502, 2)
    cap(jacket, "S", texture="weave", seed=18502)
    f = jacket.front
    for y in range(3):
        for x in range(3 - min(y, 1), 5 + min(y, 1)):
            f.clear(x, y)
    f.vline(4, 3, 10, "S1")
    for y in (4, 6, 8):
        f.set(3, y, "M3")
    for x0 in (1, 5):
        f.hline(x0, x0 + 1, 7, "S3"), f.hline(x0, x0 + 1, 9, "S1")
    f.set(6, 7, "S4")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "A2"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "A1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 18503, 2, 0, 11)
        strip_fabric(sleeve, "S", "weave", 18504 + (side == "left"), 2, 0, 10)
        fabric(sleeve.top, "S", "weave", 18504, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "A2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "A1")
    chalk = g.piece("chalk", "TORSO", (0, -1, 0), (1, 2, 1), pivot=(2.0, 6.4, -2.9), scale=(.5, .5, .5))
    solid(chalk, "S", "plain", 18506, 4, edge=False)
