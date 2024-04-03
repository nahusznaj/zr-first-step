# Request with javascript rendering, premium proxy and proxy country, 
# Set a logic for timeout
#
# 
import os 
from dotenv import load_dotenv
load_dotenv()
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

zenrowsApiKey = os.getenv("api_key")

apikey = zenrowsApiKey
urls = ['https://scrapeme.live/']

zenrows_api_base = "https://api.zenrows.com/v1/"

for url in urls:
	try:
		response = requests.get(zenrows_api_base, timeout=(1,20), params={
			"apikey": apikey,
			"url": url
		})

		print(response.text)  # process response
	except Exception as e:
		print(f'Failed: {e}')  # will print "Max retries exceeded"
