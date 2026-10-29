"""Drape Kunoichi: a fitted sleeveless top with a high neck, a long curtain drape thrown over the
left shoulder and falling down the back to the knee, grey wraps from elbow to knuckle, a dark sash
and the amber lantern charm at the hip."""
from kit import arm_bone, arm_x
from kit_tobari import lantern, pleats, plain_body, sash
from paint import fabric, solid

META = {
    "name": "Drape Kunoichi",
    "gender": "unisex",
    "description": "Sleeveless high-neck top, a long pleated drape over the left shoulder to the knee, forearm wraps, a lantern.",
    "tags": ["shinobi"],
}


def build(g):
    body = plain_body(g, "D", "rib", 25510)
    body.front.hline(2, 5, 0, "D3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for y in range(5, 11):
            for x in range(arm.strip.w):
                arm.strip.set(x, y, "S2" if (x + 2 * y) % 4 == 0 else "S3")
        fabric(arm.bottom, "S", "plain", 25511, 2)
    neck = g.piece("high_neck", "TORSO", (-2.5, -1.2, -1.5), (5, 2, 3), inflate=.1)
    solid(neck, "D", "rib", 25512, 2, edge=False)
    shoulder = g.piece("drape_shoulder", arm_bone("left"), (arm_x("left") - .5, -2.6, -2.5), (5, 4, 5), inflate=.2)
    solid(shoulder, "P", "twill", 25513, 2)
    for face in shoulder.sides:
        pleats(face, "P")
    front = g.piece("drape_front", "TORSO", (-1.5, 0, -.5), (3, 8, 1), pivot=(2.7, .4, -2.85), motion="flap_front")
    solid(front, "P", "twill", 25514, 2)
    pleats(front.front, "P")
    back = g.piece("drape_back", "TORSO", (-2.5, 0, -.5), (6, 17, 1), pivot=(1.5, .2, 2.75), motion="flap_back")
    solid(back, "P", "twill", 25515, 2)
    pleats(back.back, "P")
    sash(g, "sash", "K", y=9.2, knot="right")
    lantern(g, "lantern", pivot=(-2.6, 10.4, -2.9))
