
        

class SectionNode():
    def __init__(self, section, content_nodes):
        self.section = section
        self.content = content_nodes

class ContentNode():
    def __init__(self, type, value):
        self.type = type
        self.value = value