#!/usr/bin/env python3

import subprocess
import shutil

def lint_shell():
    print("\n🟢 Running Shell linters on entire repo...")

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
