from enum import Enum

class SectionType(Enum):
    TITLE = "title"
    DESCR = "description"
    IMAGE = "image"
    INGRE = "ingredients"
    INSTR = "instructions"

class ContentType(Enum):
    TEXT = "text"
    

# Parent
class SectionNode():
    def __init__(self, section, content_nodes):
        self.section = section
        self.content = content_nodes

# Child
class ContentNode():
    def __init__(self, type, value):
        self.type = type
        self.value = value