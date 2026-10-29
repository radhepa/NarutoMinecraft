"""Ash Training Wrap: the clan at training, after Asuma's sparring gear. A sleeveless chain-mesh
undershirt, a cloth sash slung over the right shoulder and knotted at the left hip, taped
forearms and a trench knife on the right fist."""
from kit_sarutobi import trench_knife
from kit_shinobi import bandage, mesh
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Ash Training Wrap",
    "gender": "unisex",
    "description": "Sleeveless mesh undershirt, a sash slung over the shoulder, taped forearms, a trench knife.",
    "tags": ["shinobi", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 9830, 2)
    cap(body, "K", seed=9830, base=2)
    for f in body.sides:
        mesh(f, 0, 0, f.w - 1, 11, "K1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for f in arm.sides:
            bandage(f, 0, 6, f.w - 1, 9)
    # The sash across the chest from the right shoulder to the left hip, and its knot.
    for name, face in (("front", body.front), ("back", body.back)):
        for i in range(10):
            x = i * 7 // 9
            x = x if name == "front" else 7 - x
            face.set(x, i + 1, "A2"), face.set(min(7, x + 1) if name == "front" else max(0, x - 1), i + 1, "A3")
    knot = g.piece("sash_knot", "TORSO", (-1, -1, -1), (2, 2, 2), pivot=(3.4, 10.4, -2.4))
    solid(knot, "A", "weave", 9831, 2)
    end = g.piece("sash_end", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(3.6, 11.2, -2.6), rotation=(0, 0, -8), motion="sway")
    solid(end, "A", "weave", 9832, 2)
    sh = g.piece("sash_shoulder", "TORSO", (-1, 0, -2.5), (2, 1, 5), pivot=(-3.2, -.3, 0), inflate=.15)
    solid(sh, "A", "weave", 9833, 2)
    sh.top.fill(k("A", 3))
    trench_knife(g, "right", 9834)
