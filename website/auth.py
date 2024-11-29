from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", boolean=True)


@auth.route("/logout")
def logout():
    return "<p>Logout<p>"


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("email must be greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("fiirst name must be greater than 3 characters.", category="error")
        elif password1 != password2:
            flash("password dont match.", category="error")
        elif len(password1) < 5:
            flash("password must be at least 5 characters.", category="error")
        else:
            flash("account created", category="success")

    return render_template("signUp.html")
