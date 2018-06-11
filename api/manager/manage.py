#!/usr/bin/env python
import os

import click

from api.apps import create_app
from api.apps.extensions import mongodb

# Initialize Flask object.
app = create_app(os.getenv('SHIFTGIG_FLASK_CONFIG') or 'develop')


# Shell context.
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, mongo=mongodb)
