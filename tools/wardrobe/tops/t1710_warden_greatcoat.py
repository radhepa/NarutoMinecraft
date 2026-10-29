"""Warden's Greatcoat: the clan head's ankle-length black greatcoat, a wide oxblood mantle collar
over the shoulders, a steel chain clasped across the chest, an oxblood sash and the pine crest of
the Morino on the back."""
from kit import arm_x
from kit_morino import back_crest, coat_skirts
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Warden's Greatcoat",
    "gender": "unisex",
    "description": "Ankle-length black greatcoat, wide oxblood mantle collar, steel chain clasp, crest on the back.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 17321, 2)
    cap(body, "D", seed=17321)
    strip_fabric(jacket, "P", "twill", 17322, 2)
    cap(jacket, "P", texture="twill", seed=17322)
    for y in range(12):
        jacket.front.clear(3, y), jacket.front.clear(4, y)
        jacket.front.set(2, y, "P3"), jacket.front.set(5, y, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 9, "A2"), jacket.strip.hline(0, jacket.strip.w - 1, 10, "A1")
    for x in (2, 3, 4, 5):
        jacket.front.set(x, 9, "A2"), jacket.front.set(x, 10, "A1")
    chain = g.piece("chain", "TORSO", (-2, 0, 0), (4, 1, 1), pivot=(0, 2.6, -2.75))
    solid(chain, "M", "plain", 17323, 3)
    chain.front.set(1, 0, "M1"), chain.front.set(3, 0, "M1")
    mantle = g.piece("mantle", "TORSO", (-4.5, -.4, -2.6), (9, 3, 5), inflate=.35)
    solid(mantle, "A", "weave", 17324, 1)
    fabric(mantle.top, "A", "weave", 17324, 2)
    for face in mantle.sides:
        face.hline(0, face.w - 1, 0, "A2")
        face.hline(0, face.w - 1, 2, "A0")
    mantle.front.vline(4, 0, 2, "A0")
    neck = g.piece("collar", "TORSO", (-4.5, -2.4, -2.6), (9, 2, 5), inflate=.4)
    solid(neck, "A", "weave", 17325, 1)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "A2")
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 17326 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "twill", 17326, 3)
        strip_fabric(sleeve, "P", "twill", 17328, 2, 0, 10)
        fabric(sleeve.top, "P", "twill", 17328, 3)
        cuff = g.piece(f"{side}_cuff", bone, (arm_x(side) - .4, 8.6, -2.4), (5, 2, 5), inflate=.1)
        solid(cuff, "A", "weave", 17329, 1)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 0, "A2")
    back_crest(g, "P", "A2", 17330, y=3.4, z=2.55)
    coat_skirts(g, "skirt", 11, "P", 17331, lining="A1", hem="A1")
