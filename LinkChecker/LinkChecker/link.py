import http.client


class LinkType:
    ANCHOR = 1
    STYLESHEET = 2
    SCRIPT = 3
    IMAGE = 4


class Link(object):
    """Represents a link to a resource"""

    def __init__(self, value, type=LinkType.ANCHOR, depth=0):
        self.value = value
        self.type = type
        self.resultStatusCode = None
        self.depth = depth
        self.responseData = None

    def is_link_broken(self):
        return ((self.resultStatusCode < http.client.OK) or
                (self.resultStatusCode >= http.client.BAD_REQUEST))
