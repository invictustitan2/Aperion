from rich.console import Console
from time import sleep

console = Console()

def slow_print(text, delay=0.05):
    for char in text:
        console.print(char, end='', style="bold cyan")
        sleep(delay)
    console.print("")