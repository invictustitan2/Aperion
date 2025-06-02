#!/bin/bash
# aperion_verity_suite.sh: Unified integrity & security check for Aperion.cc

BASE_DIRS=("/var/www/aperion.cc/car-tracker" "/var/www/aperion.cc/cavern-of-evil")
SSL_DIR="/etc/letsencrypt/live/aperion.cc"
SECURITY_DIR="/var/www/aperion.cc/security"

# Summary variables
ssl_ok=true
guardian_ok=true
entropy_ok=true
verity_ok=true
integrity_ok=true
nginx_ok=true

echo -e "\n🔍 Starting full Aperion Verity & Security Suite..."

# Verity check for each directory
for BASE_DIR in "${BASE_DIRS[@]}"; do
	echo -e "\n🔍 Checking integrity of: $BASE_DIR"
	find $BASE_DIR -type f | sort | while read f; do
		sha256sum "$f"
	done >"$BASE_DIR/verity_manifest.sha256"
	echo "✅ Manifest created for $(basename $BASE_DIR)"
done

# SSL certificate checks
echo -e "\n🔍 Verifying SSL certificate presence & permissions..."
if [ -d "$SSL_DIR" ]; then
	echo "✅ SSL directory found: $SSL_DIR"
	CERT="$SSL_DIR/fullchain.pem"
	KEY="$SSL_DIR/privkey.pem"

	if [ -f "$CERT" ]; then
		echo "✅ SSL certificate file: $CERT"
	else
		echo "❌ SSL certificate file missing!"
		ssl_ok=false
	fi

	if [ -f "$KEY" ]; then
		echo "✅ SSL key file: $KEY"
	else
		echo "❌ SSL key file missing!"
		ssl_ok=false
	fi

	echo "🔍 SSL file permissions:"
	ls -l $CERT $KEY

	if command -v openssl >/dev/null 2>&1 && [ -f "$CERT" ]; then
		EXPIRY_DATE=$(openssl x509 -enddate -noout -in $CERT | cut -d= -f2)
		echo "✅ SSL certificate expires on: $EXPIRY_DATE"
	else
		echo "⚠️ OpenSSL not available or cert missing—skipping expiration check."
		ssl_ok=false
	fi
else
	echo "❌ SSL directory missing: $SSL_DIR"
	ssl_ok=false
fi

# Run tailored Python security scripts
echo -e "\n🔍 Running tailored guardian_v3_1.py..."
python3 $SECURITY_DIR/guardian_v3_1.py || guardian_ok=false

echo -e "\n🔍 Running tailored entropy_monitor.py..."
python3 $SECURITY_DIR/entropy_monitor.py || entropy_ok=false

echo -e "\n🔍 Running tailored verity.py..."
python3 $SECURITY_DIR/verity.py || verity_ok=false

echo -e "\n🔍 Running tailored integrity_check.py..."
python3 $SECURITY_DIR/integrity_check.py || integrity_ok=false

# Nginx config check
echo -e "\n🔍 Checking Nginx site configurations..."

if [ -f /etc/nginx/sites-enabled/default ]; then
	echo "❌ Default Nginx config is still enabled!"
	nginx_ok=false
else
	echo "✅ Default Nginx config removed."
fi

if [ -L /etc/nginx/sites-enabled/aperion.conf ]; then
	echo "✅ Aperion config linked in sites-enabled."
else
	echo "❌ Aperion config not linked or missing!"
	nginx_ok=false
fi

# Final summary
echo -e "\n\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩"
echo "📝 Summary of Aperion Verity Suite:"
echo "--------------------------------------"

[[ "$ssl_ok" == true ]] && echo "✅ SSL Certificate Checks: PASSED" || echo "❌ SSL Certificate Checks: FAILED"
[[ "$guardian_ok" == true ]] && echo "✅ guardian_v3_1.py: PASSED" || echo "❌ guardian_v3_1.py: FAILED"
[[ "$entropy_ok" == true ]] && echo "✅ entropy_monitor.py: PASSED" || echo "❌ entropy_monitor.py: FAILED"
[[ "$verity_ok" == true ]] && echo "✅ verity.py: PASSED" || echo "❌ verity.py: FAILED"
[[ "$integrity_ok" == true ]] && echo "✅ integrity_check.py: PASSED" || echo "❌ integrity_check.py: FAILED"
[[ "$nginx_ok" == true ]] && echo "✅ Nginx Config Check: PASSED" || echo "❌ Nginx Config Check: FAILED"

echo "--------------------------------------"
echo "✅ Aperion Verity & Security Suite: COMPLETED"
echo -e "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩"
