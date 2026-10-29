"""Lily Wrap Shirt: a genin's wrap-front shirt crossed left over right with a broad white lapel, a
leaf-green obi, bell sprigs printed on the sleeves and fingerless gloves to keep the hands free for
seals and herbs."""
from kit import belt
from kit_suzuran import bell_sprig
from paint import cap, fabric, k, strip_fabric

META = {
    "name": "Lily Wrap Shirt",
    "gender": "unisex",
    "description": "Wrap-front shirt with a broad white lapel, green obi, bell-printed sleeves, fingerless gloves.",
    "tags": ["shinobi", "wrap", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 24511, 2)
    cap(body, "P", seed=24511)
    # The crossover: the lapel runs from the left shoulder down to the right hip.
    f = body.front
    for y in range(8):
        x = 7 - y
        f.set(x, y, "S3"), f.set(max(0, x - 1), y, "S4")
        if x + 1 < 8:
            f.set(x + 1, y, "P1")
    f.set(0, 0, "S3"), f.set(1, 0, "S4")
    for face in (body.right, body.left, body.back):
        face.hline(0, face.w - 1, 0, "S3")
    belt(g, "obi", y=7.6, role="D", height=2, buckle=None, inflate=.12)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 24512 + (side == "left"), 2, 0, 7)
        fabric(arm.top, "P", "weave", 24512, 3)
        outer = arm.right if side == "right" else arm.left
        bell_sprig(outer, 0, 2, bells=3, shade=k("P", 1))
        arm.strip.hline(0, arm.strip.w - 1, 7, "S3")
        for y in (9, 10, 11):
            arm.strip.hline(0, arm.strip.w - 1, y, "K2")
        arm.strip.hline(0, arm.strip.w - 1, 9, "K3")
        arm.front.set(1, 11, None), arm.front.set(2, 11, None)
