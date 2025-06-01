#!/usr/bin/env python3
# /var/www/aperion.cc/cavern2055/game.py

from time import sleep

from rich.console import Console
from rich.panel import Panel

console = Console()


def slow_print(text, delay=0.05):
    for char in text:
        console.print(char, end="", style="bold cyan")
        sleep(delay)
    console.print("")  # newline


def intro_scene():
    console.clear()

    # Title
    console.print(
        Panel.fit(
            "[bold red]CAVERN OF EVIL: 2055[/bold red]\n"
            "[dim]A neon-lit labyrinth of forgotten secrets.[/dim]",
            border_style="magenta",
            padding=(1, 4),
        )
    )

    sleep(1)

    # Introduction Text
    intro_text = (
        "\n[bold white]The year is 2055. Neon veins pulse through the city's underbelly, "
        "and you're about to descend into the Cavern of Evil.[/bold white]\n"
        "Every step echoes a memory... but whose?\n"
    )
    slow_print(intro_text)

    sleep(1)

    # Command Prompt
    console.print(
        "\n[bold green]What will you do?[/bold green] (type 'help' for commands)"
    )
    user_input = input("> ")
    return user_input


def main():
    while True:
        action = intro_scene()
        if action.lower() in ["exit", "quit"]:
            console.print("[bold red]Exiting game...[/bold red]")
            break
        else:
            console.print(f"[bold yellow]You entered:[/bold yellow] {action}")
            sleep(1)


if __name__ == "__main__":
    main()
