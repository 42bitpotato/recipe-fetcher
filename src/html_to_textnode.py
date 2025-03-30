from html_content import HTMLFile
from textnode import *

from bs4 import BeautifulSoup


def html_to_textnode(html_file):
    if len(html_file.content) == 0:
        raise ValueError(f"Missing content: {html_file.content}")
    for content in html_file.content:
        if not isinstance(content.type, SectionType):
            raise ValueError(f"Missing SectionType Enum: {content}")
    
def title_to_textnode(html):
    string = str(html.string)
    return ContentChildNode(string.strip())

def description_to_textnode(html):
    string = str(html.p.string)
    return ContentChildNode(string.strip())

def ingredients_to_textnode(html):
    list_of_ingredients = []
    for ingredient in html:
        ingredient_txt = ingredient.get_text(strip=True)

        if not ingredient_txt:  # Catches both None and "", skip empty elements
            continue

        for line in ingredient_txt.splitlines():
            if line.isspace() or line == "":
                continue
            else:
                list_of_ingredients.append(ContentChildNode(line.strip()))

    if len(list_of_ingredients) == 0: # Raise an error if no valid content was extracted
        raise ValueError(f"Failed to extract text from HTML. list_of_ingredients: {list_of_ingredients}")

    return list_of_ingredients

def instructions_to_textnode(html):
    list_of_instructions = []
    for instr_step in html:
        instr_step_txt = instr_step.get_text(strip=True)
        
        if not instr_step_txt:  # Catches both None and "", skip empty elements
            continue
        
        for line in instr_step_txt.splitlines():
            if line.isspace() or line == "":
                continue
            else:
                list_of_instructions.append(ContentChildNode(line.strip()))

    if len(list_of_instructions) == 0: # Raise an error if no valid content was extracted
        raise ValueError(f"Failed to extract text from HTML. list_of_instructions: {list_of_instructions}")
    
    return list_of_instructions

def image_to_textnode(html):
    split_html = str(html.get("srcset")).split(",")
    for image_url in split_html:
        if image_url.endswith("816w"):
            for url in image_url.split():
                if url.startswith("http"):
                    return ContentChildNode(url)
                continue
    raise ValueError(f"Missing url: {html}")
