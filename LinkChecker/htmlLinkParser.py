from html.parser import HTMLParser

class HTMLLinkParser(HTMLParser):
    """Parses HTML markup and returns the number of discovered links "as-is" (i.e., no path transformations)"""
    def __init__(self):
        super().__init__(self)
        self.links = set()

    # tag and attribute values are automatically lowercased
    def handle_starttag(self, tag, attrs):        
        if (tag == "a"):
            for attr in attrs:
                attrName, attrValue = attr

                if (attrName == "href"):                    
                    self.links.add(attrValue)