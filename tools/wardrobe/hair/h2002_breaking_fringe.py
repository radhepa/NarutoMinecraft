"""Breaking Fringe: a short cut whose fringe is combed across the brow in one direction, each lock
lifting and curling over at the tip like a wave about to break, the nape neat."""
from anime import ring_shell
from kit_namiashi import wave_lock
from paint import scalp

META = {"name": "Breaking Fringe", "gender": "unisex",
        "description": "Short cut, the fringe swept across the brow, each lock curling over at the tip like a wave."}

# (x, rz): every lock leans the same way, the outer ones curl highest.
FRINGE = [(-3.1, -24), (-1.6, -30), (0.1, -36), (1.8, -44)]


def build(g):
    scalp(g, 20031, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 20032, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, rz) in enumerate(FRINGE):
        wave_lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), [(((2, 2),), 0, 0), (((1, 2),), 0, -40)],
                  seed=20035 + i * 5)
    wave_lock(g, "temple", (4.35, -7.6, -3.0), (0, 0, -6), [(((1, 3),), 0, 0), (((1, 2),), 0, -40)], seed=20060)
