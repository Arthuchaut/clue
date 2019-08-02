"""The main file of the project.

It contains the main function for lauching the Slack bot.
"""

import logging

from config.configure import CONFIG
from libs.rtm_dispatcher import RTMDispatcher
from tasks import (
    task_print_usage,
    task_search,
)

def main() -> int:
    """The entry point of the project.
    """

    rtm: RTMDispatcher = RTMDispatcher(CONFIG['api']['slack']['token'])

    rtm.impl(command=None, task=task_print_usage.task_print_usage)
    rtm.impl(command='help', task=task_print_usage.task_print_usage)
    rtm.impl(command='search', task=task_search.task_search)

    rtm.run()

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
