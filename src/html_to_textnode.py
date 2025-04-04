from html_content import HTMLFile
from textnode import *

from bs4 import BeautifulSoup


def html_to_textnode(html_file: "HTMLFile"):
    if len(html_file.content) == 0:
        raise ValueError(f"Missing content: {html_file.content}")
    
    section_nodes = []
    recipe_head = RecipeHead("", section_nodes)

    for content in html_file.content:
        if not isinstance(content.type, SectionType):
            raise ValueError(f"Missing SectionType Enum: {content}")
        
        match content.type:
            case SectionType.TITLE:
                section_node = SectionNode(SectionType.TITLE)

                childnode = title_to_textnode(content.html)

                recipe_head.title = childnode.value

                section_node.content.append(ContentParentNode(ContentType.TEXT, childnode))
                section_nodes.append(section_node)
                
            case SectionType.DESCR:
                section_node = SectionNode(SectionType.DESCR)

                childnode = description_to_textnode(content.html)

                section_node.content.append(ContentParentNode(ContentType.TEXT, childnode))
                section_nodes.append(section_node)
                
            case SectionType.INGRE:
                section_node = SectionNode(SectionType.INGRE)

                childnode = ingredients_to_textnode(content.html)

                section_node.content.append(ContentParentNode(ContentType.UOLIST, childnode))
                section_nodes.append(section_node)
                
            case SectionType.INSTR:
                section_node = SectionNode(SectionType.INSTR)

                childnode = instructions_to_textnode(content.html)

                section_node.content.append(ContentParentNode(ContentType.OLIST, childnode))
                section_nodes.append(section_node)
                
            case SectionType.IMAGE:
                section_node = SectionNode(SectionType.IMAGE)

                childnode = image_to_textnode(content.html)

                section_node.content.append(ContentParentNode(ContentType.IMAGE, childnode))
                section_nodes.append(section_node)
                
    return recipe_head

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
