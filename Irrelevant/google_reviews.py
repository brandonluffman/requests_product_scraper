from selenium import webdriver
from parsel import Selector
import json


chromedrive_path = './chromedriver' # use the path to the driver you downloaded from previous steps
driver = webdriver.Chrome(chromedrive_path)

url = 'https://www.google.com/shopping/product/11415085711667766387/reviews?hl=en&q=apple+airpods+max&prds=eto:3963812343973418838_0;8191234564920633265_0;353421421838069624_0,local:1,pid:13998887421003899116,prmr:2,rsk:PC_7069147378898153804&sa=X&ved=0ahUKEwj34L6cpsH9AhW7KVkFHTCOBm4QqSQIhQE'

driver.get(url)

page_content = driver.page_source

response = Selector(page_content)

results = []

for el in response.xpath("//body/div[@id='AGcbBb']/div[@id='sg-product__pdp-container']/div[@class='dPIF2d']/div[@class='rktlcd']/div[@id='sh-rol__reviews-cont']/div"):
    results.append({
        'title': el.xpath('./div/text()').extract_first(''),
        'review': el.xpath('./div[3]/div[2]').extract_first(''),
        'stars': el.xpath('./div[2]/div').extract_first(''),
        'date': el.xpath('./div[2]/span').extract_first('')
    })



# json_object = json.dumps(results, indent=4)


# with open("reviews.json", "w") as f:
#     f.write(json_object)


print(results)

driver.quit()
