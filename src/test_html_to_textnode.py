import unittest
import os
from bs4 import BeautifulSoup
from html_content import *
from html_to_textnode import title_to_textnode, description_to_textnode
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

    def test_description_to_textnode(self):
        html_file = HTMLFile(soup)

        html_description_node = html_file.content[1]
        html_description = html_description_node.html

        description = description_to_textnode(html_description)

        self.assertEqual(description, ContentChildNode("Ugnsbakad lax med underbar sås och frisk och krispig sallad. En middag som är lätt att laga där fisken sköter sig själv i ugnen, såsen kokar snabbt ihop med grädde, citron och smör och salladen blir krispig och god med färsk fänkål och citron."))
        