#!/usr/bin/python3
"""State class module"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.
    Attrinutes:
        name (str): Name of the state.
    """
    name = ""
