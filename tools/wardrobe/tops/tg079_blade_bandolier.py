"""Blade Bandolier: the young weapons specialist's sleeveless tunic with a bandolier of kunai
across the chest, rings up for a fast draw, leather bracers and taped fingers."""
from kit_specialist import bandolier
from paint import cap, strip_fabric

META = {
    "name": "Blade Bandolier",
    "gender": "unisex",
    "description": "Sleeveless tunic with a bandolier of kunai across the chest, leather bracers.",
    "tags": ["shinobi", "tunic", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 34360, 2)
    cap(body, "P", texture="weave", seed=34360)
    body.strip.hline(0, body.strip.w - 1, 0, "P3")
    body.strip.hline(0, body.strip.w - 1, 9, "S2"), body.strip.hline(0, body.strip.w - 1, 10, "S1")
    body.front.set(3, 9, "M3"), body.front.set(4, 9, "M3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "L", "leather", 34361, 2, 6, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "L3")
        arm.strip.hline(0, arm.strip.w - 1, 11, "S3")
    bandolier(g, "bandolier", "right", blades=4, seed=34362)
