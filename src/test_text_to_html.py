import unittest
import os
from test_html_to_textnode import html_file, recipe_head
from text_to_html import text_to_html

class TestTextToHTML(unittest.TestCase):
    def test_text_to_html(self):

        html_recipe = text_to_html(recipe_head)
        
        if os.path.exists("html_template/template_test.html"):
            with open("html_template/template_test.html", "r") as template_file:
                html_test_template = template_file.read()
        else:
            raise ValueError(f'HTML template file not found: "html_template/template_test.html"')

        self.assertEqual(html_test_template, html_recipe)
