"""Everyday Kimono: the plain kimono worn round the house and to the market, a cotton weave flecked
with splash-dyed kasuri, a contrasting collar over a white under-collar, loose elbow sleeves and a
narrow obi knotted flat at the back. Tucked in, so it sits with trousers, skirts and hakama alike."""
from kit_household import kasuri, overlap, sash, wide_sleeves
from paint import cap, strip_fabric

META = {
    "name": "Everyday Kimono",
    "gender": "unisex",
    "description": "Kasuri-flecked cotton kimono, contrasting collar, loose elbow sleeves, narrow obi tied at the back.",
    "tags": ["civilian", "kimono", "wrap"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 37000, 2)
    cap(body, "P", texture="weave", seed=37000)
    kasuri(body.strip, "P3", step=3, seed=1)
    overlap(body.front, "D2", "P1", rows=8, under="S3")
    wide_sleeves(g, "sleeve", "P", "weave", 37001, top=2.6, length=5, hem="P1",
                 pattern=lambda f, rows=None: kasuri(f, "P3", step=3, seed=2, rows=rows))
    sash(g, "obi", "A", y=7.6, height=2, knot="back", seed=37006)
