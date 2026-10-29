"""Ink Haori: the head of the family's dress. A black haori worn open over a deep teal kimono with
pale crossed lapels, the haori's short skirts and wide sleeves hemmed in the pale wave, the wave
crest on the back, an accent obi and the kokuto through it."""
from kit import flaps
from kit_namiashi import crest, hip_kokuto, wave_band
from paint import cap, fabric, line, strip_fabric

META = {
    "name": "Ink Haori",
    "gender": "unisex",
    "description": "Black haori open over a teal kimono with pale lapels, wave-hemmed skirts and sleeves, crest on the back.",
    "tags": ["shinobi", "jonin", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 20231, 2)
    cap(body, "P", seed=20231)
    line(body.front, 1, 0, 4, 4, "S3"), line(body.front, 6, 0, 4, 3, "S2")
    body.strip.hline(0, body.strip.w - 1, 8, "A2"), body.strip.hline(0, body.strip.w - 1, 9, "A1")
    strip_fabric(jacket, "K", "weave", 20232, 2)
    cap(jacket, "K", seed=20232)
    for y in range(12):
        for x in (2, 3, 4, 5):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "S2"), jacket.front.set(6, y, "S2")
    for face in flaps(g, "haori", 4, "K", "weave", 20233, width=9, top=11.0, front_z=-2.8, back_z=1.8):
        wave_band(face, 2, "S", 2)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 20234 + (side == "left"), 2, 0, 9)
        strip_fabric(sleeve, "K", "weave", 20236 + (side == "left"), 2, 0, 9)
        fabric(sleeve.top, "K", "weave", 20236, 3)
        wave_band(sleeve.strip, 8, "S", 2, phase=2)
    crest(g, "back_crest", (0, 3.0, 2.3), role="K", base=2, mark="S3")
    hip_kokuto(g)
