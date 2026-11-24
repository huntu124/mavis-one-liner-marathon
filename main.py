"""One-line entry for One-Liner Marathon: writes the line the judge reads to /output/entry.txt."""

import os

LINE = (
    "My agent finished the to-do list, then wrote a longer one so I'd never discover what free time feels like."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
