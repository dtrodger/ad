#!/usr/bin/env python
import os

import click

from api.apps import create_app
from api.apps.extensions import mongodb
from api.apps.narcissus.utilities.mongo_cli import (
    cli_bootstrap_db_narcissus,
    cli_clear_db_narcissus
)
from api.apps.narcissus.utilities.tests_cli import (
    cli_tests_narcissus,
    cli_tests_narcissus_middleware,
    cli_tests_narcissus_models
)
from api.apps.utilities.mongo_cli import (
    cli_bootstrap_db,
    cli_clear_db
)

# Initialize Flask object.
app = create_app(os.getenv('CENTRO_FLASK_CONFIG') or 'develop')


# Shell context.
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, mongo=mongodb)


# Unit tests.
@app.cli.command()
def test_api():
    """Test API"""
    cli_tests_narcissus()


@app.cli.command()
def test_narcissus():
    """Test Narcissus"""
    cli_tests_narcissus()


@app.cli.command()
def test_narcissus_middleware():
    """Test Narcissus middleware"""
    cli_tests_narcissus_middleware()


@app.cli.command()
def test_narcissus_models():
    """Test Narcissus models"""
    cli_tests_narcissus_models()


# DB Operations
@app.cli.command()
def db_bootstrap():
    """Bootstraps API db"""
    cli_bootstrap_db()


@app.cli.command()
def db_bootstrap_narcissus():
    """Bootstraps Narcissus db"""
    cli_bootstrap_db_narcissus()


@app.cli.command()
def db_drop():
    """Clears API db"""
    cli_clear_db()


@app.cli.command()
def db_drop_narcissus():
    """Clears Narcissus db"""
    cli_clear_db_narcissus()
