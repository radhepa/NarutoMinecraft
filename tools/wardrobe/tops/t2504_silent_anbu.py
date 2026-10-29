"""Silent ANBU: the Tobari night squads' ANBU armor, the plates dulled to slate so they catch no
moon, a short pleated half-cape hung from the right shoulder, black gloves and guards, and a
dark muffler worn down at the throat, its ends tucked behind."""
from kit import arm_bone, arm_x
from kit_shinobi import anbu_arms, anbu_plates
from kit_tobari import muffler, pleats, plain_body
from paint import solid

META = {
    "name": "Silent ANBU",
    "gender": "unisex",
    "description": "Slate ANBU plates, a short pleated half-cape on the right shoulder, black gloves, a muffler worn down.",
    "tags": ["shinobi", "armor"],
}


def build(g):
    plain_body(g, "D", "weave", 25390)
    anbu_plates(g, seed=25391)
    anbu_arms(g, tattoo=True)
    cape = g.piece("half_cape", arm_bone("right"), (arm_x("right") - .6, -2.6, -2.6), (5, 4, 5), inflate=.1)
    solid(cape, "K", "twill", 25392, 2)
    for face in cape.sides:
        pleats(face, "K", base=2)
    back = g.piece("half_cape_back", "TORSO", (-4.5, 0, 0), (5, 9, 1), pivot=(0, -.2, 2.55), motion="flap_back")
    solid(back, "K", "twill", 25393, 2)
    pleats(back.back, "K")
    muffler(g, "muffler", "K", "knit", 25394, tails="back")
