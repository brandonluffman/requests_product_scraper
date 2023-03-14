import requests, json
from parsel import Selector
import time
import random
from proxies import proxyList
from user_agents import user_agent_list

chosen_proxy = random.choice(proxyList)
proxy = {'http' : chosen_proxy}
user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}

def get_reviews_results(url, headers):
    data = []

    while True:
        html = requests.get(url, headers=headers, proxies=proxy)
        time.sleep(1)
        selector = Selector(html.text)
        i = 0
        for review in selector.css('.fade-in-animate'):
            title = review.css('.P3O8Ne::text').get()
            date = review.css('.ff3bE::text').get()
            rating = int(review.css('.UzThIf::attr(aria-label)').get()[0])
            content = review.css('.g1lvWe div::text').get()
            source = review.css('.sPPcBf').xpath('normalize-space()').get()

            data.append({
                'title': title,
                'date': date,
                'rating': rating,
                'content': content,
                'source': source
            })

            

        next_page_selector = selector.css('.sh-fp__pagination-button::attr(data-url)').get()

        if next_page_selector:
            # re-assigns requests.get url to a new page url
            url = 'https://www.google.com' + selector.css('.sh-fp__pagination-button::attr(data-url)').get()
        else:
            break

    return data


def main():
    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers

    URL = 'https://www.google.com/shopping/product/14019378181107046593/reviews?hl=en&gl=us'

    reviews_results = get_reviews_results(URL, headers)

    print(json.dumps(reviews_results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()