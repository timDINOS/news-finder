from database.db_init import accounts
import flask
import hashlib
import uuid

def encrypt_password(password):
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string

def login_handler(username, password):
    user_account = accounts.find_one({'username': username})
    if "username" in flask.session or user_account is None:
        return flask.abort(500)
    if password != encrypt_password(password):
        return flask.abort(500)
    flask.sessions["username"] = username
    return flask.redirect()