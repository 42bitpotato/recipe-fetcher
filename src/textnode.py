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
        self.sections = sections

    def __repr__(self):
        return f"RecipeHead({self.title}, {self.sections})"
    
    def __eq__(self, other):
        if isinstance(other, RecipeHead):
            return (self.title == other.title and 
                    self.sections == other.sections)
        return False

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