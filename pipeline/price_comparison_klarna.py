import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}

def get_source(url):
    """Return the source code for the provided URL. 
    Args: 
        url (string): URL of the page to scrape.
    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        print(e)

def get_results(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.klarna.com/us/shopping/results/?q=" + query)
    
    return response

def parse_results(response):
    
    css_identifier_results = ".k6oEmfY83J a"
    # search_link = "a"

    result = response.html.find(css_identifier_results, first=True).attrs['href']

    # link = results.find(search_link, first=True).attrs['href']
    prices = 'https://www.klarna.com' + result
    time.sleep(5)

    return prices


def google_search(query):
    response = get_results(query)
    return parse_results(response)


queries = ['jabra elite 75t', 'sony wh-1000xm5', 'bose quietcomfort 45']

results = []
for query in queries:
    results.append(google_search(query))

print(results)

