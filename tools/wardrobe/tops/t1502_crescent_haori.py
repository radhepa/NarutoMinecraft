"""Crescent Haori: the clan's formal coat: a night-indigo haori to mid-thigh over a pale kimono,
wide sleeves, a silver crescent on the back between the shoulders and a cord tie at the chest."""
from kit import flaps
from kit_gekko import crescent
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Crescent Haori",
    "gender": "unisex",
    "description": "Indigo haori to mid-thigh over a pale kimono, wide sleeves, a silver crescent on the back.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 15720, 2)
    cap(body, "S", seed=15720)
    strip_fabric(jacket, "P", "velvet", 15721, 2)
    cap(jacket, "P", texture="velvet", seed=15721)
    f = jacket.front
    # Open front: the kimono shows in a V, the haori's lapels edged a shade lighter.
    for y in range(12):
        half = 2 if y < 5 else 1
        for x in range(4 - half, 4 + half):
            f.clear(x, y)
        f.set(3 - half, y, "P3"), f.set(4 + half, y, "P3")
    body.front.vline(3, 0, 6, "S1")
    # The cord tie across the opening.
    tie = g.piece("chest_cord", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 5.6, -2.8))
    solid(tie, "A", "plain", 15722, 2, edge=False)
    knot = g.piece("chest_cord_knot", "TORSO", (-.5, 0, 0), (1, 2, 1), pivot=(0, 5.6, -3.0))
    solid(knot, "A", "plain", 15723, 3)
    flaps(g, "haori", 5, "P", "velvet", 15724, width=9, hem="P1", top=11.0, front_z=-2.75, back_z=1.75, slit=True)
    crescent(g, "back_crescent", (0, 3.4, 2.32), role="P", mark="S4")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 15726, 2, 0, 10)
        fabric(arm.top, "S", "weave", 15726, 3)
        strip_fabric(sleeve, "P", "velvet", 15727 + (side == "left"), 2, 0, 8)
        fabric(sleeve.top, "P", "velvet", 15727, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "P1")
        for face in sleeve.sides:
            if face.name in ("front", "back"):
                face.vline(0, 0, 8, "P1")
