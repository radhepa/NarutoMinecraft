"""Lily Blouse: a grown kunoichi's sleek sleeveless purple blouse with a high neck, a soft lavender
shawl draped round the shoulders and pinned with a blossom brooch, and long fingerless arm sleeves."""
from kit_yamanaka import flower
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Lily Blouse",
    "gender": "unisex",
    "description": "Sleeveless high-neck purple blouse, lavender shoulder shawl with a blossom brooch, long arm sleeves.",
    "tags": ["shinobi", "yamanaka"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "smooth", 7060, 2)
    cap(body, "P", texture="smooth", seed=7060)
    body.front.vline(2, 4, 10, "P1"), body.front.vline(5, 4, 10, "P3")
    strip_fabric(jacket, "P", "smooth", 7061, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 7062 + (side == "left"), 2, 3, 10)
        strip_fabric(sleeve, "P", "smooth", 7064, 2, 3, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "P3")
    shawl = g.piece("shawl", "TORSO", (-4.5, -.4, -2.6), (9, 3, 5), inflate=.2)
    solid(shawl, "S", "knit", 7065, 3)
    fabric(shawl.top, "S", "knit", 7065, 4)
    for face in shawl.sides:
        face.hline(0, face.w - 1, 2, "S2")
    for side, x in (("right", -5.4), ("left", 4.4)):
        drape = g.piece(f"shawl_{side}", "TORSO", (0, 0, -2.5), (1, 4, 5), pivot=(x, .2, 0))
        solid(drape, "S", "knit", 7066 + (x > 0), 3)
    neck = g.piece("high_neck", "TORSO", (-2, -1.6, -1.5), (4, 2, 3))
    solid(neck, "P", "smooth", 7068, 2)
    flower(g, "brooch", (-2.2, 1.0, -3.3), bone="TORSO", size=5)
