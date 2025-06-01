#!/usr/bin/env bash
echo "🔧 Lint & Format script starting..."

# Setup test files
echo -e "def BADstyle():\n  print( 'bad' )\n\n  \n  \n  \n\n  " > test_bad.py
echo "<html><body><h1>Title</h1></body></html>" > test_bad.html
echo "body { color: red; }" > test_bad.css
echo "function badStyle(){console.log('bad');}" > test_bad.js

# Lint & Format Python
echo "🐍 Running pylint on test_bad.py..."
pylint test_bad.py

echo "🐍 Running black on test_bad.py..."
black test_bad.py

# Lint with coala for HTML, CSS, JS
echo "🌐 Running coala on test files..."
coala -v --files=test_bad.html,test_bad.css,test_bad.js --apply-patches

# Clean up test files
echo "🧹 Cleaning up test files..."
rm -f test_bad.py test_bad.html test_bad.css test_bad.js

echo "✅ Lint & Format script completed!"
