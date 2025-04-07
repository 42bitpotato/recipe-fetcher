from file_handling import copy_template
from textnode import RecipeHead, SectionType

def text_to_html(recipe_obj: "RecipeHead"):
    html_template = copy_template()

    sections = recipe_obj.sections

    html_template_split = html_template.splitlines()
    
    for line_num in range(len(html_template_split)):
        strip_line = html_template_split[line_num].strip() # Remove leading and trailing whitespaces

        # Title
        if strip_line.startswith("<title>"):
            line = html_template_split[line_num]
            for c in range(len(line)):
                if line[c] == ">":
                    new_line = line[:c+1] + sections[SectionType.TITLE] + line[c+1:]
                    html_template_split[line_num] = new_line
                    break
        if strip_line.startswith("<h1>"):
            line = html_template_split[line_num]
            for c in range(len(line)):
                if line[c] == ">":
                    new_line = line[:c+1] + sections[SectionType.TITLE] + line[c+1:]
                    html_template_split[line_num] = new_line
                    break
            continue
        
        # Description
        if strip_line.startswith('<p class="description">'):
            line = html_template_split[line_num+1]
            new_line = line + sections[SectionType.DESCR]
            html_template_split[line_num+1] = new_line
            continue

        # Image
        if strip_line.startswith("<img"):
            line = html_template_split[line_num]
            for c in range(len(line)):
                if line[c] == '"':
                    new_line = line[:c+1] + sections[SectionType.IMAGE] + line[c+1:]
                    html_template_split[line_num] = new_line
                    break
            continue

        # Ingredients
        if strip_line.startswith("<h2>Ingredients</h2>"):
            ing_line_num = line_num+2
            line = html_template_split[ing_line_num]

            spaces = " " * line.count(" ") # Count indentation spaces
            list_items = sections[SectionType.INGRE].copy()

            add_list_item(html_template_split, ing_line_num, spaces, list_items)
            continue

        # Instructions
        if strip_line.startswith("<h2>Instructions</h2>"):
            ing_line_num = line_num+2
            line = html_template_split[ing_line_num]

            spaces = " " * line.count(" ") # Count indentation spaces
            list_items = sections[SectionType.INSTR].copy()

            add_list_item(html_template_split, ing_line_num, spaces, list_items)
            continue

    return "\n".join(html_template_split)

def add_list_item(html_template_split, line_nr, spaces, list_items):
    if len(list_items) == 0:
        return
    line = spaces + "<li>" + list_items.pop() + "</li>"
    html_template_split[line_nr:line_nr] = line
    return add_list_item(html_template_split, line_nr + 1, spaces, list_items)
