import unittest
import os
from bs4 import BeautifulSoup
from html_content import *

html_path = os.path.join("test_env", "html_file.html")
file = open(html_path, "r")

soup = BeautifulSoup(file, "html.parser")

class TestTextNode(unittest.TestCase):
    def test_HTMLFile(self):
        html_file = HTMLFile(soup)

        self.assertTrue(len(html_file.content) > 0)