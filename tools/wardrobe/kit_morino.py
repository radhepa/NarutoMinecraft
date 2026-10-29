"""Morino clan building blocks: close-clipped and hard-combed hair, the cloth cap the interrogators
tie over the whole head, heavy buckled boots and the long skirts of a greatcoat."""
from anime import ring_shell
from kit import SIDES, leg_bone
from kit_shinobi import forehead_protector
from paint import fabric, k, rnd, scalp, solid, strip_fabric


def clipped(g, seed: int, side_rows: int = 3, back_rows: int = 5, base: int = 1, stubble: bool = True,
            crown: bool = True):
    """Hair clipped to the scalp: a shadow over the skin flecked with hair (`stubble`), or a short
    flat coat painted on the head with no sideburn. `crown` adds a thin stubble cap for a style with
    nothing else on top."""
    if not stubble:
        scalp(g, seed, side_rows=side_rows, back_rows=back_rows, sideburn=0, base=base, shadow=False)
        return
    head = g.part("head")
    for face, rows in ((head.top, 8), (head.back, back_rows), (head.right, side_rows), (head.left, side_rows)):
        for y in range(rows):
            for x in range(face.w):
                face.set(x, y, k("H", base) if rnd(x, y, seed + face.x0 * 7 + face.y0) < .08 else "X2")
    head.front.hline(0, 7, 0, "X2")
    if not crown:
        return
    pad = g.piece("stubble_crown", "HEAD", (-4, -1, -4), (8, 1, 8), pivot=(0, -8, 0), scale=(1.06, .3, 1.06))
    for face in pad.faces:
        face.fill("X2")
    for y in range(8):
        for x in range(8):
            if rnd(x, y, seed + 5) < .06:
                pad.top.set(x, y, k("H", base))


def combed_back(g, seed: int, side_rows: int = 4, back_rows: int = 6, sideburn: int = 1):
    """Hair combed hard back from the brow and flattened: painted scalp, a tight shell and comb lines
    running back over the crown."""
    scalp(g, seed, side_rows=side_rows, back_rows=back_rows, sideburn=sideburn)
    hat = ring_shell(g, seed + 1, side_rows=side_rows, back_rows=back_rows, ring_row=1)
    for x in (1, 2, 5, 6):
        hat.top.vline(x, 0, 7, k("H", 1 if x in (2, 5) else 3))
    return hat


