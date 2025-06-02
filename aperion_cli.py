#!/usr/bin/env python3

"""
Aperion CLI - Lint and auto-fix across multiple languages.
"""

import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import glob

import click
from rich.console import Console
from rich.progress import Progress


@click.group()
def cli():
    """
    Aperion CLI Entry Point.
    """


def build_tasks(console, source_dirs):
    """
    Build a list of linting and formatting tasks for each source directory.
    """
    tasks = []

    for folder in source_dirs:
        if not os.path.exists(folder):
            console.print(f"⚠️ Skipping {folder}, does not exist.")
            continue

        if "coala-env-old" in folder:
            console.print(f"⚠️ Skipping legacy folder: {folder}")
            continue

        tasks.extend([
            (f"Python auto-formatting ({folder})",
            ["black", folder]),
            (f"Python linting (Ruff) ({folder})",
            ["ruff", "check", folder]),
            (f"Python linting (Flake8) ({folder})",
            ["flake8", folder]),
            (f"Python linting (Pylint) ({folder})",
            ["pylint", folder]),
            (f"JavaScript linting (ESLint) ({folder})",
            ["eslint", folder, "--fix"]),
            (f"CSS linting (Stylelint) ({folder})",
            ["stylelint", f"{folder}/**/*.css", "--fix"]),
            (f"Markdown linting (Markdownlint) ({folder})",
            ["markdownlint", folder]),
        ])

        sh_files = glob.glob(f"{folder}/**/*.sh", recursive=True)
        if sh_files:
            tasks.extend([
                (f"Shell script linting ({folder})",
                 ["shellcheck"] + sh_files),
                (f"Shell script auto-formatting ({folder})",
                 ["shfmt", "-w", folder]),
            ])
        else:
            console.print(
                f"⚠️ Skipping shell lint in {folder}, no .sh files found."
            )

        cpp_files = glob.glob(f"{folder}/**/*.[ch]pp", recursive=True) + \
                    glob.glob(f"{folder}/**/*.[ch]", recursive=True)
        if cpp_files:
            tasks.append(
                (f"C/C++ linting (Cppcheck) ({folder})",
                 ["cppcheck", folder])
            )
        else:
            console.print(
                f"⚠️ Skipping C/C++ lint in {folder}, "
                f"no .c/.cpp files found."
            )

    if os.path.exists("go.mod"):
        tasks.append(
            ("Go linting (golangci-lint)",
             ["golangci-lint", "run"])
        )
    else:
        console.print("⚠️ Skipping Go linting, no go.mod found.")

    return tasks


def run_task(desc, cmd, console, log_file, results_summary):
    """
    Run a single linting or formatting task and log the output.
    """
    console.print(f"▶️ {desc}...")
    log_file.write(f"\n===== {desc} =====\n")
    try:
        result = subprocess.run(
            cmd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stdout.strip():
            console.print(result.stdout.strip())
            log_file.write(result.stdout.strip() + "\n")
        if result.stderr.strip():
            console.print(result.stderr.strip())
            log_file.write(result.stderr.strip() + "\n")
        results_summary.append((desc, "Completed"))
    except subprocess.SubprocessError as e:
        console.print(f"❌ {desc} failed: {e}")
        log_file.write(f"❌ {desc} failed: {e}\n")
        results_summary.append((desc, "Failed"))
    return desc


def commit_and_push(console):
    """
    Commit and push changes to Git.
    """
    console.print(
        "[bold green]💾 Committing changes to Git...[/bold green]"
    )
    subprocess.run(
        ["git", "config", "--global", "user.name", "Eric Gray"],
        check=False
    )
    subprocess.run(
        ["git", "config", "--global", "user.email",
         "obeyvanta@aperion.cc"],
        check=False
    )
    subprocess.run(["git", "add", "."], check=False)
    subprocess.run(
        ["git", "commit", "-m",
         "Automated lint & auto-fix: apply PEP8 and best practices"],
        check=False
    )
    console.print("[bold green]✅ Changes committed![/bold green]")

    console.print(
        "[bold green]🚀 Pushing changes to GitHub...[/bold green]"
    )
    subprocess.run(["git", "push", "origin", "main"],
                   check=False)
    console.print(
        "[bold green]✅ Changes pushed to GitHub![/bold green]"
    )


@cli.command()
def lint():
    """
    Lint and auto-fix across supported source folders.
    """
    console = Console()
    console.print(
        "[bold green]🔧 Starting lint & auto-fix session...[/bold green]"
    )

    source_dirs = ["aperion.cc", "scripts", "projects"]
    tasks = build_tasks(console, source_dirs)
    results_summary = []

    with open("lint_log.txt", "w", encoding="utf-8") as log_file:
        with Progress() as progress:
            task_id = progress.add_task(
                "Linting & auto-fixing files...",
                total=len(tasks)
            )

            with ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(
                        run_task, desc, cmd, console,
                        log_file, results_summary
                    )
                    for desc, cmd in tasks
                ]
                for future in as_completed(futures):
                    _ = future.result()
                    progress.advance(task_id)

    console.print(
        "[bold green]✅ Linting & auto-fix completed![/bold green]"
    )

    console.print("\n[bold green]📊 Summary:[/bold green]")
    for desc, status in results_summary:
        console.print(f"- {desc}: {status}")

    commit_and_push(console)

    console.print(
        "\n[bold green]📝 Full log written to lint_log.txt[/bold green]"
    )


if __name__ == "__main__":
    cli()
