"""Inuzuka building blocks: shaggy fur trim, claw slashes, paw prints and fang triangles, plus a
radiating burst of hair spikes for the clan's untamed manes."""
from __future__ import annotations

from anime import spike
from paint import k, rnd


def fur_face(face, role: str = "S", seed: int = 0, base: int = 2):
    """Tufted fur: columns of clumps with lit tips and shaded roots, staggered so the edge reads ragged."""
    for y in range(face.h):
        for x in range(face.w):
            clump = (x + int(rnd(x // 2, 3, seed) * 3)) % 3
            s = base + (1 if clump == 1 else 0) - (1 if clump == 0 and rnd(x, y, seed) < .6 else 0)
            if y == 0 and rnd(x, 9, seed) < .5:
                s += 1
            if y == face.h - 1 and face.h > 1:
                s -= 1
            face.set(x, y, k(role, s))


def fur_box(box, role: str = "S", seed: int = 0, base: int = 2):
    """A cuboid of fur on every face: lit top, shaded underside."""
    for f in box.sides:
        fur_face(f, role, seed + f.x0, base)
    fur_face(box.top, role, seed + 1, base + 1)
    box.bottom.fill(k(role, base - 1))
    return box


def fur_edge(face, y: int, role: str = "S", seed: int = 0, base: int = 2, depth: int = 2):
    """A ragged band of fur `depth` rows deep starting at row y, its lower edge broken into tufts."""
    for x in range(face.w):
        for dy in range(depth):
            if dy == depth - 1 and rnd(x, y, seed) < .4:
                continue
            face.set(x, y + dy, k(role, base + (1 if (x + dy) % 3 == 1 else 0) - (1 if (x + seed) % 4 == 0 else 0)))


def claw_marks(face, x0: int, y0: int, key: str, length: int = 4, n: int = 3, gap: int = 2):
    """Parallel slashes raked down and to the right, like a hound's claws."""
    for i in range(n):
        for j in range(length):
            face.set(x0 + i * gap + j // 2, y0 + j, key)


PAW = ["a.b.a",
       ".....",
       ".ccc.",
       "ccccc",
       ".ccc."]


def paw(face, x0: int, y0: int, key: str):
    """A paw print: three toes over a broad pad, 5 x 5 texels."""
    for dy, row in enumerate(PAW):
        for dx, ch in enumerate(row):
            if ch != ".":
                face.set(x0 + dx, y0 + dy, key)


def fang(face, x0: int, y0: int, key: str, h: int = 3):
    """A downward fang triangle centred on x0, the clan mark worn on cloth: h rows narrowing to a point."""
    for dy in range(h):
        face.hline(x0 - (h - 1 - dy), x0 + (h - 1 - dy), y0 + dy, key)


def fang_small(face, x0: int, y0: int, key: str):
    """A 3-wide fang: three texels over one."""
    face.hline(x0, x0 + 2, y0, key)
    face.set(x0 + 1, y0 + 1, key)


def burst(g, prefix: str, specs, seed: int, depth: int = 2, y: float = -7.7):
    """A crown of spikes: specs are (x, z, segments, tilt x, tilt z); negative tilt x leans back,
    positive tilt z leans to the character's left."""
    for i, (x, z, segs, rx, rz) in enumerate(specs):
        spike(g, f"{prefix}_{i}", (x, y, z), (rx, 0, rz), segs, depth, seed + i * 3)
