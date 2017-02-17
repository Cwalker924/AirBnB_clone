#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """ City Class
    Holds two public attributes: 'state_id', 'name'.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ init method
        initializes class
        """
        super().__init__(*args, **kwargs)
