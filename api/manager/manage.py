#!/usr/bin/env python
import os

import click

from api.apps import create_app
from api.apps.extensions import mongodb
from api.apps.narcissus.utilities.tests_cli import (
    cli_tests_narcissus,
    cli_tests_narcissus_models
)

# Initialize Flask object.
app = create_app(os.getenv('CENTRO_FLASK_CONFIG') or 'develop')


# Shell context.
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, mongo=mongodb)


# Unit tests.
@app.cli.command()
def test_narcissus():
    """Test Narcissus models"""
    cli_tests_narcissus()


@app.cli.command()
def test_narcissus_models():
    """Test Narcissus models"""
    cli_tests_narcissus_models()
