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
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    return response


def parse_results(response):
    

    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"
    css_identifier_result_youtube = ".dFd2Tb"
    css_identifier_link_youtube = '.DhN8Cf a'


        
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:
            item = {
                # 'title': result.find(css_identifier_title, first=True).text,
                'link': result.find(css_identifier_link, first=True).attrs['href'],
                # 'text': result.find(css_identifier_text, first=True).text
            }  
            
            output.append(item)
        
    return output

def parse_youtube_results(response):
    
    css_identifier_result = ".dFd2Tb"
    css_identifier_link = '.DhN8Cf a'
 
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:
            item = {
                # 'title': result.find(css_identifier_title, first=True).text,
                "link": result.find(css_identifier_link, first=True).attrs['href'],
                # 'text': result.find(css_identifier_text, first=True).text
            }  
            
            output.append(item)
        
    return output

def google_search(query):
    response = get_results(query)
    return parse_results(response)

def youtube_search(query):
    response = get_results(query)
    return parse_youtube_results(response)



query = input("What would you like to get the links for? \n")

results = [google_search(query), google_search(query + " reddit"), youtube_search(query + " youtube")]
reddit_results = google_search(query + ' reddit')
youtube_results = google_search(query + ' youtube')
tiktok_results = google_search(query + ' tiktok')

print(results)
# print(reddit_results)
# print(youtube_results)
# print(tiktok_results)

