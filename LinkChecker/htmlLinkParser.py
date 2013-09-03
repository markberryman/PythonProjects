import link
from html.parser import HTMLParser

class HTMLLinkParser(HTMLParser):
    """Parses HTML markup and returns the number of discovered links "as-is" (i.e., no path transformations)"""
    def __init__(self):
        super().__init__(self)
        self.links = set()

    # tag and attribute values are automatically lowercased
    def handle_starttag(self, tag, attrs):
        newLink = None

        if (tag == "a"):
            newLink = self.__process_anchor_tag(attrs)
                        
        if (tag == "link"):
            newLink = self.__process_link_tag(attrs)

        if (tag == "script"):
            newLink = self.__process_script_tag(attrs)

        if (tag == "img"):
            newLink = self.__process_image_tag(attrs)

        # handling tags that don't have a link (i.e., bad markup)
        if (newLink is not None):
            self.links.add(newLink)

    @staticmethod
    def __process_anchor_tag(attrs):
        newLink = None

        for attr in attrs:
            attrName, attrValue = attr

            if (attrName == "href"):
                newLink = link.Link(attrValue, link.LinkType.ANCHOR)

        return newLink

    @staticmethod
    def __process_link_tag(attrs):
        newLink = None
        newLinkHrefValue = None
        isStyleSheetLink = False

        for attr in attrs:
            attrName, attrValue = attr

            if (attrName == "href"):
                newLinkHrefValue = attrValue

            if (attrName == "rel"):
                if (attrValue == "stylesheet"):
                    isStyleSheetLink = True

        if (isStyleSheetLink):
            newLink = link.Link(newLinkHrefValue, link.LinkType.STYLESHEET)

        return newLink

    @staticmethod
    def __process_script_tag(attrs):
        newLink = None

        for attr in attrs:
            attrName, attrValue = attr

            if (attrName == "src"):
                newLink = link.Link(attrValue, link.LinkType.SCRIPT)

        return newLink

    @staticmethod
    def __process_image_tag(attrs):
        newLink = None

        for attr in attrs:
            attrName, attrValue = attr

            if (attrName == "src"):
                newLink = link.Link(attrValue, link.LinkType.IMAGE)

        return newLink