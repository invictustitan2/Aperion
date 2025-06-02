#!/usr/bin/env python3.9
"""
Code Guardian: Automated linting, auto-fixing, and refactoring assistant
Multi-language support + custom thresholds
Compatible with Python 3.9 and coala-bears, Rope
"""

import os
import re
import subprocess

from rope.base.project import Project


def run_coala():
    """
    Runs coala in verbose mode with extended bears for multiple languages
    and custom thresholds.
    """
    print("🔍 Running coala with multi-language bears (auto-fix enabled)...")
    result = subprocess.run(
        [
            "coala",
            "-v",
            "--files=**/*",
            "--bears=PyLintBear,PEP8Bear,PyImportSortBear,PEP257Bear,RadonBear,"
            "TrailingWhitespaceBear,LineLengthBear,FilenameBear,JSONFormatBear,"
            "YAMLLintBear,MarkdownBear,HTMLLintBear,CSSLintBear,JSHintBear,"
            "ShellCheckBear,DockerfileLintBear,CPPLintBear,ClangFormatBear,"
            "GoVetBear,GoLintBear,RustfmtBear,CargoCheckBear,DuplicateFileBear",
            "--apply-patches",
            "--settings=RadonBear:radon_complexity_threshold=10",
            "--settings=LineLengthBear:max_line_length=88",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    print(result.stdout)
    return result.stdout


def run_rope_rename(project_dir, file_path, old_name, new_name):
    """
    Uses Rope to safely rename variables or functions across a file.
    """
    project = Project(project_dir)
    resource = project.get_file(file_path)
    changes = project.do_rename(resource, old_name, new_name)
    project.do(changes)
    print(f"✅ Rope renamed '{old_name}' -> '{new_name}' in {file_path}")


if __name__ == "__main__":
    # Step 1: Linting and auto-fixing
    coala_output = run_coala()

    # Step 2: Identify variable naming issues from coala output (for Python files)
    naming_issues = re.findall(
        r"invalid-name.*?Variable name \"(\w+)\".*?", coala_output
    )
    if naming_issues:
        print("\n⚠️ Variable naming issues detected by coala (Python only):")
        for var in naming_issues:
            new_name = input(
                f"🔄 Rename variable '{var}' to (press enter to skip): "
            ).strip()
            if new_name:
                file_path = input(f"📄 Enter file path for variable '{var}': ").strip()
                if os.path.exists(file_path):
                    run_rope_rename(os.getcwd(), file_path, var, new_name)
                else:
                    print(f"❌ File {file_path} does not exist. Skipping...")

    # Step 3: Prompt to commit and push to GitHub
    commit_decision = (
        input("\n💡 Do you want to commit these changes? (y/n): ").strip().lower()
    )
    if commit_decision == "y":
        subprocess.run(["git", "add", "."])
        commit_message = input("✏️ Enter commit message: ").strip()
        subprocess.run(["git", "commit", "-m", commit_message])
        subprocess.run(["git", "push", "origin", "main"])
        print("✅ Changes committed and pushed to GitHub.")
    else:
        print("🚫 Skipping Git commit.")

    print("🎉 Code Guardian finished! Happy coding, Tiger 🐅🚀")
