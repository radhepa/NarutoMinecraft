"""Mountain Hakama: full wide hakama falling to the ankle, its hem darkened by mud, belted with a
thick twisted rope and worn over pale tabi and straw sandals: the mountain hermit's trousers."""
from kit import legs, waistband
from kit_rugged import baggy_legs, rope, straw_sandals, tabi

META = {"name": "Mountain Hakama", "gender": "unisex",
        "description": "Full ankle-length hakama with a muddied hem, a thick rope belt, pale tabi and straw sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    waistband(g, "P", "twill", 35440, 2)
    legs(g, "P", "twill", 35441, 2, rows=(0, 8), crease=False)
    for box in baggy_legs(g, "hakama", "P", 35442, top=0.0, length=10, flare=4):
        for face in box.sides:
            face.hline(0, face.w - 1, 9, "L1"), face.hline(0, face.w - 1, 8, "L2")
    tabi(g, rows=(10, 11))
    straw_sandals(g)
    rope(g, "waist_rope", y=9.3, role="S", base=2)
