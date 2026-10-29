"""Guard Haori: a dusky short haori worn open over a steel-grey shirt, pale trim down the fronts,
wide sleeves to the elbow and the Shiranui flame on the back: the clan head's dress for standing at
the Hokage's shoulder."""
from kit import belt
from kit_shiranui import crest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Guard Haori",
    "gender": "unisex",
    "description": "Dusky short haori open over a steel shirt, pale trim, elbow sleeves, the flame crest on the back.",
    "tags": ["shinobi", "jonin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 16780, 2)
    cap(body, "P", seed=16780)
    strip_fabric(jacket, "D", "twill", 16781, 2)
    cap(jacket, "D", texture="twill", seed=16781)
    for x in (2, 3, 4, 5):
        for y in range(12):
            jacket.front.clear(x, y)
    jacket.front.vline(1, 0, 11, "S3"), jacket.front.vline(6, 0, 11, "S3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "D1")
    belt(g, "belt", y=9.2, role="K", buckle=None, inflate=.08)
    crest(g, "back_crest", (0, 4.0, 2.6), role="D", mark="S3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 16783 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "weave", 16783, 3)
        strip_fabric(sleeve, "D", "twill", 16785 + (side == "left"), 2, 0, 6)
        fabric(sleeve.top, "D", "twill", 16785, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 6, "S3")
