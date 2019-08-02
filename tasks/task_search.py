"""Task for search solutions about a given technical problem the bot usage.
"""

from typing import Dict, List, Any

from config.custom_type import WebClient
from libs.stack_exchange import StackExchange

async def task_search(**kwargs: Dict[str, Any]) -> None:
    """Print bot usage for the emitter.

    Args:
        **kwargs (Dict[str, Any]): The data mapping sent from the dispatcher.
    """

    web_client: WebClient = kwargs['web_client']
    argv: List[str] = kwargs['data']['argv']
    usage: str = '```Usage: search <lang> <problem description>```'
    response: str = None

    if len(argv) < 4:
        response = usage
    else:
        tag: str = argv[2]
        description: str = '%20'.join(argv[3:])
        
        response = StackExchange.api_search(
            sort='votes',
            q=description,
            tagged=tag
        )

    await web_client.chat_postMessage(
        channel=kwargs['data']['channel'],
        text=response,
        mrkdwn=False
    )
