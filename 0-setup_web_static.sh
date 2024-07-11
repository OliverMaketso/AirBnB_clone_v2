#!/usr/bin/env bash
#Sets up the web servers for deployment of web-static

sudo apt-get update
sudo apt-get -y install  nginx
sudo ufw allow 'Nginx HTTP'

mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo '<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "s/server_name _;/&\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t\tindex index.html;\n\t}\n/" /etc/nginx/sites-available/default

sudo service nginx restart
