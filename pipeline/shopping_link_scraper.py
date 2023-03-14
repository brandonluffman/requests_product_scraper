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
    response = get_source("https://www.google.com/search?tbm=shop&hl=en&psb=1&ved=0CAAQvOkFahcKEwj4lfLEmsv9AhUAAAAAHQAAAAAQJQ&q=" + query)
    
    return response
def parse_results(response):
    
    css_identifier_results = ".i0X6df"
    css_identifier_link = "span a"
    css_identifier_test_2 = ".Ldx8hd a span"
    css_product_reviews = ".QIrs8"
    product_results = response.html.find(css_identifier_results)
    output = {}
    link_count = 0
    ### For Loop Below loops through queries to find Shopping Link and Integer Representing Amounnt of Stores that are linked to that product ###
    for product_result in product_results:
        product_link = 'https://www.google.com' + product_result.find(css_identifier_link, first=True).attrs['href']
        product_compare = product_result.find(css_identifier_test_2, first=True)
        product_review_count = product_result.find(css_product_reviews, first=True).text

        
        if product_compare:
            product_compare = product_compare.text
            if product_compare.endswith('+'):
                product_compare = product_compare[:-1]

        
            if link_count < 3:
                output[f'link #{link_count}'] = {
                    'Data' : product_link, 
                    'Count' : int(product_compare),
                    'Review Count' : int(product_review_count.split()[5].replace(',',''))
                }
                link_count += 1

    return output




def google_search(query):
    response = get_results(query)
    return parse_results(response)


queries = ['jabra elite 75t', 'sony wh-1000xm5', 'bose quietcomfort 45']



def card_per_product(products): 
    final_dict = {}   
    for product in products:
        searches = {
            f'{product.title()}' : google_search(product)
        }
        print("SEARCHES:",searches)
        
        row_data = searches.values()
        for item in row_data:
            cards = item.values() 
            card_count = 0
            distrib_count_lis = []
            review_count_lis = []
            cards_with_max_distribs = []
            for card in cards:
                card_count +=1 
                distrib_count_lis.append(card['Count'])
                review_count_lis.append(card['Review Count'])
            max_distribs = max(distrib_count_lis)
            max_reviews = max(review_count_lis)
            for card in cards:
                if card['Count'] == max_distribs:
                    cards_with_max_distribs.append(card)
            if len(cards_with_max_distribs) > 1:
                for card in cards_with_max_distribs:
                    if card['Review Count'] == max_reviews:
                        final_dict[product] = card
            else:
                final_dict[product] = cards_with_max_distribs[0]


    return final_dict

print("TOP CARD:",card_per_product(queries))

