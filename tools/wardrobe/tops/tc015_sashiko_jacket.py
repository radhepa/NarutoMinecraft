"""Sashiko Jacket: a heavy jacket of layered cotton quilted all over in white running stitch for
wear, the collar band in a plain dark cloth, the sleeves pushed to three quarters and a cloth belt."""
from kit_kurama import wrap_front
from kit_market import sash, sashiko, sleeves
from paint import cap, strip_fabric

META = {
    "name": "Sashiko Jacket",
    "gender": "unisex",
    "description": "Heavy jacket quilted all over in white running stitch, dark collar band, three-quarter sleeves.",
    "tags": ["civilian", "jacket", "work", "wrap"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 36300, 2)
    cap(body, "P", seed=36300)
    for face in body.sides:
        sashiko(face, "P4", 3)
    wrap_front(body.front, "K2", "K3", rows=8, start=1)
    body.front.set(0, 0, "K3")
    sleeves(g, "P", "plain", 36301, rows=(0, 8))
    for side in ("right", "left"):
        sashiko(g.part(f"{side}_sleeve").strip, "P4", 3, rows=range(0, 8))
    sash(g, "belt", "K", 36303, y=8.8, height=1, base=3, knot="back")
