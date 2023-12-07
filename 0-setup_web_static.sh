#!/usr/bin/env bash
# set up web server for deployment

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx -y
fi
    sudo mkdir -p /data/web_static/releases/test/
    sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <h1>This is a test page for Nginx configuration</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null
# create symbolic link
ln -fs /data/web_static/releases/test/ /data/web_static/current
# set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the
# content of /data/web_static/current/
config_file="/etc/nginx/sites-available/default"
sudo sed -i '/^server {/a \
\
    location /hbnb_static {\
        alias /data/web_static/current/;\
    }\
' $config_file

sudo service nginx restart
