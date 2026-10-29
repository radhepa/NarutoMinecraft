"""Corded Tail: combed back and tied low at the nape in one long, stiff tail bound with black cord
at three points down its length."""
from anime import lock, tie
from kit_morino import combed_back

META = {"name": "Corded Tail", "gender": "unisex",
        "description": "Combed back into one long low tail bound with black cord at three points."}

TAIL = ((3, 3), (3, 3), (2, 3), (2, 2), (1, 2))


def build(g):
    combed_back(g, 17071, side_rows=4, back_rows=7)
    pivot, rot = (0, -3.6, 4.6), (14, 0, 0)
    lock(g, "tail", pivot, rot, TAIL, 2, 17072, motion="sway")
    for i, y in enumerate((0.0, 3.0, 6.0)):
        tie(g, f"cord_{i}", pivot, rot, (4 if i < 2 else 3, 1, 3), y=y, key="K2", motion="sway")
