"""Bowl Cut: a glossy helmet of straight hair, the fringe cut in one blunt line high on the forehead so the brows show and
the sides squared off over the ears, with a bright sheen across the crown."""
from anime import cel_box
from paint import scalp

META = {"name": "Bowl Cut", "gender": "unisex", "description": "Glossy bowl cut with a blunt fringe and squared sides."}


def build(g):
    scalp(g, 801, side_rows=4, back_rows=5, sideburn=0)
    cap = g.piece("bowl_crown", "HEAD", (-4.5, -8.6, -4.5), (9, 1, 9))
    cel_box(cap, 802, base=2, ring=0, top_delta=1, clump=4)
    fringe = g.piece("bowl_fringe", "HEAD", (-4.5, -8.0, -4.6), (9, 2, 1))
    cel_box(fringe, 803, base=2, ring=0, clump=4)
    for side, x in (("right", -4.6), ("left", 3.6)):
        wall = g.piece(f"bowl_{side}", "HEAD", (x, -7.6, -4.6), (1, 4, 9))
        cel_box(wall, 804 + (x > 0), base=2, ring=0, clump=4)
    back = g.piece("bowl_back", "HEAD", (-4.5, -7.6, 3.6), (9, 5, 1))
    cel_box(back, 806, base=2, ring=0, clump=4)
