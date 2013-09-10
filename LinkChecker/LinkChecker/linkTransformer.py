import link

class LinkTransformer(object):
    """Abstract class for defining link transformers."""

    def transform(self, link):
        raise NotImplementedError()

class RelativeLinkTransformer(LinkTransformer):
    """Transforms relative links to absolute links."""
    def __init__(self, currentLink):
        self.currentLink = currentLink
        
    def transform(self, link):
        if ((link.value.lower().startswith("http://") == False) and
            (link.value.lower().startswith("mailto:") == False)):
            link.value = "{}/{}".format(self.currentLink.value, link.value)

        return link