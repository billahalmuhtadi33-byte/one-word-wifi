#!/usr/bin/env python3
"""One Word for Your Wi-Fi: Peekaboo.

Wi-Fi at home plays peekaboo - now you see it, now you don't.
Writes exactly one word to /output/entry.txt.
"""
import os

WORD = "Peekaboo"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)

if __name__ == "__main__":
    main()
