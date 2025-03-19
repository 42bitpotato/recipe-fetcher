import unittest
import os
from bs4 import BeautifulSoup
from html_content import *
from html_to_textnode import title_to_textnode, description_to_textnode, ingredients_to_textnode
from textnode import *

html_path = os.path.join("test_env", "html_file.html")
file = open(html_path, "r")

soup = BeautifulSoup(file, "html.parser")

url = "https://www.koket.se/lax-med-sandefjordsas-och-citronfankal"

class TestTextNode(unittest.TestCase):
    def test_title_to_textnode(self):
        html_file = get_html(url) # HTMLFile(soup)

        html_title_node = html_file.content[0]
        html_title = html_title_node.html

        title = title_to_textnode(html_title)

        self.assertEqual(title, ContentChildNode("Lax med sandefjordsås och citronfänkål"))

    def test_description_to_textnode(self):
        html_file = get_html(url) # HTMLFile(soup)

        html_description_node = html_file.content[1]
        html_description = html_description_node.html

        description = description_to_textnode(html_description)

        self.assertEqual(description, ContentChildNode("Ugnsbakad lax med underbar sås och frisk och krispig sallad. En middag som är lätt att laga där fisken sköter sig själv i ugnen, såsen kokar snabbt ihop med grädde, citron och smör och salladen blir krispig och god med färsk fänkål och citron."))

    def test_ingredients_to_textnode(self):
        html_file = get_html(url) # HTMLFile(soup)

        html_ingredients_node = html_file.content[2]
        html_ingredients = html_ingredients_node.html

        ingredients = ingredients_to_textnode(html_ingredients)
        
        self.assertEqual(ingredients, [ContentChildNode('700 g röding, i portionsbitar (eller laxfilé)'), 
                                       ContentChildNode('2 tsk olivolja'), 
                                       ContentChildNode('1,5 dl grädde'), 
                                       ContentChildNode('1,5 dl crème fraîche'), 
                                       ContentChildNode('150 g smör, tärnat'), 
                                       ContentChildNode('50 g regnbågsrom'), 
                                       ContentChildNode('1 knippe färsk gräslök, finhackad'), 
                                       ContentChildNode('1 citron'), ContentChildNode('2 fänkål'), ContentChildNode('0,5 gurka'), 
                                       ContentChildNode('1 knippe färsk dill, finhackad (spara några vippor till garnering)'), 
                                       ContentChildNode('900 g delikatesspotatis'), 
                                       ContentChildNode('salt'), ContentChildNode('svartpeppar, nymalen')]
                                       )