"""Warring Topknot: Sasuke Sarutobi, Hiruzen's father, in the Warring States. The hair pulled tight
off a high forehead into a stiff topknot tied on the crown, its brush splaying up and back."""
from anime import spike, tie
from paint import k, scalp

META = {"name": "Warring Topknot", "gender": "unisex",
        "description": "Hair pulled tight to a stiff tied topknot on the crown, its brush splaying back."}


def build(g):
    scalp(g, 9361, side_rows=5, back_rows=8, sideburn=3)
    head = g.part("head")
    for x in (1, 3, 4, 6):
        head.top.vline(x, 0, 7, k("H", 3 if x in (3, 4) else 1))
    hat = g.part("hat")
    for f, rows in ((hat.right, 4), (hat.left, 4), (hat.back, 7)):
        for y in range(rows):
            for x in range(f.w):
                f.set(x, y, k("H", 2 if (x + 2 * y) % 4 else 3))
    pivot = (0, -8.0, 1.2)
    tie(g, "bun_tie", pivot, (-20, 0, 0), (3, 2, 3), y=-2.0, key="A2")
    root = g.piece("bun_root", "HEAD", (-1.5, -1, -1.5), (3, 1, 3), pivot=pivot, rotation=(-20, 0, 0))
    from anime import cel_box
    cel_box(root, 9370)
    for i, (rx, rz) in enumerate(((-58, 0), (-44, -22), (-44, 22), (-74, -10), (-74, 10))):
        spike(g, f"bun_{i}", (0, -10.0, 1.9), (rx, 0, rz), ((2, 2), (2, 2), (1, 1)), 2, 9380 + i * 3)
