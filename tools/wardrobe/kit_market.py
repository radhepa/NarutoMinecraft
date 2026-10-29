"""Market building blocks: the working village's aprons, tasuki cords, shop marks, work prints and
footwear, shared by the market collection's civilian tops, bottoms and headwear."""
from kit import SIDES, arm_bone, arm_x, leg_bone
from paint import cap, fabric, grid, k, rnd, solid, strip_fabric

# Shop marks (yago) stamped on aprons and coat backs, drawn at full resolution.
IGETA = [".#.#.",
         "#####",
         ".#.#.",
         "#####",
         ".#.#."]
MARU = [".###.",
        "#...#",
        "#.#.#",
        "#...#",
        ".###."]
YAMA = ["..#..",
        ".#.#.",
        "#...#",
        ".....",
        "#####"]
KAGI = ["####.",
        "...#.",
        ".###.",
        ".#...",
        ".####"]
MARKS = {"igeta": IGETA, "maru": MARU, "yama": YAMA, "kagi": KAGI}


def mark(face, name: str, x0: int, y0: int, key: str):
    grid(face, x0, y0, MARKS[name], {"#": key})


# -- prints ----------------------------------------------------------------------------------
def stripes(face, key: str, step: int = 2, vertical: bool = True, offset: int = 0, rows=None):
    """Plain shima stripes, vertical or across, every `step` texels."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            if ((x if vertical else y) + offset) % step == 0:
                face.set(x, y, key)


def checks(face, key: str, size: int = 2, rows=None):
    """Ichimatsu checks: alternate squares of `size` overpainted in `key`."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            if (x // size + y // size) % 2:
                face.set(x, y, key)


