#!/bin/bash

set -e

echo "🚀 Starting Aperion Portal Setup..."

# 1️⃣ Update & upgrade
sudo apt update && sudo apt upgrade -y

# 2️⃣ Install nginx if not present
if ! dpkg -l | grep -q nginx; then
	echo "🔧 Installing Nginx..."
	sudo apt install -y nginx
fi

# 3️⃣ Install Python if needed
if ! command -v python3 &>/dev/null; then
	echo "🔧 Installing Python3..."
	sudo apt install -y python3 python3-pip
fi

# 4️⃣ Remove any old deploy of aperion.cc
echo "🔄 Removing old /var/www/aperion.cc..."
sudo rm -rf /var/www/aperion.cc

# 5️⃣ Deploy the repo to /var/www
echo "📁 Deploying to /var/www/aperion.cc..."
sudo cp -r $(pwd) /var/www/aperion.cc
sudo chown -R www-data:www-data /var/www/aperion.cc
sudo find /var/www/aperion.cc -type d -exec chmod 755 {} \;
sudo find /var/www/aperion.cc -type f -exec chmod 644 {} \;

# 6️⃣ Nginx config for local-only
NGINX_CONF="/etc/nginx/sites-available/aperion.cc"
if [ ! -f "$NGINX_CONF" ]; then
	echo "📝 Creating Nginx config..."
	cat <<EOL | sudo tee $NGINX_CONF
server {
    listen 127.0.0.1:80;
    server_name aperion.local;

    root /var/www/aperion.cc;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOL
	sudo ln -sf $NGINX_CONF /etc/nginx/sites-enabled/aperion.cc
fi

# 7️⃣ Reload Nginx
echo "🔄 Reloading Nginx..."
sudo nginx -t && sudo systemctl reload nginx

echo "✅ Aperion Portal is set up locally at http://127.0.0.1"

# 8️⃣ Optional SSL (commented out)
# sudo apt install -y certbot python3-certbot-nginx
# sudo certbot --nginx -d YOURDOMAIN.com

# 9️⃣ Optional Firewall (commented out)
# sudo ufw allow 'Nginx Full'
# sudo ufw enable

echo "🔒 Local access only. Edit Nginx config for external access when ready."
