"""Gekko building blocks: the clan's long sword (a katana worn on the back or through the sash at the
hip), the sword strap painted across a torso, and the crescent moon crest.

Every piece paints key colors only: the hilt wrap and sheath in K, the guard in M, the sword cord
(sageo) in A, so a palette decides how a family blade looks."""
from glyphs import stamp
from paint import fabric, k, solid

# The crescent moon, drawn at double resolution on a half-scale decal (8 x 8 texels).
CRESCENT = ["...###..",
            ".##.....",
            "##......",
            "#.......",
            "#.......",
            "##......",
            ".##.....",
            "...###.."]


def katana(g, prefix: str = "katana", pivot=(-1.4, 2.2, 2.95), rotation=(0, 0, -27), bone: str = "TORSO", length: int = 11,
           hilt: int = 4, cord: str | None = "A2", wrap: str = "S3"):
    """A long sword in its sheath, the guard at the pivot: a diamond-wrapped hilt along local -y, a
    steel guard, a black sheath along +y with a steel end cap and the cord tied round its mouth.
    The default pose hangs it on the back, the hilt over the right shoulder."""
    grip = g.piece(f"{prefix}_hilt", bone, (-.5, -hilt, -.5), (1, hilt, 1), pivot=pivot, rotation=rotation)
    solid(grip, "K", "smooth", 15001, 2, edge=False)
    for face in grip.sides:
        for y in range(0, hilt, 2):
            face.set(0, y, wrap)
    grip.top.fill("M3")
    guard = g.piece(f"{prefix}_guard", bone, (-1, 0, -1), (2, 1, 2), pivot=pivot, rotation=rotation)
    solid(guard, "M", "plain", 15002, 3)
    sheath = g.piece(f"{prefix}_sheath", bone, (-.5, 1, -.5), (1, length, 1), pivot=pivot, rotation=rotation)
    solid(sheath, "K", "smooth", 15003, 2)
    for face in sheath.sides:
        face.set(0, length - 1, "M2")
        if cord:
            face.set(0, 1, cord)
    sheath.bottom.fill("M2")
    return grip, guard, sheath


def hip_katana(g, prefix: str = "katana", side: str = "left", cord: str | None = "A2"):
    """A katana thrust through the sash on one hip: the hilt angled forward and up across the belly,
    the sheath running back and down past the hip."""
    sign = 1 if side == "left" else -1
    return katana(g, prefix, pivot=(2.9 * sign, 9.6, -2.9), rotation=(62, 0, -14 * sign), length=11, hilt=4, cord=cord)


def sword_strap(face, role: str = "L", base: int = 2, mirror: bool = False, rows: int = 12, x0: int = 0):
    """A two-texel strap running diagonally down a torso face from one shoulder to the other hip.
    On a front face x runs from the wearer's right, so the default goes right shoulder to left hip;
    `mirror` draws it the other way, as it reads on the back."""
    w = face.w
    for y in range(rows):
        x = x0 + round(y * (w - 2 - x0) / (rows - 1))
        if mirror:
            x = w - 1 - x
            face.set(x, y, k(role, base + 1)), face.set(x - 1, y, k(role, base - 1))
        else:
            face.set(x, y, k(role, base + 1)), face.set(x + 1, y, k(role, base - 1))


def crescent(g, pid: str, pivot, bone: str = "TORSO", role: str = "P", base: int = 2, mark: str = "M3",
             face: str = "back", flip: bool = False):
    """A half-scale crescent decal (4 x 4 model pixels) on a flat plate one texel deep."""
    rows = [r[::-1] for r in CRESCENT] if flip else CRESCENT
    z0 = 0 if face == "back" else -1
    plate = g.piece(pid, bone, (-4, -4, z0), (8, 8, 1), pivot=pivot, scale=(.5, .5, .5))
    for f in plate.faces:
        fabric(f, role, "plain", 15004, base)
    stamp(getattr(plate, face), rows, 0, 0, {"#": mark})
    return plate
