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

# https://www.google.com/webhp?tbm=shop
# https://shopping.google.com/?nord=1
# https://shopping.google.com/search?q=
def get_results(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?tbm=shop&hl=en&psb=1&ved=0CAAQvOkFahcKEwj4lfLEmsv9AhUAAAAAHQAAAAAQJQ&q=" + query)
    
    return response

def parse_results(response):
    
    css_identifier_result = ".sh-pr__product-results-grid"
    css_identifier_title = "h2"
    css_identifier_link = "a"
    css_identifier_text = "sh-t__title"


    results = response.html.find(css_identifier_result)
    
    output = {}
    link_count = 0


    # for result in results:
    #     if link_count < len(queries):
    #     # link_count += 1
    #         output[f'Link #{link_count}'] = result.find(css_identifier_link, first=True).attrs['href'], result.find(css_identifier_title, first=True).text
    #         link_count += 1
    for result in results:
        # link_count += 1
            link = 'https://www.google.com/' + result.find(css_identifier_link, first=True).attrs['href']
            output[f'Link #{link_count}'] = link, result.find(css_identifier_link, first=True).text
            link_count += 1


    return output


def google_search(query):
    response = get_results(query)
    return parse_results(response)

# query = input("What would you like to get the links for? \n")

queries = ['airpods', 'sony wh-1000xm5', 'bose quiet comfort 45']


for quer in queries:
    searches = {
        'Product Links' : google_search(quer)
    }
    print(quer)
    print(searches)

