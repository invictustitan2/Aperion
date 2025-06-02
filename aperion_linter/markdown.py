#!/usr/bin/env python3

import subprocess
import shutil

def lint_markdown():
    print("\n🟢 Running Markdown linters on entire repo...")

    if shutil.which("npx") is None:
        print("❌ npx not installed. Skipping.")
        return

    cmd = ["npx", "markdownlint", "."]
    print(f"▶️ {' '.join(cmd)}")
    subprocess.run(cmd)
