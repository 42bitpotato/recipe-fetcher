import requests
import re
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup

def extract_title(html):
    title = html.find_all("h1", class_=re.compile("title"))
    return str(title)

def extract_description(html):
    description = html.find_all("div", class_=re.compile("description"))
    return str(description)


