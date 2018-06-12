from flask import current_app

from api.apps.narcissus.utilities.mongo_cli import (
    cli_bootstrap_db_narcissus,
    cli_clear_db_narcissus
)


def cli_bootstrap_db():
    """
    CLI command function for running Narcissus bootstrap functions.
    """

    current_app.logger.info('Running API bootstrap db')
    cli_bootstrap_db_narcissus()


def cli_clear_db():
    """
    CLI command function for clearing Narcissus db.
    """

    current_app.logger.info('Running API clear db')
    cli_clear_db_narcissus()
