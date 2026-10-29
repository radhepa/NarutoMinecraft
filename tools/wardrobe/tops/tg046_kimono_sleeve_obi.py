"""Kimono Sleeve Top: a short wrapped top with wide kimono sleeves that hang open to the elbow,
lined in the accent, closed by a wide obi with a cord and a flat bow at the back."""
from kit_kunoichi import kimono_sleeves, obi, wrap_front
from paint import cap, strip_fabric

META = {
    "name": "Kimono Sleeve Top",
    "gender": "unisex",
    "description": "Short wrap top with wide hanging kimono sleeves, a wide obi with cord and back bow.",
    "tags": ["shinobi", "chunin", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 33100, 2, 0, 10)
    cap(body, "P", texture="weave", seed=33100)
    wrap_front(body.front, "P", rows=7)
    for y in range(6):
        body.front.set(min(7, 2 + y), y, "S3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 33101, 2, 0, 5)
        strip_fabric(arm, "S", "plain", 33102, 3, 6, 9)
    kimono_sleeves(g, "kimono_sleeve", "P", 33103, length=6, trim="A2")
    obi(g, "obi", y=7.6, role="A", height=2, knot="back", cord="S3", seed=33105)
