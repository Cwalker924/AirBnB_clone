#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Place Class
    Hold one public attribute: 'name'.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ init module
        initializes class
        """
                super().__init__(*args, **kwargs)
