"""Backward Bandana: the forehead protector tied as a bandana and turned round, Genma Shiranui's
way: dusky cloth over the crown, the steel plate riding on the back of the head, the knot perched
on the brow and the hair left to fall loose from underneath."""
from kit_shiranui import backward_bandana

META = {"name": "Backward Bandana", "gender": "unisex", "hides_hair": ["crown", "fringe"],
        "description": "Bandana protector turned backwards: plate on the back of the head, knot on the brow."}


def build(g):
    backward_bandana(g, "D", seed=16890)
