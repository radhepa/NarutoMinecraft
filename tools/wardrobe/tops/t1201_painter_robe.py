"""Painter's Robe: Yakumo Kurama's everyday dress. A soft robe wrapped left over right, the collar
edged in cream with the red chain mesh showing at the throat, long sleeves to the wrist, a wide sash
with two square pockets on the front for brushes and chalk, and the skirt to mid-thigh, split at the
sides. The Kurama crest sits between the shoulders."""
from kit import belt, flaps
from kit_kurama import back_crest, wrap_front
from kit_shinobi import mesh
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Painter's Robe",
    "gender": "unisex",
    "description": "Yakumo's wrapped robe: cream-edged collar over mesh, a sash with two front pockets, split skirt.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 12600, 2)
    cap(body, "P", texture="velvet", seed=12600)
    f = body.front
    # The mesh undershirt in the open V of the collar, then the cream-edged wrap.
    for x, y in [(1, 0), (2, 0), (3, 0), (2, 1), (3, 1), (3, 2)]:
        f.clear(x, y)
    mesh(f, 1, 0, 3, 2, "A1")
    wrap_front(f, "S3", "P1", rows=7, start=2)
    f.set(0, 0, "S3"), f.set(1, 1, "S2")
    f.vline(7, 6, 7, "P1")
    # The wide sash and its two front pockets.
    sash = belt(g, "sash", y=7.4, role="A", height=3, buckle=None, inflate=.15)
    for face in sash.sides:
        face.hline(0, face.w - 1, 2, "A1")
    for i, x in enumerate((-3.3, 1.1)):
        pocket = g.piece(f"pocket_{i}", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(x, 9.4, -3.0))
        solid(pocket, "P", "velvet", 12602 + i, 2)
        pocket.front.hline(0, 1, 0, "S3")
    for face in flaps(g, "robe", 6, "P", "velvet", 12605, width=9, hem="S3", top=10.6, front_z=-2.8, back_z=1.8):
        face.vline(0, 1, 5, "P1"), face.vline(8, 1, 5, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 12607 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "velvet", 12607, 3)
        strip_fabric(sleeve, "P", "velvet", 12609, 2, 0, 9)
        fabric(sleeve.top, "P", "velvet", 12609, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "S3")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "P1")
    back_crest(g, role="P", ink="S3", texture="velvet")
