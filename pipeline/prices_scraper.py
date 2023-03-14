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
    response = get_source(url)
    
    return response

def parse_results(response):
    
    css_identifier_results = ".pr-1u8qly9"
    search_link = "a"

    results = response.html.find(css_identifier_results)
    output = []

    for result in results:
        link = result.find(search_link, first=True).attrs['href']
        prices = 'https://www.klarna.com' + link
        output.append(prices)

    return output


def google_search(query):
    response = get_results(query)
    return parse_results(response)


urls = ['https://www.klarna.com/us/shopping/pl/cl94/5055320/Headphones/Jabra-Elite-75t-TWS/', 'https://www.klarna.com/us/shopping/pl/cl94/3201350617/Headphones/Sony-WH-1000XM5/', 'https://www.klarna.com/us/shopping/pl/cl94/3200324880/Headphones/Bose-QuietComfort-45/']

results = []
for url in urls:
    results.append(google_search(url))

print(results)

