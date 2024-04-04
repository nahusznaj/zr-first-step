#  Request with javascript rendering, premium proxy and proxy country, 
# Set a logic for timeout
#
# pip install zenrows
#from zenrows import ZenRowsClient
import os 
from dotenv import load_dotenv
load_dotenv()

zenrowsApiKey = os.getenv("api_key")

import requests

apikey = zenrowsApiKey
urls = ['https://www.google.com']


zenrows_api_base = "https://api.zenrows.com/v1/"

for url in urls:
	try:
		response = requests.get(zenrows_api_base, params={
			"apikey": apikey,
			"url": url,
			"js_render": "true",
			"premium_proxy": "true"
		})

		print(response.text[1:100])  # process response
	except Exception as e:
		print(f'Failed: {e}')  # will print "Max retries exceeded"
