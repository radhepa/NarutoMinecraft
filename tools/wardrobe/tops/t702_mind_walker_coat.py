"""Mind Walker Coat: the clan head's long sleeveless coat in purple, open down the front over a
padded lavender vest, a tall collar, long tails to the knee behind and narrow front panels, over
a dark long-sleeved shirt and fingerless gloves."""
from kit import collar
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Mind Walker Coat",
    "gender": "unisex",
    "description": "Long open sleeveless purple coat over a padded vest, tall collar, knee tails, dark sleeves.",
    "tags": ["shinobi", "yamanaka", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # The padded vest under the coat: quilted ribs and a centre zip.
    strip_fabric(body, "S", "plain", 7250, 2)
    cap(body, "S", seed=7250)
    for y in (2, 5, 8):
        body.strip.hline(0, body.strip.w - 1, y, "S1")
    body.front.vline(3, 0, 11, "M2")
    # The coat: open between the lapels so the vest shows.
    strip_fabric(jacket, "P", "weave", 7251, 2)
    cap(jacket, "P", texture="weave", seed=7251)
    for x in range(2, 6):
        for y in range(12):
            jacket.front.clear(x, y)
    jacket.front.vline(1, 0, 11, "S3"), jacket.front.vline(6, 0, 11, "S3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(2, 1, 10, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 7252 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "D", "weave", 7252, 3)
        strip_fabric(arm, "K", "smooth", 7254, 2, 10, 11)
        arm.strip.hline(0, arm.strip.w - 1, 10, "K3")
        strip_fabric(sleeve, "P", "weave", 7255, 2, 0, 2)
        fabric(sleeve.top, "P", "weave", 7255, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 2, "S3")
    # The tails: one long panel behind, a narrow panel each side of the opening in front.
    tail = g.piece("coat_tail", "TORSO", (-4.5, 0, 0), (9, 9, 1), pivot=(0, 11.4, 2.05), motion="flap_back")
    solid(tail, "P", "weave", 7256, 2)
    tail.back.vline(4, 1, 8, "P1"), tail.back.hline(0, 8, 8, "S3")
    for i, x in enumerate((-4.6, 2.6)):
        panel = g.piece(f"coat_front_{i}", "TORSO", (0, 0, 0), (2, 8, 1), pivot=(x, 11.4, -3.05), motion="flap_front")
        solid(panel, "P", "weave", 7257 + i, 2)
        panel.front.vline(1 if i == 0 else 0, 0, 7, "S3"), panel.front.hline(0, 1, 7, "S3")
    neck = collar(g, "collar", "P", "weave", height=2, y=-1.6)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "S3")
    neck.front.hline(3, 5, 0, k("P", 0)), neck.front.hline(3, 5, 1, k("P", 0))
