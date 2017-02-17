#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """ User Class
    Holds four public attributes: 'email', 'password', 'first_name',
    'last_name'.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ init method
        initializes class
        """
        super().__init__(*args, **kwargs)
