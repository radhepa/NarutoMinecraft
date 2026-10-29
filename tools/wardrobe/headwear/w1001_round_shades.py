"""Round Shades: the Aburame's small round dark glasses, worn always, so no one sees where the
wearer is looking."""
from kit_aburame import lenses

META = {"name": "Round Shades", "gender": "unisex", "covers_face": True,
        "description": "Small round dark glasses with thin metal frames."}


def build(g):
    lenses(g, "K", "M", "round")
