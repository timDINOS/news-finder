import flask

def logout_handler():
    flask.session.clear()
    return flask.redirect()