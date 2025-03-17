import requests
import re
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup

def extract_title_html(html):
    title = html.find_all("h1", class_=re.compile("title"))
    return str(title)

def extract_description_html(html):
    description = html.find_all("div", class_=re.compile("description"))
    return str(description)

def extract_ingredients_html(html):
    ingredients = html.find_all("span", class_=re.compile("ingredient"))
    return str(ingredients)

def extract_instructions_html(html):
    instructions = html.find_all("span", class_=re.compile("instruction"))
    return str(instructions)

def extract_image_html(html):
    image = html.find_all("source", srcset=True)
    return str(image)