import requests

url = "https://quotes.toscrape.com/"
r = requests.get(url)

print(r.status_code)