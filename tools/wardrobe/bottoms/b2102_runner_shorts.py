"""Runner Shorts: gunmetal knee shorts with a rust stripe down each side for the messengers who run
the village, off-white wraps on the calves under short steel shin plates, and sandals."""
from kit import legs, waistband
from kit_hagane import shin_guards
from kit_shinobi import sandals, wraps

META = {"name": "Runner Shorts", "gender": "unisex",
        "description": "Gunmetal knee shorts with a rust side stripe, wrapped calves, short steel shin plates, sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "twill", 21985, 2)
    for leg in legs(g, "P", "twill", 21986, 2, rows=(0, 4), crease=False):
        leg.strip.hline(0, leg.strip.w - 1, 4, "P1")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        outer = leg.right if side == "right" else leg.left
        outer.vline(1, 0, 4, "A2"), outer.vline(2, 0, 4, "A2")
    wraps(g, 5, 9)
    sandals(g)
    shin_guards(g, top=6.0, height=3, seed=21987)
