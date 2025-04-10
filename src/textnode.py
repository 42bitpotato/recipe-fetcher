from enum import Enum

class SectionType(Enum):
    TITLE = "title"
    DESCR = "description"
    IMAGE = "image"
    INGRE = "ingredients"
    INSTR = "instructions"

class ContentType(Enum):
    TEXT = "text"
    UOLIST = "unordered list"
    OLIST = "ordered list"
    IMAGE = "image"

class RecipeHead():
    def __init__(self, title, sections=dict()):
        self.title = title
        self.pdf_name = title.replace(" ", "_") + ".pdf"
        self.sections = sections

    def __repr__(self):
        return f"RecipeHead({self.title}, {self.sections})"
    
    def __eq__(self, other):
        if isinstance(other, RecipeHead):
            return (self.title == other.title and 
                    self.sections == other.sections)
        return False
    
    def to_html(self):
        from text_to_html import text_to_html
        return text_to_html(self)

# Not in use

class ContentSection():
    def __init__(self, section_type, value=[]):
        self.section_type = section_type
        self.value = value

    def __repr__(self):
        return f"ContentSection({self.section_type}, {self.value})"
    
    def __eq__(self, other):
        if isinstance(other, ContentSection):
            return (self.section_type == other.section_type and 
                    self.value == other.value)
        return False