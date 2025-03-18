import unittest
import os
from bs4 import BeautifulSoup
from html_content import *
from html_to_textnode import title_to_textnode
from textnode import *

html_path = os.path.join("test_env", "html_file.html")
file = open(html_path, "r")

soup = BeautifulSoup(file, "html.parser")

class TestTextNode(unittest.TestCase):
    def test_title_to_textnode(self):
        html_file = HTMLFile(soup)

        html_title_node = html_file.content[0]
        html_title = html_title_node.html

        title = title_to_textnode(html_title)

        self.assertEqual(title, ContentChildNode("Lax med sandefjordsås och citronfänkål"))