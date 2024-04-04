# Request with javascript rendering, premium proxy and proxy country, 
# Zenrows SDK in use 
# pip install zenrows
from zenrows import ZenRowsClient
import os 
from dotenv import load_dotenv
load_dotenv()

zenrowsApiKey = os.getenv("api_key")

client = ZenRowsClient(zenrowsApiKey)
url = "https://httpbin.io/get"

params = {
    # enable Javascript rendering in a headless browser
    "js_render": "true",
    # enable a premium residential proxy
    "premium_proxy": "true",
    "proxy_country": "de"
}

response = client.get(url, params=params)

with open('output_z.html', 'a') as f:
    if response.ok:
        print(response.text)
    else:
        print("error")