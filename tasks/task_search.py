"""Task for search solutions about a given technical problem the bot usage.
"""

import logging
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
    response: str = None
    usage: str = '```Usage: search <lang> <problem description>```'
    error: str = 'Sorry, no response found ' + \
                 'for your question... :confused:'

    if len(argv) < 4:
        response = usage
    else:
        tag: str = argv[2]
        description: str = '%20'.join(argv[3:])
        
        res: Dict[str, Any] = StackExchange.api_search(
            sort='votes',
            q=description,
            tagged=tag
        )

        try:
            question_id: int = res['items'][0]['question_id']
        except (KeyError, IndexError):
            response = error
        else:
            res: Dict[str, Any] = StackExchange.api_questions_answers(
                question_id=question_id,
                sort='votes',
                filter='!9Z(-wzftf'
            )

            try:
                response = res['items'][0]['body_markdown']
            except (KeyError, IndexError):
                response = error

    await web_client.chat_postMessage(
        channel=kwargs['data']['channel'],
        text=response,
        mrkdwn=False
    )
