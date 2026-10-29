"""Teahouse Kosode: the server's kosode at the roadside teahouse, a small woven check, the sleeves
cut at the elbow for carrying trays, and a wide obi tied in a flat bow at the back."""
from kit_hyuga import obi
from kit_kurama import wrap_front
from kit_market import checks, sleeves
from paint import cap, k, strip_fabric

META = {
    "name": "Teahouse Kosode",
    "gender": "unisex",
    "description": "Small-check kosode with elbow sleeves and a wide obi tied in a flat bow at the back.",
    "tags": ["civilian", "wrap", "kimono"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36100, 3)
    cap(body, "P", seed=36100, base=3)
    for face in body.sides:
        checks(face, k("P", 2), 1)
    wrap_front(body.front, "S3", "S2", rows=8, start=1)
    sleeves(g, "P", "weave", 36101, rows=(0, 5), base=3)
    for side in ("right", "left"):
        for face in g.part(f"{side}_sleeve").sides:
            checks(face, k("P", 2), 1, rows=range(0, 5))
    obi(g, "obi", "A", y=7.2, height=3, knot="back", accent="S3", seed=36103)
