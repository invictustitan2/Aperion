#!/usr/bin/env python3

"""
Aperion CLI - Lint and auto-fix across multiple languages.
"""

import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

import click
from rich.console import Console
from rich.progress import Progress


@click.group()
def cli():
    """
    Aperion CLI Entry Point.
    """


@cli.command()
def lint():
    """
    Lint and auto-fix across supported languages.
    """
    console = Console()
    console.print("[bold green]🔧 Starting lint & auto-fix session...[/bold green]")

    tasks = [
        ("Python auto-formatting", ["black", "."]),
        ("Python linting (Ruff)", ["ruff", "."]),
        ("Python linting (Flake8)", ["flake8", "."]),
        ("Python linting (Pylint)", ["pylint", "."]),
        ("JavaScript linting (ESLint)", ["eslint", ".", "--fix"]),
        ("CSS linting (Stylelint)", ["stylelint", "**/*.css", "--fix"]),
        ("Markdown linting (Markdownlint)", ["markdownlint", "."]),
        ("Shell script linting", ["shellcheck", "./**/*.sh"]),
        ("Shell script auto-formatting", ["shfmt", "-w", "."]),
        ("C/C++ linting (Cppcheck)", ["cppcheck", "."]),
        ("Go linting (golangci-lint)", ["golangci-lint", "run"]),
    ]

    def run_task(desc, cmd):
        console.print(f"▶️ {desc}...")
        try:
            result = subprocess.run(
                cmd,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.stdout.strip():
                console.print(result.stdout.strip())
            if result.stderr.strip():
                console.print(result.stderr.strip())
        except FileNotFoundError:
            console.print(f"⚠️ {desc} tool not found, skipping.")
        return desc

    with Progress() as progress:
        task_id = progress.add_task("Linting & auto-fixing files...", total=len(tasks))

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(run_task, desc, cmd) for desc, cmd in tasks]
            for future in as_completed(futures):
                _ = future.result()
                progress.advance(task_id)

    console.print("[bold green]✅ Linting & auto-fix completed![/bold green]")

    # Automatically commit changes if there are any
    console.print("[bold green]💾 Committing changes to Git...[/bold green]")
    subprocess.run(["git", "config", "--global", "user.name", "Eric Gray"], check=False)
    subprocess.run(
        ["git", "config", "--global", "user.email", "obeyvanta@aperion.cc"], check=False
    )
    subprocess.run(["git", "add", "."], check=False)
    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            "Automated lint & auto-fix: apply PEP8 and best practices",
        ],
        check=False,
    )
    console.print("[bold green]✅ Changes committed![/bold green]")


if __name__ == "__main__":
    cli()
