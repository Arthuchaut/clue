"""Task for print the bot usage.
"""

from typing import Dict, Any

from config.custom_type import WebClient

async def task_print_usage(**kwargs: Dict[str, Any]) -> None:
    """Print bot usage for the emitter.

    Args:
        **kwargs (Dict[str, Any]): The data mapping sent from the dispatcher.
    """

    web_client: WebClient = kwargs['web_client']
    usage: str = '```' + \
                 'Command                                    Description\n\n' + \
                 'help, [NULL]                               Print usage\n' + \
                 'search <lang> <problem description>        Clue try to figure out your problem' + \
                 '```'

    await web_client.chat_postMessage(
        channel=kwargs['data']['channel'],
        text=usage,
        mrkdwn=True
    )
