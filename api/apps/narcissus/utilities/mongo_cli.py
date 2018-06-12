from flask import current_app

from api.apps.narcissus.utilities.mock_data import bootstrap_centro_exersize_data, drop_narcissus_collections


def cli_bootstrap_db_narcissus():
    """
    CLI command function for running Narcissus bootstrap functions.
    """

    current_app.logger.info('Running Narcissus bootstrap db')
    bootstrap_centro_exersize_data()


def cli_clear_db_narcissus():
    """
    CLI command function for clearing Narcissus db.
    """

    current_app.logger.info('Running Narcissus clear db')
    drop_narcissus_collections()
