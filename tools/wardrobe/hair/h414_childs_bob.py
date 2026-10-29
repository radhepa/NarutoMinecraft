"""Child's Bob: a round little bob cut level at the jaw all the way round, a full blunt fringe to
the brows and the ends curving softly in towards the neck."""
from anime import cel_box
from kit_hyuga import blunt_fringe, crown, ear_panels

META = {"name": "Child's Bob", "gender": "unisex",
        "description": "A round bob cut level at the jaw, full blunt fringe, ends curving in at the neck."}


def build(g):
    crown(g, 4561, side_rows=7, back_rows=8, sideburn=2)
    back = g.piece("bob_back", "HEAD", (-5, 0, -.5), (10, 7, 1), pivot=(0, -6.6, 4.8), rotation=(4, 0, 0))
    cel_box(back, 4565, ring=1)
    curl = g.piece("bob_curl", "HEAD", (-5, 0, -1), (10, 1, 2), pivot=(0, .2, 4.6))
    cel_box(curl, 4567, top_delta=0)
    ear_panels(g, "bob_side", 7, 4570, z0=-3, depth=8, flare=5)
    blunt_fringe(g, "fringe", 4575, length=3, xs=(-3.0, -1.0, 1.0, 3.0), tips=False)
