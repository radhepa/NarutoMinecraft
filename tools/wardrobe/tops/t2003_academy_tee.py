"""Academy Tee: a pale grey tee for the family's youngest, a teal wave rolling across the chest and
round the back, the wave crest between the shoulders, sleeves turned up in teal."""
from kit import roll
from kit_namiashi import crest, wave_band
from paint import cap, fabric, strip_fabric

META = {
    "name": "Academy Tee",
    "gender": "unisex",
    "description": "Pale grey tee with a teal wave across the chest, the wave crest on the back, teal sleeve turn-ups.",
    "tags": ["shinobi", "genin", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 20221, 3)
    cap(body, "S", seed=20221)
    for x in (3, 4):
        body.front.set(x, 0, "P2")
    wave_band(body.strip, 5, "P", 2)
    body.strip.hline(0, body.strip.w - 1, 7, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "S1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 20222 + (side == "left"), 3, 0, 3)
        fabric(arm.top, "S", "weave", 20222, 4)
    roll(g, "P", 1.6, base=2, prefix="sleeve_turn")
    crest(g, "back_crest", (0, 2.2, 2.05), role="S", base=3, mark="P2")
