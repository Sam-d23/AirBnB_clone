#!/usr/bin/python3
"""A User class is created in this module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