def kasuri(face, key: str, seed: int, density: float = .14, rows=None):
    """Kasuri ikat: short blurred dashes scattered across the cloth, two texels wide."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(0, face.w, 2):
            if rnd(x, y, seed) < density and (y % 2 == 0):
                face.set(x, y, key), face.set(x + 1, y, key)


def sashiko(face, key: str, step: int = 3, rows=None, offset: int = 0):
    """Sashiko running stitch: rows of short dashes every `step` texels, each row offset half a
    stitch from the last."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        if (y + offset) % step:
            continue
        shift = (y // step) % 2 * 2
        for x in range(face.w):
            if (x + shift) % 4 < 2:
                face.set(x, y, key)


def dots(face, key: str, step: int = 3, rows=None, offset: int = 0):
    """Mame shibori: small tie-dyed dots on a half-drop grid."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        if (y + offset) % step:
            continue
        shift = (y // step) % 2 * (step // 2 + 1)
        for x in range((shift + offset) % step, face.w, step):
            face.set(x, y, key)


def patch(face, x0: int, y0: int, w: int, h: int, role: str, base: int = 2, stitch: str | None = None):
    """A darned patch: a square of other cloth with a stitched edge."""
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            face.set(x, y, k(role, base))
    if stitch:
        for x in range(x0, x0 + w, 2):
            face.set(x, y0, stitch), face.set(x, y0 + h - 1, stitch)


# -- tops ------------------------------------------------------------------------------------
def open_front(face, band: str, inner: str | None, rows, left: int = 2, right: int = 5):
    """A happi or haori open down the front: two collar bands from the shoulders, the undershirt
    (or chest) showing between them."""
    for y in rows:
        face.set(left, y, band), face.set(right, y, band)
        if inner:
            for x in range(left + 1, right):
                face.set(x, y, inner)


def sleeves(g, role: str, texture: str, seed: int, rows=(0, 4), base: int = 2, cuff: str | None = None,
            overlay: bool = True):
    """Short work sleeves on the arm and its overlay, ending at row `rows[1]` with a cuff line."""
    for side in SIDES:
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, role, texture, seed + (side == "left"), base, rows[0], rows[1])
        fabric(arm.top, role, texture, seed, base + 1)
        if overlay:
            sleeve = g.part(f"{side}_sleeve")
            strip_fabric(sleeve, role, texture, seed + 2 + (side == "left"), base, rows[0], rows[1])
            fabric(sleeve.top, role, texture, seed + 2, base + 1)
            sleeve.strip.hline(0, sleeve.strip.w - 1, rows[1], cuff or k(role, base - 1))


def tasuki(g, key: str, puff_role: str | None = None, seed: int = 36001, base: int = 2):
    """The tasuki cord crossed over the back and over both shoulders, tying the sleeves up out of the
    way; `puff_role` adds the sleeve cloth gathered into a puff above the elbow."""
    jacket = g.part("jacket")
    for i in range(9):
        jacket.back.set(i, i + 1, key), jacket.back.set(7 - i, i + 1, key)
    jacket.top.set(0, 1, key), jacket.top.set(7, 1, key), jacket.top.set(0, 2, key), jacket.top.set(7, 2, key)
    jacket.front.set(0, 0, key), jacket.front.set(7, 0, key), jacket.front.set(0, 1, key), jacket.front.set(7, 1, key)
    if puff_role:
        for side in SIDES:
            puff = g.piece(f"{side}_tied_sleeve", arm_bone(side), (arm_x(side) - .5, -2.2, -2.5), (5, 5, 5), inflate=.1)
            solid(puff, puff_role, "weave", seed + (side == "left"), base)
            for face in puff.sides:
                for x in range(0, face.w, 2):
                    face.vline(x, 1, 3, k(puff_role, base - 1))
                face.hline(0, face.w - 1, 3, key)
            puff.bottom.fill(k(puff_role, base - 2))


def waist_apron(g, prefix: str, role: str, length: int, seed: int, width: int = 8, base: int = 3, top: float = 9.0,
                z: float = -2.95, texture: str = "weave", band: str | None = None, ties: bool = True, hem: str | None = None):
    """A maekake work apron tied at the waist: a front panel that swings with the stride, a band
    round the waist (named for the top, so it is never hidden) and two ties hanging at the back."""
    panel = g.piece(f"{prefix}_panel", "TORSO", (-width / 2, 0, 0), (width, length, 1), pivot=(0, top, z), motion="flap_front")
    solid(panel, role, texture, seed, base)
    front = panel.front
    front.hline(0, width - 1, 0, k(role, base + 1))
    if hem:
        front.hline(0, width - 1, length - 1, hem)
    for y in range(1, length):
        front.set(0, y, k(role, base - 1)), front.set(width - 1, y, k(role, base - 1))
    ring = g.piece(f"{prefix}_band", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, top - .6, 0), inflate=.14)
    solid(ring, band[0] if band else role, "weave", seed + 1, int(band[1]) if band else base, edge=False)
    if ties:
        for i, (x, rz) in enumerate(((-.8, 12), (.8, -10))):
            tie = g.piece(f"{prefix}_tie_{i}", "TORSO", (-.5, 0, 0), (1, 4 - i, 1), pivot=(x, top - .2, 2.6),
                          rotation=(8, 0, rz), motion="sway")
            solid(tie, band[0] if band else role, "weave", seed + 2 + i, int(band[1]) if band else base)
    return front


def bib(g, prefix: str, role: str, seed: int, length: int = 8, width: int = 6, top: float = 1.0, base: int = 3,
        texture: str = "weave", strap: str | None = None, z: float = -2.75):
    """An apron bib over the chest, with its neck strap painted on the jacket and straps crossed
    behind. Returns the bib's front face."""
    panel = g.piece(f"{prefix}_bib", "TORSO", (-width / 2, 0, 0), (width, length, 1), pivot=(0, top, z))
    solid(panel, role, texture, seed, base)
    panel.front.hline(0, width - 1, 0, k(role, base + 1))
    jacket = g.part("jacket")
    key = strap or k(role, base - 1)
    jacket.top.set(1, 3, key), jacket.top.set(6, 3, key), jacket.top.set(1, 2, key), jacket.top.set(6, 2, key)
    for y in range(9):
        jacket.back.set(1 + y * 6 // 9, y, key), jacket.back.set(6 - y * 6 // 9, y, key)
    return panel.front


def pocket(g, pid: str, role: str, pivot, size=(3, 2), seed: int = 36003, base: int = 2, z_depth: int = 1, bone="TORSO"):
    w, h = size
    box = g.piece(pid, bone, (-w / 2, 0, 0), (w, h, z_depth), pivot=pivot)
    solid(box, role, "weave", seed, base)
    box.front.hline(0, w - 1, 0, k(role, base + 1))
    return box


def towel_at_neck(g, role: str = "S", seed: int = 36004, accent: str | None = None):
    """A tenugui towel slung round the neck, the two ends hanging down the chest."""
    ring = g.piece("neck_towel", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, -.4, 0), inflate=.18)
    solid(ring, role, "weave", seed, 3, edge=False)
    for i, x in enumerate((-2.6, 2.6)):
        end = g.piece(f"towel_end_{i}", "TORSO", (-.75, 0, 0), (2, 5 - i, 1), pivot=(x, .3, -2.9), scale=(.75, 1, 1),
                      motion="sway")
        solid(end, role, "weave", seed + 1 + i, 3)
        if accent:
            end.front.hline(0, 1, 3 - i, accent)


def furoshiki(g, pid: str, role: str, seed: int, pivot=(0, 3.0, 3.6), size=(6, 5, 3), knot_key: str | None = None,
              print_key: str | None = None):
    """A cloth-wrapped bundle carried on the back, its corners knotted over the chest."""
    w, h, d = size
    box = g.piece(pid, "TORSO", (-w / 2, -h / 2, -d / 2), size, pivot=pivot, rotation=(-6, 0, 0))
    solid(box, role, "weave", seed, 2)
    cap(box, role, seed=seed)
    if print_key:
        for face in box.sides:
            dots(face, print_key, 2)
    knot = g.piece(f"{pid}_knot", "TORSO", (-1, -1, -.5), (2, 2, 1), pivot=(0, 1.2, -2.85))
    solid(knot, role, "weave", seed + 1, 3)
    jacket = g.part("jacket")
    for x, y in ((2, 0), (1, 1), (5, 0), (6, 1)):
        jacket.front.set(x, y, knot_key or k(role, 2))
    for x in (1, 6):
        jacket.top.set(x, 3, knot_key or k(role, 2))
    return box


def sash(g, pid: str, role: str, seed: int, y: float = 8.4, height: int = 2, base: int = 2, knot: str | None = "front"):
    """A cloth sash wound round the waist and knotted, its short ends hanging."""
    box = g.piece(pid, "TORSO", (-4.6, y, -2.6), (9, height, 5), inflate=.12)
    solid(box, role, "weave", seed, base, edge=False)
    for face in box.sides:
        face.hline(0, face.w - 1, 0, k(role, base + 1))
    if knot:
        x, z = (2.6, -2.95) if knot == "front" else (0, 2.95)
        nub = g.piece(f"{pid}_knot", "TORSO", (-1, 0, -.5), (2, 2, 1), pivot=(x, y, z))
        solid(nub, role, "weave", seed + 1, base + 1)
        for i in range(2):
            end = g.piece(f"{pid}_end_{i}", "TORSO", (-.5, 0, -.5), (1, 3 - i, 1), pivot=(x - .5 + i, y + 1.8, z),
                          rotation=(0, 0, 10 - 20 * i), motion="sway")
            solid(end, role, "weave", seed + 2 + i, base)
    return box


# -- bottoms ---------------------------------------------------------------------------------
def straw_sandals(g, role: str = "L", tie: str = "S3", seed: int = 36005):
    """Waraji: woven straw soles with cords crossing over the instep and tied round the ankle."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        leg.strip.hline(0, leg.strip.w - 1, 9, tie)
        leg.front.set(1, 10, tie), leg.front.set(2, 10, tie)
        leg.bottom.fill(k(role, 2))
        for face in pants.sides:
            for x in range(face.w):
                face.set(x, 11, k(role, 3 if (x + int(rnd(x, 11, seed) * 2)) % 2 else 2))
        pants.bottom.fill(k(role, 1))


def geta(g, wood: str = "L", strap: str = "A2", sock: str | None = None):
    """Geta: a raised wooden clog with a cloth thong; bare feet or white tabi socks."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        if sock:
            strip_fabric(leg, sock[0], "plain", 36006, int(sock[1]), 9, 10)
            leg.front.vline(2, 9, 10, k(sock[0], int(sock[1]) - 1))
        leg.front.set(1, 10, strap), leg.front.set(2, 10, strap), leg.front.set(1, 9, strap)
        leg.bottom.fill(k(wood, 1))
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, k(wood, 3))
        pants.front.set(0, 11, k(wood, 2)), pants.front.set(3, 11, k(wood, 2))
        pants.bottom.fill(k(wood, 0))


