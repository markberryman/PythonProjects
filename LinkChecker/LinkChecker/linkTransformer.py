import link
from urllib.parse import urlparse

class LinkTransformer(object):
    """Abstract class for defining link transformers."""

    def transform(self, link):
        raise NotImplementedError()

class RelativeLinkTransformer(LinkTransformer):
    """Transforms relative links to absolute links."""
    def __init__(self, currentLink):
        self.currentLink = currentLink
        
    def transform(self, link):
        if (link.value.lower().startswith("http://") == False):
            link.value = "{}/{}".format(self.currentLink.value, link.value)

        return link