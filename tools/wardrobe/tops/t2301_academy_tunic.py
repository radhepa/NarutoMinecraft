"""Academy Tunic: the clan children's plain plum tunic, short-sleeved and belted low, its sleeves and
hem edged with an ochre web-line trim and a small earth spider stitched on the breast."""
from kit import belt, body, neckline, sleeves
from kit_tsuchigumo import spider_crest, web_hem

META = {
    "name": "Academy Tunic",
    "gender": "unisex",
    "description": "Short-sleeved plum tunic edged in ochre web-line trim, a small spider on the breast.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    torso = body(g, "P", "weave", 23401)
    neckline(torso.front, "round", "P")
    for face in torso.sides:
        web_hem(face, 11, "A2", "A1")
    for arm in sleeves(g, "P", "weave", 23402, rows=(0, 4)):
        for face in arm.sides:
            web_hem(face, 4, "A2", "A1", up=True)
    sash = belt(g, "belt", y=9.0, role="D", height=1, buckle=None)
    sash.front.set(4, 0, "A3")
    spider_crest(g, "breast_spider", "P", "A3", pivot=(1.6, 2.2, -2.15), face="front", scale=.3)
