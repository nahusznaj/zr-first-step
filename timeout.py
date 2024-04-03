#  Request with javascript rendering, premium proxy and proxy country, 
# Set a case if there's an error or not.
# Set a retry logic for timeout
#
# pip install zenrows
#from zenrows import ZenRowsClient
import os 
from dotenv import load_dotenv
load_dotenv()

zenrowsApiKey = os.getenv("api_key")


import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

apikey = zenrowsApiKey
urls = ['https://www.google.com', 'https://www.amazon.com/']


zenrows_api_base = "https://api.zenrows.com/v1/"

for url in urls:
	try:
		response = requests.get(zenrows_api_base, timeout=(1,20), params={
			"apikey": apikey,
			"url": url,
			"js_render": "true",
			"premium_proxy": "true"
		})

		print(response.text)  # process response
	except Exception as e:
		print(f'Failed: {e}')  # will print "Max retries exceeded"