def jika_tabi(g, role: str = "K", top: int = 7, seed: int = 36007, clasp: str = "M3"):
    """Jika-tabi: split-toe cloth work boots with rubber soles, fastened up the back with clasps."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, role, "plain", seed + (side == "left"), 2, top, 11)
        leg.front.vline(2 if side == "right" else 1, 10, 11, k(role, 0))
        leg.strip.hline(0, leg.strip.w - 1, top, k(role, 3))
        for y in range(top + 1, 10, 1):
            leg.back.set(1 if side == "right" else 2, y, clasp)
        leg.bottom.fill("K1")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "K1")
        pants.bottom.fill("K0")


def kyahan(g, role: str, rows=(4, 9), seed: int = 36008, tie: str | None = None):
    """Kyahan: cloth gaiters wrapped from knee to ankle, tied at the top, for walking the roads."""
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, role, "twill", seed + (side == "left"), 2, rows[0], rows[1])
        leg.strip.hline(0, leg.strip.w - 1, rows[0], k(role, 3))
        for y in range(rows[0] + 1, rows[1] + 1):
            leg.front.set(0 if side == "right" else 3, y, k(role, 1))
        if tie:
            leg.strip.hline(0, leg.strip.w - 1, rows[0] + 1, tie)
            leg.strip.hline(0, leg.strip.w - 1, rows[1], tie)


def rolled_cuffs(g, prefix: str, y: float, role: str, seed: int, base: int = 2):
    """A rolled trouser cuff round each leg at leg-local height y."""
    rings = []
    for side in SIDES:
        ring = g.piece(f"{side}_{prefix}", leg_bone(side), (-2.5, y, -2.5), (5, 2, 5))
        solid(ring, role, "twill", seed + (side == "left"), base)
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k(role, base + 2)), face.hline(0, face.w - 1, 1, k(role, base))
        rings.append(ring)
    return rings


def gathered_ankles(g, prefix: str, role: str, seed: int, y: float = 8.6, base: int = 2):
    """Monpe ankles: the loose leg gathered into an elasticated cuff above the foot."""
    rings = []
    for side in SIDES:
        ring = g.piece(f"{side}_{prefix}", leg_bone(side), (-2.5, y, -2.5), (5, 1, 5), inflate=.05)
        solid(ring, role, "rib", seed + (side == "left"), base, edge=False)
        for face in ring.sides:
            face.paint(lambda x, yy, cur: k(role, base - (x % 2)))
        rings.append(ring)
    return rings


def loose_legs(g, prefix: str, role: str, seed: int, length: int = 8, texture: str = "twill", base: int = 2, top: float = .3,
               flare: float = 1.5):
    """Wide trouser legs as loose boxes over each leg, standing a little proud of the skin."""
    boxes = []
    for side, sign in (("right", -1), ("left", 1)):
        box = g.piece(f"{prefix}_{side}", leg_bone(side), (-2.5, 0, -2.5), (5, length, 5), pivot=(0, top, 0),
                      rotation=(0, 0, -flare * sign), inflate=.06)
        solid(box, role, texture, seed + (sign > 0), base)
        box.bottom.fill(k(role, base - 2))
        boxes.append(box)
    return boxes
