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
    def __init__(self, title, sections=[]):
        self.title = title
        self.sections = sections

    def __repr__(self):
        return f"RecipeHead({self.title}, {self.sections})"
    
    def __eq__(self, other):
        if isinstance(other, RecipeHead):
            return (self.title == other.title and 
                    self.sections == other.sections)
        return False

class SectionNode():
    def __init__(self, section_type, content_nodes=[]):
        self.section_type = section_type
        self.content = content_nodes

    def __repr__(self):
        return f"SectionNode({self.section_type}, {self.content})"
    
    def __eq__(self, other):
        if isinstance(other, SectionNode):
            return (self.section_type == other.section_type and 
                    self.content == other.content)
        return False

class ContentParentNode():
    def __init__(self, type, children):
        self.type = type
        self.children = children

    def __repr__(self):
        return f"ContentParentNode({self.type}, {self.children})"
    
    def __eq__(self, other):
        if isinstance(other, ContentParentNode):
            return (self.type == other.type and
                    self.children == other.children)
        return False

class ContentChildNode():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"ContentChildNode({self.value})"
    
    def __eq__(self, other):
        if isinstance(other, ContentChildNode):
            return self.value == other.value
        return False