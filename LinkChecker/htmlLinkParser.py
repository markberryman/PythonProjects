from html.parser import HTMLParser

class HTMLLinkParser(HTMLParser):
    """Parses HTML markup and returns the number of discovered links "as-is" (i.e., no path transformations)"""
    def __init__(self):
        super().__init__(self)
        self.links = set()

    # tag and attribute values are automatically lowercased
    def handle_starttag(self, tag, attrs):
        # todo - what type of tags do we want to look for?
        if (tag == "a"):
            for attr in attrs:
                # todo - use list comprehension to make this cleaner
                attrName, attrValue = attr

                if (attrName == "href"):
                    # todo - should do the link union here for optimization
                    self.links.add(attrValue)