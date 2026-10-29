"""Bracer Tee: an off-white tee with short gunmetal raglan sleeves and a rust stripe across the
chest, the forearms bare but for heavy riveted steel bracers: the young guard who still blocks with
the arms."""
from kit_hagane import bracers
from paint import cap, fabric, strip_fabric

META = {
    "name": "Bracer Tee",
    "gender": "unisex",
    "description": "Off-white tee with short gunmetal raglan sleeves, a rust chest stripe, heavy riveted bracers.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "plain", 21900, 2)
    cap(body, "S", seed=21900)
    fabric(body.top, "P", "plain", 21901, 3)
    for face in body.sides:
        face.hline(0, face.w - 1, 0, "P2")
    body.front.set(3, 0, "P1"), body.front.set(4, 0, "P1"), body.front.set(3, 1, "P2"), body.front.set(4, 1, "P2")
    body.strip.hline(0, body.strip.w - 1, 4, "A2"), body.strip.hline(0, body.strip.w - 1, 5, "A1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "plain", 21902 + (side == "left"), 2, 0, 3)
        fabric(arm.top, "P", "plain", 21902, 3)
        arm.strip.hline(0, arm.strip.w - 1, 3, "P1")
    bracers(g, top=5.0, height=5, seed=21904)
