#!/usr/bin/env python3

import subprocess
import shutil
import os

def lint_cpp():
    print("\n🟢 Running C++ linters on entire repo...")

    if shutil.which("cppcheck") is None:
        print("❌ cppcheck not installed. Skipping.")
        return

    cmd = ["cppcheck", "."]
    print(f"▶️ {' '.join(cmd)}")
    subprocess.run(cmd)
