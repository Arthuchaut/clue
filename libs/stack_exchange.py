"""The StackExchange class declaration.
"""

import json
from typing import Dict, Any

import requests

from config.custom_type import Response

class StackExchange:
    """The stack exchange api class declaration.
    """

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
        """Requests to the search method's Stack Exchnage API.

        Args:
            order (str, optional): The response order ('asc' or 'desc').
                Defaults to 'desc'.
            sort (str, optional): The sorting value.
                Accepted:
                    - 'activity'
                    - 'votes'
                    - 'creation'
                    - 'relevance'
            q (str): The query string of the search.
            tagged (str): The context of searching.
            site (str): The site to request.

        Returns:
            Dict[str, Any]: The HTTP request JSON parsed body.

        Raises:
             StackExchangeResponseError:
                If the HTTP reponse code if not in 200 values.
        """

        params: str = cls.__parse_params(
            order=order,
            sort=sort,
            q=q,
            tagged=tagged,
            site=site
        )
        uri: str = f'{cls.__URL}/{cls.__VERSION}/search/advanced?{params}'

        res: Response = requests.get(uri)

        if res.status_code < 200 or res.status_code >= 300:
            raise StackExchangeResponseError(
                f'Bad HTTP response with a status code {res.status_code}'
            )

        return json.loads(res.text)


    @classmethod
    def api_questions_answers(
        cls,
        *,
        question_id: int,
        order: str = 'desc',
        sort: str = None,
        filter: str = None,
        site: str = 'stackoverflow'
    ) -> Dict[str, Any]:
        """Requests to the questions/{id}/anwsers method's Stack Exchnage API.

        Args:
            question_id (int): The question id.
            order (str, optional): The response order ('asc' or 'desc').
                Defaults to 'desc'.
            sort (str, optional): The sorting value.
                Accepted:
                    - 'activity'
                    - 'votes'
                    - 'creation'
                    - 'relevance'
            filter (str): The formatted string of filter.
            site (str): The site to request.

        Returns:
            Dict[str, Any]: The HTTP request JSON parsed body.

        Raises:
             StackExchangeResponseError:
                If the HTTP reponse code if not in 200 values.
        """

        params: str = cls.__parse_params(
            question_id=question_id,
            order=order,
            sort=sort,
            filter=filter,
            site=site
        )
        uri: str = (
            f'{cls.__URL}/{cls.__VERSION}'
            f'/questions/{question_id}/answers?{params}'
        )

        res: Response = requests.get(uri)

        if res.status_code < 200 or res.status_code >= 300:
            raise StackExchangeResponseError(
                f'Bad HTTP response with a status code {res.status_code}'
            )

        return json.loads(res.text)


    @classmethod
    def __parse_params(cls, **params) -> str:
        """The GET HTTP parameters parser.

        Get a Dictionnary and parse it to an str
        correct GET HTTP parameters.

        Args:
            **kwargs (Dict[str, Any]): The dictionnary parameter to format.

        Returns:
            str: THe GET HTTTP parameters format.
        """

        fmt: str = ''

        for attr_key, attr_val in params.items():
            if attr_val is not None:
                fmt += f'{attr_key}={attr_val}&'

        return fmt[:-1]


class StackExchangeResponseError(Exception):
    """The StackExchange HTTP response exception declaration.
    """

    def __init__(self, message: str) -> None:
        """The StackExchangeResponseError constructor.
        """

        super().__init__(message)
