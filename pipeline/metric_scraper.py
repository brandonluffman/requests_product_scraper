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
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    return response

def parse_results(response,source=''):
    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"
    css_identifier_result_youtube = ".dFd2Tb"
    css_identifier_link_youtube = '.DhN8Cf a'

    results = response.html.find(css_identifier_result)
    youtube_results = response.html.find(css_identifier_result_youtube)
    
    output = {}
    link_count = 0

    if results: 
        if source:
            for result in results:
                link_count += 1
                output[f'{source.title()} Link #{link_count}'] = result.find(css_identifier_link, first=True).attrs['href']
        else:
            for result in results:
                link_count += 1
                output[f'Google Link #{link_count}'] = result.find(css_identifier_link, first=True).attrs['href']  
    else:
        for youtube_result in youtube_results:
            link_count += 1
            output[f'{source.title()} Link #{link_count}'] = youtube_result.find(css_identifier_link_youtube, first=True).attrs['href']

    return output

def google_search(query, source=''):
    final_query = query + ' ' + source
    response = get_results(final_query)
    return parse_results(response, source)

query = input("What would you like to get the links for? \n")

if 'best' not in query:
    query = 'best ' + query 
else:
    pass

results = {
            "Google Links": google_search(query),
            "Reddit Links": google_search(query,'reddit'),
            "Youtube Links": google_search(query, 'youtube')
        }

print(results)