"""Crest Tunic: a young Senju's short-sleeved tunic with a cream yoke and the clan crest on the chest,
bandaged forearms and a leather belt with a pouch at the hip, made for running in the woods."""
from kit import belt, pouch, roll
from kit_senju import crest
from kit_shinobi import bandage
from paint import cap, fabric, strip_fabric

META = {
    "name": "Crest Tunic",
    "gender": "unisex",
    "description": "Short-sleeved tunic, cream yoke, Senju crest on the chest, bandaged forearms, belt pouch.",
    "tags": ["shinobi", "senju", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 1560, 2)
    cap(body, "P", seed=1560)
    body.strip.hline(0, body.strip.w - 1, 0, "S3"), body.strip.hline(0, body.strip.w - 1, 1, "S2")
    body.front.clear(3, 0), body.front.clear(4, 0)
    body.front.vline(1, 2, 8, "P1"), body.front.vline(6, 2, 8, "P1")
    badge = g.piece("chest_crest", "TORSO", (-4, 0, -1), (8, 8, 1), pivot=(.6, 2.6, -2.05), scale=(.375, .375, .375))
    for face in badge.faces:
        fabric(face, "P", "weave", 1561, 2)
    crest(badge.front, 0, 0, "S3", bar="A2")
    belt(g, "belt", y=9.4, role="L", height=2)
    pouch(g, "hip_pouch", (-3.6, 10.0, -1.2), size=(2, 2, 2), flap="L3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 1562, 2, 0, 3)
        fabric(arm.top, "P", "weave", 1562, 3)
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 9)
    roll(g, "S", 2.0, prefix="sleeve_hem")
