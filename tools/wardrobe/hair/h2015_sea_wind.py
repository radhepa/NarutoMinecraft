"""Sea Wind: tousled hair blown to one side, every lock on the crown and fringe streaming the same
way, the ends lifting, the nape grown to the collar."""
from anime import back_fan, ring_shell
from kit_namiashi import wave_lock
from paint import scalp

META = {"name": "Sea Wind", "gender": "unisex",
        "description": "Tousled hair blown to one side, the locks streaming the same way, ends lifting."}

# (x, y, z, rz): crown locks lying over toward the wearer's left.
CROWN = [(-3.0, -8.4, -2.4, -100), (-3.0, -8.4, .4, -104), (-3.0, -8.4, 3.0, -100), (-.6, -8.6, -1.2, -96), (-.6, -8.6, 1.8, -96)]


def build(g):
    scalp(g, 20411, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 20412, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, y, z, rz) in enumerate(CROWN):
        wave_lock(g, f"crown_{i}", (x, y, z), (0, 0, rz), [(((2, 3), (2, 2)), 0, 0), (((1, 2),), 0, 30)], depth=2,
                  seed=20415 + i * 5)
    for i, (x, rz) in enumerate(((-3.0, -30), (-1.4, -38), (.4, -44))):
        wave_lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), [(((2, 2),), 0, 0), (((1, 1),), 0, -30)], seed=20450 + i * 3)
    back_fan(g, "nape", [(-2.6, ((3, 3), (2, 1)), 22, 14), (0, ((3, 3), (2, 2)), 12, 12), (2.6, ((3, 3), (2, 1)), 4, 16)],
             seed=20460)
