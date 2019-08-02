"""The main file of the project.

It contains the main function for lauching the Slack bot.
"""

from configure import (
    init_app,
    CONFIG
)

def main() -> int:
    """The entry point of the project.
    """

    init_app()

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
