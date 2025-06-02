#!/usr/bin/env python3

import subprocess
import shutil

def lint_css():
    print("\n🟢 Running CSS linters on entire repo...")

    if shutil.which("npx") is None:
        print("❌ npx not installed. Skipping.")
        return

    cmd = ["npx", "stylelint", "**/*.css"]
    print(f"▶️ {' '.join(cmd)}")
    subprocess.run(cmd)
