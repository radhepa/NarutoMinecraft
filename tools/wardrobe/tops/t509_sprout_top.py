"""Sprout Top: the next generation's look. A dark close-cut zip top with a high collar, short sleeves
over mesh forearms, an accent stripe down each side and the crest on the back."""
from kit_nara import back_crest, net
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Sprout Top",
    "gender": "unisex",
    "description": "Dark high-collared zip top, short sleeves over mesh, side stripes, crest on the back.",
    "tags": ["shinobi", "genin", "nara"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "smooth", 5581, 2)
    cap(body, "D", texture="smooth", seed=5581)
    body.front.vline(3, 0, 11, "D0"), body.front.vline(4, 0, 11, "D3")
    body.front.set(3, 0, "M3")
    for face in (body.right, body.left):
        face.vline(1, 0, 11, "A2")
    back_crest(g, "D", "A2", 5582, y=1.6, z=2.05)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "smooth", 5583, 2, 0, 4)
        fabric(arm.top, "D", "smooth", 5583, 3)
        strip_fabric(sleeve, "D", "smooth", 5584 + (side == "left"), 2, 0, 4)
        fabric(sleeve.top, "D", "smooth", 5584, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "A2")
        net(arm.strip, 0, 5, arm.strip.w - 1, 10)
    collar = g.piece("collar", "TORSO", (-4.5, -1.8, -2.6), (9, 2, 5), inflate=.06)
    solid(collar, "D", "smooth", 5586, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "D3")
    collar.front.vline(4, 0, 1, "D0")
