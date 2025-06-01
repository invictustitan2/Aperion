#!/usr/bin/env python3

from commands import parse_command

from rooms import cavern_entrance
from utils.display import slow_print


def main():
    slow_print("Welcome to Cavern of Evil: 2055!", 0.05)
    current_room = cavern_entrance
    while True:
        current_room.enter()
        user_input = input("> ")
        verb, obj = parse_command(user_input)

        if verb in ["exit", "quit"]:
            print("Exiting game...")
            break
        elif verb == "unknown":
            print("I don’t understand that command.")
        else:
            # Placeholder for actual room command handling
            print(f"[DEBUG] Recognized Command: {verb}, Object: {obj}")


if __name__ == "__main__":
    main()
