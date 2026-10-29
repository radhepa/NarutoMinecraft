"""Rose Bun: the clan's waves wound into a loose low bun at the nape like a rose bud, with wavy
tendrils escaping over the ears and down the cheeks: the elegant look of a Yuhi hostess."""
from anime import bangs, tie
from kit_yuhi import wave_box, wave_lock, wave_shell
from paint import scalp

META = {"name": "Rose Bun", "gender": "unisex",
        "description": "Waves wound into a loose low bun at the nape, wavy tendrils escaping at the cheeks."}


def build(g):
    scalp(g, 14241, side_rows=6, back_rows=8, sideburn=2)
    wave_shell(g, 14242, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 24), (-1.2, ((2, 1), (1, 1)), 34), (1.3, ((2, 1), (1, 1)), -30),
                        (2.9, ((2, 2), (1, 1)), -20)], seed=14250)
    # The bun: a wound outer coil with a smaller turn on top, offset so it reads as a bud.
    outer = g.piece("bun", "HEAD", (-2.5, -2, -1.5), (5, 4, 3), pivot=(0, -2.6, 5.4))
    wave_box(outer, 14260, base=2, ring=0, amp=.6)
    inner = g.piece("bun_turn", "HEAD", (-1.5, -1.5, -1), (3, 3, 2), pivot=(.4, -3.4, 6.9), rotation=(0, 0, 20))
    wave_box(inner, 14261, base=2, ring=0)
    tie(g, "bun_tie", (0, -2.6, 4.6), size=(4, 1, 1), y=-.5)
    for side, sign in (("right", -1), ("left", 1)):
        wave_lock(g, f"tendril_{side}", (4.3 * sign, -7.6, -3.2), (0, 0, -6 * sign), ((2, 3), (1, 3), (1, 2), (1, 1)), 1,
                  14270 + (sign > 0), amp=.4, flip=sign > 0, motion="sway")
