"""Braided Crown: hair parted in the middle and drawn back, the length plaited into a single braid
wound round the head like a crown, sitting above the brow and over the back of the head: neat
under a medic's kerchief or a hood, and as tidy at sixty as at twenty."""
from anime import cel_box, ring_shell
from kit_kurama import part_line
from paint import k, scalp

META = {"name": "Braided Crown", "gender": "unisex",
        "description": "Middle-parted hair drawn back into a braid wound round the head as a crown."}


def plait(box, seed):
    cel_box(box, seed, top_delta=0)
    for f in box.sides + [box.top]:
        for x in range(f.w):
            for y in range(f.h):
                if (x + y) % 3 == 0:
                    f.set(x, y, k("H", 1))
                elif (x - y) % 3 == 1:
                    f.set(x, y, k("H", 3))


def build(g):
    scalp(g, 34870, side_rows=5, back_rows=7, sideburn=2, part=3)
    ring_shell(g, 34871, side_rows=4, back_rows=6, ring_row=1)
    part_line(g, 3)
    # The crown braid: a front span over the brow, two side spans over the ears and one round the back.
    for name, origin, size in (("braid_front", (-4.5, -9.0, -4.9), (9, 2, 1)),
                               ("braid_right", (-4.9, -8.4, -4.5), (1, 2, 9)),
                               ("braid_left", (3.9, -8.4, -4.5), (1, 2, 9)),
                               ("braid_back", (-4.5, -7.6, 3.9), (9, 2, 1))):
        box = g.piece(name, "HEAD", origin, size, inflate=.25)
        plait(box, 34872 + len(name))
