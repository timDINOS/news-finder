from database.db_init import accounts
import flask
import hashlib
import uuid
import re

def verify_name(name):
    return len(name) > 0 and all(char.isalpha() for char in name)

def verify_email(email):
    email_pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    return re.match(email_pattern, email)

def verify_username(username):
    results = accounts.find_one({"username": username})
    return len(username) > 0 and username is not None and results is None

def verify_password(password):
    special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return len(password) > 0 and len(password) <= 20 and any(char.isDigit() for char in password) and any(char.isDigit() for char in password) and special.search(password) is not None

def matches(password, repeated_password):
    return password == repeated_password

def encrypt_password(password):
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string

def register_handler(user):
    if "username" in flask.sessions or verify_name(user.name) or verify_email(user.email) or verify_username(user.username) or verify_password(user.password) or matches(user.password, user.repeated_password):
        return flask.abort(500)
    new_password = encrypt_password(user.password)
    new_user = {
        "name": user.name,
        "email": user.email,
        "username": user.username,
        "password": new_password,
        "queries": []
    }
    accounts.insert_one(new_user)
    flask.sessions["username"] = user.username
    return flask.redirect()