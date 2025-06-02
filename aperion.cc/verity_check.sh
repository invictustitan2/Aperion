#!/bin/bash
# Verity script for aperion.cc ecosystem

BASE_DIRS=("/var/www/aperion.cc/car-tracker" "/var/www/aperion.cc/cavern-of-evil")
echo "🔍 Starting full verity check for aperion.cc..."

for BASE_DIR in "${BASE_DIRS[@]}"; do
	echo "🔍 Checking in $BASE_DIR"
	find $BASE_DIR -type f | sort | while read f; do
		sha256sum "$f"
	done >"$BASE_DIR/verity_manifest.sha256"
	echo "🔍 Manifest created for $(basename $BASE_DIR)"
done

echo "✅ Verity check complete!"
