"""Tide Jacket: a zip-front deep teal jacket with a pale grey shoulder yoke, a steel zip, the pale
wave round the hem and both cuffs and the wave crest on the yoke behind."""
from kit_namiashi import crest, wave_band
from paint import cap, fabric, strip_fabric

META = {
    "name": "Tide Jacket",
    "gender": "unisex",
    "description": "Zip-front teal jacket, pale grey shoulder yoke, steel zip, wave hem and cuffs, crest behind.",
    "tags": ["shinobi", "jacket"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 20251, 2)
    cap(body, "P", seed=20251)
    fabric(body.top, "S", "twill", 20251, 3)
    for y in (0, 1):
        body.strip.hline(0, body.strip.w - 1, y, "S3" if y == 0 else "S2")
    body.strip.hline(0, body.strip.w - 1, 2, "S1")
    body.front.vline(4, 0, 11, "M3"), body.front.vline(3, 2, 11, "P1")
    wave_band(body.strip, 10, "S", 2)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 20252 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "S", "twill", 20252, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "S2"), arm.strip.hline(0, arm.strip.w - 1, 1, "S1")
        wave_band(arm.strip, 10, "S", 2, phase=1)
    crest(g, "yoke_crest", (0, 4.4, 2.05), role="P", mark="S3")
