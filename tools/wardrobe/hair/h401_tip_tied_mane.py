"""Tip-Tied Mane: the Hyuga prodigy's long dark hair, parted in the middle with two long locks
framing the face to the chest, the length falling loose down the back and tied off near its tip
with a plain band, so it hangs like a brush to the small of the back."""
from anime import sidelocks
from kit_hyuga import crown, ear_panels, gathered_tail, parted_fringe

META = {"name": "Tip-Tied Mane", "gender": "unisex",
        "description": "Middle-parted long hair, chest-length face locks, the length tied near its tip."}


def build(g):
    crown(g, 4041, side_rows=7, back_rows=8, sideburn=1, part=3)
    parted_fringe(g, "fringe", 4045, reach=2)
    sidelocks(g, "frame", 11, seed=4050, x=4.3, z=-3.5, flare=2, width=2)
    ear_panels(g, "side", 8, 4055, z0=-2, depth=6)
    gathered_tail(g, "mane", (0, -6.2, 4.7), -5, ((8, 5), (6, 4), (5, 4), (4, 3)), 4060, tie_at=3,
                  tip=((4, 2), (3, 2), (2, 1)), depth=2)
