"""Iron Coat: the jonin's long gunmetal coat, open over a dark shirt and lined in rust that shows
at the lapels and hem, a riveted steel pauldron on the right shoulder and plated bracers: the clan
elder who commands the gate watch."""
from kit import belt, flaps, sleeves
from kit_hagane import bracers, plate
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Iron Coat",
    "gender": "unisex",
    "description": "Long open gunmetal coat lined in rust, a riveted steel pauldron, plated bracers.",
    "tags": ["shinobi", "jonin", "coat"],
    "rejects": ["skirt"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 21920, 2)
    cap(body, "D", seed=21920)
    strip_fabric(jacket, "P", "twill", 21921, 2)
    cap(jacket, "P", texture="twill", seed=21921)
    # Open front: the dark shirt between rust-lined lapels.
    for y in range(0, 12):
        for x in (3, 4):
            jacket.front.clear(x, y)
    for y in range(0, 12):
        jacket.front.set(2, y, "A2" if y < 5 else "P1"), jacket.front.set(5, y, "A2" if y < 5 else "P1")
    for arm in sleeves(g, "P", "twill", 21922, 2, rows=(0, 11)):
        arm.strip.hline(0, arm.strip.w - 1, 11, "A2")
    belt(g, "belt", y=9.6, role="L", height=1, buckle="M", inflate=.1)
    front, back = flaps(g, "coat_tail", 6, "P", "twill", 21923, hem="A2")
    pauldron = g.piece("pauldron", "RIGHT_ARM", (-3.6, -1.2, -2.6), (5, 3, 5), rotation=(0, 0, 8))
    solid(pauldron, "M", "plain", 21924, 2)
    for face in pauldron.sides:
        plate(face, 0, 0, face.w, 3)
    fabric(pauldron.top, "M", "plain", 21924, 3)
    bracers(g, top=7.0, height=4, seed=21925, inflate=.1)
