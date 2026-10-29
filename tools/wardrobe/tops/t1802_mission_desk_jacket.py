"""Mission Desk Jacket: what the chunin at the mission desk wear to hand out assignments, a short
navy jacket worn open over a sand shirt, its hem printed with a band of sea-blue waves, the
forehead protector's cloth tied round the right arm as a duty band and a brush behind the ear-line
of the collar."""
from kit_umino import waves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Mission Desk Jacket",
    "gender": "unisex",
    "description": "Short open navy jacket over a sand shirt, a band of waves at the hem, a duty band on the right arm.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 18421, 2)
    cap(body, "S", seed=18421)
    body.front.vline(4, 1, 8, "S1")
    strip_fabric(jacket, "D", "twill", 18422, 2)
    cap(jacket, "D", texture="twill", seed=18422)
    f = jacket.front
    for y in range(12):
        for x in range(3, 5) if y < 2 else range(2, 6):
            f.clear(x, y)
    f.vline(1, 2, 11, "D3"), f.vline(6, 2, 11, "D1")
    f.set(2, 0, "D3"), f.set(5, 0, "D1"), f.set(2, 1, "D3"), f.set(5, 1, "D1")
    for face in (jacket.right, jacket.back, jacket.left):
        waves(face, 9, "A3")
        face.hline(0, face.w - 1, 11, "D0")
    waves(f, 9, "A3", 0, 1), waves(f, 9, "A3", 6, 7, phase=2)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "twill", 18423 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "D", "twill", 18423, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "S3"), arm.strip.hline(0, arm.strip.w - 1, 11, "S2")
    band = g.piece("duty_band", "RIGHT_ARM", (-3.45, 1.0, -2.45), (5, 2, 5))
    solid(band, "A", "weave", 18425, 2, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, "A3")
    band.right.set(2, 1, "S4")
