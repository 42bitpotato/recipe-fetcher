from html_content import HTMLFile
from textnode import *

from bs4 import BeautifulSoup



def html_to_textnode(html_file):
    if len(html_file.content) == 0:
        raise ValueError(f"Missing content: {html_file.content}")
    
def title_to_textnode(html_title):
    string = str(html_title.string)
    return ContentChildNode(string.strip())

def description_to_textnode(html_description):
    string = str(html_description.p.string)
    return ContentChildNode(string.strip())
    