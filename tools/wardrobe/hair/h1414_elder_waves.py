"""Elder Waves: a Yuhi elder's long wavy mane brushed straight back from a high brow, without a
fringe, gathered loosely at the nape by a cloth tie and falling in waves down the back."""
from anime import tie
from kit_yuhi import wave_lock, wave_shell
from paint import scalp

META = {"name": "Elder Waves", "gender": "unisex",
        "description": "Long wavy mane brushed back off a high brow, loosely tied at the nape with cloth."}


def build(g):
    scalp(g, 14521, side_rows=6, back_rows=8, sideburn=3)
    wave_shell(g, 14522, side_rows=6, back_rows=8, ring_row=0)
    # Swept-back waves over the crown: low wide locks lying flat toward the back.
    for i, (x, rz) in enumerate(((-2.6, 6), (0, 0), (2.6, -6))):
        wave_lock(g, f"sweep_{i}", (x, -8.2, -3.6), (86, 0, rz), ((3, 3), (3, 3), (3, 2)), 1, 14530 + i, amp=.3, flip=bool(i % 2))
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"side_{side}", (4.4 * sign, -7.0, 1.2), (14, 0, -6 * sign), ((2, 4), (2, 3), (1, 1)), 4,
                  14535 + (sign > 0), amp=.3, flip=sign > 0)
    tie(g, "tie", (0, -2.0, 4.8), size=(4, 2, 2), y=-1, key="S3")
    wave_lock(g, "mane", (0, -1.4, 4.9), (12, 0, 0), ((4, 3), (5, 3), (5, 3), (4, 2), (3, 2), (1, 1)), 2, 14540, ring=None,
              motion="sway", amp=.5)
