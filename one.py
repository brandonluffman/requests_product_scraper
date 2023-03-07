import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup


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
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    return response


def parse_results(response):
    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"
    
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:
            item = {
                # 'title': result.find(css_identifier_title, first=True).text,
                'link': result.find(css_identifier_link, first=True).attrs['href'],
                # 'text': result.find(css_identifier_text, first=True).text
            }
            
            output.append(item['link'])
            print(item['link'])
            
            for link in item.values():
                 # Making a GET request
                r = requests.get(link)
                
                # Parsing the HTML
                soup = BeautifulSoup(r.content, 'html.parser')
            
                for link in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                    content = link.text
                    print(content)
        
    return output

def google_search(query):
    response = get_results(query)
    return parse_results(response)


query = input('What would you like to get the links for? \n')

results = google_search(query)

print(results)



