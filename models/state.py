#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """ State Class
    Holds one public attribute: 'name'.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ init method
        initializes class
        """
        super().__init__(*args, **kwargs)
