"""Mesh Tee: a loose, rumpled short-sleeved shirt with a wide open neck showing the mesh undershirt,
the Nara crest on the back and the shirt hanging untucked. Cloud-watching clothes."""
from kit_nara import back_crest, net
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Mesh Tee",
    "gender": "unisex",
    "description": "Loose untucked short-sleeved shirt, open neck over mesh, the Nara crest on the back.",
    "tags": ["shinobi", "nara"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 5511, 2)
    cap(body, "P", seed=5511)
    f = body.front
    # A wide scooped neck with the mesh showing.
    for x, y in ((2, 0), (3, 0), (4, 0), (5, 0), (3, 1), (4, 1)):
        f.set(x, y, "K2" if (x + y) % 2 else None)
    f.set(1, 0, "P3"), f.set(6, 0, "P3"), f.set(2, 1, "P3"), f.set(5, 1, "P3")
    # Rumpled folds and an untucked hem over the belt line.
    f.vline(2, 3, 8, "P1"), f.set(5, 4, "P1"), f.set(5, 5, "P1"), f.set(6, 7, "P1")
    strip_fabric(jacket, "P", "weave", 5512, 2, 9, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 9, "P3"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    back_crest(g, "P", "K1", 5513, y=1.5)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 5514, 2, 0, 4)
        fabric(arm.top, "P", "weave", 5514, 3)
        strip_fabric(sleeve, "P", "weave", 5515 + (side == "left"), 2, 0, 4)
        fabric(sleeve.top, "P", "weave", 5515, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "P1")
        net(arm.strip, 0, 5, arm.strip.w - 1, 6)
