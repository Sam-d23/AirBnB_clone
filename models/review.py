#!/usr/bin/python3
"""A Review class is created in this module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that manages review objects"""

    place_id = ""
    user_id = ""
    text = ""
