"""Flak Wrap: the Leaf's flak vest worn over a wrap-front shirt with kimono-cut sleeves to the
elbow and forearm guards, a sash knotted at the hip below the vest."""
from kit_kunoichi import kimono_sleeves, obi
from kit_shinobi import flak_vest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Flak Wrap",
    "gender": "unisex",
    "description": "Flak vest over a wrap shirt with kimono sleeves, forearm guards, a hip-knotted sash.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 33140, 2)
    cap(body, "S", texture="weave", seed=33140)
    flak_vest(g, shoulder_swirls=False, seed=33141)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 33150, 2, 0, 5)
        fabric(arm.top, "S", "weave", 33150, 3)
        strip_fabric(sleeve, "M", "plain", 33151, 2, 6, 9)
        sleeve.strip.hline(0, 15, 6, "M3"), sleeve.strip.hline(0, 15, 9, "M1")
    kimono_sleeves(g, "kimono_sleeve", "S", 33152, length=4, top=.6, trim="S1")
    obi(g, "sash", y=10.4, role="A", height=1, knot="side", seed=33154)
