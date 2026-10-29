"""Sentinel Coat: the night guard's coat. Deep teal to the knee with a high stand collar, an
ink-dark sash, the skirts hemmed in the pale wave, and the kokuto worn across the back above the
sash."""
from kit import collar, flaps
from kit_namiashi import kokuto, wave_band
from paint import cap, fabric, strip_fabric

META = {
    "name": "Sentinel Coat",
    "gender": "unisex",
    "description": "Knee-length teal coat, high stand collar, dark sash, wave-hemmed skirts, kokuto across the back.",
    "tags": ["shinobi", "jonin", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 20261, 2)
    cap(body, "D", seed=20261)
    strip_fabric(jacket, "P", "twill", 20262, 2)
    cap(jacket, "P", texture="twill", seed=20262)
    jacket.front.vline(3, 0, 11, "P0"), jacket.front.vline(2, 0, 11, "S2")
    for y in (8, 9):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "K2" if y == 8 else "K1")
    collar(g, "collar", "P", "twill", height=2, y=-1.6, inflate=.3)
    for face in flaps(g, "coat", 7, "P", "twill", 20263, width=9, top=11.0, front_z=-2.8, back_z=1.8, slit=True):
        wave_band(face, 5, "S", 2)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 20264 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "twill", 20264, 3)
        strip_fabric(sleeve, "P", "twill", 20266, 2, 0, 10)
        fabric(sleeve.top, "P", "twill", 20266, 3)
        wave_band(sleeve.strip, 9, "S", 2, phase=1)
    kokuto(g, pivot=(-2.6, 7.6, 3.05))
