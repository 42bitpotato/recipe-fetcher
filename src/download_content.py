import requests
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup




