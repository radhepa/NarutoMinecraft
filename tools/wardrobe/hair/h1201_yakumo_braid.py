"""Painter's Braid: Yakumo Kurama's hair. Long light-brown hair parted on one side, the fringe swept
across the brow; one side falls straight and loose past the collarbone, the other is worked into a
braid that hangs over the front of the shoulder, held at the temple by a clip of two round beads.
The back falls in one soft sheet to the shoulder blades."""
from anime import braid, cel_box, curtain, lock, ring_shell
from kit_kurama import bead_clip, part_line, side_fringe, wave_lock
from paint import scalp

META = {"name": "Painter's Braid", "gender": "female",
        "description": "Yakumo's side part: one side loose and straight, a braid over the other shoulder, a two-bead clip."}


def build(g):
    scalp(g, 12000, side_rows=7, back_rows=8, sideburn=1, part=2)
    ring_shell(g, 12001, side_rows=7, back_rows=8, ring_row=1)
    part_line(g, 2)
    curtain(g, "back", (0, -6.0, 4.6), (-8, 0, 0), 9, 10, hem=[(0, 3, 2), (3, 3, 3), (6, 3, 2)], seed=12002)
    side_fringe(g, "fringe", 12010)
    # The loose side: a long straight lock in front of the right ear, past the collarbone.
    wave_lock(g, "loose", (-4.4, -7.6, -2.6), (0, 0, 4), ((2, 6), (2, 4), (2, 3), (1, 1)), 2, 12020, amp=.2)
    # The braided side: hair gathered over the left ear into a braid down the front of the shoulder.
    side = g.piece("braid_root", "HEAD", (-1, 0, -1.5), (2, 8, 3), pivot=(4.5, -7.6, -2.4))
    cel_box(side, 12025, ring=1)
    lock(g, "braid_gather", (4.6, -.2, -2.8), (0, 0, -4), ((2, 1),), 2, 12027, ring=None)
    braid(g, "braid", (4.7, .6, -2.9), (0, 0, -3), links=5, width=2, seed=12030)
    bead_clip(g, "clip", (5.0, -6.6, -2.4), step=(0, 1.1, .1))
