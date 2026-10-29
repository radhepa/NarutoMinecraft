"""Shop Clerk's Maekake: the counter apprentice's striped kosode under a heavy dark maekake apron to
the knee, its shop mark printed large in white, the strings wound twice round the waist."""
from kit_kurama import wrap_front
from kit_market import mark, sleeves, stripes, waist_apron
from paint import cap, k, strip_fabric

META = {
    "name": "Shop Clerk's Maekake",
    "gender": "unisex",
    "description": "Striped kosode under a dark knee-length maekake apron printed large with a white shop mark.",
    "tags": ["civilian", "kimono", "wrap", "apron"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36260, 3)
    cap(body, "P", seed=36260, base=3)
    for face in body.sides:
        stripes(face, k("P", 1), 3)
    wrap_front(body.front, "S3", "P1", rows=8, start=1)
    sleeves(g, "P", "weave", 36261, rows=(0, 6), base=3)
    for side in ("right", "left"):
        stripes(g.part(f"{side}_sleeve").strip, k("P", 1), 3, rows=range(0, 6))
    front = waist_apron(g, "maekake", "D", 9, 36263, width=8, base=2, top=8.6, texture="twill", band="D1")
    mark(front, "yama", 1, 2, "S3")
    front.hline(0, 7, 8, "D1")
