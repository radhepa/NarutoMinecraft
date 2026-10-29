"""Ash Chinstrap: the Ash Pile Burning user's look. Short dark hair combed straight back over the
crown into a few stiff points at the nape, sideburns running into a thin beard along the jaw."""
from anime import ring_shell, spike
from kit_sarutobi import beard
from paint import k, scalp

META = {"name": "Ash Chinstrap", "gender": "male",
        "description": "Hair combed straight back to stiff points at the nape, a thin chinstrap beard."}

BACK = [(-2.6, -6.4, 3.8, ((3, 2), (2, 1), (1, 1)), -112, -18), (0.0, -6.6, 4.0, ((3, 2), (2, 2), (1, 1)), -108, 0),
        (2.6, -6.4, 3.8, ((3, 2), (2, 1), (1, 1)), -112, 18), (-1.4, -4.6, 4.0, ((2, 2), (1, 1)), -132, -10),
        (1.4, -4.6, 4.0, ((2, 2), (1, 1)), -132, 10)]


def build(g):
    scalp(g, 9411, side_rows=5, back_rows=7, sideburn=3)
    hat = ring_shell(g, 9412, side_rows=5, back_rows=7, ring_row=1)
    for x in (1, 3, 4, 6):
        hat.top.vline(x, 0, 7, k("H", 1 if x in (1, 4) else 3))
    lift = g.piece("crown_lift", "HEAD", (-4, -1, -4.4), (8, 1, 6), pivot=(0, -8.2, 0), rotation=(-6, 0, 0))
    from anime import cel_box
    cel_box(lift, 9415, top_delta=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(BACK):
        spike(g, f"back_{i}", (x, y, z), (rx, 0, rz), segs, 2, 9420 + i * 3)
    beard(g, 9450, style="chinstrap")
