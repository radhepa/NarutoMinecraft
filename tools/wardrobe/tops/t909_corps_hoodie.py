"""Corps Hoodie: the Konohamaru Corps at play. A pullover hoodie with the hood down showing two
round monkey ears, the Sarutobi crest on the chest, a kangaroo pocket and striped cuffs."""
from kit_sarutobi import crest_patch
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Corps Hoodie",
    "gender": "unisex",
    "description": "Pullover hoodie, hood down with monkey ears, the crest on the chest, striped cuffs.",
    "tags": ["genin", "casual"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 9840, 2)
    cap(body, "P", seed=9840)
    f = body.front
    for x in range(1, 7):
        f.set(x, 7, "P3")
        for y in (8, 9):
            f.set(x, y, "P2")
    for y in (8, 9):
        f.set(1, y, "P0"), f.set(6, y, "P0")
    strip_fabric(jacket, "P", "rib", 9841, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "D2")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm, cuff = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "plain", 9842 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "P", "plain", 9842, 3)
        strip_fabric(cuff, "P", "rib", 9844, 2, 8, 10)
        cuff.strip.hline(0, cuff.strip.w - 1, 9, "D2")
        cuff.strip.hline(0, cuff.strip.w - 1, 10, "P1")
    hood = g.piece("hood", "TORSO", (-4.5, 0, -1.5), (9, 4, 3), pivot=(0, -1.2, 3.0), rotation=(24, 0, 0))
    solid(hood, "P", "plain", 9845, 2)
    fabric(hood.top, "S", "plain", 9846, 2)
    hood.back.hline(0, 8, 3, "P1")
    for side, x in (("right", -3.6), ("left", 3.6)):
        ear = g.piece(f"hood_ear_{side}", "TORSO", (-1, -1, -.5), (2, 2, 1), pivot=(x, -.6, 3.2), rotation=(24, 0, 0))
        solid(ear, "P", "plain", 9847, 2)
        ear.back.set(0, 1, "S2") if side == "right" else ear.back.set(1, 1, "S2")
    crest_patch(g, "chest_crest", "TORSO", (0, 1.6, -2.08), "P", "A2", 9848, face="front", ground="S3")
