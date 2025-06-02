#!/usr/bin/env bash

set -e

echo "🚀 Setting up Aperion Linter Suite..."

# 1️⃣ Create the linter directory
mkdir -p ~/Aperion/aperion_linter

# 2️⃣ Create __init__.py
echo "# Initialize the linter suite" > ~/Aperion/aperion_linter/__init__.py

# 3️⃣ Create python.py
cat <<EOF > ~/Aperion/aperion_linter/python.py
#!/usr/bin/env python3

import subprocess
import shutil
import os

def lint_python():
    print("\\n🟢 Running Python linters on entire repo...")

    tools = ["black", "flake8", "pylint", "mypy"]
    for tool in tools:
        if shutil.which(tool) is None:
            print(f"❌ {tool} not installed. Skipping.")
            continue

        cmd = [tool, "."]
        print(f"▶️ {' '.join(cmd)}")
        subprocess.run(cmd)
EOF

# 4️⃣ Create js.py
cat <<EOF > ~/Aperion/aperion_linter/js.py
#!/usr/bin/env python3

import subprocess
import shutil

def lint_js():
    print("\\n🟢 Running JavaScript linters on entire repo...")

    if shutil.which("npx") is None:
        print("❌ npx not installed. Skipping.")
        return

    cmd = ["npx", "eslint", "."]
    print(f"▶️ {' '.join(cmd)}")
    subprocess.run(cmd)
EOF

# 5️⃣ Create css.py
cat <<EOF > ~/Aperion/aperion_linter/css.py
#!/usr/bin/env python3

import subprocess
import shutil

def lint_css():
    print("\\n🟢 Running CSS linters on entire repo...")

    if shutil.which("npx") is None:
        print("❌ npx not installed. Skipping.")
        return

    cmd = ["npx", "stylelint", "**/*.css"]
    print(f"▶️ {' '.join(cmd)}")
    subprocess.run(cmd)
EOF

# 6️⃣ Create markdown.py
cat <<EOF > ~/Aperion/aperion_linter/markdown.py
#!/usr/bin/env python3

import subprocess
import shutil

def lint_markdown():
    print("\\n🟢 Running Markdown linters on entire repo...")

    if shutil.which("npx") is None:
        print("❌ npx not installed. Skipping.")
        return

    cmd = ["npx", "markdownlint", "."]
    print(f"▶️ {' '.join(cmd)}")
    subprocess.run(cmd)
EOF

# 7️⃣ Create shell.py
cat <<EOF > ~/Aperion/aperion_linter/shell.py
#!/usr/bin/env python3

import subprocess
import shutil

def lint_shell():
    print("\\n🟢 Running Shell linters on entire repo...")

    if shutil.which("shellcheck") is not None:
        cmd_shellcheck = ["shellcheck", "**/*.sh"]
        print(f"▶️ {' '.join(cmd_shellcheck)}")
        subprocess.run(cmd_shellcheck)
    else:
        print("❌ shellcheck not installed. Skipping.")

    if shutil.which("shfmt") is not None:
        cmd_shfmt = ["shfmt", "-d", "."]
        print(f"▶️ {' '.join(cmd_shfmt)}")
        subprocess.run(cmd_shfmt)
    else:
        print("❌ shfmt not installed. Skipping.")
EOF

# 8️⃣ Create cpp.py
cat <<EOF > ~/Aperion/aperion_linter/cpp.py
#!/usr/bin/env python3

import subprocess
import shutil
import os

def lint_cpp():
    print("\\n🟢 Running C++ linters on entire repo...")

    if shutil.which("cppcheck") is None:
        print("❌ cppcheck not installed. Skipping.")
        return

    cmd = ["cppcheck", "."]
    print(f"▶️ {' '.join(cmd)}")
    subprocess.run(cmd)
EOF

# 9️⃣ Create summary.py
cat <<EOF > ~/Aperion/aperion_linter/summary.py
#!/usr/bin/env python3

def final_summary():
    print("\\n✅ All linting tasks completed!")
EOF

# 🔟 Create the main CLI script
cat <<EOF > ~/Aperion/aperion
#!/usr/bin/env python3

from aperion_linter import python, js, css, markdown, shell, cpp, summary

def main():
    print("🚀 Starting Aperion Linter Suite for the ENTIRE REPO!")

    python.lint_python()
    js.lint_js()
    css.lint_css()
    markdown.lint_markdown()
    shell.lint_shell()
    cpp.lint_cpp()

    summary.final_summary()

if __name__ == "__main__":
    main()
EOF

# Set executable permissions
chmod +x ~/Aperion/aperion
chmod +x ~/Aperion/aperion_linter/*.py

echo "✅ Aperion Linter Suite setup complete!"
echo "▶️ Run it with: ./aperion"
