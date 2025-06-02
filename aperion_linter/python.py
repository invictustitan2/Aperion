#!/usr/bin/env python3

import subprocess
import shutil
import os

def lint_python():
    print("\n🟢 Running Python linters on entire repo...")

    tools = ["black", "flake8", "pylint", "mypy"]
    for tool in tools:
        if shutil.which(tool) is None:
            print(f"❌ {tool} not installed. Skipping.")
            continue

        cmd = [tool, "."]
        print(f"▶️ {' '.join(cmd)}")
        subprocess.run(cmd)
