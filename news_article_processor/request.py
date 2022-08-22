import requests
from serpapi import GoogleSearch
import os

def search_article(query):
    search_parameters = {
        "q": query,
        "tbm": "nws",
        "api_key": os.environ['SEARCH_API_KEY']
    }

    search = GoogleSearch(search_parameters)
    search_results = search.get_dict()
    articles = search_results["news_results"]
    return articles

def search(query):
    return search_article(query)