"""Crossed Wrap: a short-sleeved wrap top crossed left over right, a pale collar band, a wide
accent obi rolled with the pale wave, fine mesh at the forearms, the kokuto through the obi."""
from kit_namiashi import hip_kokuto, wave_band
from kit_shinobi import mesh
from paint import cap, fabric, line, strip_fabric

META = {
    "name": "Crossed Wrap",
    "gender": "unisex",
    "description": "Short-sleeved crossed wrap top, pale collar band, wide wave-rolled obi, mesh forearms, kokuto.",
    "tags": ["shinobi", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 20271, 2)
    cap(body, "P", seed=20271)
    line(body.front, 1, 0, 5, 6, "S3"), line(body.front, 2, 0, 6, 6, "S2")
    line(body.front, 6, 0, 5, 2, "S2")
    for y in range(7, 11):
        body.strip.hline(0, body.strip.w - 1, y, "A2")
    wave_band(body.strip, 8, "S", 2, ground="A2")
    body.strip.hline(0, body.strip.w - 1, 7, "A3"), body.strip.hline(0, body.strip.w - 1, 10, "A1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 20272 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 20272, 3)
        arm.strip.hline(0, arm.strip.w - 1, 4, "S2")
        mesh(arm.strip, 0, 7, arm.strip.w - 1, 10)
    hip_kokuto(g)
