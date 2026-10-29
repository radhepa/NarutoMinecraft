"""Instructor Vest: Iruka's day at the Academy, the chunin flak vest zipped over a warm navy
long-sleeved shirt, sleeves pushed to just above the wrist, a lesson scroll tucked in the back
of the vest and the cuffs trimmed with a sea-blue wave."""
from kit_shinobi import flak_vest
from kit_umino import scroll, waves
from paint import cap, fabric, strip_fabric

META = {
    "name": "Instructor Vest",
    "gender": "unisex",
    "description": "Chunin flak vest over a navy long-sleeved shirt, wave-trimmed cuffs, a lesson scroll at the back.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 18401, 2)
    cap(body, "D", seed=18401)
    flak_vest(g, seed=18402)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 18410 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "D", "weave", 18410, 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "D3")
        waves(arm.strip, 7, "A3")
    scroll(g, "lesson_scroll", (1.6, 3.6, 2.9), (0, 0, -62), length=7)
