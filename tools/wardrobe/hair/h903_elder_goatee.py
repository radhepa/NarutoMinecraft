"""Elder Goatee: the Third Hokage in his old age. A high bare forehead, short hair left at the
sides and back in tufts that stick out over the ears, and a pointed goatee on the chin."""
from anime import cel_box, spike
from kit_sarutobi import beard
from paint import k, scalp

META = {"name": "Elder Goatee", "gender": "male",
        "description": "Receding hair in short tufts over the ears and at the back, a pointed goatee."}

TUFTS = [(-4.0, -5.6, 1.0, ((2, 2), (1, 1)), -30, -70), (4.0, -5.6, 1.0, ((2, 2), (1, 1)), -30, 70),
         (-3.8, -5.0, 2.8, ((2, 2), (1, 1)), -60, -54), (3.8, -5.0, 2.8, ((2, 2), (1, 1)), -60, 54),
         (-2.0, -6.4, 3.8, ((3, 2), (1, 1)), -96, -24), (2.0, -6.4, 3.8, ((3, 2), (1, 1)), -96, 24),
         (0.0, -7.6, 2.8, ((2, 1), (1, 1)), -60, 0)]


def build(g):
    scalp(g, 9111, side_rows=6, back_rows=8, sideburn=2, shadow=False)
    head = g.part("head")
    # The receding hairline: forehead skin left bare across the front of the crown.
    for y in range(4, 8):
        for x in range(1 if y > 5 else 2, 7 if y > 5 else 6):
            head.top.set(x, y, None)
    head.front.hline(1, 6, 0, None)
    hat = g.part("hat")
    for f, rows in ((hat.right, 5), (hat.left, 5), (hat.back, 7)):
        for y in range(rows):
            for x in range(f.w):
                f.set(x, y, k("H", 2 if (x + y) % 3 else 1))
    for i, (x, y, z, segs, rx, rz) in enumerate(TUFTS):
        spike(g, f"crown_{i}", (x, y, z), (rx, 0, rz), segs, 2, 9120 + i * 3)
    knob = g.piece("back_knob", "HEAD", (-3, -6.8, 3.6), (6, 4, 1))
    cel_box(knob, 9140, base=2)
    beard(g, 9150, style="goatee", goatee=3)
