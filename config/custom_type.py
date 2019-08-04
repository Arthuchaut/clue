"""Here we implement your custom types.
"""

from typing import NewType
import asyncio
import sys

import slack
import requests

if sys.platform == 'win32':
    EventLoop = NewType(
        'EventLoop',
        asyncio.windows_events._WindowsSelectorEventLoop
    )
else:
    EventLoop = NewType(
        'EventLoop',
        asyncio.unix_events._UnixSelectorEventLoop
    )
    

RTMClient = NewType('RTMClient', slack.RTMClient)
WebClient = NewType('WebClient', slack.WebClient)
Response = NewType('Response', requests.models.Response)
