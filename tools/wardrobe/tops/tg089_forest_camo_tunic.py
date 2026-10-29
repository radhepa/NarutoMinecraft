"""Forest Camo Tunic: a long-sleeved tunic blotched in leaf-shadow camouflage, a leather chest
harness with two pouches, the sleeves ending in fingerless dark gloves and a mesh scarf of netting
round the neck: for the patrols who live in the trees."""
from kit import pouch, sleeves
from kit_rugged import camo
from kit_shinobi import mesh
from paint import fabric, solid, strip_fabric, strip_line

META = {
    "name": "Forest Camo Tunic",
    "gender": "unisex",
    "description": "Long-sleeved tunic in leaf-shadow camouflage, a leather harness with pouches, a netting scarf.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 35090, 2, 0, 10)
    fabric(body.top, "P", "weave", 35090, 3)
    camo(body.strip, 35091, 0, 0, None, 11)
    camo(body.top, 35091)
    body.strip.hline(0, body.strip.w - 1, 10, "P1")
    sleeves(g, "P", "weave", 35092, 2, rows=(0, 9))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        camo(arm.strip, 35093 + (side == "left"), 0, 0, None, 9)
        camo(arm.top, 35093)
        strip_fabric(arm, "K", "leather", 35095, 2, 9, 11)
        arm.strip.hline(0, arm.strip.w - 1, 9, "K3")
        arm.front.set(1, 11, None), arm.front.set(2, 11, None)
    # The leather harness: two straps over the shoulders crossing on the back, joined by a chest band.
    jacket = g.part("jacket")
    for x in (5, 10):
        jacket.strip.vline(x, 0, 6, "L2")
    strip_line(jacket, [(18, 0), (23, 5)], "L2"), strip_line(jacket, [(21, 0), (16, 5)], "L2")
    jacket.strip.vline(17, 5, 7, "L2"), jacket.strip.vline(22, 5, 7, "L2")
    jacket.strip.hline(4, 11, 6, "L1")
    jacket.front.set(1, 6, "M3")
    pouch(g, "chest_pouch_right", (-2.6, 4.2, -2.9), size=(2, 2, 1), flap="M3")
    pouch(g, "chest_pouch_left", (2.4, 4.2, -2.9), size=(2, 2, 1), flap="M3")
    scarf = g.piece("net_scarf", "TORSO", (-4.5, -1.4, -2.7), (9, 2, 5), inflate=.08)
    solid(scarf, "K", "weave", 35096, 2)
    for face in scarf.faces:
        mesh(face, 0, 0, face.w - 1, face.h - 1, "L1")