def head_cloth(g, role: str, seed: int, plate: bool = True, tails: int = 4, hem: str | None = None, base: int = 2):
    """The cloth cap tied over the whole head, its knot and tails at the nape: with the protector
    plate sewn on the brow, or plain. `hem` traces the edge above the brow and round the ears."""
    cap = g.piece("head_cloth", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.62)
    solid(cap, role, "weave", seed, base, edge=False)
    fabric(cap.top, role, "weave", seed, base + 1)
    for face in cap.sides:
        face.hline(0, face.w - 1, 0, k(role, base + 1))
        face.hline(0, face.w - 1, 1, hem or k(role, 1))
    back = g.piece("head_cloth_back", "HEAD", (-4, -6, 3), (8, 4, 1), inflate=.62)
    solid(back, role, "weave", seed + 1, base)
    back.back.hline(0, 7, 3, k(role, 1))
    for face in (back.right, back.left):
        face.fill(k(role, 1))
    if plate:
        forehead_protector(g, role, seed=seed + 2, ring=False)
    knot = g.piece("head_cloth_knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -4.4, 4.7))
    solid(knot, role, "weave", seed + 3, 2)
    for i, (x, rz) in enumerate(((-.6, 18), (.6, -14))):
        tail = g.piece(f"head_cloth_tail_{i}", "HEAD", (-.5, 0, 0), (1, tails, 1), pivot=(x, -3.8, 4.8),
                       rotation=(12, 0, rz), motion="sway")
        solid(tail, role, "weave", seed + 4 + i, 2)
        tail.back.set(0, tails - 1, k(role, 1))


def heavy_boots(g, top: int = 5, role: str = "K", strap: str = "L", buckle: str = "M", seed: int = 17900):
    """Tall heavy boots: a thick sole and toe cap on the overlay, two buckled straps round the shaft
    and a stiff boot top that stands proud of the leg."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, role, "leather", seed, 2, top, 11)
        for face in pants.sides:
            fabric(face, role, "leather", seed + 1, 2, 0, top, face.w, 12 - top)
            face.hline(0, face.w - 1, top, k(role, 3))
            face.hline(0, face.w - 1, 10, k(role, 1))
            face.hline(0, face.w - 1, 11, "K0")
        pants.front.hline(0, 3, 10, k(role, 3)), pants.front.hline(0, 3, 9, k(role, 2))
        for y in (top + 2, top + 4):
            if y < 10:
                for face in pants.sides:
                    face.hline(0, face.w - 1, y, k(strap, 1))
                outer = pants.right if side == "right" else pants.left
                outer.set(1, y, k(buckle, 3)), outer.set(2, y, k(buckle, 2))
        leg.bottom.fill("K0"), pants.bottom.fill("K0")
        rim = g.piece(f"{side}_boot_top", leg_bone(side), (-2.5, top - .4, -2.5), (5, 1, 5), inflate=.15)
        solid(rim, role, "leather", seed + 2, 3)
        sole = g.piece(f"{side}_boot_sole", leg_bone(side), (-2.5, 11.4, -2.9), (5, 1, 6), inflate=.05)
        solid(sole, "K", "leather", seed + 3, 1)
        sole.front.hline(0, 4, 0, "K2")


def coat_skirts(g, prefix: str, length: int, role: str, seed: int, lining: str | None = None, hem: str | None = None,
                top: float = 11.0, open_front: bool = True):
    """The long skirts of a coat: two front panels (parted at the centre when `open_front`), a back
    panel split up the middle for the stride, and side panels; `lining` edges the opening."""
    pieces = []
    fronts = (((-4.6, 4), (.6, 4)) if open_front else ((-4.6, 9),))
    for i, (x, w) in enumerate(fronts):
        panel = g.piece(f"{prefix}_front_{i}", "TORSO", (0, 0, 0), (w, length, 1), pivot=(x, top, -3.0), motion="flap_front")
        solid(panel, role, "twill", seed + i, 2)
        panel.front.hline(0, w - 1, 0, k(role, 3))
        if hem:
            panel.front.hline(0, w - 1, length - 1, hem)
        if lining and open_front:
            panel.front.vline(w - 1 if i == 0 else 0, 0, length - 1, lining)
        pieces.append(panel)
    back = g.piece(f"{prefix}_back", "TORSO", (0, 0, 0), (9, length, 1), pivot=(-4.6, top, 2.0), motion="flap_back")
    solid(back, role, "twill", seed + 3, 2)
    back.back.vline(4, 2, length - 1, k(role, 0))
    back.back.hline(0, 8, 0, k(role, 3))
    if hem:
        back.back.hline(0, 8, length - 1, hem)
    pieces.append(back)
    for name, x in (("right", -5.0), ("left", 4.0)):
        side = g.piece(f"{prefix}_side_{name}", "TORSO", (0, 0, -2), (1, length, 4), pivot=(x, top, 0))
        solid(side, role, "twill", seed + 4, 2)
        if hem:
            for face in side.sides:
                face.hline(0, face.w - 1, length - 1, hem)
        pieces.append(side)
    return pieces


def armband(g, side: str = "left", role: str = "A", y: float = 1.6, mark: str | None = "K1"):
    """The Torture and Interrogation band round the upper arm, a dark bar across its outer face."""
    from kit import arm_bone, arm_x
    band = g.piece(f"{side}_armband", arm_bone(side), (arm_x(side) - .3, y, -2.3), (5, 2, 5), inflate=.05)
    solid(band, role, "weave", 17950 + (side == "left"), 2)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, k(role, 3))
    if mark:
        outer = band.left if side == "left" else band.right
        outer.set(1, 1, mark), outer.set(2, 1, mark), outer.set(3, 1, mark)
    return band


def gloves(g, role: str = "K", top: int = 9):
    """Black leather gloves from row `top` of the arm to the fingertips, a strap at the wrist."""
    for side in SIDES:
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, role, "leather", 17960 + (side == "left"), 2, top, 11)
        fabric(arm.bottom, role, "leather", 17960, 1)
        arm.strip.hline(0, arm.strip.w - 1, top, k(role, 3))


# The Morino crest: a pine of three tiers over a trunk, for the forest in the name.
CREST = ["...##...",
         "..####..",
         "...##...",
         ".######.",
         "..####..",
         "########",
         "...##...",
         "...##..."]


def back_crest(g, ground: str, key: str, seed: int, y: float = 1.6, z: float = 2.3, pid: str = "back_crest"):
    """The crest on a cloth patch across the shoulder blades."""
    from glyphs import stamp
    patch = g.piece(pid, "TORSO", (-4, 0, 0), (8, 8, 1), pivot=(0, y, z), scale=(.75, .75, .75))
    fabric(patch.back, ground, "weave", seed, 2)
    for face in (patch.top, patch.bottom, patch.right, patch.left, patch.front):
        face.fill(k(ground, 2))
    stamp(patch.back, CREST, 0, 0, {"#": key})
    return patch


def nape_hem(g, seed: int, y: float = -2.6, rows: int = 1):
    """A short blunt block of hair across the nape, where a crop is cut level."""
    from anime import cel_box
    hem = g.piece("nape_hem", "HEAD", (-4, 0, 0), (8, rows, 1), pivot=(0, y, 4.3))
    cel_box(hem, seed, top_delta=0)
    return hem
