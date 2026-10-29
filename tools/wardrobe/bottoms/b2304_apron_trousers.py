"""Apron Trousers: plum-black trousers under a front and back apron of umber cloth edged with a web
line, tucked into dark leg wraps, the work wear of the clan's terrace farmers and spinners."""
from kit import flaps, footwear, legs, waistband
from kit_tsuchigumo import web_hem

META = {"name": "Apron Trousers", "gender": "unisex",
        "description": "Dark trousers under umber front and back aprons edged with a web line, dark leg wraps.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 23841)
    legs(g, "D", "twill", 23842, rows=(0, 8), crease=False)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        for y in range(5, 9):
            leg.strip.hline(0, leg.strip.w - 1, y, "K2" if y % 2 else "K1")
    footwear(g, "shoe", top=9, role="K")
    for face in flaps(g, "apron", 5, "L", "weave", 23845, width=7):
        web_hem(face, 4, "A2", "A1")
