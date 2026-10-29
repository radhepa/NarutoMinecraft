"""Shinobi Face: the Village Friends Starlit face, painted on the head: brows, lash line, eyes, mouth."""

META = {"name": "Shinobi Face", "gender": "unisex", "description": "Starlit eyes looking forward, straight brows, small mouth."}

# Eyes sit in face columns 1-2 and 5-6 with the iris on the inner column, so the face looks at you.
EYES = ((1, 2), (6, 5))   # (outer, inner) per eye


def paint(g, brows: bool = True, eyes: bool = True):
    f = g.part("head").front
    for outer, inner in EYES:
        if brows:
            f.set(outer, 2, "H1"), f.set(inner, 2, "H1")
        if eyes:
            f.set(outer, 3, "E0"), f.set(inner, 3, "E0")
            f.set(outer, 4, "E4"), f.set(inner, 4, "E0")
            f.set(outer, 5, "E4"), f.set(inner, 5, "E2")
    f.set(3, 6, "X1"), f.set(4, 6, "X1")
    return f


def build(g):
    paint(g)
