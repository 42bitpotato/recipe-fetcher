from html_content import HTMLFile
from textnode import *

from bs4 import BeautifulSoup


def html_to_textnode(html_file):
    if len(html_file.content) == 0:
        raise ValueError(f"Missing content: {html_file.content}")
    
def title_to_textnode(html):
    string = str(html.string)
    return ContentChildNode(string.strip())

def description_to_textnode(html):
    string = str(html.p.string)
    return ContentChildNode(string.strip())

def ingredients_to_textnode(html):
    list_of_ingredients = []
    for ingredient in html:
        ingredient_txt = str(ingredient.string)
        for line in ingredient_txt.splitlines():
            if line.isspace() or line == "":
                continue
            else:
                list_of_ingredients.append(ContentChildNode(line.strip()))
    return list_of_ingredients

def instructions_to_textnode(html):
    pass
