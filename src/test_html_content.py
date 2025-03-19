import unittest
import os
from bs4 import BeautifulSoup
from html_content import *

html_path = os.path.join("test_env", "html_file.html")
file = open(html_path, "r")

soup = BeautifulSoup(file, "html.parser")

url = "https://www.koket.se/lax-med-sandefjordsas-och-citronfankal"

class TestTextNode(unittest.TestCase):
    def test_HTMLFile(self):
        html_file_url = get_html(url)

        self.assertTrue(len(html_file_url.content) == 5)
        # self.assertEqual(html_file_url, )