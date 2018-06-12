import unittest

from flask import current_app

from api.apps.narcissus.utilities.tests_cli import cli_tests_narcissus


def cli_test_api():
    """
    CLI command function for running all Api tests.
    """
    current_app.logger.info('Running all Api tests')

    cli_test_app_config()
    cli_tests_narcissus()


def cli_test_apps():
    """
    CLI command function for running all App tests.
    """
    current_app.logger.info('Running all App tests')

    cli_tests_narcissus()


def cli_test_app_config():
    """
    Finds and runs Flask application configuration tests.
    """
    current_app.logger.info('Running application configuration tests')

    # Find tests.
    tests = unittest.TestLoader().discover('apps.tests')

    # Run rests.
    unittest.TextTestRunner().run(tests)