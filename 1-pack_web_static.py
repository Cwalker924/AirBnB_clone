#!/usr/bin/python3
"""
This is module 1-pack_web_static.py
The following is a fabfile
"""
from fabric.api import local
import datetime


def do_pack():
    """
    a Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.
    """
    time = datetime.datime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static/"
              .format(time))
        return ("versions/web_static_{}.tgz".format(time))
    except:
        return (None)
