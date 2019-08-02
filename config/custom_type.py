"""Here we implement your custom types.
"""

from typing import NewType
import asyncio

import slack

_WindowsSelectorEventLoop = NewType(
    '_WindowsSelectorEventLoop',
    asyncio.windows_events._WindowsSelectorEventLoop
)

RTMClient = NewType('RTMClient', slack.RTMClient)
WebClient = NewType('WebClient', slack.WebClient)
