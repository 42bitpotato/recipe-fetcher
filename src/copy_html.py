import requests

def get_html(url):
    request = requests.get(url)
    return request.text