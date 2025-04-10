import os
import shutil
from bs4 import BeautifulSoup

from html_content import get_html
from html_to_textnode import html_to_textnode
from text_to_html import text_to_html
from render_pdf import render_pdf




def main():

    # Make list of url's
    url = "https://www.koket.se/lax-med-sandefjordsas-och-citronfankal"

    # Automate these two to save
    html = get_html(url) 
    textnode = html_to_textnode(html)

    render_pdf(textnode)

if __name__ == "__main__":
    main()