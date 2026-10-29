"""Wrap Skirt: a long charcoal wrap skirt to the ankle, split at the front over dark leggings,
its edge piped in dark red, with open-toe sandals: a kunoichi of the council's household."""
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Wrap Skirt", "gender": "female",
        "description": "Long charcoal wrap skirt split at the front over dark leggings, a dark-red edge, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 13860, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "weave", 13860, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 13861 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "K", "smooth", 13861, 2)
    sandals(g)
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 4, -2.95, "flap_front"),
                                   ("skirt_front_left", 1.6, 3, -2.9, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 11, 1), pivot=(x0, 11.6, z), motion=motion)
        solid(skirt, "D", "weave", 13863 + len(name) % 7, 2)
        for x in range(1, w, 2):
            skirt.front.vline(x, 1, 10, "D1"), skirt.back.vline(x, 1, 10, "D1")
        skirt.strip.hline(0, skirt.strip.w - 1, 10, "A2")
    edge = g.piece("skirt_edge", "TORSO", (0, 0, 0), (1, 11, 1), pivot=(-.6, 11.6, -3.05), motion="flap_front")
    solid(edge, "A", "weave", 13870, 2, edge=False)
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 10, 4), pivot=(x, 11.6, 0))
        solid(panel, "D", "weave", 13871, 2)
        panel.strip.hline(0, panel.strip.w - 1, 9, "A2")
