import os
import shutil
from textnode import RecipeHead, SectionType

def text_to_html(recipe_text: "RecipeHead"):
    html_template = copy_template()

    sections = recipe_text.sections_dict

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
        
        # Description
        if strip_line.startswith('<p class="description">'):
            line = html_template_split[line_num+1]
            new_line = line + sections[SectionType.DESCR]
            html_template_split[line_num+1] = new_line
            break

        # Ingredients
        if strip_line.startswith("<h2>Ingredients</h2>"):
            ing_line_num = line_num+2
            line = html_template_split[ing_line_num]
            
            for l in range(len(html_template_split[ing_line_num+1])):
                if line[c] == ">":
                    new_line = line[:c+1] + sections[SectionType.TITLE] + line[c+1:]
                    html_template_split[line_num] = new_line
                    break

def copy_template(template_dir=None):
    template_dir = "html_template" if template_dir == None else template_dir

    html_template_path = os.path.join(template_dir, "template.html")

    if os.path.exists(html_template_path):
        with open(html_template_path, "r") as template_file:
            html_template = template_file.read()
    else:
        raise ValueError(f'HTML template file not found: "{html_template_path}"')
    
    return html_template

def add_text_to_line(line, start, end, enum: "SectionType"):
    new_line = line[start] + sections[SectionType.TITLE] + line[end]
    return new_line
    # If multiple lines, split list and add bottom to new list before extending with new lines, then add old lines again

def remove_name_spaces(file_name):
    new_name = file_name.replace(" ", "_")
    new_name.join(".html")
    return new_name
