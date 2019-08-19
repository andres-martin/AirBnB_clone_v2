#!/usr/bin/env bash
# configuration file or webserver deploy static content

sudo apt-get update 
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/  /data/web_static/releases/test/
echo "Tests Nginx Static" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
hbnb_static="\\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}"
sudo sed -i "56i $hbnb_static" /etc/nginx/sites-available/default
sudo service nginx restart

