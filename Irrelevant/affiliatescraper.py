
import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.cnet.com/home/yard-and-outdoors/best-grill/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# find all the anchor tags with "href"


# for link in soup.find_all('a'):
#     if 'https://www.cnn.com/' not in link:
#         print(link.get('href'))

for link in soup.find_all('h2'):
        print(link.text)