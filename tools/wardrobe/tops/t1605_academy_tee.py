"""Academy Tee: a pale short-sleeved tee with steel-grey shoulders and the Shiranui flame on the
chest, a dusky belt cord: the first clothes of a child who already twirls a pencil like a needle."""
from kit import belt
from kit_shiranui import crest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Academy Tee",
    "gender": "unisex",
    "description": "Pale tee with steel shoulders, the flame crest on the chest, a dusky belt cord.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 16800, 2)
    cap(body, "P", seed=16800)
    body.strip.hline(0, body.strip.w - 1, 0, "P2"), body.strip.hline(0, body.strip.w - 1, 1, "P1")
    for x in (3, 4):
        body.front.set(x, 0, "S1")
    crest(g, "chest_crest", (0, 4.0, -2.05), role="S", mark="A2", face="front")
    belt(g, "belt", y=9.6, role="D", buckle=None, height=1, inflate=.06)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "P", "weave", 16801 + (side == "left"), 2, 0, 3)
        fabric(sleeve.top, "P", "weave", 16801, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "S3")
