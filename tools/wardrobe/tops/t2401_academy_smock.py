"""Academy Smock: the Suzuran child's first working clothes, a short-sleeved tunic with a white
collar band, a green sash tied at the side and a little herb pouch at the hip for the plants the
elders send them out to gather."""
from kit import belt, neckline, roll
from kit_suzuran import bell_sprig, herb_pouch
from paint import cap, fabric, strip_fabric

META = {
    "name": "Academy Smock",
    "gender": "unisex",
    "description": "Short-sleeved tunic with a white collar band, green side sash and a herb pouch at the hip.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 24501, 2)
    cap(body, "P", seed=24501)
    neckline(body.front, "round", "P")
    body.front.hline(1, 6, 1, "S3"), body.front.set(1, 0, "S3"), body.front.set(6, 0, "S3")
    for face in (body.right, body.left, body.back):
        face.hline(0, face.w - 1, 0, "S3")
    bell_sprig(body.front, 4, 4, bells=2)
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 24502 + (side == "left"), 2, 0, 3)
        fabric(arm.top, "P", "weave", 24502, 3)
    roll(g, "S", 1.6, base=3)
    sash = belt(g, "sash", y=8.0, role="D", height=1, buckle=None, inflate=.1)
    sash.front.set(6, 0, "D3")
    for i, (x, rz) in enumerate(((3.6, 8), (4.2, -6))):
        end = g.piece(f"sash_end_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 8.8, -2.5), rotation=(0, 0, rz),
                      motion="sway")
        fabric(end.front, "D", "weave", 24504, 2)
        for f in end.faces:
            if f is not end.front:
                f.fill("D2")
        end.front.set(0, 2, "D1")
    herb_pouch(g, "pouch", (-3.6, 8.8, -2.6))
