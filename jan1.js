#!/usr/bin/env python3
import os
import sys
import time
import random
import shutil
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ---------- UTIL ----------
def clear():
    # Clear screen using ANSI sequences (works well with colorama on Windows)
    print("\033[H\033[J", end="")

def slow_print(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ---------- ASCII ART ----------
HAPPY_NEW_YEAR = r"""
██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗
██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
███████║███████║██████╔╝██████╔╝ ╚████╔╝ 
██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝  
██║  ██║██║  ██║██║     ██║        ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝   

███╗   ██╗███████╗██╗    ██╗
████╗  ██║██╔════╝██║    ██║
██╔██╗ ██║█████╗  ██║ █╗ ██║
██║╚██╗██║██╔══╝  ██║███╗██║
██║ ╚████║███████╗╚███╔███╔╝
╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ 

██████╗  ██████╗ ██████╗ ██████╗
╚════██╗██╔═══██╗╚════██╗██╔═══╝
 █████╔╝██║   ██║ █████╔╝███████╗
██╔═══╝ ██║   ██║██╔═══╝ ██═══██║
███████╗╚██████╔╝███████╗███████║
╚══════╝ ╚═════╝ ╚══════╝╚══════╝
"""


COLORS = [
    Fore.RED, Fore.YELLOW, Fore.GREEN,
    Fore.CYAN, Fore.MAGENTA, Fore.BLUE
]

# ---------- FIREWORK ----------
def firework(width=60, height=20):
    # Ensure sensible bounds
    min_x = 10
    max_x = max(min_x, width - 10)
    x = random.randint(min_x, max_x)

    # Launch: a '|' that moves upward
    launch_steps = max(0, height - 5)
    for i in range(launch_steps):
        clear()
        # Print the rocket at a rising position
        print("\n" * (height - i) + " " * x + Fore.WHITE + "|")
        time.sleep(0.04)

    # Explosion: expanding circles
    for r in range(1, 8):
        clear()
        color = random.choice(COLORS)
        for dy in range(-r, r + 1):
            line_chars = []
            for dx in range(-r, r + 1):
                if dx * dx + dy * dy <= r * r:
                    # Add colored star and reset style after the star to avoid bleeding
                    line_chars.append(color + "*" + Style.RESET_ALL)
                else:
                    line_chars.append(" ")
            indent = max(0, x - r)
            print(" " * indent + "".join(line_chars))
        time.sleep(0.06)

# ---------- MAIN ----------
def main():
    try:
        clear()
        slow_print(Fore.CYAN + "✨ Loading New Year Celebration ✨", 0.05)
        time.sleep(1)

        clear()
        print(Fore.MAGENTA + HAPPY_NEW_YEAR)
        time.sleep(2)

        slow_print(Fore.YELLOW + "🎆 Let the fireworks begin! 🎆\n", 0.05)

        # Detect terminal size to make the animation adapt
        cols, rows = shutil.get_terminal_size(fallback=(80, 24))

        for _ in range(8):
            firework(width=cols, height=rows)
            time.sleep(0.25)

        clear()
        slow_print(Fore.GREEN + "🚀 2026 IS YOUR YEAR 🚀", 0.07)
        slow_print(Fore.CYAN + "Create. Iterate. Conquer.", 0.07)
        slow_print(Fore.MAGENTA + "Happy New Year 💫", 0.07)

    except KeyboardInterrupt:
        clear()
        print(Fore.RED + "\nAnimation interrupted. Happy New Year! 🎉")

if __name__ == "__main__":
    main()
