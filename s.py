# pip install zenrows
import os 
from zenrows import ZenRowsClient
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup


from dotenv import load_dotenv
load_dotenv()

zenrowsApiKey = os.getenv("api_key")

client = ZenRowsClient(zenrowsApiKey)
url = "https://scrapeme.live/shop/"

response = requests.get(url)

# print(response.text)

with open('output_s.txt', 'a') as f:
    if response.ok:
        # parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")
        #print(type(soup.text))
        #f.write(soup.text)
        
        all_amounts = soup.find_all("span", {"class":"woocommerce-Price-amount amount"})
        prices = []
        for div in all_amounts:
            prices.append(div.text)
        # if search_input_element is not None:
        #     print(search_input_element)
        f.write(str(prices))
        print(prices)
    else:
        print(response)