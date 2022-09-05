import requests

def get_webpage(url):
    page = requests.get(url)
    return page.text
url = 'http://google.com'
print(get_webpage(url))
