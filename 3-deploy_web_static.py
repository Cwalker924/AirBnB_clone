#!/usr/bin/python3
"""
This is 3-deploy_web_static.py module and houses the 'do_pack','do_deploy' and
'deploy' function.
"""
from fabric.api import *


env.hosts = ['107.20.68.230:34185']
env.user = 'root'


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


def do_deploy(archive_path):
    try:

        file_name = archive_path.split("/")[-1]
        file_strip = file_name.split(".")[0]
        dir_target = "/data/web_static/releases/{}".format(file_strip)

        put(archive_path, "/tmp")
        run("mkdir -p {}".format(dir_target))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, dir_target, file_strip))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}{}/web_static/* {}".format(dir_target, file_strip, dir_target, file_strip))
        run("sudo rm -rf {}{}/web_static".format(dir_target, file_strip))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(dir_target, file_strip))
        return (True)
    except:
        return (False)


def deploy():
        try:
                path = do_pack()
                deploy = do_deploy(path)
                return (deploy)
        except:
                return (False)
