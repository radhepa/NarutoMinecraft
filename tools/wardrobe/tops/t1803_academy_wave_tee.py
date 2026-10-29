"""Academy Wave Tee: a pupil's loose sand tee with a navy ringed collar and short sleeves, a sea-blue
wave rolling across the chest and a navy one on the back."""
from kit_umino import surf
from paint import cap, fabric, strip_fabric

META = {
    "name": "Academy Wave Tee",
    "gender": "unisex",
    "description": "Loose sand tee with a navy collar and short sleeves, a sea-blue wave across the chest.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 18441, 3)
    cap(body, "S", texture="weave", seed=18441, base=3)
    body.strip.hline(0, body.strip.w - 1, 0, "D2")
    body.front.set(3, 1, "D2"), body.front.set(4, 1, "D2")
    for face in body.sides:
        surf(face, 5, "A3", "A2", rows=2, phase=face.x0)
    body.strip.hline(0, body.strip.w - 1, 11, "S2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 18442 + (side == "left"), 3, 0, 3)
        fabric(arm.top, "S", "weave", 18442, 4)
        arm.strip.hline(0, arm.strip.w - 1, 3, "D2")
