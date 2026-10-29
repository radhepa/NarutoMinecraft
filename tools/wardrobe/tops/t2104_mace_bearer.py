"""Mace Bearer: a sleeveless high-necked gunmetal shirt, a rust sash knotted at the waist and the
clan's iron mace slung across the back on a leather baldric, steel bracers on bare arms: the guard
who answers trouble at the gate."""
from kit import belt
from kit_hagane import bracers, harness, mace
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Mace Bearer",
    "gender": "unisex",
    "description": "Sleeveless high-necked gunmetal shirt, a rust sash, an iron mace on a leather baldric, bracers.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 21910, 2)
    cap(body, "P", texture="weave", seed=21910)
    strip_fabric(jacket, "P", "weave", 21911, 2, 0, 1)
    fabric(jacket.top, "P", "weave", 21911, 3)
    jacket.strip.hline(0, jacket.strip.w - 1, 1, "P1")
    body.front.vline(4, 1, 8, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.top, "P", "weave", 21912, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2")
    sash = belt(g, "sash", y=9.4, role="A", buckle=None, height=2, inflate=.1)
    sash.front.set(6, 0, "A3"), sash.front.set(6, 1, "A1")
    knot = g.piece("sash_tail", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(1.6, 10.6, -2.95), rotation=(0, 0, -10))
    solid(knot, "A", "weave", 21913, 2)
    bracers(g, top=6.0, height=4, seed=21914)
    harness(g, seed=21915)
    mace(g, seed=21917)
