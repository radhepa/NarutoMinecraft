"""Academy Tee: a cheerful academy student's short-sleeved tee in the family's colour, contrast
raglan sleeves, a round collar, a striped hem and the white circle on the chest."""
from kit import neckline, sleeves
from kit_haruno import back_crest, chest_crest
from paint import cap, k, strip_fabric

META = {
    "name": "Academy Tee",
    "gender": "unisex",
    "description": "Short-sleeved tee with contrast raglan sleeves, round collar, striped hem, circle on the chest.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 19530, 2, 0, 10)
    cap(body, "P", texture="plain", seed=19530)
    neckline(body.front, "round", "P")
    body.strip.hline(0, body.strip.w - 1, 9, k("S", 3)), body.strip.hline(0, body.strip.w - 1, 10, k("P", 1))
    # Raglan seams: the sleeve colour runs up to the collar.
    for x, y in ((1, 0), (0, 1), (6, 0), (7, 1)):
        body.front.set(x, y, k("S", 3)), body.back.set(x, y, k("S", 3))
    for box in sleeves(g, "S", "plain", 19531, 3, rows=(0, 3), cuff=k("A", 2)):
        box.strip.hline(0, box.strip.w - 1, 2, k("S", 2))
    chest_crest(g, "chest_crest", -1.6, y=2.0, z=-2.1)
    back_crest(g, "P", texture="plain", seed=19536, size=8, pivot=(0, 2.0, 2.05))
