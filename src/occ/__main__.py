import argparse
import random
import sys
import time
from importlib.metadata import version
from pathlib import Path

from occ.colors import Color, get_color
from occ.config import EXTENSIONS, FILES, LABELS, SUCCESSES, WARNINGS


def main() -> None:

    # This workaround because using argparse to add a new argument requires a positional argument to be passed
    # Something like 'occ -v <something>' for version to be displayed
    if len(sys.argv) == 2:
        if sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print(f"occ v{version('occ')} (optimistic)")
            return

    parser = argparse.ArgumentParser(
        description="The Optimistic Compiler Collection — because every program deserves to succeed"
    )
    parser.add_argument("-v", "--version", help="Display version")

    parser.add_argument("path", nargs="?", default="", help="Source file to compile")
    parser.add_argument(
        "-Wall",
        action="store_true",
        help="Show all warnings",
    )

    args = parser.parse_args()

    messages: list[tuple[str, str]] = []

    if args.path == "":
        messages = FILES["VOID"]
    else:
        suffix: str = Path(args.path).suffix
        ext = EXTENSIONS.get(suffix, "UNKNOWN")
        messages = FILES.get(ext, FILES["UNKNOWN"])

    warning_index = random.randint(1, len(messages) - 1)
    messages.insert(warning_index, (random.choice(LABELS), random.choice(WARNINGS)))

    if args.Wall:
        for _ in range(random.randint(1, 4)):
            warning_index = random.randint(1, len(messages) - 1)
            messages.insert(
                warning_index, (random.choice(LABELS), random.choice(WARNINGS))
            )

    for label, message in messages:
        color = get_color(label)
        print(f"{color}{label:<14} {message}{Color.RESET}")
        time.sleep(random.uniform(0.1, 0.6))

    print(f"{Color.GREEN}{random.choice(SUCCESSES)}{Color.RESET}")


if __name__ == "__main__":
    main()
