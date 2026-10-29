"""Shinobi Face: the Village Friends Living Eyes face. The lashes, pupils, glints, brows and mouth
are face planes (see living_eyes.py), so the skin only carries the eye row they sample: the eye
whites on the outer columns and the irises on the inner ones, painted from the eye color."""

META = {"name": "Shinobi Face", "gender": "unisex",
        "description": "Living Eyes (Starlit or Soft Glint, set per character) in the character's eye color."}

# Face row 4 (texture y 12): white, iris | skin | iris, white. Columns 3-4 stay skin for the lids.
SAMPLES = {1: "E4", 2: "E2", 5: "E2", 6: "E4"}


def build(g):
    f = g.part("head").front
    for x, key in SAMPLES.items():
        f.set(x, 4, key)
