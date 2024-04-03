## no zenrows power involved, and see how it fails!

import requests

url = "https://www.g2.com/products/asana/reviews"

response = requests.get(url)

print(response)