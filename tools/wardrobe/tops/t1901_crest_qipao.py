"""Crest Qipao: Sakura's Part I dress top, a sleeveless red qipao cut to the hip with side slits, a
standing collar, a slanted opening fastened with white frog clasps from the throat to the right
underarm, and the white circle of the Haruno on the back."""
from kit import flaps
from kit_haruno import back_crest, frog_clasps, mandarin_collar
from paint import cap, k, line, strip_fabric

META = {
    "name": "Crest Qipao",
    "gender": "unisex",
    "description": "Sleeveless red qipao to the hip with side slits, standing collar, slanted clasps, circle crest on the back.",
    "tags": ["shinobi", "qipao"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 19510, 2)
    cap(body, "P", texture="smooth", seed=19510)
    f = body.front
    # The slanted opening: piping from the throat across to the wearer's right underarm.
    line(f, 4, 0, 0, 3, k("S", 3))
    line(f, 5, 0, 1, 3, k("P", 1))
    frog_clasps(f, ((3, 1), (1, 2)))
    f.vline(2, 5, 11, k("P", 1)), f.vline(5, 5, 11, k("P", 3))
    for face in (body.right, body.left):
        face.vline(1, 4, 11, k("P", 1))
    body.strip.hline(0, body.strip.w - 1, 11, k("S", 3))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        arm.strip.hline(0, arm.strip.w - 1, 0, k("P", 2)), arm.top.fill(k("P", 3))
    mandarin_collar(g, "P", 19511, trim=k("S", 3))
    back_crest(g, "P", texture="smooth", seed=19512)
    for face in flaps(g, "qipao_skirt", 3, "P", "smooth", 19513, width=8, hem=k("S", 3), top=11.6, front_z=-2.6, back_z=1.6):
        face.vline(0, 1, 1, k("P", 1)), face.vline(7, 1, 1, k("P", 1))
