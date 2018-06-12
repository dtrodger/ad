import unittest

from flask import current_app


def cli_tests_narcissus_middleware():
    """
    CLI command function for running Narcissus middleware tests.
    """

    current_app.logger.info('Running Narcissus model tests.')
    tests = unittest.TestLoader().discover('api.apps.narcissus.middleware.tests')
    unittest.TextTestRunner().run(tests)


def cli_tests_narcissus_models():
    """
    CLI command function for running Narcissus model tests.
    """

    current_app.logger.info('Running Narcissus model tests.')
    tests = unittest.TestLoader().discover('api.apps.narcissus.models.tests')
    unittest.TextTestRunner().run(tests)


def cli_tests_narcissus():
    """
    CLI command function for running all Narcissus.
    """

    current_app.logger.info('Running Narcissus tests.')
    cli_tests_narcissus_middleware()
    cli_tests_narcissus_models()
