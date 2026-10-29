"""Tabard Tunic: a sleeveless tunic slit at the sides and falling in two short panels over the hips,
belted with a rope cord over a plain long-sleeved shirt with wrapped wrists."""
from kit import flaps
from kit_academy import shirt
from kit_shinobi import bandage
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Tabard Tunic",
    "gender": "unisex",
    "description": "Sleeveless side-slit tunic in two short panels, a rope cord belt, long sleeves and wrapped wrists.",
    "tags": ["shinobi", "genin"],
    "covers_waist": True,
}


def build(g):
    body, arms = shirt(g, "S", "plain", 31120, sleeve=11)
    for arm in arms:
        bandage(arm.strip, 0, 9, arm.strip.w - 1, 11)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "weave", 31121, 2)
    fabric(jacket.top, "P", "weave", 31121, 3)
    jacket.top.rect(2, 0, 4, 4, None)
    for face in (jacket.right, jacket.left):
        for y in range(12):
            face.clear(1, y), face.clear(2, y)
        face.vline(0, 0, 11, "P1"), face.vline(3, 0, 11, "P1")
    for face in (jacket.front, jacket.back):
        face.clear(3, 0), face.clear(4, 0)
        face.hline(2, 5, 0, "A2") if face is jacket.front else face.hline(1, 6, 0, "A2")
        face.vline(0, 0, 11, "A2"), face.vline(7, 0, 11, "A2")
    jacket.front.set(3, 1, "A2"), jacket.front.set(4, 1, "A2")
    cord = g.piece("cord", "TORSO", (-4.6, 8.4, -2.6), (9, 1, 5), inflate=.08)
    solid(cord, "L", "weave", 31122, 3, edge=False)
    for face in cord.sides:
        for x in range(0, face.w, 2):
            face.set(x, 0, "L2")
    for i, x in enumerate((-.8, .2)):
        end = g.piece(f"cord_end_{i}", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(x, 9.2, -2.9), rotation=(0, 0, 10 - 20 * i),
                      motion="flap_front")
        solid(end, "L", "weave", 31123 + i, 3)
    for face in flaps(g, "panel", 3, "P", "weave", 31125, width=8, hem=k("A", 2), top=11.4,
                      front_z=-2.75, back_z=1.75):
        face.vline(0, 0, 2, "A2"), face.vline(7, 0, 2, "A2")
