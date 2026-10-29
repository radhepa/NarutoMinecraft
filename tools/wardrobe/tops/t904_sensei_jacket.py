"""Sensei Jacket: Konohamaru as a jonin and Team 7's sensei. A dark long-sleeved jacket zipped to a
stand collar, the Sarutobi crest large on the back and small on the right sleeve, and a shorter
blue scarf with one end over the chest."""
from kit_sarutobi import crest_patch, scarf
from paint import cap, fabric, strip_fabric

META = {
    "name": "Sensei Jacket",
    "gender": "unisex",
    "description": "Dark zipped jacket with the Sarutobi crest on back and sleeve, a blue scarf over the chest.",
    "tags": ["shinobi", "jonin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 9770, 2)
    cap(body, "P", texture="twill", seed=9770)
    strip_fabric(jacket, "P", "twill", 9771, 2, 9, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 9, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    f = body.front
    f.vline(3, 0, 11, "P0"), f.vline(4, 0, 11, "M3")
    for x, y in ((1, 5), (6, 5)):
        f.hline(x - 1 if x > 3 else x, x if x > 3 else x + 1, y, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 9772 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "twill", 9772, 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "S2"), arm.strip.hline(0, arm.strip.w - 1, 10, "P1")
    crest_patch(g, "back_crest", "TORSO", (0, 1.6, 2.33), "P", "A2", 9774, ground="S3")
    crest_patch(g, "sleeve_crest", "RIGHT_ARM", (-3.33, 0.4, 0), "P", "A2", 9775, face="right", ground="S3")
    scarf(g, "D", 9780, tail=6, front_tail=5)
