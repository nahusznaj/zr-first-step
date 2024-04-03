# pip install zenrows
from zenrows import ZenRowsClient
import os 
from dotenv import load_dotenv
load_dotenv()

zenrowsApiKey = os.getenv("api_key")

client = ZenRowsClient(zenrowsApiKey)
url = "https://www.amazon.com/"

params = {
    # enable Javascript rendering in a headless browser
    "js_render": "true",
    # enable a premium residential proxy
    "premium_proxy": "true"
}

response = client.get(url, params=params)

with open('output.html', 'a') as f:
    f.write(response.text)