"""Uzumaki building blocks: hair clips, kanzashi hairpins and buns for the clan's hairstyles, and for
its garments the whirlpool crest, wave trim and seal-script tags of Uzushiogakure."""
from __future__ import annotations

from anime import cel_box
from glyphs import SWIRL, SWIRL_SMALL, stamp
from paint import fabric, k, solid


# -- hair ------------------------------------------------------------------------------------
def clip(g, pid: str, pivot, rotation=(0, 0, 0), length: int = 3, key: str = "K"):
    """A slim hair clip pinned flat against the hair: a dark bar with a glint at its head."""
    box = g.piece(pid, "HEAD", (-.5, 0, -.5), (1, length, 1), pivot=pivot, rotation=rotation, inflate=.05)
    solid(box, key, "smooth", 2001, 2, edge=False)
    for f in box.sides:
        f.set(0, 0, k(key, 4))
        f.set(0, length - 1, k(key, 1))
    return box


def hairpin(g, pid: str, pivot, rotation=(0, 0, 0), length: int = 12, ornament: str = "A"):
    """A kanzashi: a thin steel stick drawn at half scale with a round bead at its outer end."""
    stick = g.piece(f"{pid}_stick", "HEAD", (-.5, 0, -.5), (1, length, 1), pivot=pivot, rotation=rotation,
                    scale=(.5, .5, .5))
    solid(stick, "M", "plain", 2002, 3, edge=False)
    bead = g.piece(f"{pid}_bead", "HEAD", (-1, -2, -1), (2, 2, 2), pivot=pivot, rotation=rotation, scale=(.5, .5, .5))
    solid(bead, ornament, "smooth", 2003, 2, edge=False)
    bead.top.set(0, 0, k(ornament, 4))
    return stick


def bun(g, pid: str, pivot, rotation=(0, 0, 0), size=(4, 3, 4), seed: int = 0, base: int = 2, coil: bool = True):
    """A round bun: a hair block with a smaller cap, and a coiled strand line winding round it."""
    w, h, d = size
    box = g.piece(pid, "HEAD", (-w / 2, -h, -d / 2), size, pivot=pivot, rotation=rotation)
    cel_box(box, seed, base, ring=None, top_delta=1)
    if coil:
        for i, f in enumerate(box.sides):
            for x in range(f.w):
                f.set(x, (x + i * f.w) % h if h > 1 else 0, k("H", base - 1))
    top = g.piece(f"{pid}_cap", "HEAD", (-(w - 2) / 2, -h - 1, -(d - 2) / 2), (w - 2, 1, d - 2), pivot=pivot,
                  rotation=rotation)
    cel_box(top, seed + 1, base + 1, ring=None, top_delta=1)
    return box


def wrap_tie(g, pid: str, pivot, rotation=(0, 0, 0), size=(3, 1, 3), y: float = 0.0, key: str = "A", tag: bool = False):
    """A cloth hair wrap; with `tag` a paper seal tag hangs from it, inked with a script stroke."""
    w, h, d = size
    box = g.piece(pid, "HEAD", (-w / 2, y, -d / 2), size, pivot=pivot, rotation=rotation)
    solid(box, key, "weave", 2004, 2, edge=False)
    for f in box.sides:
        f.hline(0, f.w - 1, 0, k(key, 3))
    if tag:
        paper = g.piece(f"{pid}_tag", "HEAD", (-1, y + h, d / 2 - .5), (2, 4, 1), pivot=pivot, rotation=rotation,
                        motion="sway")
        solid(paper, "S", "plain", 2005, 3, edge=False)
        for f in (paper.back, paper.front):
            f.set(0, 1, "K1"), f.set(1, 2, "K1"), f.set(0, 3, "A2"), f.set(1, 3, "A2")
    return box


# -- garments --------------------------------------------------------------------------------
def crest_patch(g, pid: str, bone: str, pivot, size: int = 12, ground: str = "P2", ink: str = "A2", outward=None,
                rotation=(0, 0, 0)):
    """The red whirlpool of the Uzumaki on a thin double-resolution patch. `outward` names the face
    that shows ("back" on a back, "right"/"left" on the outer side of a sleeve)."""
    if outward in ("right", "left"):
        patch = g.piece(pid, bone, (0, 0, -size / 2), (1, size, size), pivot=pivot, rotation=rotation, scale=(.5, .5, .5))
    else:
        patch = g.piece(pid, bone, (-size / 2, 0, 0), (size, size, 1), pivot=pivot, rotation=rotation, scale=(.5, .5, .5))
    for f in patch.faces:
        f.fill(ground)
    rows = SWIRL if size >= 12 else SWIRL_SMALL
    face = getattr(patch, outward or "back")
    if outward == "right":
        rows = [r[::-1] for r in rows]
    off = (size - len(rows)) // 2
    stamp(face, rows, off, off, {"#": ink})
    return patch


def waves(face, y: int, role: str = "S", base: int = 3, x0: int = 0, x1: int | None = None, phase: int = 0):
    """A two-row band of rolling waves: crests on the upper row every four texels, troughs below."""
    x1 = face.w - 1 if x1 is None else x1
    for x in range(x0, x1 + 1):
        p = (x + phase) % 4
        face.set(x, y + 1, k(role, base))
        if p in (1, 2):
            face.set(x, y, k(role, base + (1 if p == 1 else 0)))
        if p == 3:
            face.set(x, y + 1, k(role, base - 1))


def seal_script(face, x0: int, y0: int, h: int, ink: str = "K1", seed: int = 0):
    """A column of seal script on a paper tag: short strokes and dots one texel wide."""
    from paint import rnd
    for y in range(y0, y0 + h):
        if rnd(x0, y, seed) < .55:
            face.set(x0, y, ink)


def seal_tags(face, y0: int, h: int, every: int = 3, paper: str = "S3", ink: str = "K1", seed: int = 0, start: int = 0):
    """A trim of paper seal tags: cream strips every `every` texels, inked down their middle."""
    for x in range(start, face.w, every):
        for y in range(y0, y0 + h):
            face.set(x, y, paper)
        seal_script(face, x, y0 + 1, max(1, h - 2), ink, seed + x)
