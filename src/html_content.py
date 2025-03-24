import requests
import re
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return HTMLFile(soup, url)

class HTMLContent():
    def __init__(self, type, html):
          self.type = type
          self.html = html

    def __repr__(self):
        return f"HTMLContent({self.type}, {self.html})"
    
    def __eq__(self, other):
        if isinstance(other, HTMLContent):
            return (self.type == other.type and
                    self.html == other.html
                    )
        return False

class HTMLFile():
    def __init__(self, html, url):
        self._html = html
        self. _url = url
        self._title = str(self._html.find("h1", class_=re.compile("title")).string)
        self.content = []
        
        self.extract_title()
        self.extract_description()
        self.extract_ingredients()
        self.extract_instructions()
        self.extract_image()

    def __repr__(self):
        return f"HTMLFile({self._title}: {self._url}, {self.content})"
    
    def __eq__(self, other):
        if isinstance(other, HTMLFile):
            return (self._html == other._html and
                    self._url == other._url and
                    self._title == other._title and
                    self.content == other.content
                    )
        return False

    def extract_title(self):
        title = self._html.find("h1", class_=re.compile("title"))
        self.content.append(HTMLContent("title", title))

    def extract_description(self):
        description = self._html.find("div", class_=re.compile("description"))
        self.content.append(HTMLContent("description", description))

    def extract_ingredients(self):
        ingredients = self._html.find_all("span", class_=re.compile("ingredient"))
        self.content.append(HTMLContent("ingredients", ingredients))

    def extract_instructions(self):
        instructions = self._html.find_all("span", class_=re.compile("instruction"))
        self.content.append(HTMLContent("instructions", instructions))

    def extract_image(self):
        images = self._html.find_all("source", srcset=True, type="image/jpeg")
        self.content.append(HTMLContent("image", images))
    