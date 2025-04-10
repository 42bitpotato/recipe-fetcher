from weasyprint import HTML, CSS
import os
from file_handling import css_file_path
from textnode import RecipeHead

def render_pdf(recipe_head: "RecipeHead"):
    html_template = recipe_head.to_html()

    html = HTML(string=html_template)
    css = CSS(filename=css_file_path())

    pdf_path = os.path.join("pdf_output", recipe_head.pdf_name)

    html.write_pdf(pdf_path, stylesheets=[css])
