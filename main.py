"""The main file of the project.

It contains the main function for lauching the Slack bot.
"""

from typing import Dict, Awaitable

from config.configure import CONFIG
from libs.rtm_dispatcher import RTMDispatcher
from tasks import (
    task_print_usage,
    task_search
)

def main() -> int:
    """The entry point of the project.
    """

    tasks: Dict[str, Awaitable] = {
        None: task_print_usage.task_print_usage,
        'help': task_print_usage.task_print_usage,
        'search': task_search.task_search
    }

    rtm: RTMDispatcher = RTMDispatcher(CONFIG['api']['slack']['token'])

    for attr_key, attr_val in tasks.items():
        rtm.impl(command=attr_key, task=attr_val)

    rtm.run()

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
