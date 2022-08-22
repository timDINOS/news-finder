from bs4 import BeautifulSoup
import json
from newspaper import Article
import nltk
nltk.download('punkt')

def parse_article(article):
    article_obj = Article(article["link"])

    article_obj.download()

    article_obj.parse()

    article_obj.nlp()

    news_article = {}

    news_article["source"] = article_obj.brand

    news_article["authors"] = article_obj.authors

    news_article["keywords"] = article_obj.keywords

    news_article["summary"] = article_obj.summary

    news_article["text"] = article_obj.text
    
    news_article["images"] = article_obj.images

    news_article["movies"] = article_obj.movies

    return news_article




def verify_articles(articles, network=None):
    limited = False if network is None else True
    full_articles = []
    for article in articles:
        if limited:
            if article["source"] == network:
                full_articles.append(parse_article(article))
        else:
            full_articles.append(parse_article(article))
    return full_articles
