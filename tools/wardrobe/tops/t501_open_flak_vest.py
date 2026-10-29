"""Open Flak Vest: the chunin flak vest worn hanging open over a dark long-sleeved shirt with a mesh
collar, the forehead protector tied round the left upper arm: too much trouble to zip it up."""
from kit_nara import arm_protector, net
from kit_shinobi import flak_vest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Open Flak Vest",
    "gender": "unisex",
    "description": "Flak vest hanging open over a dark shirt with a mesh collar, protector tied on the left arm.",
    "tags": ["shinobi", "vest", "nara"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 5501, 2)
    cap(body, "D", seed=5501)
    net(body.front, 2, 0, 5, 1)
    flak_vest(g, seed=5502)
    # Unzipped: the two fronts hang apart, their edges rolled dark.
    for y in range(12):
        for x in (3, 4):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "P1"), jacket.front.set(5, y, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 5504 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "D", "weave", 5504, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
    arm_protector(g, "D", 5506)
