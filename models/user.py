#!/usr/bin/python3
"""User class module."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class

    Attributes:
        email (str): The email of the user.
        password (str): Users password.
        first_name (str): User first name.
        last_name (str): User last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
