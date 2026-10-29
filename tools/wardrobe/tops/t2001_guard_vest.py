"""Guard's Plate Vest: the Hokage's guard. A close-fitting deep teal vest of stitched lamellar
rows with a stand collar, worn over a dark long-sleeved undersuit, the pale wave trim at the hem
and cuffs, and the black kokuto across the small of the back."""
from kit import collar
from kit_namiashi import kokuto, wave_band
from paint import cap, fabric, strip_fabric

META = {
    "name": "Guard's Plate Vest",
    "gender": "unisex",
    "description": "Deep teal lamellar vest with a stand collar over a dark undersuit, wave-trimmed hem, kokuto at the back.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 20201, 2)
    cap(body, "D", seed=20201)
    strip_fabric(jacket, "P", "plain", 20202, 2, 0, 11)
    cap(jacket, "P", seed=20202)
    # Lamellar rows: each row lit along its top edge, shaded along its lower edge.
    for y in (0, 3, 6):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P3")
        jacket.strip.hline(0, jacket.strip.w - 1, y + 2, "P1")
    for x in range(0, jacket.strip.w, 3):
        for y in (1, 4, 7):
            jacket.strip.set(x + (y // 3) % 2, y, "P1")
    jacket.front.vline(4, 0, 9, "K2")
    wave_band(jacket.strip, 9, "S", 2, ground="P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "K2")
    collar(g, "collar", "P", "plain", height=2, y=-1.4, inflate=.3)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 20203 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "plain", 20203, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2"), arm.strip.hline(0, arm.strip.w - 1, 1, "P1")
        wave_band(arm.strip, 9, "S", 2, phase=1)
        arm.strip.hline(0, arm.strip.w - 1, 11, "K2")
    kokuto(g, pivot=(-2.6, 9.4, 2.85))
