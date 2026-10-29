"""Wave Hoodie: an academy hoodie in deep teal, a broad pale wave rolling round the chest, the hood
down behind the neck, a front pocket and ribbed cuffs."""
from kit_namiashi import wave_band
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Wave Hoodie",
    "gender": "unisex",
    "description": "Deep teal hoodie, a broad pale wave round the chest, hood down, front pocket, ribbed cuffs.",
    "tags": ["shinobi", "genin", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 20291, 2)
    cap(body, "P", seed=20291)
    for y in (4, 5):
        body.strip.hline(0, body.strip.w - 1, y, "S2")
    wave_band(body.strip, 3, "S", 2)
    body.strip.hline(0, body.strip.w - 1, 6, "S1")
    body.front.hline(2, 5, 8, "P3"), body.front.vline(1, 8, 10, "P1"), body.front.vline(6, 8, 10, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    body.front.set(3, 1, "S3"), body.front.set(4, 1, "S3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 20292 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "twill", 20292, 3)
        for y in (10, 11):
            for x in range(arm.strip.w):
                arm.strip.set(x, y, "P1" if x % 2 else "P2")
    hood = g.piece("hood", "TORSO", (-3.5, 0, 0), (7, 3, 2), pivot=(0, -1.0, 1.6), rotation=(-12, 0, 0))
    solid(hood, "P", "twill", 20293, 2)
    hood.top.fill("P1")
    for face in hood.sides:
        face.hline(0, face.w - 1, 0, "S2")
