"""The StackExchange class declaration.
"""

import json
from typing import Dict, Any

import requests

class StackExchange:
    __URL: str = 'https://api.stackexchange.com'
    __VERSION: str = '2.2'

    @classmethod
    def api_search(
        cls,
        *,
        order: str = 'desc',
        sort: str = None,
        q: str,
        tagged: str,
        site: str = 'stackoverflow'
    ) -> Dict[str, Any]:
        params: str = cls.__parse_params(
            order=order,
            sort=sort,
            q=q,
            tagged=tagged,
            site=site
        )
        uri: str = f'{cls.__URL}/{cls.__VERSION}/search/advanced?{params}'

        return uri


    @classmethod
    def __parse_params(cls, **params) -> str:
        fmt: str = ''

        for attr_key, attr_val in params.items():
            if attr_val is not None:
                fmt += f'{attr_key}={attr_val}&'

        return fmt[-1]

# order=desc&sort=votes&q=null%20pointer%20exception&tagged=java&site=stackoverflow
