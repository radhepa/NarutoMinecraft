"""Shadow Sideburns: the clan head's look. The high spiky tail, a little fuller, with thick
sideburns grown long down the jaw so they read like a short beard from the side."""
from anime import lock
from kit_nara import pineapple, pulled_back

META = {"name": "Shadow Sideburns", "gender": "male",
        "description": "High spiky pineapple tail with thick sideburns grown down to the jaw."}

LONG = ((4, 3), (3, 3), (2, 2), (1, 2))
MID = ((3, 3), (3, 2), (2, 2), (1, 1))
SPIKES = [(LONG, -26, 0), (LONG, -44, -26), (LONG, -44, 26), (MID, -68, -12), (MID, -68, 12), (MID, -16, -42),
          (MID, -16, 42), (((2, 3), (1, 2)), -86, 0)]


def build(g):
    pulled_back(g, 5051, side_rows=3, back_rows=6, sideburn=4)
    pineapple(g, "tail", (0, -7.4, 4.2), SPIKES, seed=5060)
    # Sideburns: wide in front of the ears, running down to the jaw line and curling under it.
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"sideburn_{side}", (4.4 * sign, -5.4, -1.6), (0, 0, 0), ((2, 4), (2, 1)), 3, 5080 + (sign > 0), ring=None)
        lock(g, f"jaw_{side}", (4.3 * sign, -.4, -2.2), (0, 0, -80 * sign), ((2, 2),), 2, 5085 + (sign > 0), ring=None)
