from flask import current_app

from api.apps.zelos.utilities.mongo_cli import (
    cli_bootstrap_db_zelos,
    cli_clear_db_zelos
)


def cli_bootstrap_db():
    """
    CLI command function for running apps bootstrap functions.
    """

    current_app.logger.info('Running API bootstrap db')
    cli_bootstrap_db_zelos()


def cli_clear_db():
    """
    CLI command function for clearing apps db.
    """

    current_app.logger.info('Running API clear db')
    cli_clear_db_zelos()
