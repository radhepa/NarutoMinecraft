"""Half-Zip Jacket: a steel-grey field jacket with a high collar zipped only halfway, the sleeves
shoved up past the elbow over bandaged forearms."""
from kit import collar, roll
from kit_shinobi import bandage
from paint import cap, fabric, strip_fabric

META = {
    "name": "Half-Zip Jacket",
    "gender": "unisex",
    "description": "Steel field jacket half unzipped at a high collar, sleeves pushed up over bandaged forearms.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 16790, 1)
    strip_fabric(jacket, "P", "twill", 16791, 2)
    cap(jacket, "P", texture="twill", seed=16791)
    f = jacket.front
    for y in range(4):
        f.clear(3, y), f.clear(4, y)
    f.set(2, 0, "P3"), f.set(5, 0, "P1"), f.set(2, 1, "P3"), f.set(5, 1, "P1")
    f.vline(3, 4, 11, "M3"), f.vline(4, 4, 11, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P3"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    collar(g, "collar", "P", texture="twill", height=2, y=-1.4, inflate=.12).front.vline(4, 0, 1, "M3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 16793 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "P", "twill", 16793, 3)
        bandage(arm.strip, 0, 7, arm.strip.w - 1, 11)
    roll(g, "P", 4.4)
