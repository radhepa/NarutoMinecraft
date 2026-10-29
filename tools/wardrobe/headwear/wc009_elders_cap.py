"""Elder's Cap: the soft round brimless cap of grandfathers, tea masters and retired scholars, dark
felt gathered into a puffed crown with a little stalk at the top, worn a touch to one side."""
from paint import fabric, solid

META = {"name": "Elder's Cap", "gender": "unisex", "hides_hair": ["*"],
        "description": "Soft round brimless felt cap with a puffed crown and a little stalk, worn a touch to one side."}


def build(g):
    band = g.piece("cap_band", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.64)
    solid(band, "K", "velvet", 37930, 3, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 1, "K2")
    crown = g.piece("cap_crown", "HEAD", (-4.5, -2, -4.5), (9, 2, 9), pivot=(.3, -8.4, .2), rotation=(0, 0, -5))
    solid(crown, "K", "velvet", 37931, 3, edge=False)
    fabric(crown.top, "K", "velvet", 37931, 4)
    for face in crown.sides:
        face.hline(0, face.w - 1, 1, "K2")
        for x in range(1, face.w, 3):
            face.set(x, 0, "K2")
    stalk = g.piece("cap_stalk", "HEAD", (-.5, -1, -.5), (1, 1, 1), pivot=(.1, -10.4, .2))
    solid(stalk, "K", "velvet", 37932, 2, edge=False)
