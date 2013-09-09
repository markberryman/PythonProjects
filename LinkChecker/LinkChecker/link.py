class LinkType:
    ANCHOR = 1
    STYLESHEET = 2
    SCRIPT = 3
    IMAGE = 4

class Link(object):
    """Represents a link to a resource"""

    def __init__(self, value, type = LinkType.ANCHOR):
        self.value = value
        self.type = type