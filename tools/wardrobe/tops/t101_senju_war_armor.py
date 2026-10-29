"""Senju War Armor: Hashirama's Warring States armor. A cuirass of red lacquered lames laced in
forest green over a dark robe, broad laced shoulder guards, dark forearm guards with steel studs,
a green obi and the split-circle crest of the Senju across the back."""
from kit import belt, sleeves
from kit_senju import crest, lames, shoulder_guards
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Senju War Armor",
    "gender": "unisex",
    "description": "Red lacquered cuirass laced in green over a dark robe, laced shoulder guards, Senju crest on the back.",
    "tags": ["shinobi", "senju", "armor"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 1500, 2)
    cap(body, "D", seed=1500)
    # The cuirass: three laced lames over the chest and belly, a lit breastplate rim on top.
    strip_fabric(jacket, "P", "smooth", 1501, 2, 0, 8)
    fabric(jacket.top, "P", "smooth", 1501, 3)
    lames(jacket.strip, "P", 0, 8, step=3, lace="A2")
    jacket.front.vline(0, 0, 8, "P1"), jacket.front.vline(7, 0, 8, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 8, "K1")
    belt(g, "obi", y=8.9, role="A", height=2, buckle=None, inflate=.32)
    # Breastplate: a raised chest plate with a lit rim.
    chest = g.piece("breastplate", "TORSO", (-4, 0, -1), (8, 4, 1), pivot=(0, .4, -2.25), inflate=.1)
    solid(chest, "P", "smooth", 1502, 2)
    chest.front.hline(0, 7, 0, "P4"), chest.front.hline(0, 7, 3, "P0")
    chest.front.vline(3, 1, 2, "P1"), chest.front.vline(4, 1, 2, "P3")
    # The crest on the back at double resolution.
    back = g.piece("back_crest", "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(0, 1.2, 2.3), scale=(.5, .5, .5))
    for face in back.faces:
        fabric(face, "P", "smooth", 1503, 2)
    lames(back.back, "P", 0, 11, step=4, lace=None)
    crest(back.back, 2, 2, "S3", bar="P0")
    # Dark robe sleeves, forearm guards and the shoulder guards.
    sleeves(g, "D", "weave", 1504, 2, rows=(0, 10))
    for side in ("right", "left"):
        guard = g.part(f"{side}_sleeve")
        strip_fabric(guard, "K", "leather", 1506, 2, 5, 9)
        guard.strip.hline(0, guard.strip.w - 1, 5, "K3"), guard.strip.hline(0, guard.strip.w - 1, 9, "K1")
        for x in range(1, guard.strip.w, 4):
            guard.strip.set(x, 7, k("M", 3))
    shoulder_guards(g, length=6, seed=1508)
    collar = g.piece("collar", "TORSO", (-4.5, -1.0, -2.6), (9, 1, 5), inflate=.08)
    solid(collar, "D", "weave", 1510, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "D3")
