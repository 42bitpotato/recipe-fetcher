from file_handling import copy_template
from textnode import RecipeHead, SectionType

def text_to_html(recipe_obj: "RecipeHead"):
    html_template = copy_template()
    sections = recipe_obj.sections
    html_template_split = html_template.splitlines()
    
    line_num = 0

    while line_num < len(html_template_split) - 1:
        line_num += 1
        strip_line = html_template_split[line_num].strip() # Remove leading and trailing whitespaces

        # Title
        if strip_line.startswith("<title>"):
            line = html_template_split[line_num]
            for c in range(len(line)):
                if line[c] == ">":
                    new_line = line[:c+1] + sections[SectionType.TITLE] + line[c+1:]
                    html_template_split[line_num] = new_line
                    break
        elif strip_line.startswith("<h1>"):
            line = html_template_split[line_num]
            for c in range(len(line)):
                if line[c] == ">":
                    new_line = line[:c+1] + sections[SectionType.TITLE] + line[c+1:]
                    html_template_split[line_num] = new_line
                    break
            continue
        
        # Description
        elif strip_line.startswith('<p class="description">'):
            line = html_template_split[line_num+1]
            new_line = line + sections[SectionType.DESCR]
            html_template_split[line_num+1] = new_line
            continue

        # Image
        elif strip_line.startswith("<img"):
            line = html_template_split[line_num]
            for c in range(len(line)):
                if line[c] == '"':
                    new_line = line[:c+1] + sections[SectionType.IMAGE] + line[c+1:]
                    html_template_split[line_num] = new_line
                    break
            continue

        # Ingredients
        elif strip_line.startswith("<h2>Ingredients</h2>"):
            ing_line_num = line_num+2
            line = html_template_split[ing_line_num]

            add_list_item(html_template_split, ing_line_num, sections[SectionType.INGRE])
            continue

        # Instructions 
        elif strip_line.startswith("<h2>Instructions</h2>"):
            ins_line_num = line_num+2
            line = html_template_split[ins_line_num]

            add_list_item(html_template_split, ins_line_num, sections[SectionType.INSTR])
            continue 

    return "\n".join(html_template_split)

def add_list_item(html_template_split, line_nr, list_items):
    line = html_template_split[line_nr]
    spaces = line[:len(line) - len(line.lstrip())] + "  " # Indent list in html

    for i, item in enumerate(list_items):
        item_line = spaces + f"<li>{item}</li>"
        html_template_split[line_nr+i:line_nr+i] = [item_line]

    if html_template_split[line_nr + len(list_items)].strip() == "":
        html_template_split.pop(line_nr + len(list_items))

