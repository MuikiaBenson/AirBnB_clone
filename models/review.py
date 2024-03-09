#!/usr/bin/python3
"""Review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
    Attributes:
        place_id (str): Place id
        user_id (str): User id
        text (str): The review text
    """
    place_id = ""
    user_id = ""
    text = ""
