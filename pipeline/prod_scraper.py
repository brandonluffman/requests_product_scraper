import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import time
import random

def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """
    # user_agent_list = ['Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; Google Pixel Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; HTC Desire 21 pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; Wildfire U20 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3', 'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1', 'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1', 'Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1', ' Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1', ' Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1',
    #                     'Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1', 'Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1', 'Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3', 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254', 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536', 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058', 'Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246', 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1', 'Dalvik/2.1.0 (Linux; U; Android 9; ADT-2 Build/PTT5.181126.002)', 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36', 'Roku4640X/DVP-7.70 (297.70E04154A)', 'Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30', 'Mozilla/5.0 (Linux; Android 9; AFTWMST22 Build/PS7233; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36', 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)', 'AppleTV11,1/11.1', 'AppleTV6,2/11.1', 'AppleTV5,3/9.1.1', 'Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15', 'Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)', 'Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393', 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586', 'Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343', 'Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US', 'Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)', 'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)', 'Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+', 'Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)']
    # proxies = ['197.243.20.178:80', '51.75.206.209:80', '190.104.173.62:80', '54.251.32.206:80', '185.15.244.162:80', '34.135.0.68:80', '146.59.199.12:80', '61.111.38.5:80', '82.223.102.92:9443', '158.69.157.172:80', '201.217.49.2:80', '34.170.89.64:80', '196.1.97.209:80', '51.75.141.46:80', '137.184.232.148:80', '93.180.222.134:8080', '167.172.158.85:81', '51.75.122.80:80', '110.34.3.229:3128', '78.46.175.184:80', '209.169.71.193:80', '104.45.128.122:80', '23.238.33.186:80', '82.180.163.163:80', '116.203.27.109:80', '190.128.228.182:80', '54.82.79.59:80', '191.101.1.116:80', '138.68.235.51:80', '153.19.91.77:80', '15.236.135.81:80', '156.67.217.159:80', '181.16.201.53:80', '62.106.95.52:2222', '167.99.124.118:80', '142.93.61.46:80', '65.108.230.239:42899', '164.52.192.156:80', '41.74.91.244:80', '89.117.32.237:80', '162.144.233.16:80', '80.48.119.28:8080', '34.81.72.31:80', '8.208.85.34:8081', '47.91.45.235:45554', '8.209.64.208:8080', '2.92.49.249:80', '157.254.193.139:80', '43.255.113.232:8082', '187.217.54.84:80', '185.162.251.76:80', '47.74.152.29:8888', '82.146.37.145:80', '173.212.195.139:80', '49.249.155.3:80', '45.85.45.30:80', '178.131.58.50:90', '65.108.9.181:80', '115.144.8.91:80', '182.16.12.26:8088', '182.16.12.28:8088', '182.16.12.30:8088', '216.137.184.253:80', '185.103.87.30:8081', '95.183.140.94:80', '95.183.140.89:80', '190.52.178.17:80', '164.132.170.100:80', '201.212.246.80:80', '74.205.128.200:80', '14.139.242.7:80', '115.96.208.124:8080', '103.155.217.156:41472', '203.150.113.189:8080', '154.118.228.212:80', '178.49.14.57:3128', '134.209.108.182:8888', '182.16.12.29:8088', '113.161.131.43:80', '117.54.120.229:8888', '124.13.181.7:80', '3.226.168.144:80', '190.60.28.31:80', '198.49.68.80:80', '196.1.95.124:80', '182.72.203.246:80', '203.146.127.159:80', '45.118.139.196:80', '143.198.241.47:80', '184.72.36.89:80', '14.178.142.11:80', '200.69.210.59:80', '46.47.197.210:3128', '80.13.0.226:80', '110.238.113.119:10006', '92.118.232.74:80', '52.88.105.39:80', '64.227.106.157:80', '200.92.212.90:999', '89.217.59.77:80', '103.234.55.173:80', '190.52.178.17:80', '5.48.179.150:80', '142.11.222.22:80', '146.255.100.226:80', '194.225.227.130:3128', '34.23.45.223:80', '91.234.195.124:80', '45.118.139.196:80', '185.218.125.70:80', '62.182.66.209:9090', '107.6.27.132:80', '144.76.75.25:4444', '108.161.128.43:80', '159.203.13.121:80', '13.51.207.47:80', '195.190.144.6:80', '52.41.249.10:80', '37.148.228.117:8090', '24.199.82.12:80', '178.62.92.133:80', '184.72.36.89:80', '162.144.236.128:80', '72.52.217.188:80', '52.24.80.166:80', '80.232.242.125:9002', '3.128.142.113:80', '138.91.159.185:80', '196.251.0.198:8080', '4.188.236.47:80', '181.65.200.53:80', '90.103.95.90:80', '24.230.33.96:3128', '54.82.79.59:80', '18.142.81.218:80', '65.0.95.24:80', '146.59.14.159:80', '43.255.113.232:8084', '104.45.128.122:80', '178.49.14.57:3128', '51.178.47.12:80', '61.111.38.5:80', '173.212.209.233:3128', '13.232.245.132:80', '18.179.20.228:8181', '37.152.181.83:89', '146.83.118.9:80', '41.93.71.12:80', '74.208.177.198:80', '158.69.157.172:80', '189.250.93.75:80', '87.217.176.18:80', '45.188.166.50:1994', '95.216.106.70:3128', '41.204.63.118:80', '83.40.137.251:80', '179.49.239.2:999', '90.65.1.102:80', '134.209.108.182:8888', '5.78.87.47:8080', '209.126.6.159:80', '190.128.241.102:80', '14.178.142.11:80', '197.243.20.178:80', '93.188.166.232:80', '178.32.101.200:80', '164.92.200.113:80', '45.85.45.30:80', '185.103.87.30:8081', '164.132.170.100:80']
    
    # chosen_proxy = random.choice(proxies)
    # proxy = {'http' : chosen_proxy}
    # user_agent = random.choice(user_agent_list)
    # headers = {'User-Agent': user_agent}
    try:
        session = HTMLSession()
        response = session.get(url)
        # response = session.get(url, proxies=proxy, headers=headers)
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

  
    output = []
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

        item = {
            'product_title' : result.find(css_product_title, first=True).text,
            'product_description' : result.find(css_product_description, first=True).text,
            'product_rating' : result.find(css_product_rating, first=True).text,
            'review_count' : result.find(css_product_review_count, first=True).text,
            'product_img' : result.find(css_product_img, first=True).attrs['src'],
            'product_specs' : product_specifications_list,
            'all_reviews_link': reviews_link,
            'product_purchasing' : purchase_links
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

