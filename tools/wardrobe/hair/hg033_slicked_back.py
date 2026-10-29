"""Slicked Back: short hair combed straight back from the brow and set flat, the comb lines showing
over the crown, the ends turning up a little at the nape: a jonin analyst's or courier captain's cut."""
from anime import lock
from kit_nara import pulled_back

META = {"name": "Slicked Back", "gender": "unisex",
        "description": "Short hair combed straight back and set flat, ends flicking up at the nape."}


def build(g):
    pulled_back(g, 34820, side_rows=5, back_rows=7, sideburn=3)
    for i, x in enumerate((-2.6, -.9, .9, 2.6)):
        lock(g, f"swept_{i}", (x, -8.55, -3.6), (94, 0, 0), ((2, 4), (2, 3)), 1, 34822 + i * 5, ring=0)
    for i, (x, rz) in enumerate(((-2.4, 14), (0, 0), (2.4, -14))):
        lock(g, f"nape_{i}", (x, -1.0, 4.3), (40, 0, rz), ((3, 1), (2, 1)), 1, 34842 + i * 3, ring=None)
