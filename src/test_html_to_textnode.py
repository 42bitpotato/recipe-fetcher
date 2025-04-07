import unittest
import os
from bs4 import BeautifulSoup
from html_content import *
from html_to_textnode import title_to_textnode, description_to_textnode, ingredients_to_textnode, instructions_to_textnode, image_to_textnode, html_to_textnode
from textnode import *

html_path = os.path.join("test_env", "html_file.html")
file = open(html_path, "r")

soup = BeautifulSoup(file, "html.parser")

url = "https://www.koket.se/lax-med-sandefjordsas-och-citronfankal"

html_file = get_html(url)

class TestTextNode(unittest.TestCase):
    def test_title_to_textnode(self):
        # html_file = get_html(url) # HTMLFile(soup)

        html_title_node = html_file.content[0]
        html_title = html_title_node.html

        title = title_to_textnode(html_title)

        self.assertEqual(title, "Lax med sandefjordsås och citronfänkål")

    def test_description_to_textnode(self):
        # html_file = get_html(url) # HTMLFile(soup)

        html_description_node = html_file.content[1]
        html_description = html_description_node.html

        description = description_to_textnode(html_description)

        self.assertEqual(description, "Ugnsbakad lax med underbar sås och frisk och krispig sallad. En middag som är lätt att laga där fisken sköter sig själv i ugnen, såsen kokar snabbt ihop med grädde, citron och smör och salladen blir krispig och god med färsk fänkål och citron.")

    def test_ingredients_to_textnode(self):
        # html_file = get_html(url) # HTMLFile(soup)

        html_ingredients_node = html_file.content[2]
        html_ingredients = html_ingredients_node.html

        ingredients = ingredients_to_textnode(html_ingredients)
        
        self.assertEqual(ingredients, ['700 g röding, i portionsbitar (eller laxfilé)', 
                                       '2 tsk olivolja', 
                                       '1,5 dl grädde', 
                                       '1,5 dl crème fraîche', 
                                       '150 g smör, tärnat', 
                                       '50 g regnbågsrom', 
                                       '1 knippe färsk gräslök, finhackad', 
                                       '1 citron', '2 fänkål', '0,5 gurka', 
                                       '1 knippe färsk dill, finhackad (spara några vippor till garnering)', 
                                       '900 g delikatesspotatis', 
                                       'salt', 'svartpeppar, nymalen']
                                       )
        
    def test_instructions_to_textnode(self):
        # html_file = get_html(url) # HTMLFile(soup)

        html_instructions_node = html_file.content[3]
        html_instructions = html_instructions_node.html

        instructions = instructions_to_textnode(html_instructions)

        self.assertEqual(instructions, ["Sätt ugnen på 150 grader varmluft.", 
                                        "Skiva fänkål så tunt du kan, gärna med mandolin. Riv över zest från citronen och pressa saften över, spara lite saft till såsen. På med finhackad dill och rör om. Låt stå.", 
                                        "Koka potatisen i lättsaltat vatten, håll varmt.", 
                                        "Salta och peppra fisken. Pensla med olivolja och tillaga i ugnen tills fiskens innertemperatur är 48-50 grader, ca 15-18 minuter.", 
                                        "Kärna ur gurkan och skär i små tärningar.", 
                                        "Koka upp grädde i en liten kastrull. Vispa ner crème fraiche och låt få ett uppkok. Ta av från värmen. Vispa ner lite smör i taget, smaka av med citron, salt och peppar. Tillsätt hälften av rommen samt hackad gräslök, rör om och smaka av med lite citron.", 
                                        "Servera den bakade fisken med sandefjordsås, citronfänkål, gurka och potatis."])
        
    def test_image_to_textnode(self):
        html_image_node = html_file.content[4]
        html_image = html_image_node.html

        no_url_txt = '<source sizes="(min-width: 1025px) 50vw, 100vw" srcset="https://img.koket.se/wide-mini/lax-med-sandefjordsas-och-citronfankal.png.jpg 88w, https://img.koket.se/wide-small/lax-med-sandefjordsas-och-citronfankal.png.jpg 192w, https://img.koket.se/wide-medium/lax-med-sandefjordsas-och-citronfankal.png.jpg 400w, https://img.koket.se/wide-large/lax-med-sandefjordsas-och-citronfankal.png.jpg 608w, https://img.koket.se/wide-giant/lax-med-sandefjordsas-och-citronfankal.png.jpg 816w, https://img.koket.se/wide-mega/lax-med-sandefjordsas-och-citronfankal.png.jpg 1224w" type="image/jpeg"/>'
        no_url = BeautifulSoup(no_url_txt, "html.parser")

        image = image_to_textnode(html_image)

        self.assertEqual(image, "https://img.koket.se/wide-giant/lax-med-sandefjordsas-och-citronfankal.png.jpg")

        with self.assertRaises(ValueError):
            image_to_textnode(no_url)

    def test_html_to_textnode(self):
        recipe_head = html_to_textnode(html_file)

        used_sections = {section for section in recipe_head.sections.keys()}
        all_sections = set(SectionType)

        self.assertTrue(all_sections.issubset(used_sections))