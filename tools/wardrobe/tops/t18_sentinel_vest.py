"""Sentinel Vest: the jonin flak vest over a navy shirt, black fingerless gloves with steel back
plates and a tanto riding across the small of the back: the jonin on the wall at night."""
from kit_shinobi import flak_vest, tanto
from paint import fabric, strip_fabric

META = {
    "name": "Sentinel Vest",
    "gender": "unisex",
    "description": "Flak vest over a navy shirt, steel-plated fingerless gloves and a tanto at the back.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 351, 2)
    fabric(body.top, "D", "weave", 351, 3), fabric(body.bottom, "D", "weave", 352, 1)
    flak_vest(g, seed=353)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 360 + (side == "left"), 2, 0, 8)
        fabric(arm.top, "D", "weave", 360, 3)
        strip_fabric(arm, "K", "smooth", 362, 2, 9, 11)
        arm.strip.hline(0, arm.strip.w - 1, 9, "K3")
        # A steel plate on the back of each hand, the fingertips bare below the glove.
        outer = arm.right if side == "right" else arm.left
        for face in (arm.front, outer):
            face.hline(1, face.w - 2, 10, "M3"), face.hline(1, face.w - 2, 11, "M2")
        arm.bottom.fill("K1")
    tanto(g, "tanto", pivot=(-3.0, 9.2, 2.6), rotation=(0, 0, -78), length=8)
