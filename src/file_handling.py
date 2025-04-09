import os

def copy_template(template_dir=None):
    template_dir = "html_template" if template_dir == None else template_dir

    html_template_path = os.path.join(template_dir, "template.html")

    if os.path.exists(html_template_path):
        with open(html_template_path, "r") as template_file:
            html_template = template_file.read()
    else:
        raise ValueError(f'HTML template file not found: "{html_template_path}"')
    
    return html_template


def remove_name_spaces(file_name):
    new_name = file_name.replace(" ", "_")
    new_name.join(".html")
    return new_name

def copy_css(css_dir=None):
    css_dir = "html_template" if css_dir == None else css_dir

    css_template_path = os.path.join(css_dir, "style.css")

    if os.path.exists(css_template_path):
        with open(css_template_path, "r") as css_file:
            css_template = css_file.read()
    else:
        raise ValueError(f'CSS template file not found: "{css_template_path}"')
    
    return css_template

def css_file_path(css_dir=None):
    css_dir = "html_template" if css_dir == None else css_dir
    css_file_path = os.path.join(css_dir, "style.css")
    return css_file_path