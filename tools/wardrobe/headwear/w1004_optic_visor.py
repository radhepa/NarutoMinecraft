"""Optic Visor: the war-era Aburame's field visor, three dark strips of lens wrapped across the eyes
and round the head to a clasp at the back."""
from paint import k

META = {"name": "Optic Visor", "gender": "unisex", "covers_face": True,
        "description": "Three strips of dark lens wrapped across the eyes and round the head."}


def build(g):
    for i, y in enumerate((-4.8, -4.0, -3.2)):
        band = g.piece(f"visor_{i}", "HEAD", (-4.5, 0, -4.5), (9, 1, 9), pivot=(0, y, 0), scale=(.96, .6, .96))
        for f in band.faces:
            f.fill(k("K", 1))
        for f in band.sides:
            f.hline(0, f.w - 1, 0, k("K", 2))
        band.front.set(1 + i, 0, k("K", 4)), band.front.set(2 + i, 0, k("K", 3))
        band.front.set(5 + i % 2, 0, k("K", 3))
    clasp = g.piece("visor_clasp", "HEAD", (-1, 0, 0), (2, 3, 1), pivot=(0, -4.8, 4.62))
    for f in clasp.faces:
        f.fill(k("M", 2))
    clasp.back.set(0, 1, k("M", 4))
