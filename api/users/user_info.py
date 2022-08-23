import flask
from api._init_ import app
from database.db_init import accounts

@app.route('/users/searches', methods=["GET"])
def get_nth_recent_queries():
    if "username" in flask.sessions:
        return flask.abort(500)
    user = accounts.find_one({'username': flask.sessions["username"]})
    all_searches = []
    for search in user.queries:
        all_searches.append(search)
    all_searches.reverse()
    return flask.jsonify(all_searches[0:flask.request.args.get("n")]), 200

@app.route('/users/results', methods=["GET"])
def get_search_results():
    if "username" in flask.sessions:
        return flask.abort(500)
    query = flask.request.args.get("query")
    user = accounts.find_one({'username': flask.sessions["username"]})
    results = []
    for q in user.queries:
        if q.query == query:
            results = q.results
    if len(results) == 0:
        return flask.abort(500)
    return flask.jsonify(results), 200
