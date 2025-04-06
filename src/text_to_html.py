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

def copy_template(template_dir=None):
    template_dir = "html_template" if template_dir == None else template_dir

    html_template_path = os.path.join(template_dir, "template.html")

    if os.path.exists(html_template_path):
        with open(html_template_path, "r") as template_file:
            html_template = template_file.read()
    else:
        raise ValueError(f'HTML template file not found: "{html_template_path}"')
    
    return html_template

def add_text_to_line(html_template_split, line_num, enum: "SectionType"):
    line = html_template_split[line_num]
    # If multiple lines, split list and add bottom to new list before extending with new lines, then add old lines again

def remove_name_spaces(file_name):
    new_name = file_name.replace(" ", "_")
    new_name.join(".html")
    return new_name
