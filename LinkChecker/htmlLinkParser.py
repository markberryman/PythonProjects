from html.parser import HTMLParser

class HTMLLinkParser(HTMLParser):
    """Parses HTML markup and returns the number of discovered links "as-is" (i.e., no path transformations)"""
    def __init__(self):
        super().__init__(self)
        self.links = set()

    # tag and attribute values are automatically lowercased
    def handle_starttag(self, tag, attrs):
        link = None

        if (tag == "a"):
            link = self.__process_anchor_tag(attrs)
                        
        if (tag == "link"):
            link = self.__process_link_tag(attrs)

        # handling tags that don't have a link
        if (link is not None):
            self.links.add(link)

    @staticmethod
    def __process_anchor_tag(attrs):
        link = None

        for attr in attrs:
            attrName, attrValue = attr

            if (attrName == "href"):
                link = attrValue

        return link

    @staticmethod
    def __process_link_tag(attrs):
        link = None
        isStyleSheetLink = False

        for attr in attrs:
            attrName, attrValue = attr

            if (attrName == "href"):
                link = attrValue

            if (attrName == "rel"):
                if (attrValue == "stylesheet"):
                    isStyleSheetLink = True

        if (isStyleSheetLink):
            return link