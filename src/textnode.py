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

class SectionNode():
    def __init__(self, section, content_nodes):
        self.section = section
        self.content = content_nodes

class ContentParentNode():
    def __init__(self, type, children):
        self.type = type
        self.children = children

class ContentChildNode():
    def __init__(self, value):
        self.value = value