from flask import current_app

from api.apps.zelos.utilities.mock_data import bootstrap_centro_exersize_data, drop_zelos_collections


def cli_bootstrap_db_zelos():
    """
    CLI command function for running Zelos bootstrap functions.
    """

    current_app.logger.info('Running Zelos bootstrap db')
    bootstrap_centro_exersize_data()


def cli_clear_db_zelos():
    """
    CLI command function for clearing Zelos db.
    """

    current_app.logger.info('Running Zelos clear db')
    drop_zelos_collections()
