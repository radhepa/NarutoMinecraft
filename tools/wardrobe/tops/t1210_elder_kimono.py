"""Elder's Layered Kimono: the full formal kimono the clan heads wear, after Murakumo and Uroko
Kurama. An outer kimono over a cream under-collar in two layered lines, long hanging sleeves, a broad
obi tied with a cord and the Kurama crest across the back. One garment with its skirt."""
from kit import belt
from kit_kurama import back_crest, kimono_sleeves, wisteria_hem, wrap_front
from paint import cap, solid, strip_fabric

META = {
    "name": "Elder's Layered Kimono",
    "gender": "unisex",
    "description": "Formal layered kimono: cream under-collars, long hanging sleeves, broad obi with a cord, crest.",
    "tags": ["robe"],
    "covers_waist": True,
    "locked_to": "b1206_elder_kimono_skirt",
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 12825, 2)
    cap(body, "P", texture="velvet", seed=12825)
    f = body.front
    wrap_front(f, "S3", "A2", rows=7, start=2)
    for y in range(7):
        if y + 1 <= 7:
            f.set(y + 1, y, "S2")
    f.set(0, 0, "S3"), f.set(1, 0, "A2")
    obi = belt(g, "obi", y=6.4, role="A", height=4, buckle=None, inflate=.16)
    for face in obi.sides:
        face.hline(0, face.w - 1, 0, "A3"), face.hline(0, face.w - 1, 3, "A1")
    cord = belt(g, "obi_cord", y=7.9, role="S", height=1, buckle=None, inflate=.32)
    cord.front.set(4, 0, "A3")
    knot = g.piece("obi_knot", "TORSO", (-2, -1.5, 0), (4, 3, 2), pivot=(0, 8.0, 2.4))
    solid(knot, "A", "velvet", 12826, 2)
    knot.back.vline(1, 0, 2, "A1"), knot.back.vline(2, 0, 2, "A1")
    for side in ("right", "left"):
        strip_fabric(g.part(f"{side}_arm"), "S", "weave", 12827, 3, 9, 10)
    for sleeve in kimono_sleeves(g, "P", "velvet", 12828, length=10, trim="S3"):
        for face in sleeve.sides:
            if sleeve.h == 3:
                continue
            wisteria_hem(face, 12830, light="A3", dark="A2", stem="P1", step=2, y0=1)
    back_crest(g, role="P", ink="S3", texture="velvet", pivot=(0, 1.0, 2.06))
