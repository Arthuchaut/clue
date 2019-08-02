"""The main file of the project.

It contains the main function for lauching the Slack bot.
"""

import logging

from config.configure import CONFIG
from libs.rtm_dispatcher import RTMDispatcher

def main() -> int:
    """The entry point of the project.
    """

    print(CONFIG)

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
