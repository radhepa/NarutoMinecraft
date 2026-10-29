"""Deep Hood: Shino's Shippuden hood pulled up and forward, so that between the hood and the round
shades nothing of the face is left but shadow."""
from kit_aburame import deep_hood, lenses

META = {"name": "Deep Hood", "gender": "unisex", "covers_face": True, "hides_hair": ["*"],
        "description": "A deep hood pulled up over the head, round dark shades in its shadow."}


def build(g):
    deep_hood(g, "P", "twill", 10901)
    lenses(g, "K", "M", "round", temples=False)
