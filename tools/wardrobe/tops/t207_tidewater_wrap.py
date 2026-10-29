"""Tidewater Wrap: a short kimono-cut wrap top crossed left over right, short sleeves and a short
skirt all banded in white waves, tied with an orange obi: the Uzushio genin's summer kit."""
from kit import belt, flaps
from kit_uzumaki import waves
from paint import cap, fabric, strip_fabric

META = {
    "name": "Tidewater Wrap",
    "gender": "unisex",
    "description": "Short wrap top with white wave bands on the sleeves and skirt, orange obi.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 2270, 2)
    cap(body, "P", seed=2270)
    f = body.front
    for y in range(7):
        f.set(y, y, "S3")
        if y + 1 <= 7:
            f.set(y + 1, y, "P1")
    for face in (body.right, body.back, body.left):
        waves(face, 1, "S", 3)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 2271, 2, 0, 4)
        fabric(arm.top, "P", "weave", 2271, 3)
        strip_fabric(sleeve, "P", "weave", 2272, 2, 0, 4)
        fabric(sleeve.top, "P", "weave", 2272, 3)
        waves(sleeve.strip, 3, "S", 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "D2"), arm.strip.hline(0, arm.strip.w - 1, 10, "D2")
    obi = belt(g, "obi", y=7.8, role="A", height=2, buckle=None, inflate=.12)
    obi.front.set(4, 0, "S3"), obi.front.set(4, 1, "S3")
    for face in flaps(g, "skirt", 3, "P", "weave", 2273, top=10.0, hem="S3"):
        waves(face, 1, "S", 3)
