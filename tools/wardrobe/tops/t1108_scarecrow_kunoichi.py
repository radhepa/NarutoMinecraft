"""Scarecrow Kunoichi: a sleeveless slate tunic with a high neck to meet a mask, the Hatake crest on
the back, a navy sash with short tails, chain mesh on the upper arms and black arm warmers."""
from kit_hatake import CREST, decal
from kit_shinobi import mesh
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Scarecrow Kunoichi",
    "gender": "unisex",
    "description": "Sleeveless high-neck slate tunic with the clan crest, a navy sash, mesh arms and black warmers.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 11701, 2)
    cap(body, "P", seed=11701)
    body.front.vline(2, 1, 8, "P1"), body.front.vline(5, 1, 8, "P1")
    strip_fabric(jacket, "D", "weave", 11702, 2, 8, 9)
    jacket.strip.hline(0, jacket.strip.w - 1, 8, "D3")
    jacket.front.set(6, 9, "D1")
    for i, x in enumerate((1.4, 2.4)):
        sash = g.piece(f"sash_tail_{i}", "TORSO", (0, 0, 0), (1, 4, 1), pivot=(x, 9.6, -2.75), rotation=(0, 0, -6 + i * 8))
        solid(sash, "D", "weave", 11703 + i, 2)
    decal(g, "back_crest", CREST, {"o": "S3", "f": "S4"}, "P2", (0, 1.4, 2.3))
    neck = g.piece("high_neck", "TORSO", (-4.4, -1.6, -2.5), (9, 2, 5), inflate=.05)
    solid(neck, "P", "rib", 11705, 2)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "P3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for face in arm.sides:
            mesh(face, 0, 0, face.w - 1, 4)
        fabric(arm.top, "K", "smooth", 11706, 2)
        strip_fabric(arm, "K", "rib", 11707, 2, 6, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "K3")
        arm.strip.hline(0, arm.strip.w - 1, 10, "K3")
    # Short split flaps over the hips.
    for name, z, motion, face_name in (("front", -2.85, "flap_front", "front"), ("back", 1.85, "flap_back", "back")):
        flap = g.piece(f"flap_{name}", "TORSO", (-4.5, 0, 0), (9, 3, 1), pivot=(0, 10.4, z), motion=motion)
        solid(flap, "P", "weave", 11708, 2)
        getattr(flap, face_name).vline(4, 0, 2, "P0")
