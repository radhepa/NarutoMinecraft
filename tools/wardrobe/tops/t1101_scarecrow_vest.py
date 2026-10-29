"""Scarecrow Vest: Kakashi's jonin uniform, the green flak vest over a navy long-sleeved shirt with the
red swirls on the shoulders, black fingerless gloves with steel plates on the backs of the hands and a
tool pouch at the back of the hip."""
from kit_shinobi import flak_vest
from paint import fabric, solid, strip_fabric

META = {
    "name": "Scarecrow Vest",
    "gender": "unisex",
    "description": "Flak vest over a navy long-sleeved shirt, steel-plated fingerless gloves, a hip pouch.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 11001, 2)
    fabric(body.top, "D", "weave", 11001, 3), fabric(body.bottom, "D", "weave", 11002, 1)
    flak_vest(g, seed=11003)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 11010 + (side == "left"), 2, 0, 8)
        fabric(arm.top, "D", "weave", 11010, 3)
        # Folds at the elbow and the shirt cuff under the glove.
        arm.strip.hline(0, arm.strip.w - 1, 5, "D1")
        strip_fabric(arm, "K", "smooth", 11012, 2, 9, 11)
        arm.strip.hline(0, arm.strip.w - 1, 9, "K3")
        outer = arm.right if side == "right" else arm.left
        for face in (arm.front, outer):
            face.hline(1, face.w - 2, 10, "M3"), face.hline(1, face.w - 2, 11, "M2")
        arm.bottom.fill("K1")
    pouch = g.piece("hip_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(1.0, 9.0, 2.3))
    solid(pouch, "L", "leather", 11015, 2)
    pouch.back.hline(0, 2, 0, "L3"), pouch.back.set(1, 1, "M3")
