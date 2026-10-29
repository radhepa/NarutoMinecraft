"""Kage Hat: the Hokage's wide stepped kasa, red with a white front panel bearing 火 (fire), and a white
veil hanging over the nape and shoulders."""
from glyphs import FIRE, stamp
from paint import fabric, k, rnd

META = {"name": "Kage Hat", "gender": "unisex",
        "description": "Stepped red kasa, white front panel with the fire kanji, white veil.",
        "hides_hair": ["crown", "nape"], "extras_width": 128}

# (width, top y): a stepped cone from a forehead-level brim to a narrow crown, each step two
# texels tall and overlapping the one below so the cone climbs at about 43 degrees.
STEPS = [(18, -7.0), (15, -8.4), (12, -9.8), (9, -11.2), (6, -12.6), (3, -14.0)]


def build(g):
    for i, (w, y) in enumerate(STEPS):
        disc = g.piece(f"kasa_{i}", "HEAD", (-w / 2, y, -w / 2), (w, 2 if i else 1, w))
        for face in disc.sides:
            for x in range(face.w):
                face.set(x, 0, k("A", 2 - (1 if rnd(x, i, 5) < .12 else 0)))
                if face.h > 1:
                    face.set(x, 1, "A1")
        for yy in range(w):
            for x in range(w):
                ring = min(x, yy, w - 1 - x, w - 1 - yy)
                disc.top.set(x, yy, k("A", 3 if ring == 0 else 2))
        disc.bottom.fill("A0")
        if i == 0:
            # A white rim around the brim.
            for face in disc.sides:
                face.hline(0, face.w - 1, 0, "S2")
            for yy in range(w):
                for x in range(w):
                    if min(x, yy, w - 1 - x, w - 1 - yy) == 0:
                        disc.top.set(x, yy, "S3")
    # The white front panel lies along the step noses, leaning back at the cone's slope.
    panel = g.piece("front_panel", "HEAD", (-6, -16, 0), (12, 16, 1), pivot=(0, -7.05, -9.05),
                    rotation=(-47, 0, 0), scale=(.5, .5, .5))
    fabric(panel.front, "S", "plain", 7, 3)
    stamp(panel.front, FIRE, 0, 1, {"#": "A2"})
    panel.front.hline(0, 11, 15, "S2")
    for face in (panel.top, panel.bottom, panel.right, panel.left, panel.back):
        face.fill("S2")
    # Veil: over the back and sides of the neck, under the brim.
    back = g.piece("veil_back", "HEAD", (-5, 0, 0), (10, 8, 1), pivot=(0, -6.6, 4.6))
    sides = [g.piece(f"veil_{s}", "HEAD", (0, 0, -1.5), (1, 7, 6), pivot=(x, -6.6, 1.0)) for s, x in (("right", -5.6), ("left", 4.6))]
    for box in [back] + sides:
        for face in box.faces:
            fabric(face, "S", "weave", 9, 3)
        for face in box.sides:
            for x in range(face.w):
                if x % 3 == 1:
                    face.vline(x, 1, face.h - 1, "S2")
            face.hline(0, face.w - 1, face.h - 1, "S1")
        box.bottom.fill("S1")
