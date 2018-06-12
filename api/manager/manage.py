#!/usr/bin/env python
import os

import click

from api.apps import create_app
from api.apps.extensions import mongodb
from api.apps.zelos.utilities.centro_exercise_cli import (
    cli_zelos_centro_2a
)
from api.apps.zelos.utilities.mongo_cli import (
    cli_bootstrap_db_zelos,
    cli_clear_db_zelos
)
from api.apps.zelos.utilities.tests_cli import (
    cli_tests_zelos,
    cli_tests_zelos_endpoints,
    cli_tests_zelos_middleware,
    cli_tests_zelos_models
)
from api.apps.utilities.mongo_cli import (
    cli_bootstrap_db,
    cli_clear_db
)
from api.apps.utilities.test_cli import (
    cli_test_api,
    cli_test_app_config,
    cli_test_apps
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
    cli_test_api()


@app.cli.command()
def test_app_config():
    """Test application configuration"""
    cli_test_app_config()


@app.cli.command()
def test_apps_config():
    """Test all Apps"""
    cli_test_apps()


@app.cli.command()
def test_zelos():
    """Test Zelos"""
    cli_tests_zelos()


@app.cli.command()
def test_zelos_endpoints():
    """Test Zelos endpoints"""
    cli_tests_zelos_endpoints()


@app.cli.command()
def test_zelos_middleware():
    """Test Zelos middleware"""
    cli_tests_zelos_middleware()


@app.cli.command()
def test_zelos_models():
    """Test Zelos models"""
    cli_tests_zelos_models()


# DB Operations
@app.cli.command()
def db_bootstrap():
    """Bootstraps API db"""
    cli_bootstrap_db()


@app.cli.command()
def db_bootstrap_zelos():
    """Bootstraps Zelos db"""
    cli_bootstrap_db_zelos()


@app.cli.command()
def db_drop():
    """Clears API db"""
    cli_clear_db()


@app.cli.command()
def db_drop_zelos():
    """Clears Zelos db"""
    cli_clear_db_zelos()


# Centro exercises
@app.cli.command()
def zelos_centro_2a():
    """Runs Centro exercise 2a"""
    cli_zelos_centro_2a()
