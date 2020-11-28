# -*- coding: utf-8 -*-
"""Views, that's right, all of them."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

from challenge.extensions import login_manager
from challenge.forms import LoginForm
from challenge.models import User
from challenge.utils import flash_errors

blueprint = Blueprint("views", __name__)


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get_or_404(user_id)


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    login_form = LoginForm(request.form)
    # Handle logging in
    if request.method == "POST":
        if login_form.validate_on_submit():
            login_user(login_form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("views.users")
            return redirect(redirect_url)
        else:
            flash_errors(login_form)
    return render_template("home.html", login_form=login_form)


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("views.home"))


@blueprint.route("/users/")
def users():
    """Get a list of users."""
    return render_template("users.html", users=User.query.all())
