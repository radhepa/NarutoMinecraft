"""Barrier Robe: the robe of the barrier corps, who raise the village's sensing wall. A long wrapped
robe to the knee over a pale under-collar, wide sleeves edged with a row of paper seal tags, a
dark sash with spare tags tucked in it, and tags sewn round the hem."""
from kit import belt
from kit_kurama import wrap_front
from kit_specialist import coat_skirts, seal_trim
from kit_uzumaki import wide_sleeves
from paint import cap, solid, strip_fabric

META = {
    "name": "Barrier Robe",
    "gender": "unisex",
    "description": "Knee-length wrapped robe, wide sleeves and hem trimmed with paper seal tags, dark sash.",
    "tags": ["shinobi", "robe", "chunin"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 34060, 2)
    cap(body, "P", texture="twill", seed=34060)
    wrap_front(body.front, "S3", "S2", rows=8, start=1)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 34061, 2, 0, 9)
        strip_fabric(arm, "S", "weave", 34062, 3, 10, 10)
    wide_sleeves(g, "P", "twill", 34063, top=-1.6, length=8, drop=3, trim="A2", tags=True)
    sash = belt(g, "sash", y=8.0, role="K", height=2, buckle=None, inflate=.14)
    for face in sash.sides:
        face.hline(0, face.w - 1, 0, "K3")
    for i, (x, rz) in enumerate(((-2.6, -6), (-1.6, 4), (2.4, 8))):
        tag = g.piece(f"sash_tag_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 8.4, -3.0), rotation=(0, 0, rz))
        solid(tag, "S", "plain", 34066 + i, 3, edge=False)
        tag.front.set(0, 1, "K1"), tag.front.set(0, 2, "A2")
    coat_skirts(g, "robe_skirt", 8, "P", "twill", 34070, open_front=False)
    for p in g.pieces:
        if p.id.startswith("robe_skirt"):
            seal_trim(p.box.strip, p.box.h - 3, 3, every=3, seed=34078)
