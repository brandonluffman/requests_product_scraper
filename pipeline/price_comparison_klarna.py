import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import time
import random
from proxies import proxyList
from user_agents import user_agent_list

chosen_proxy = random.choice(proxyList)
proxy = {'http' : chosen_proxy}
user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url, headers=headers, proxies=proxy)
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

