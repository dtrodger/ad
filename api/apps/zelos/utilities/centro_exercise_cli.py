from flask import current_app

from api.apps.zelos.utilities.centro_exercise import centro_exercise_2a


def cli_zelos_centro_2a():
    """
    CLI command function for running Centro exercise 2a.
    """

    current_app.logger.info('Running Zelos Centro exercise 2a')
    centro_exercise_2a()