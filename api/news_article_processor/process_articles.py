import flask
from api._init_ import app
from request import search
from scraper import verify_articles
from  ..database.db_init import accounts

def validate_query(query):
    if len(query) == 0 or query is None:
        return False
    return True

def find_cached_results(user, query):
    user_account = accounts.find({"username": user})
    results = []
    for q in user_account.queries:
        if q.query == query:
            results = q.query.results
    return results

def create_results_entry(user, query, articles):
    index = 0
    all_queries = accounts.find({'username': user})
    for q in all_queries.queries:
        if q.query == query:
            break
        index = index + 1
    if index == len(all_queries.queries):
        return flask.abort(500)
    accounts.update_one({
        'username': user,
        'queries.query': all_queries.queries[index].query
    }, 
    {
        '$set': {
            'queries.$.results': articles
        }
    })

@app.route("/articles/access", methods=["GET"])
def search_and_process_articles(query, network=None):
    processed_articles = []
    if not validate_query(query):
        flask.abort(404)
    res = find_cached_results(flask.session['username'], query)
    if len(res) == 0 or res is None:
        all_articles = search(query)
        processed_articles = verify_articles(all_articles, network)
        create_results_entry(flask.session['username'], query, processed_articles)
    else:
        processed_articles = res
    return flask.jsonify(processed_articles), 200
