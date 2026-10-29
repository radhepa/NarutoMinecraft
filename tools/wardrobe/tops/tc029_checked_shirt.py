"""Checked Shirt: a short-sleeved summer shirt of woven gingham, an open camp collar, a breast
pocket and a pale button placket. Worn loose over anything, by fathers, uncles and older boys."""
from kit_household import arm_cloth, checks
from paint import cap, solid, strip_fabric

META = {
    "name": "Checked Shirt",
    "gender": "unisex",
    "description": "Short-sleeved gingham shirt with an open camp collar, a breast pocket and pale buttons.",
    "tags": ["civilian", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 37060, 3)
    cap(body, "P", seed=37060, base=3)
    checks(body.strip, "P2", every=3, cross="P1")
    f = body.front
    f.set(3, 0, None), f.set(4, 0, None), f.set(3, 1, None)
    f.vline(4, 1, 11, "S3")
    for y in (3, 6, 9):
        f.set(4, y, "S1")
    f.rect(5, 2, 2, 2, "P3"), f.hline(5, 6, 2, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for arm in arm_cloth(g, "P", "plain", 37061, rows=(0, 4), base=3, hem="P1"):
        checks(arm.strip, "P2", every=3, cross="P1", rows=range(0, 4))
    for side, x, rz in (("right", -2.2, 30), ("left", 2.2, -30)):
        lapel = g.piece(f"collar_{side}", "TORSO", (-1, 0, 0), (2, 3, 1), pivot=(x, -.3, -2.55), rotation=(0, 0, rz))
        solid(lapel, "P", "plain", 37064 + (side == "left"), 3, edge=False)
        lapel.front.hline(0, 1, 2, "P1")
