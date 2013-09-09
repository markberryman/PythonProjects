from urllib.parse import urlparse

class LinkTransformer(object):
    """Abstract class for defining link transformers."""

    def transform(self, link):
        raise NotImplementedError()

class RelativeLinkTransformer(LinkTransformer):
    """Transforms relative links to absolute links."""

    def transform(self, currentLink, newLink):
        return newLink if newLink.lower().startswith("http://") else "{}/{}".format(currentLink, newLink)