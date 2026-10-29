"""Yamanaka building blocks: the flower-shop thread that runs through the clan's wardrobe. A small
five-petal blossom for hairpins, ties, brooches and floral trim, painted in the outfit's accent so
a hairpin always matches the clothes it is worn with."""
from paint import fabric, k


def flower(g, pid: str, pivot, bone: str = "HEAD", rotation=(0, 0, 0), petal: str = "A", base: int = 3,
           centre: str = "S4", size: int = 3, at=(0, 0, 0)):
    """A blossom at half scale: a cross of petals with a bright heart standing just proud of it,
    facing local -z. `size` 3 gives a 1.5-pixel flower, 5 a 2.5-pixel one; `at` moves it along the
    rotated axes, so a bloom can sit partway down a tail that shares its pivot."""
    s = (.5, .5, .5)
    ax, ay, az = (2 * v for v in at)
    across = g.piece(f"{pid}_across", bone, (ax - size / 2, ay - .5, az - .5), (size, 1, 1), pivot=pivot, rotation=rotation,
                     scale=s)
    down = g.piece(f"{pid}_down", bone, (ax - .5, ay - size / 2, az - .4), (1, size, 1), pivot=pivot, rotation=rotation, scale=s)
    for box in (across, down):
        for f in box.faces:
            f.fill(k(petal, base))
        for f in box.sides:
            f.set(0, 0, k(petal, base - 1)), f.set(f.w - 1, f.h - 1, k(petal, base - 1))
    heart = g.piece(f"{pid}_heart", bone, (ax - .5, ay - .5, az - .9), (1, 1, 1), pivot=pivot, rotation=rotation, scale=s)
    for f in heart.faces:
        f.fill(centre)
    return across, down, heart


def floral_trim(face, y: int, role: str = "A", ground: str | None = None, step: int = 3, start: int = 0):
    """A row of tiny blossoms along a hem: a bright texel flanked by petal shade every `step` columns."""
    if ground:
        face.hline(0, face.w - 1, y, ground)
    for x in range(start, face.w, step):
        face.set(x, y, k(role, 3))
        if x + 1 < face.w:
            face.set(x + 1, y, k(role, 2))


def wrapped(face, x0: int, y0: int, x1: int, y1: int, role: str = "S"):
    """Bandage turns that lean the other way from kit_shinobi.bandage, with a lit upper edge per turn."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            face.set(x, y, k(role, 2) if (x - y) % 3 == 0 else k(role, 4 if (x - y) % 3 == 1 else 3))


def petal_fabric(face, role: str, seed: int, base: int = 2, motif: str = "A"):
    """Cloth scattered with a sparse print of tiny four-texel blossoms."""
    fabric(face, role, "plain", seed, base)
    for y in range(1, face.h - 1, 4):
        for x in range((y // 4) % 2 * 2 + 1, face.w - 1, 4):
            face.set(x, y, k(motif, 3))
            face.set(x + 1, y, k(motif, 2)), face.set(x, y + 1, k(motif, 2))
