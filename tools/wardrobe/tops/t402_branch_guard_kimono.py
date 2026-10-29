"""Branch Guard Kimono: the branch house's duty kimono, an off-white wrap with long sleeves that
hang loose from the elbow, slate trim on the collar and cuffs and a dark obi tied in a flat bow at
the back, worn tucked into hakama."""
from kit_hyuga import kimono_sleeves, obi, wrap_front
from paint import cap, solid, strip_fabric

META = {
    "name": "Branch Guard Kimono",
    "gender": "unisex",
    "description": "Off-white long-sleeved wrap kimono, slate trim, a dark obi bowed at the back.",
    "tags": ["shinobi", "hyuga", "wrap", "kimono"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 4661, 2)
    cap(body, "P", texture="velvet", seed=4661)
    wrap_front(body.front, trim="A1", rows=8)
    body.front.vline(1, 7, 11, "P1")
    obi(g, "obi", "D", y=7.0, height=3, knot="back", accent="A2", seed=4663)
    kimono_sleeves(g, "sleeve", "P", "velvet", 4666, top=3.5, length=5, trim="A1", hand_rows=9)
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.06)
    solid(collar, "P", "velvet", 4671, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "A1")
