from weasyprint import HTML, CSS
import os
from file_handling import css_file_path

def render_pdf(html_file):
    html = HTML(string=html_file)
    css = CSS(filename=css_file_path())

    pdf_path = os.path.join("pdf_output", html_file.pdf_name)

    html.write_pdf(pdf_path, stylesheets=[css])
