"""Tassel Shades: Shibi's dark round glasses with a single cord and tassel hanging from the right
arm of the frame, as the clan's elders wear them."""
from kit_aburame import lenses
from paint import k

META = {"name": "Tassel Shades", "gender": "unisex", "covers_face": True,
        "description": "Round dark glasses with a cord and tassel hanging from one arm."}


def build(g):
    lenses(g, "K", "M", "round")
    cord = g.piece("tassel_cord", "HEAD", (-.5, 0, -.5), (1, 8, 1), pivot=(-4.35, -3.9, -2.4), rotation=(0, 0, 4),
                   scale=(.25, .5, .25), motion="sway")
    for f in cord.faces:
        f.fill(k("A", 2))
    tassel = g.piece("tassel", "HEAD", (-1, 0, -1), (2, 4, 2), pivot=(-4.5, .1, -2.4), rotation=(0, 0, 4),
                     scale=(.5, .5, .5), motion="sway")
    for f in tassel.faces:
        f.fill(k("A", 2))
    for f in tassel.sides:
        f.vline(0, 1, 3, k("A", 1)), f.hline(0, 1, 0, k("M", 3))
