import unittest

from flask import current_app


def cli_tests_zelos_endpoints():
    """
    CLI command function for running Zelos endpoint tests.
    """

    current_app.logger.info('Running Narcissus endpoint tests')
    tests = unittest.TestLoader().discover('api.apps.zelos.endpoints.tests')
    unittest.TextTestRunner().run(tests)


def cli_tests_zelos_middleware():
    """
    CLI command function for running Zelos middleware tests.
    """

    current_app.logger.info('Running Zelos model tests')
    tests = unittest.TestLoader().discover('api.apps.zelos.middleware.tests')
    unittest.TextTestRunner().run(tests)


def cli_tests_zelos_models():
    """
    CLI command function for running Zelos model tests.
    """

    current_app.logger.info('Running Zelos model tests')
    tests = unittest.TestLoader().discover('api.apps.zelos.models.tests')
    unittest.TextTestRunner().run(tests)


def cli_tests_zelos():
    """
    CLI command function for running all Zelos.
    """

    current_app.logger.info('Running Zelos tests')
    cli_tests_zelos_endpoints()
    cli_tests_zelos_middleware()
    cli_tests_zelos_models()
