"""Cowl Vest: a side-buckled vest with a soft cloth cowl bunched round the neck and folded down over
the collarbone, worn over a long-sleeved shirt with taped knuckles: a scout's dust and cold guard."""
from kit_field import pocket, shirt, tape, vest
from paint import k, solid

META = {
    "name": "Cowl Vest",
    "gender": "unisex",
    "description": "Side-buckled vest with a bunched cloth cowl at the neck over a long-sleeved shirt.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    shirt(g, "D", 32260)
    vest(g, "P", 32264, closure="side", ribs=(4, 8))
    cowl = g.piece("cowl", "TORSO", (-4.5, -2, -2.7), (9, 3, 5), inflate=.14)
    solid(cowl, "S", "knit", 32265, 2, edge=False)
    for face in cowl.sides:
        face.hline(0, face.w - 1, 0, k("S", 3)), face.hline(0, face.w - 1, 2, k("S", 1))
    fold = g.piece("cowl_fold", "TORSO", (-3, 0, -1), (6, 2, 1), pivot=(0, .8, -2.5), rotation=(18, 0, 0))
    solid(fold, "S", "knit", 32266, 2)
    fold.front.hline(0, 5, 1, k("S", 1)), fold.front.set(2, 0, k("S", 3))
    pocket(g, "chest_pocket", (-2.4, 3.4, -2.3), (3, 4, 1), "P", 32267, snap="M3")
    for side in ("right", "left"):
        tape(g.part(f"{side}_arm"), (10,))
