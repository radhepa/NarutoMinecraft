"""Runner Wrap: a sleeveless fitted gunmetal top for the fastest messengers, off-white bandage
wound round the upper arms, a rust sash and a slim dispatch tube across the back; plated bracers
on the forearms."""
from kit import belt
from kit_hagane import bracers
from kit_shinobi import bandage
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Runner Wrap",
    "gender": "unisex",
    "description": "Sleeveless fitted gunmetal top, bandaged upper arms, a rust sash, a dispatch tube, bracers.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "smooth", 21960, 2)
    cap(body, "D", texture="smooth", seed=21960)
    body.front.hline(2, 5, 0, "D1"), body.front.set(3, 1, "D1"), body.front.set(4, 1, "D1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.top, "D", "smooth", 21961, 3)
        for face in arm.sides:
            bandage(face, 0, 1, face.w - 1, 3)
    belt(g, "sash", y=9.2, role="A", buckle=None, height=2, inflate=.1)
    tube = g.piece("dispatch_tube", "TORSO", (-1, -5, -1), (2, 10, 2), pivot=(0, 5.0, 3.1), rotation=(0, 0, -40))
    solid(tube, "P", "smooth", 21962, 2)
    for face in tube.sides:
        face.hline(0, 1, 0, "M3"), face.hline(0, 1, 9, "M3"), face.hline(0, 1, 4, "A2")
    strap = g.piece("tube_strap", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.0, 2.65), rotation=(0, 0, 38))
    solid(strap, "L", "leather", 21963, 2)
    bracers(g, top=6.0, height=4, seed=21964)
