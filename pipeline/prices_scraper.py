import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import time
import random

proxyList = ['197.243.20.178:80', '51.75.206.209:80', '190.104.173.62:80', '54.251.32.206:80', '185.15.244.162:80', '34.135.0.68:80', '146.59.199.12:80', '61.111.38.5:80', '82.223.102.92:9443', '158.69.157.172:80', '201.217.49.2:80', '34.170.89.64:80', '196.1.97.209:80', '51.75.141.46:80', '137.184.232.148:80', '93.180.222.134:8080', '167.172.158.85:81', '51.75.122.80:80', '110.34.3.229:3128', '78.46.175.184:80', '209.169.71.193:80', '104.45.128.122:80', '23.238.33.186:80', '82.180.163.163:80', '116.203.27.109:80', '190.128.228.182:80', '54.82.79.59:80', '191.101.1.116:80', '138.68.235.51:80', '153.19.91.77:80', '15.236.135.81:80', '156.67.217.159:80', '181.16.201.53:80', '62.106.95.52:2222', '167.99.124.118:80', '142.93.61.46:80', '65.108.230.239:42899', '164.52.192.156:80', '41.74.91.244:80', '89.117.32.237:80', '162.144.233.16:80', '80.48.119.28:8080', '34.81.72.31:80', '8.208.85.34:8081', '47.91.45.235:45554', '8.209.64.208:8080', '2.92.49.249:80', '157.254.193.139:80', '43.255.113.232:8082', '187.217.54.84:80', '185.162.251.76:80', '47.74.152.29:8888', '82.146.37.145:80', '173.212.195.139:80', '49.249.155.3:80', '45.85.45.30:80', '178.131.58.50:90', '65.108.9.181:80', '115.144.8.91:80', '182.16.12.26:8088', '182.16.12.28:8088', '182.16.12.30:8088', '216.137.184.253:80', '185.103.87.30:8081', '95.183.140.94:80', '95.183.140.89:80', '190.52.178.17:80', '164.132.170.100:80', '201.212.246.80:80', '74.205.128.200:80', '14.139.242.7:80', '115.96.208.124:8080', '103.155.217.156:41472', '203.150.113.189:8080', '154.118.228.212:80', '178.49.14.57:3128', '134.209.108.182:8888', '182.16.12.29:8088', '113.161.131.43:80', '117.54.120.229:8888', '124.13.181.7:80', '3.226.168.144:80', '190.60.28.31:80', '198.49.68.80:80', '196.1.95.124:80', '182.72.203.246:80', '203.146.127.159:80', '45.118.139.196:80', '143.198.241.47:80', '184.72.36.89:80', '14.178.142.11:80', '200.69.210.59:80', '46.47.197.210:3128', '80.13.0.226:80', '110.238.113.119:10006', '92.118.232.74:80', '52.88.105.39:80', '64.227.106.157:80', '200.92.212.90:999', '89.217.59.77:80', '103.234.55.173:80', '190.52.178.17:80', '5.48.179.150:80', '142.11.222.22:80', '146.255.100.226:80', '194.225.227.130:3128', '34.23.45.223:80', '91.234.195.124:80', '45.118.139.196:80', '185.218.125.70:80', '62.182.66.209:9090', '107.6.27.132:80', '144.76.75.25:4444', '108.161.128.43:80', '159.203.13.121:80', '13.51.207.47:80', '195.190.144.6:80', '52.41.249.10:80', '37.148.228.117:8090', '24.199.82.12:80', '178.62.92.133:80', '184.72.36.89:80', '162.144.236.128:80', '72.52.217.188:80', '52.24.80.166:80', '80.232.242.125:9002', '3.128.142.113:80', '138.91.159.185:80', '196.251.0.198:8080', '4.188.236.47:80', '181.65.200.53:80', '90.103.95.90:80', '24.230.33.96:3128', '54.82.79.59:80', '18.142.81.218:80', '65.0.95.24:80', '146.59.14.159:80', '43.255.113.232:8084', '104.45.128.122:80', '178.49.14.57:3128', '51.178.47.12:80', '61.111.38.5:80', '173.212.209.233:3128', '13.232.245.132:80', '18.179.20.228:8181', '37.152.181.83:89', '146.83.118.9:80', '41.93.71.12:80', '74.208.177.198:80', '158.69.157.172:80', '189.250.93.75:80', '87.217.176.18:80', '45.188.166.50:1994', '95.216.106.70:3128', '41.204.63.118:80', '83.40.137.251:80', '179.49.239.2:999', '90.65.1.102:80', '134.209.108.182:8888', '5.78.87.47:8080', '209.126.6.159:80', '190.128.241.102:80', '14.178.142.11:80', '197.243.20.178:80', '93.188.166.232:80', '178.32.101.200:80', '164.92.200.113:80', '45.85.45.30:80', '185.103.87.30:8081', '164.132.170.100:80']

user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13.2; rv:110.0) Gecko/20100101 Firefox/110.0', 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:110.0) Gecko/20100101 Firefox/110.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:110.0) Gecko/20100101 Firefox/110.0', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:110.0) Gecko/20100101 Firefox/110.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.69', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.69', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/96.0.4693.50', 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/96.0.4693.50', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/96.0.4693.50', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/96.0.4693.50', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 YaBrowser/23.1.2 Yowser/2.5 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 YaBrowser/23.1.2 Yowser/2.5 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 YaBrowser/23.1.2 Yowser/2.5 Safari/537.36'] 

chosen_proxy = random.choice(proxyList)
proxy = {'http' : chosen_proxy}
user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}

def get_source(url):
    """Return the source code for the provided URL. 
    Args: 
        url (string): URL of the page to scrape.
    Returns:
        response (object): HTTP response object from requests_html. 
    """

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

