import requests
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup

def extract_title(html):
    title = str(html.title)
    split_title = []
    for line in title.splitlines():
        if line.endswith("title>"):
            continue
        else:
            split_title.append(line)
    title = "\n".join(split_title)
    return title



