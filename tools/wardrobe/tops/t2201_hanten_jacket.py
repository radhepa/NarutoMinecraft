"""Hanten Jacket: the builder's short indigo work coat, open over a cream undershirt with a broad
cream collar band running down both front edges, sashiko-stitched shoulders, sleeves rolled to the
elbow, a cedar sash at the waist and the Kinoshita square-in-a-ring crest large on the back."""
from kit import belt, roll
from kit_kinoshita import back_crest, sashiko
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Hanten Jacket",
    "gender": "unisex",
    "description": "Short indigo work coat with cream collar bands, rolled sleeves, a cedar sash, crest on the back.",
    "tags": ["shinobi", "kinoshita", "work"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 22301, 3)
    cap(body, "S", base=3, seed=22301)
    # The coat: open down the front, the collar band in cream from the neck to the hem.
    strip_fabric(jacket, "P", "weave", 22302, 2)
    cap(jacket, "P", seed=22302)
    for face in jacket.sides:
        sashiko(face, "P3", 0, 0, face.w, 3)
    for y in range(12):
        for x in (3, 4):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "S3"), jacket.front.set(5, y, "S2")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    sash = belt(g, "sash", y=8.6, role="A", height=1, buckle=None, inflate=.12)
    sash.front.set(3, 0, "A1")
    back_crest(g, "P", "S3", 22303, y=1.4)
    # Rolled sleeves: the coat to the elbow, a rolled cuff, bare forearms.
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 22304 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 22304, 3)
        strip_fabric(sleeve, "P", "weave", 22306, 2, 0, 3)
        fabric(sleeve.top, "P", "weave", 22306, 3)
        sashiko(sleeve.strip, "P3", 0, 0, sleeve.strip.w, 3)
    roll(g, "P", 4.0)
    # A hip-length hem below the waist, front halves either side of the opening and the back.
    for name, x0, w, z, motion in (("hem_front_right", -4.6, 4, -2.95, "flap_front"),
                                   ("hem_front_left", .6, 4, -2.95, "flap_front"),
                                   ("hem_back", -4.6, 9, 1.95, "flap_back")):
        hem = g.piece(name, "TORSO", (0, 0, 0), (w, 3, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(hem, "P", "weave", 22307, 2)
        face = hem.front if z < 0 else hem.back
        sashiko(face, "P3", 0, 1, w, 1)
        if name == "hem_front_right":
            face.vline(w - 1, 0, 2, "S3")
        elif name == "hem_front_left":
            face.vline(0, 0, 2, "S2")
