import requests
import re
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return HTMLFile(soup)

class HTMLContent():
    def __init__(self, type, html):
          self.type = type
          self.html = html

    def __repr__(self):
        return f"HTMLContent({self.type}, {self.html})"

class HTMLFile():
    def __init__(self, html):
        self._html = html
        self.content = []
        
        self.extract_title()
        self.extract_description()
        self.extract_ingredients()
        self.extract_instructions()
        self.extract_image()

    def __repr__(self):
        return f"HTMLFile(HTML, {self.content})"

    def extract_title(self):
        title = self._html.find_all("h1", class_=re.compile("title"))
        self.content.append(HTMLContent("title", title))

    def extract_description(self):
        description = self._html.find_all("div", class_=re.compile("description"))
        self.content.append(HTMLContent("description", description))

    def extract_ingredients(self):
        ingredients = self._html.find_all("span", class_=re.compile("ingredient"))
        self.content.append(HTMLContent("ingredients", ingredients))

    def extract_instructions(self):
        instructions = self._html.find_all("span", class_=re.compile("instruction"))
        self.content.append(HTMLContent("instructions", instructions))

    def extract_image(self):
        image = self._html.find_all("source", srcset=True)
        self.content.append(HTMLContent("image", image))
    