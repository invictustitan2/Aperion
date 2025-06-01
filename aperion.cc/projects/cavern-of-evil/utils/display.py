from time import sleep

from rich.console import Console

console = Console()


def slow_print(text, delay=0.05):
    for char in text:
        console.print(char, end="", style="bold cyan")
        sleep(delay)
    console.print("")
