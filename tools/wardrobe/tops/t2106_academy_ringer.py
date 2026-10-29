"""Academy Ringer: the clan child's rust-orange ringer tee with gunmetal collar and sleeve bands, a
small riveted steel badge on the chest and cloth-wrapped wrists, ready to scrap at the Academy."""
from kit_hagane import plate
from kit_shinobi import bandage
from paint import cap, strip_fabric

META = {
    "name": "Academy Ringer",
    "gender": "unisex",
    "description": "Rust-orange ringer tee with gunmetal bands, a small steel badge on the chest, wrapped wrists.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "A", "smooth", 21930, 2)
    cap(body, "A", texture="smooth", seed=21930)
    for face in body.sides:
        face.hline(0, face.w - 1, 0, "P2")
    body.front.set(3, 0, "P1"), body.front.set(4, 0, "P1"), body.front.set(3, 1, "P2"), body.front.set(4, 1, "P2")
    body.strip.hline(0, body.strip.w - 1, 11, "P2")
    plate(body.front, 1, 3, 3, 2, rivets=False)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "A", "smooth", 21931 + (side == "left"), 2, 0, 3)
        arm.strip.hline(0, arm.strip.w - 1, 3, "P2")
        for face in arm.sides:
            bandage(face, 0, 9, face.w - 1, 10)
