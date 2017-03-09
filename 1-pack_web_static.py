#!/usr/bin/python3
"""
This is module 1-pack_web_static.py
The following is a fabfile
"""
from fabric.api import local
from time import strftime


def do_pack():
    """
    a Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.
    """
    time = strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return (file_name)
    except:
        return (None)
