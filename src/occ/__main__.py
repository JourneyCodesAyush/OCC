import argparse
import random
import time
from pathlib import Path

from occ.config import EXTENSIONS, FILES, SUCCESSES


def main() -> None:
    parser = argparse.ArgumentParser(
        description="The Optimistic Compiler Collection — because every program deserves to succeed"
    )

    parser.add_argument("path", nargs="?", default="", help="Source file to compile")
    parser.add_argument("--verbose", action="store_true", help="Show verbose output")

    args = parser.parse_args()

    messages: list[tuple[str, str]] = []

    if args.path == "":
        messages = FILES["VOID"]
    else:
        suffix: str = Path(args.path).suffix
        ext = EXTENSIONS.get(suffix, "UNKNOWN")
        messages = FILES.get(ext, FILES["UNKNOWN"])

    for label, message in messages:
        print(f"{label:<14} {message}")
        time.sleep(random.uniform(0.1, 0.6))

    print(random.choice(SUCCESSES))


if __name__ == "__main__":
    main()
