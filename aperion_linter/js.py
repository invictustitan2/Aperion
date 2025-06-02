#!/usr/bin/env python3

import subprocess
import shutil

def lint_js():
    print("\n🟢 Running JavaScript linters on entire repo...")

    if shutil.which("npx") is None:
        print("❌ npx not installed. Skipping.")
        return

    cmd = ["npx", "eslint", "."]
    print(f"▶️ {' '.join(cmd)}")
    subprocess.run(cmd)
