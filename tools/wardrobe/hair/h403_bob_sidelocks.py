"""Bob with Sidelocks: a short rounded bob at the nape, a soft blunt fringe and two long sidelocks
that drop straight past the jaw to the collarbone, the way the clan's girls wear it young."""
from kit_hyuga import blunt_fringe, crown, ear_panels, hime_locks
from anime import cel_box

META = {"name": "Bob with Sidelocks", "gender": "unisex",
        "description": "Short rounded bob, soft blunt fringe, long straight sidelocks to the collarbone."}


def build(g):
    crown(g, 4121, side_rows=7, back_rows=8, sideburn=2)
    nape = g.piece("bob_back", "HEAD", (-5, 0, -.5), (10, 6, 1), pivot=(0, -6.0, 4.7), rotation=(6, 0, 0))
    cel_box(nape, 4125, ring=1)
    ear_panels(g, "bob_side", 6, 4128, z0=-2, depth=7, flare=8)
    hime_locks(g, "sidelock", 10, 4132, x=4.0, z=-3.6, width=1, flare=1)
    blunt_fringe(g, "fringe", 4136, length=1, xs=(-2.6, -.8, 1.0, 2.8))
