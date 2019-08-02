"""The Slack bot commands dispatcher class.
"""

from typing import Dict, Coroutine, Any
import asyncio
import logging

import slack

class SlackbotDispatcher:
    """The SlackbotDispatcher class declaration.
    """

    def __init__(self, token: str) -> None:
        self.__stack: Dict[str, Coroutine[Dict[str, Any]]] = {}
        self.__loop: _WindowsSelectorEventLoop = asyncio.get_event_loop()
        self.__rtm_client: RTMClient = slack.RTMClient(
            token=token,
            run_async=True
        )


    def impl(
        self, 
        *, 
        command: str, 
        handler: Coroutine[Dict[str, Any]]
    ) -> None:
        if command in self.__stack.keys():
            raise SlackbotDispatcherStackKeyError(
                f'Command `{command}` already in the stack.'
            )

        self.__stack[command] = handler


    def run(self) -> None:
        self.__rtm_client.on('message', self.__dispatch)
        self.__loop.run_until_complete(self.__rtm_client.start())


    async def __dispatch(self, **kwargs: Dict[str, Any]) -> None:
        web_client: WebClient = kwargs['web_client']
        argv: List[str] = kwargs['data']['text'].split()
        self_id: str = (await web_client.api_call('auth.test')).data['user_id']

        if argv[0] == f'<@{self_id}>':
            kwargs['data']['argv'] = argv
            kwargs['data']['self_id'] = self_id

            try:
                await self.__stack[argv[1]](**kwargs)
            except IndexError:
                logging.debug(f'Index 1 out of argv bound.')
            except KeyError:
                logging.debug(f'Command `{argv[1]}` doesn\'t exists in stack.')


class SlackbotDispatcherStackKeyError(Exception):
    """The SlackbotDispatcher stack key error exception declaration.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
