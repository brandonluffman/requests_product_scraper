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
        # print(response.status_code)
        # print(f"Request Recevied -- User Agent: {user_agent} -- Proxy: {proxy}")
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
    css_all_reviews_link = ".k0e9E a"
    css_product_reviews = "#-9110982622418926094-full"
    css_product_reviews_title = ".XBANlb .P3O8Ne"
    css_product_reviews_rating = ".nMkOOb div"
    css_product_review_count = ".QKs7ff .qIEPib"
    css_product_purchasing = ".kPMwsc"
    css_product_specifications = ".lW5xPd"


    product_purchasing = ".dOwBOc tbody"
    product_purchase = "a"
    product_desc = "td:nth-of-type(1)"
    product_spec = "td:nth-of-type(2)"

    results = response.html.find(css_identifier_result)
    purchasing = response.html.find(css_product_purchasing)
    specifications = response.html.find(css_product_specifications)

  
    output = {}
    purchase_links = []
    for purchase in purchasing:
        link = (purchase.find(product_purchase, first=True).text).replace('Opens in a new window', '')
        prod_links = link
        purchase_links.append(prod_links)

    product_specifications_list = []
    for specification in specifications:
        descs = specification.find(product_desc)
        specs = specification.find(product_spec)
        for spec, desc in zip(specs,descs[1:]):
            specs_object = {
                desc.text : spec.text,
            }
            product_specifications_list.append(specs_object)

    for result in results:
        reviews_link = 'https://google.com' + result.find(css_all_reviews_link, first=True).attrs['href']
        product_title = result.find(css_product_title, first=True).text
        output[product_title] = {
            'product_description' : result.find(css_product_description, first=True).text,
            'product_rating' : result.find(css_product_rating, first=True).text,
            'review_count' : result.find(css_product_review_count, first=True).text,
            'product_img' : result.find(css_product_img, first=True).attrs['src'],
            'product_specs' : product_specifications_list,
            'all_reviews_link': reviews_link,
            'product_purchasing' : purchase_links
        } 

    return output


def google_search(query):
    response = get_results(query)
    return parse_results(response)

urls = ['https://www.google.com/shopping/product/7414362887907499803?hl=en&psb=1&q=bose+quietcomfort+45&prds=eto:7699631281679971839_0,pid:5292486479779850642,rsk:PC_12836789135460115869&sa=X&ved=0ahUKEwjv9cGwic39AhWDADQIHaGVBjkQ8wII9gs', 'https://www.google.com/shopping/product/14556986932651510680?hl=en&q=sony+wh-1000xm5&prds=eto:17832498348390085438_0;16734284565725029642_0;7614542217126070872_0,pid:1061495521773557507,rsk:PC_11648784580466805463&sa=X&ved=0ahUKEwjGgJDMus39AhViFlkFHWWvAUYQ9pwGCBQ']


for url in urls:    
    results = google_search(url)
    print(results, '\n')

