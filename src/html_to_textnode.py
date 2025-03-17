from html_content import HTMLFile
from bs4 import BeautifulSoup

def html_to_textnode(html_file):
    if len(html_file.content) == 0:
        raise ValueError(f"Missing content: {html_file.content}")
    
def title_to_textnode(html_title):
    tag = html_title.h1
    string = tag.string
    return string
    