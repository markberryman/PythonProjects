import linkType


class Link(object):
    """Represents a link to a resource"""

    def __init__(self, value, type=linkType.LinkType.ANCHOR):
        self.value = value
        self.type = type
