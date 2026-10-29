"""Harness Shirt: a sleeveless dark high-neck shirt under a crossed leather harness, the longer
guard's blade slung on the back with its hilt over the left shoulder, black guards on the forearms
banded with the pale wave."""
from kit import collar
from kit_namiashi import back_blade, wave_band
from paint import cap, fabric, line, strip_fabric

META = {
    "name": "Harness Shirt",
    "gender": "unisex",
    "description": "Sleeveless dark high-neck shirt, crossed leather harness, a blade on the back, wave-banded arm guards.",
    "tags": ["shinobi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 20241, 2)
    cap(body, "D", seed=20241)
    for face in (body.front, body.back):
        line(face, 0, 0, 7, 9, "L2"), line(face, 7, 0, 0, 9, "L2")
        line(face, 1, 0, 7, 8, "L1"), line(face, 6, 0, 0, 8, "L3")
        face.set(3, 4, "M3"), face.set(4, 4, "M3")
    body.strip.hline(0, body.strip.w - 1, 10, "L2"), body.strip.hline(0, body.strip.w - 1, 11, "L1")
    collar(g, "collar", "D", height=2, y=-1.6, inflate=.12)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.top, "D", "weave", 20242, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "D2")
        strip_fabric(arm, "K", "smooth", 20243 + (side == "left"), 2, 5, 10)
        wave_band(arm.strip, 6, "S", 2)
    back_blade(g)
