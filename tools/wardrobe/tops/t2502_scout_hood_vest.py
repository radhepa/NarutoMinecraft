"""Scout Hood Vest: a quilted sleeveless vest with its hood worn down, over a moon-grey long-sleeved
shirt, dark guards from elbow to knuckle, a muffler worn down with both ends hanging behind and a
narrow belt with a pouch at the back."""
from kit import belt, pouch, sleeves
from kit_tobari import hood_down, muffler, plain_body
from paint import cap, fabric, strip_fabric

META = {
    "name": "Scout Hood Vest",
    "gender": "unisex",
    "description": "Quilted hooded vest over a moon-grey shirt, dark arm guards, a muffler worn down, a belt pouch.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    plain_body(g, "S", "weave", 25330)
    for arm in sleeves(g, "S", "weave", 25331, rows=(0, 11)):
        strip_fabric(arm, "K", "smooth", 25333, 2, 6, 11)
        arm.strip.hline(0, arm.strip.w - 1, 6, "K3")
        arm.front.hline(1, 2, 9, "M3")
        fabric(arm.bottom, "K", "smooth", 25333, 1)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "quilt", 25334, 2, 0, 10)
    cap(jacket, "P", texture="quilt", seed=25334)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1")
    jacket.front.vline(3, 0, 10, "P0"), jacket.front.vline(4, 0, 10, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(0, 0, 10, "P1")
    hood_down(g, "hood", "P", "quilt", 25335)
    muffler(g, "muffler", "D", "knit", 25337, tails="back")
    belt(g, "belt", y=9.8, role="L", height=1)
    pouch(g, "back_pouch", (1.6, 9.6, 2.6), size=(3, 2, 1))
