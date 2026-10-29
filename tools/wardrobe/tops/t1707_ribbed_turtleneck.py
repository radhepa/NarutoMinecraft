"""Ribbed Turtleneck: a close slate sweater knitted in heavy ribs, a tall rolled neck to the jaw and
black leather gloves: the young interrogator's off-duty wear."""
from kit_morino import gloves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Ribbed Turtleneck",
    "gender": "unisex",
    "description": "Close slate sweater in heavy ribs with a tall rolled neck, black leather gloves.",
    "tags": ["shinobi", "genin", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "rib", 17291, 2)
    cap(body, "S", seed=17291)
    for x in range(0, body.strip.w, 2):
        body.strip.vline(x, 1, 10, "S1")
    body.strip.hline(0, body.strip.w - 1, 11, "S3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "rib", 17292 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "S", "rib", 17292, 3)
        for x in range(0, arm.strip.w, 2):
            arm.strip.vline(x, 1, 8, "S1")
    gloves(g, top=9)
    neck = g.piece("roll_neck", "TORSO", (-2.5, -2.2, -2.5), (5, 3, 5), inflate=.1)
    solid(neck, "S", "rib", 17294, 2)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "S3")
        for x in range(0, face.w, 2):
            face.vline(x, 1, 2, "S1")
