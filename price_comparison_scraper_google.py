import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    """Return the source code for the provided URL. 
    Args: 
        url (string): URL of the page to scrape.
    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)

def get_results(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    
    return response

def parse_results(response):
    
    css_identifier_results = ".yuRUbf"
    search_link = "a"

    results = response.html.find(css_identifier_results)
    output = []

    for result in results:
        link = result.find(search_link, first=True).attrs['href']
        prices = {
            'Link' : link,
        }       
        output.append(prices)

    return output


def google_search(query, source=''):
    final_query = query + ' ' + source
    response = get_results(final_query)
    return parse_results(response)


queries = ['jabra elite 75t', 'sony wh-1000xm5', 'bose quietcomfort 45']

for query in queries:
    results = {
                "Purchase Links": google_search(query, 'for sale'),
            }

    print(results)