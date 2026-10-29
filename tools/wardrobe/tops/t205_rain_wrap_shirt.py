"""Rain Wrap Shirt: a loose dark shirt wrapped at the throat, elbow sleeves over bandaged forearms,
a rope belt with one paper seal tag and a travel hood folded down the back."""
from kit import belt
from kit_shinobi import bandage
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Rain Wrap Shirt",
    "gender": "unisex",
    "description": "Loose dark wrap shirt, bandaged forearms, rope belt with a seal tag, a hood down the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 2250, 2)
    cap(body, "P", seed=2250)
    f = body.front
    for y in range(6):
        f.set(2 + y // 2 + (y % 2), y, "P0" if y % 2 == 0 else "P3")
    for face in (body.front, body.back):
        face.vline(5, 4, 10, "P1")
    strip_fabric(jacket, "P", "twill", 2251, 2, 9, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 2252, 2, 0, 4)
        fabric(arm.top, "P", "twill", 2252, 3)
        strip_fabric(sleeve, "P", "twill", 2253, 2, 0, 5)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 5, "P1")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
    rope = belt(g, "rope", y=8.6, role="L", height=1, buckle=None, inflate=.15)
    rope.front.set(2, 0, "L3"), rope.front.set(6, 0, "L3")
    tag = g.piece("seal_tag", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(-2.6, 9.6, -2.75), rotation=(0, 0, 6),
                  motion="sway")
    solid(tag, "S", "plain", 2254, 3, edge=False)
    tag.front.set(0, 1, "K1"), tag.front.set(0, 2, "A2")
    hood = g.piece("hood", "TORSO", (-3.5, 0, 0), (7, 5, 2), pivot=(0, -.6, 2.1), rotation=(-12, 0, 0))
    solid(hood, "P", "twill", 2255, 2)
    hood.back.hline(0, 6, 0, "P3"), hood.back.vline(3, 1, 4, "P1")
    hood.bottom.fill("P0")
