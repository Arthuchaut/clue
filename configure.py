"""This is the app configurator file.

It import the config file and setup the logger.
"""

from typing import Dict, Any

import yaml

CONFIG: Dict[str, Any] = yaml.safe_load(open('config.yml', 'r'))

def init_app() -> None:
    """The application configuration initializer.

    - Configure the logger options
    """

    import logging

    from logging import (
        Logger,
        StreamHandler,
        FileHandler,
        Formatter
    )

    logger: Logger = logging.getLogger()
    formatter: Formatter = Formatter(CONFIG['logger']['formatter'])
    logger.setLevel(getattr(logging, CONFIG['logger']['file_level']))

    if CONFIG['logger']['console_handler']:
        console_handler: StreamHandler = StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(
            getattr(logging, CONFIG['logger']['console_level'])
        )
        logger.addHandler(console_handler)

    if CONFIG['logger']['file_handler']:
        file_handler: FileHandler = FileHandler(
            CONFIG['logger']['file_name'],
            'a'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
