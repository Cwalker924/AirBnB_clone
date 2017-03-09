#!/usr/bin/env bash
# a Bash script that sets up a web servers for the deployment of web_static.

# install nginx
sudo apt-get update
sudo apt-get -y install nginx

# creating needed dir if not exist
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/

# for testing purposes
echo "testing" > /data/web_static/releases/test/index.html

# Sym link for test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# adds and specifies ownership to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Nginx config to serve content
serv_conf="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "37 i\ $serv_conf" /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
