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
    response = get_source(url)
    
    return response

def parse_results(response):
    
    css_identifier_result = ".sg-product__dpdp-c"
    css_product_img = ".wTvWSc img"
    css_product_title = ".YVQvvd .BvQan"
    css_product_description = ".Zh8lCd p .sh-ds__full .sh-ds__full-txt"
    css_product_specs = ".lW5xPd .crbkUb"
    css_product_rating = ".QKs7ff .uYNZm"
    css_product_reviews = "#-9110982622418926094-full"
    css_product_reviews_title = ".XBANlb .P3O8Ne"
    css_product_reviews_rating = ".nMkOOb .UzThIf"
    css_product_review_count = ".QKs7ff .qIEPib"
    css_product_purchasing = ".dOwBOc tr"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:

        item = {
            'product_title' : result.find(css_product_title, first=True).text,
            'product_description' : result.find(css_product_description, first=True).text,
            'product_rating' : result.find(css_product_rating, first=True).text,
            'review_count' : result.find(css_product_review_count, first=True).text,
            'product_img' : result.find(css_product_img, first=True),
            'product_specs' : result.find(css_product_specs, first=True).text,
            'product_reviews_title' : result.find(css_product_reviews_title, first=True).text,
            'product_reviews_rating' : result.find(css_product_reviews_rating, first=True),
            'product_reviews' : result.find(css_product_reviews, first=True),
            'product_purchasing' : result.find(css_product_purchasing, first=True).text
        }

        output.append(item)


    return output


def google_search(query):
    response = get_results(query)
    return parse_results(response)

urls = ['https://www.google.com/shopping/product/7414362887907499803?hl=en&psb=1&q=bose+quietcomfort+45&prds=eto:7699631281679971839_0,pid:5292486479779850642,rsk:PC_12836789135460115869&sa=X&ved=0ahUKEwjv9cGwic39AhWDADQIHaGVBjkQ8wII9gs', 'https://www.google.com/shopping/product/14556986932651510680?hl=en&q=sony+wh-1000xm5&prds=eto:17832498348390085438_0;16734284565725029642_0;7614542217126070872_0,pid:1061495521773557507,rsk:PC_11648784580466805463&sa=X&ved=0ahUKEwjGgJDMus39AhViFlkFHWWvAUYQ9pwGCBQ']


for url in urls:    
    results = google_search(url)
    print(results)

