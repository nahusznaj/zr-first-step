from zenrows import ZenRowsClient
import asyncio 
from urllib.parse import urlparse, parse_qs 
import os 
from dotenv import load_dotenv
load_dotenv()

zenrowsApiKey = os.getenv("api_key")
client = ZenRowsClient(zenrowsApiKey, concurrency=5, retries=1) 


 
urls = ["https://scrapeme.live/shop/Bulbasaur/", "https://scrapeme.live/shop/"] 
 
async def main(): 
	responses = await asyncio.gather(*[client.get_async(url) for url in urls]) 
 
	for response in responses: 
		original_url = parse_qs(urlparse(response.request.url).query)["url"] 
		print({ 
			"response": response, 
			"status_code": response.status_code, 
			"request_url": original_url, 
		}) 
 
asyncio.run(main())
