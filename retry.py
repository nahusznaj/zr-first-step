#  Request with javascript rendering, premium proxy and proxy country, 
# Set a case if there's an error or not.
# Set a retry logic for HTTP errors 429, 500, etc.
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
urls = ['https://www.g2.com/products/notion/reviews']

zenrows_api_base = "https://api.zenrows.com/v1/"

requests_session = requests.Session()
retries = Retry(
	total=3,
	backoff_factor=1,
	status_forcelist=[429, 500, 502, 503, 504]
)
requests_session.mount("https://", HTTPAdapter(max_retries=retries))

for url in urls:
	try:
		response = requests_session.get(zenrows_api_base, params={
			"apikey": apikey,
			"url": url,
			"js_render": "true",
			"premium_proxy": "true"
		})

		print(response.text)  # process response
	except Exception as e:
		print(e)  # will print "Max retries exceeded"
