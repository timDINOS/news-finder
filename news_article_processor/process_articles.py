import flask
from _init_ import app
from request import search
from scraper import verify_articles
from  import accounts

def validate_query(query):
    if len(query) == 0 or query is None:
        return False
    return True

def find_cached_results(query):
    accounts.find()
    pass

@app.route("/articles/access", methods=["GET"])
def search_and_process_articles(query, network=None):
    processed_articles = []
    if not validate_query(query):
        flask.abort(404)
    res = find_cached_results(query)
    if len(res) == 0 or res is None:
        all_articles = search(query)
        processed_articles = verify_articles(all_articles, network)
    else:
        processed_articles = res
    return flask.jsonify(processed_articles)
