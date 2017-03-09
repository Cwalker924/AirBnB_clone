#!/usr/bin/python3
"""
This is 2-do_deploy_web_static.py module and houses the 'do_deploy' function.
"""
from fabric.api import *


env.hosts = ['107.20.68.230:34179']
env.user = 'root'


def do_deploy(archive_path):
    try:
        dir_target = "/data/web_static/releases/"
        file_name = archive_path.split("/")[-1]
        file_strip = file_name.split(".")[0]

        put(archive_path, "/tmp")
        run("mkdir -p {}{}".format(dir_target, file_strip))
        run("sudo tar -xzf /tmp/{} -C {}{}".format(file_name, dir_target, file_strip))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}{}/web_static/* {}".format(dir_target, file_strip, dir_target, file_strip))
        run("sudo rm -rf {}{}/web_static".format(dir_target, file_strip))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(dir_target, file_strip))
        return (True)
    except:
        return (False)
