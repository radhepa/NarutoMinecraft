"""Spinner Jacket: a short cropped jacket in ochre, open over a pale shirt, with plum web lines
running out from the collar over the shoulders and the earth spider on the back."""
from kit import body, neckline, sleeves
from kit_tsuchigumo import drawn_line, spider_crest
from paint import k

META = {
    "name": "Spinner Jacket",
    "gender": "unisex",
    "description": "Short open ochre jacket over a pale shirt, plum web lines from the collar, spider on the back.",
    "tags": ["shinobi", "jacket"],
}


def build(g):
    shirt = body(g, "S", "weave", 23611)
    neckline(shirt.front, "v", "S")
    jacket = body(g, "A", "twill", 23612, layer="jacket", rows=(0, 8))
    f = jacket.front
    for y in range(9):
        f.clear(3, y), f.clear(4, y)
    f.vline(2, 0, 8, "P2"), f.vline(5, 0, 8, "P2")
    jacket.strip.hline(0, jacket.strip.w - 1, 8, k("A", 1))
    drawn_line(jacket.back, [(0, 0), (3, 4)], "P2"), drawn_line(jacket.back, [(7, 0), (4, 4)], "P2")
    for arm in sleeves(g, "A", "twill", 23613, rows=(0, 11), layer="sleeve", cuff="P2", cuff_row=11):
        drawn_line(arm.top, [(0, 0), (3, 3)], "P2")
        for face in arm.sides:
            face.hline(0, face.w - 1, 3, "P2"), face.hline(0, face.w - 1, 7, "P2")
            face.vline(1, 0, 11, "P1")
    spider_crest(g, "back_spider", "A", "P1", pivot=(0, 3.0, 2.15), scale=.4)
