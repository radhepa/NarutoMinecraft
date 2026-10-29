"""Spring Qipao: the grown medic's long red qipao tunic, cap-sleeved and falling to mid-thigh with
deep side slits, its collar, centre opening and hem piped in rose, clasped down the front and
marked with the white circle on the back."""
from kit import flaps
from kit_haruno import back_crest, frog_clasps, mandarin_collar
from paint import cap, k, strip_fabric

META = {
    "name": "Spring Qipao",
    "gender": "unisex",
    "description": "Long cap-sleeved qipao tunic to mid-thigh with side slits, rose piping, front clasps, circle on the back.",
    "tags": ["shinobi", "qipao"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 19590, 2)
    cap(body, "P", texture="smooth", seed=19590)
    f = body.front
    f.vline(3, 0, 11, k("A", 3)), f.vline(4, 0, 11, k("P", 1))
    frog_clasps(f, ((2, 2), (2, 4), (2, 6)))
    for face in (body.right, body.left):
        face.vline(1, 2, 11, k("P", 1))
    body.strip.hline(0, body.strip.w - 1, 11, k("A", 3))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "smooth", 19591 + (side == "left"), 2, 0, 2)
        arm.top.fill(k("P", 3))
        arm.strip.hline(0, arm.strip.w - 1, 2, k("A", 3))
    mandarin_collar(g, "P", 19593, trim=k("A", 3))
    back_crest(g, "P", texture="smooth", seed=19594)
    for face in flaps(g, "qipao_skirt", 6, "P", "smooth", 19595, width=8, hem=k("A", 3), top=11.6, front_z=-2.6, back_z=1.6):
        face.vline(0, 1, 4, k("A", 3)), face.vline(7, 1, 4, k("A", 3))
        face.vline(3, 1, 4, k("P", 1))
