"""One Word, First Thought — entry for make.fun.

Writes one word to /output/entry.txt.
The entry is exactly one word: the first word that comes to mind, nothing else.
"""
import os

LINE = "Serendipity"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
