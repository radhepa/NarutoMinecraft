"""ANBU Tracker: the plated armor over a black long-sleeved undersuit, white arm guards and a
leather bandolier slung from the right shoulder to the left hip, hung with kunai."""
from kit_shinobi import anbu_arms, anbu_plates
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "ANBU Tracker",
    "gender": "unisex",
    "description": "Plated armor over black long sleeves, white arm guards, a bandolier of kunai.",
    "tags": ["shinobi", "armor"],
}

BANDOLIER = dict(bone="TORSO", pivot=(0, 5.2, -2.55), rotation=(0, 0, 38))


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 221, 2)
    cap(body, "D", seed=221)
    anbu_plates(g, seed=222)
    anbu_arms(g, top=0, shirt=None, tattoo=False)
    for side in ("right", "left"):
        fabric(g.part(f"{side}_arm").top, "K", "smooth", 229, 3)
    strap = g.piece("bandolier", BANDOLIER["bone"], (-1, -7, -.5), (2, 14, 1), pivot=BANDOLIER["pivot"],
                    rotation=BANDOLIER["rotation"])
    solid(strap, "L", "leather", 223, 2, edge=False)
    strap.front.vline(0, 0, 13, "L3")
    # Kunai in loops along the strap: steel ring pommel, black grip, the blade hidden in the loop.
    for i, y in enumerate((-5.5, -2.5, .5, 3.5)):
        loop = g.piece(f"kunai_{i}", BANDOLIER["bone"], (-1.5, y, -1.1), (3, 2, 1), pivot=BANDOLIER["pivot"],
                       rotation=BANDOLIER["rotation"])
        solid(loop, "L", "leather", 224 + i, 3, edge=False)
        loop.front.hline(0, 2, 1, "L1")
        loop.front.set(1, 0, "K1")
        ring = g.piece(f"kunai_ring_{i}", BANDOLIER["bone"], (-.5, y - 1, -1.0), (1, 1, 1), pivot=BANDOLIER["pivot"],
                       rotation=BANDOLIER["rotation"])
        solid(ring, "M", "plain", 228 + i, 3)
