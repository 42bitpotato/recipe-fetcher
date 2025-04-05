import os
import shutil
from textnode import RecipeHead

def text_to_html(recipe_text: "RecipeHead"):
    html_template = copy_template()

    sections = section_dictionary(recipe_text)

    html_template_split = html_template.splitlines()
    
    for line_num in range(html_template_split):
        strip_line = html_template_split[line_num].strip() # Remove leading and trailing whitespaces

        # Title
        if strip_line.startswith("<title>"):
            for c in html_template_split[line_num]:
                if c == ">":
                    pass

def copy_template(template_dir=None):
    template_dir = "html_template" if template_dir == None else template_dir

    html_template_path = os.path.join(template_dir, "template.html")

    if os.path.exists(html_template_path):
        with open(html_template_path, "r") as template_file:
            html_template = template_file.read()
    else:
        raise ValueError(f'HTML template file not found: "{html_template_path}"')
    
    return html_template

def section_dictionary(recipe_head):
    pass


def remove_name_spaces(file_name):
    new_name = file_name.replace(" ", "_")
    new_name.join(".html")
    return new_name

def copy_template_1(recipe_name, template_path=None, destination_path=None):
    template_path = "html_template" if template_path == None else template_path
    destination_path = "pdf_recipes" if destination_path == None else destination_path

    html_template_path = os.path.join(template_dir, "template.html")
    css_template = os.path.join(template_dir, "style.css")

    if not os.path.exists(template_path):
        raise ValueError(f'Template path not found: "{template_path}", please create directory if missing')
    if not os.path.exists(destination_path):
        raise ValueError(f'Destination path not found: "{destination_path}", please create directory if missing')

    template_path_content = os.listdir(path=template_path)
    destination_path_content = os.listdir(path=destination_path)

    new_template_name = remove_name_spaces(recipe)
    new_template_path = os.path.join(destination_path, new_template_name)

    for i in template_path_content:
        if i == "template.html":
            path = os.path.join(template_path, i)
            for j in destination_path_content:
                if j == new_template_name:
                    rm_path = os.path.join(destination_path, j)
                    os.remove(rm_path)
            shutil.copy(path, new_template_path)