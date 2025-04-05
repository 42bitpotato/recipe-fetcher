import os
import shutil
from textnode import RecipeHead

def text_to_html(recipe_text: "RecipeHead"):
    pass

def copy_template(recipe, template_path=None, destination_path=None):
    template_path = "html_template" if template_path == None else template_path
    destination_path = "pdf_recipes" if destination_path == None else destination_path

    if not os.path.exists(template_path):
        raise ValueError(f'Template path not found: "{template_path}", please create directory if missing')
    if not os.path.exists(destination_path):
        raise ValueError(f'Destination path not found: "{destination_path}", please create directory if missing')

    template_path_content = os.listdir(path=template_path)
    destination_path_content = os.listdir(path=destination_path)

    new_template_name = remove_name_spaces(recipe)

    for i in destination_path_content:
        if i == new_template_name:
            path = os.path.join(destination_path, i)
            os.remove(path)


def remove_name_spaces(file_name):
    new_name = file_name.replace(" ", "_")
    new_name.join(".html")
    return new_name
