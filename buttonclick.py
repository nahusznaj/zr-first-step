# Request with javascript rendering, premium proxy and proxy country, 
# Zenrows SDK in use 
# pip install zenrows
from zenrows import ZenRowsClient
import os 
from dotenv import load_dotenv
load_dotenv()

zenrowsApiKey = os.getenv("api_key")

client = ZenRowsClient(zenrowsApiKey)
url = "https://scrapeme.live/shop/Bulbasaur/"

# params = {
#     "js_render": "true",
#     "premium_proxy": "true",
#     "js_instructions": "[{\"click\":\"single_add_to_cart_button button alt\"}]",
#     "json_response" : "true",
#      "return_screenshot": "true"
# }

# response = client.get(url, params=params)

# with open('buttonclickresult.html', 'a') as f:
#     if response.ok:
#         f.write(response.text)
#     else:
#         print("error")