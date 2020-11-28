# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import sys

from flask import Flask, render_template

from challenge import models, views
from challenge.extensions import (
    csrf_protect,
    db,
    flask_static_digest,
    login_manager,
    migrate,
)


def create_app(config_object="challenge.config", testing=False, cli=False):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask("challenge")
    app.config.from_object(config_object)

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app, cli)
    register_blueprints(app)
    register_shellcontext(app)
    register_errorhandlers(app)
    configure_logger(app)
    return app


def configure_extensions(app, cli):
    """Register Flask extensions."""
    csrf_protect.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    flask_static_digest.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(views.blueprint)


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db, "User": models.User}

    app.shell_context_processor(shell_context)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
