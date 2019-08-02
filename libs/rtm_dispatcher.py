"""The Slack bot commands dispatcher class.
"""

from typing import Dict, List, Awaitable, Any
import asyncio
import logging

import slack

from config.custom_type import (
    _WindowsSelectorEventLoop,
    RTMClient,
    WebClient
)

class RTMDispatcher:
    """The SlackbotRTMDispatcher class declaration.
    """

    def __init__(self, token: str) -> None:
        """The RTMDispatcher constructor.
        """

        self.__stack: Dict[str, Awaitable[Dict[str, Any]]] = {}
        self.__loop: _WindowsSelectorEventLoop = asyncio.get_event_loop()
        self.__rtm_client: RTMClient = slack.RTMClient(
            token=token,
            run_async=True
        )


    def impl(
        self,
        *,
        command: str,
        task: Awaitable[Dict[str, Any]]
    ) -> None:
        """The task staking method.

        Create a new task associated with a specific command.
        When the command is sent from the slack emitter,
        the task will be called.

        Args:
            command (str): The command to listen.
            task (Awaitable[Dict[str, Any]]): The task to call.

        Raises:
            RTMDispatcherStackKeyError:
                If the command is already in the stack.
        """

        if command in self.__stack.keys():
            raise RTMDispatcherStackKeyError(
                f'Command `{command}` already in the stack.'
            )

        self.__stack[command] = task


    def run(self) -> None:
        """Run the RTM Slack API asynchronously and listen for messages.

        When a message event is catched, this method dispatch it.
        """

        slack.RTMClient.on(event='message', callback=self.__dispatch)
        self.__loop.run_until_complete(self.__rtm_client.start())


    async def __dispatch(self, **kwargs: Dict[str, Any]) -> None:
        """The handler of the RTM message event.

        Test if the first word is the bot mention.
        If the test pass, the dispatcher call the Awaitable
        associated with it.

        Args:
            **kwargs (Dict[str, Any]): The data sent
                from the RTM event handler.
                It contains these following parameters:

                data (Dict[str, Any]): The data mapping from the RTM.
                    channel (str): The emitter channel id.
                    client_msg_id (str): The emitter message id.
                    event_ts (str): The emitter thread ts id.
                    source_team (str): The emitter source team id.
                    suppress_notification (bool): A boolean which specify
                        if the emitter notification are enabled or not.
                    team (str): The emitter team id.
                    text (str): The emitter message.
                    ts (str): The emitter thread ts id.
                    user (str): The emitter id.
                    user_team (str): the emitter team id.
                rtm_client (RTMClient): The RTMClient websocket pipe.
                web_client (WebClient): The WebClient Slack API.
        """

        web_client: WebClient = kwargs['web_client']
        argv: List[str] = kwargs['data']['text'].split()
        self_id: str = (await web_client.api_call('auth.test')).data['user_id']

        if argv[0] == f'<@{self_id}>':
            kwargs['data']['argv'] = argv
            kwargs['data']['self_id'] = self_id

            command: str = argv[1] if len(argv) > 1 else None

            try:
                await self.__stack[command](**kwargs)
            except KeyError:
                logging.debug(f'Command `{command}` doesn\'t exists in stack.')


class RTMDispatcherStackKeyError(Exception):
    """The SlackbotDispatcher stack key error exception declaration.
    """

    def __init__(self, message: str) -> None:
        """The RTMDispatcherStackKeyError constructor.
        """

        super().__init__(message)
