"""Shoulder Cape Top: a sleeveless top with a short half-cape thrown over the left shoulder and
pinned at the collarbone, a belt with a kunai pouch at the back and long fingerless gloves."""
from kit import arm_x, belt, pouch
from kit_kunoichi import arm_warmers
from paint import cap, solid, strip_fabric

META = {
    "name": "Shoulder Cape Top",
    "gender": "unisex",
    "description": "Sleeveless top, a short half-cape pinned over the left shoulder, belt, long gloves.",
    "tags": ["shinobi", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "plain", 33180, 2)
    cap(body, "S", seed=33180)
    body.front.hline(2, 5, 0, "S1")
    for side in ("right", "left"):
        g.part(f"{side}_arm").strip.hline(0, 15, 0, "S2")
    arm_warmers(g, "K", 33181, rows=(4, 10), band="K3")
    # The half-cape: a mantle over the left shoulder and a panel falling down the back to the hip.
    cape = g.piece("cape", "LEFT_ARM", (arm_x("left") - .7, -2.7, -2.7), (5, 5, 5), inflate=.1)
    solid(cape, "P", "weave", 33182, 2)
    cap(cape, "P", texture="weave", seed=33182)
    for face in cape.sides:
        face.hline(0, face.w - 1, 4, "A2")
    drape = g.piece("cape_drape", "TORSO", (-2.5, 0, 0), (5, 9, 1), pivot=(1.6, -.2, 2.35), rotation=(4, 0, 0),
                    motion="flap_back")
    solid(drape, "P", "weave", 33184, 2)
    drape.back.hline(0, 4, 8, "A2"), drape.back.vline(0, 0, 8, "P1"), drape.back.vline(4, 0, 8, "P3")
    shoulder = g.piece("cape_shoulder", "TORSO", (-2.5, 0, -2.6), (5, 1, 5), pivot=(1.6, -.4, 0))
    solid(shoulder, "P", "weave", 33185, 2)
    pin = g.piece("cape_pin", "TORSO", (-.5, -.5, -.5), (1, 1, 1), pivot=(2.0, 1.6, -3.0))
    solid(pin, "M", "plain", 33183, 3)
    belt(g, "belt", y=9.6, role="L", height=1, buckle="M")
    pouch(g, "back_pouch", (0, 9.4, 2.6), size=(3, 2, 1), role="L", flap="L3")
