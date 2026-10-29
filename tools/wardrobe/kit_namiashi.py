"""Namiashi building blocks: the 'wave-foot' family of swordsmen of the Hokage's guard. The wave trim
the clan runs along its hems and cuffs, hair locks whose ends curl over like a breaking wave, the
kokuto (Raido's short black blade) worn across the small of the back or at the hip, and the wave
crest.

Every piece paints key colors only: the blade's sheath and hilt in K, its guard in M, the hilt wrap
and sheath cord in A, so a palette decides how a family blade looks."""
from anime import lock
from glyphs import stamp
from paint import fabric, k, solid
from wardrobe import rot_matrix

# The wave crest, drawn at double resolution on a half-scale decal: three crests rolling over one
# another, the clan's name ('wave-foot') in a picture.
CREST = ["...###..",
         "..#...#.",
         ".#..#..#",
         ".#.#.#..",
         "#.#..#..",
         "#.#.##.#",
         "##.#..##",
         "########"]


def wave_band(face, y: int, role: str = "S", base: int = 2, x0: int = 0, x1: int | None = None, ground: str | None = None,
              phase: int = 0):
    """The clan's wave trim, two rows from `y`: rounded crests rising every four texels over a solid
    band. Paint it on a box's strip so the waves run on round the garment. `ground` fills the gaps
    between the crests (the garment's own cloth when None)."""
    x1 = face.w - 1 if x1 is None else x1
    for x in range(x0, x1 + 1):
        p = (x + phase) % 4
        if p in (1, 2):
            face.set(x, y, k(role, base + 1 if p == 1 else base))
        elif ground:
            face.set(x, y, ground)
        face.set(x, y + 1, k(role, base - (1 if p == 3 else 0)))


def wave_lock(g, pid: str, pivot, rotation, parts, depth: int = 1, seed: int = 0, base: int = 2, motion: str = "none"):
    """A lock of hair that bends as it falls, its end curling over like a wave: `parts` lists
    (segments, extra rx, extra rz), each part starting where the last one ended, turned a little
    further. Returns the end point."""
    p, (rx, ry, rz) = tuple(pivot), tuple(rotation)
    for i, (segments, drx, drz) in enumerate(parts):
        rx, rz = rx + drx, rz + drz
        lock(g, f"{pid}_{i}", p, (rx, ry, rz), segments, depth, seed + i * 17, base, ring=1 if i == 0 else None,
             motion=motion)
        length = sum(h for _, h in segments)
        m = rot_matrix(rx, ry, rz)
        p = tuple(p[j] + m[j][1] * (length - .4) for j in range(3))
    return p


def kokuto(g, prefix: str = "kokuto", pivot=(-2.6, 9.4, 2.85), rotation=(0, 0, -84), bone: str = "TORSO", length: int = 7,
           hilt: int = 3, cord: str | None = "A2"):
    """The kokuto, a short black blade in a black lacquered sheath, the guard at the pivot: a hilt
    wrapped in diamonds along local -y, a round steel guard, the sheath along +y with a steel end
    and the cord tied round its mouth. The default pose wears it across the small of the back, the
    hilt out past the right hip where the hand finds it."""
    grip = g.piece(f"{prefix}_hilt", bone, (-.5, -hilt, -.5), (1, hilt, 1), pivot=pivot, rotation=rotation)
    solid(grip, "K", "smooth", 20901, 2, edge=False)
    for face in grip.sides:
        for y in range(hilt):
            face.set(0, y, cord if cord and y % 2 == 0 else "K3")
    grip.top.fill("M2")
    guard = g.piece(f"{prefix}_guard", bone, (-1, 0, -1), (2, 1, 2), pivot=pivot, rotation=rotation)
    solid(guard, "M", "plain", 20902, 2)
    sheath = g.piece(f"{prefix}_sheath", bone, (-.5, 1, -.5), (1, length, 1), pivot=pivot, rotation=rotation)
    solid(sheath, "K", "smooth", 20903, 1)
    for face in sheath.sides:
        face.set(0, 0, "K3")
        face.set(0, length - 1, "M1")
        face.set(0, length - 2, "M3")
        if cord:
            face.set(0, 1, cord), face.set(0, length // 2, cord)
    sheath.bottom.fill("M1")
    return grip, guard, sheath


def hip_kokuto(g, prefix: str = "kokuto", side: str = "left", cord: str | None = "A2"):
    """The kokuto thrust through the belt on one hip, hilt forward and up, sheath sloping back."""
    sign = 1 if side == "left" else -1
    return kokuto(g, prefix, pivot=(3.0 * sign, 9.2, -2.6), rotation=(70, 0, -10 * sign), length=7, cord=cord)


def back_blade(g, prefix: str = "blade", cord: str | None = "A2", length: int = 10):
    """A longer guard's blade slung on the back, hilt over the LEFT shoulder (the Gekko carry theirs
    over the right)."""
    return kokuto(g, prefix, pivot=(1.6, 2.0, 2.9), rotation=(0, 0, 24), length=length, hilt=4, cord=cord)


def crest(g, pid: str, pivot, bone: str = "TORSO", role: str = "P", base: int = 2, mark: str = "S3", face: str = "back"):
    """The wave crest on a half-scale decal plate (4 x 4 model pixels) one texel deep."""
    z0 = 0 if face == "back" else -1
    plate = g.piece(pid, bone, (-4, -4, z0), (8, 8, 1), pivot=pivot, scale=(.5, .5, .5))
    for f in plate.faces:
        fabric(f, role, "plain", 20904, base)
    stamp(getattr(plate, face), CREST, 0, 0, {"#": mark})
    return plate
