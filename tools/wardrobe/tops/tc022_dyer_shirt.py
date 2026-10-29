"""Indigo Dyer's Shirt: the dye-works' undyed cotton shirt, the sleeves tied up with a tasuki cord
and the arms stained blue to the elbow from the vats, a short dye-stained apron at the waist."""
from kit_kurama import splatter, wrap_front
from kit_market import sleeves, tasuki, waist_apron
from paint import cap, k, strip_fabric

META = {
    "name": "Indigo Dyer's Shirt",
    "gender": "unisex",
    "description": "Undyed shirt with tasuki-tied sleeves, arms stained indigo to the elbow, a short dye-stained apron.",
    "tags": ["civilian", "work", "wrap", "apron"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 36440, 2)
    cap(body, "S", seed=36440)
    wrap_front(body.front, "S4", "S1", rows=7, start=1)
    sleeves(g, "S", "weave", 36441, rows=(0, 3))
    tasuki(g, k("D", 2), puff_role="S", seed=36443)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for y in range(5, 12):
            for x in range(arm.strip.w):
                if y >= 7 or (x + y) % 3 == 0:
                    arm.strip.set(x, y, k("D", 1 if y >= 9 else 2))
        arm.bottom.fill(k("D", 1))
    front = waist_apron(g, "dye_apron", "S", 6, 36445, width=8, base=2, top=9.0, band=k("D", 2))
    splatter(front, 36446, keys=(k("D", 1), k("D", 2), k("D", 3)), density=.14)
