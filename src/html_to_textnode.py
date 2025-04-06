from html_content import HTMLFile
from textnode import *

from bs4 import BeautifulSoup


def html_to_textnode(html_file: "HTMLFile"):
    if len(html_file.content) == 0:
        raise ValueError(f"Missing content: {html_file.content}")
    
    section_nodes = []
    recipe_head = RecipeHead(html_file.title, section_nodes)

    for content in html_file.content:
        if not isinstance(content.type, SectionType):
            raise ValueError(f"Missing SectionType Enum: {content}")
        
        match content.type:
            case SectionType.TITLE:
                text = title_to_textnode(content.html)
                section_nodes.append(text)
                recipe_head.sections_dict[SectionType.TITLE] = text
                
            case SectionType.DESCR:
                text = description_to_textnode(content.html)
                section_nodes.append(text)
                recipe_head.sections_dict[SectionType.DESCR] = text
                
            case SectionType.INGRE:
                text = ingredients_to_textnode(content.html)
                section_nodes.append(text)
                recipe_head.sections_dict[SectionType.INGRE] = text
                
            case SectionType.INSTR:
                text = instructions_to_textnode(content.html)
                section_nodes.append(text)
                recipe_head.sections_dict[SectionType.INSTR] = text
                
            case SectionType.IMAGE:
                text = image_to_textnode(content.html)
                section_nodes.append(text)
                recipe_head.sections_dict[SectionType.IMAGE] = text
                
    return recipe_head

def title_to_textnode(html):
    string = str(html.string)
    return ContentSection(SectionType.TITLE, [string.strip()])

def description_to_textnode(html):
    string = str(html.p.string)
    return ContentSection(SectionType.DESCR, [string.strip()])

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
                list_of_ingredients.append(line.strip())

    if len(list_of_ingredients) == 0: # Raise an error if no valid content was extracted
        raise ValueError(f"Failed to extract text from HTML. list_of_ingredients: {list_of_ingredients}")

    return ContentSection(SectionType.INGRE, list_of_ingredients)

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
                list_of_instructions.append(line.strip())

    if len(list_of_instructions) == 0: # Raise an error if no valid content was extracted
        raise ValueError(f"Failed to extract text from HTML. list_of_instructions: {list_of_instructions}")
    
    return ContentSection(SectionType.INSTR, list_of_instructions)

def image_to_textnode(html):
    split_html = str(html.get("srcset")).split(",")
    for image_url in split_html:
        if image_url.endswith("816w"):
            for url in image_url.split():
                if url.startswith("http"):
                    return ContentSection(SectionType.IMAGE, [url])
                continue
    raise ValueError(f"Missing url: {html}")
