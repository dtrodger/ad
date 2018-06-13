from flask import current_app

from api.apps.zelos.utilities.centro_exercise import (
    centro_exercise_2a,
    centro_exercise_2b
)


def cli_zelos_centro_2a():
    """
    CLI command function for running Centro exercise 2a.
    """

    current_app.logger.info('Running Zelos Centro exercise 2a')
    imprs_costs = centro_exercise_2a()

    for imprs_cost in imprs_costs:
        print imprs_cost


def cli_zelos_centro_2b(d_start, d_end):
    """
    CLI command function for running Centro exercise 2b.
    """
    current_app.logger.info('Running Zelos Centro exercise 2b')
    imprs_cost = centro_exercise_2b(d_start, d_end)
    print imprs_cost
