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
    response = get_source("https://www.google.com/search?tbm=shop&hl=en&psb=1&ved=0CAAQvOkFahcKEwj4lfLEmsv9AhUAAAAAHQAAAAAQJQ&q=" + query)
    
    return response

def parse_results(response):
    
    css_identifier_results = ".i0X6df"
    css_identifier_link = "span a"
    css_identifier_test_2 = ".Ldx8hd a span"

    product_results = response.html.find(css_identifier_results)

    output = {}
    link_count = 0

    ### For Loop Below loops through queries to find Shopping Link and Integer Representing Amounnt of Stores that are linked to that product ###

    for product_result in product_results:
        product_link = 'https://www.google.com' + product_result.find(css_identifier_link, first=True).attrs['href']
        product_compare = product_result.find(css_identifier_test_2, first=True)
        if product_compare:
            product_compare = product_compare.text
            if product_compare.endswith('+'):
                product_compare = product_compare[:-1]

            if link_count < 1:
                output[f'Data'] = product_link 
                output['Count'] = int(product_compare)
                link_count += 1

    return output


def google_search(query):
    response = get_results(query)
    return parse_results(response)

queries = ['airpods', 'sony wh-1000xm5', 'bose quietcomfort 45']

for quer in queries:
    searches = {
        quer.title() : google_search(quer)
    }
    print(quer)
    print(searches)

