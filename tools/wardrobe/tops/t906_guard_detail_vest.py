"""Guard Detail Vest: Mirai Sarutobi on the Hokage's guard. The flak vest over a sleeveless dark
top, long dark arm warmers, her father's sash tied round the left upper arm and his two trench
knives sheathed at her hips."""
from kit_sarutobi import trench_knife
from kit_shinobi import flak_vest
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Guard Detail Vest",
    "gender": "unisex",
    "description": "Flak vest over a sleeveless top, arm warmers, a sash round the left arm, two sheathed knives.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 9800, 2)
    fabric(body.top, "K", "plain", 9800, 3), fabric(body.bottom, "K", "plain", 9801, 1)
    flak_vest(g, shoulder_swirls=False, seed=9802)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "rib", 9810 + (side == "left"), 2, 5, 10)
        arm.strip.hline(0, arm.strip.w - 1, 5, "D3")
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
    band = g.piece("left_arm_sash", "LEFT_ARM", (-1.45, 1.0, -2.45), (5, 2, 5))
    solid(band, "S", "weave", 9812, 2, edge=False)
    for f in band.sides:
        f.hline(0, f.w - 1, 0, k("S", 3))
    for i, rz in enumerate((-14, 8)):
        end = g.piece(f"left_arm_sash_end_{i}", "LEFT_ARM", (-.5, 0, -.5), (1, 4 - i, 1), pivot=(3.6, 2.6, 1.0 + i * .6),
                      rotation=(0, 0, rz), motion="sway")
        solid(end, "S", "weave", 9813 + i, 2)
    trench_knife(g, "right", 9815, sheathed=True)
    trench_knife(g, "left", 9817, sheathed=True)
