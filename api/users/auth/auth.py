from api._init_ import app
from login import login_handler
from logout import logout_handler
from register import register_handler
import flask 

@app.route("/users/auth/register", methods=["POST"])
def register():
    user = {
        flask.request.form["name"],
        flask.request.form["email"],
        flask.request.form["username"],
        flask.request.form["password"],
        flask.request.form["repeated_password"]
    }
    return register_handler(user), 202
    

@app.route("/users/auth/login", methods=["POST"])
def login():
    return login_handler(flask.request.form["username"], flask.request.form["password"]), 202

@app.route("/users/auth/logout", methods=["POST"])
def logout():
    return logout_handler(flask.request.args.get("username")), 202



