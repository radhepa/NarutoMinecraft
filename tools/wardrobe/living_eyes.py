"""Living Eyes: the Village Friends face, ported from FaceDetails.java and ResidentModel.java.

Every feature is a flat plane just in front of the face and behind the hair layer, so lashes,
brows and the mouth can be finer than a skin pixel and can animate. Face coordinates are model
pixels: x runs from -4 (the character's right edge of the face) to 4, y from -8 (top of the head)
to 0 (chin), and the face is at z = -4.

    Starlit     lash line on face row 3, a tinted white beside a dark pupil on row 4, then the
                white glint beside the iris on row 5: three rows tall.
    Soft Glint  lash line on row 4 over the glint and the iris on row 5: lower and softer.

The iris sits in each eye's inner column and the white in the outer one. In game the whites and
irises sample the face row (9,12)/(14,12) and (10,12)/(13,12), which the face piece paints from
the eye color, and the rest sample swatches baked from the hair and skin colors. An eye color
with a `pattern` replaces the pupil and iris with one high-resolution decal (the Sharingan).
"""
from __future__ import annotations

STYLES = ("starlit", "soft_glint")
EYE_BOTTOM = -2.0   # the open eye always ends on the bottom of face row 5


def eye_top(style): return -4.0 if style == "starlit" else -3.0
def brow_top(style): return -6.0 if style == "starlit" else -5.6
def lash_height(blink): return 1 - .4 * blink
def lash_bottom(style, blink): top = eye_top(style); return top + (EYE_BOTTOM - top) * blink
def wing_top(style, blink): rest = -4.0 if style == "starlit" else -5.0; return rest + (-2.8 - rest) * blink
def wing_height(blink): return 1 - .5 * blink


# -- baked swatch colors (RGB tuples) ---------------------------------------------------------
def shade(rgb, k): return tuple(round(c * k) for c in rgb)
def blend(a, b, t): return tuple(round(x + (y - x) * t) for x, y in zip(a, b))
def brow(hair): return shade(hair, .8)
def lash(hair): return shade(hair, .35)
def shadow(skin): return shade(skin, .9)
def tint(iris, white): return blend(blend(iris, (255, 255, 255), .4), white, .68)
def pupil(iris): return shade(iris, .5)
def lip(skin): return blend(shade(skin, .78), (0xA0, 0x46, 0x48), .18)
def rose_lip(skin): return blend(shade(skin, .84), (0xCD, 0x4E, 0x62), .42)
def blush(skin): return blend(skin, (0xEC, 0x68, 0x76), .32)
def mark(skin): return shade(skin, .62)


# Cheek marks: (x from the face centre, y, width, height) per side, mirrored.
MARKS = {"whiskers": [(3.3, -1.8, 1.3, .22), (3.4, -1.35, 1.3, .22), (3.3, -.9, 1.3, .22)]}


class Plane:
    """One face plane: bone, centre (x, y, z), size (w, h), and a flat color or a decal."""

    def __init__(self, bone, x, y, z, w, h, rgb=None, pattern=None, mirror=False, glow=False):
        self.bone, self.x, self.y, self.z, self.w, self.h = bone, x, y, z, w, h
        self.rgb, self.pattern, self.mirror, self.glow = rgb, pattern, mirror, glow


def fit(x, y, left, right, top, bottom, h=1.0):
    """A one-pixel-wide plane at a centre, trimmed to the open eye: (cx, cy, w, h) or None."""
    x0, x1 = max(x - .5, left), min(x + .5, right)
    y0, y1 = max(y - h / 2, top), min(y + h / 2, bottom)
    if x1 <= x0 or y1 <= y0:
        return None
    return (x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0


def planes(style, feminine, hair, skin, iris, white, pattern=None, glow=False, brows="fine", masked=False, marks=(),
           blink=0.0, gaze=(0.0, 0.0)):
    """Every face plane for one pose, laid out exactly as ResidentModel.layer + animateFace.

    Two additions to Village Friends: `brows="bold"` draws a full-pixel brow, wider than the eye
    (a taijutsu specialist's), `marks` adds thin cheek marks (whiskers) and `masked` (headwear that covers the face) leaves only
    the neck shade.
    """
    out = []
    if masked:
        return [Plane("TORSO", 0, .35, -2.055, 4, .7, shadow(skin))]
    starlit = style == "starlit"
    top, bottom = eye_top(style), EYE_BOTTOM
    lh, lb = lash_height(blink), lash_bottom(style, blink)
    lid_top, lid_bottom = top - 1, lb - lh
    wh, wt = wing_height(blink), wing_top(style, blink)
    bt = brow_top(style)
    gx, gy = gaze
    for i in (0, 1):
        side = -1 if i == 0 else 1
        inner, near, far = side * 1.5, (-3 if side < 0 else 1), (-1 if side < 0 else 3)
        if starlit:
            out.append(Plane("HEAD", side * 2, -3.5, -4.03, 2, 1, tint(iris, white)))
        out.append(Plane("HEAD", side * 2, -2.5, -4.03, 2, 1, white))
        if pattern is not None:
            # A patterned iris fills the whole inner column of the open eye.
            f = fit(inner + gx, (top + bottom) / 2 + gy, near, far, top, bottom, bottom - top)
            if f:
                out.append(Plane("HEAD", f[0], f[1], -4.045, f[2], f[3], pattern=pattern, mirror=side > 0, glow=glow))
        else:
            for shown, y, rgb in ((starlit, -3.5, pupil(iris)), (True, -2.5, iris)):
                f = fit(inner + gx, y + gy, near, far, top, bottom)
                if shown and f:
                    out.append(Plane("HEAD", f[0], f[1], -4.045, f[2], f[3], rgb))
        if lid_bottom - lid_top > .001:
            out.append(Plane("HEAD", side * 2, (lid_top + lid_bottom) / 2, -4.065, 2, lid_bottom - lid_top, skin))
        out.append(Plane("HEAD", side * 2, lb - lh / 2, -4.08, 2, lh, lash(hair)))
        if feminine:
            out.append(Plane("HEAD", side * 3.5, wt + wh / 2, -4.08, 1, wh, lash(hair)))
            out.append(Plane("HEAD", side * 1.75, bt + .175, -4.03, 1.5, .45, brow(hair)))
            out.append(Plane("HEAD", side * 2.75, bt + .375, -4.03, .5, .35, brow(hair)))
            out.append(Plane("HEAD", side * 2.875, -1.725, -4.02, 1.25, .55, blush(skin)))
        elif brows == "bold":
            out.append(Plane("HEAD", side * 2.1, bt - .1, -4.03, 2.6, 1.1, lash(hair)))
        else:
            out.append(Plane("HEAD", side * 2, bt + .275, -4.03, 2, .55, brow(hair)))
    for name in marks:
        for x, y, w, h in MARKS[name]:
            for side in (-1, 1):
                out.append(Plane("HEAD", side * x, y, -4.02, w, h, mark(skin)))
    if feminine:
        out.append(Plane("HEAD", 0, -1.45, -4.02, 1, .5, rose_lip(skin)))
    else:
        out.append(Plane("HEAD", 0, -1.425, -4.02, 1.5, .45, lip(skin)))
    out.append(Plane("TORSO", 0, .35, -2.055, 4, .7, shadow(skin)))
    return out
