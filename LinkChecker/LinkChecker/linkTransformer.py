import link
from urllib.parse import urlparse

class LinkTransformer(object):
    """Abstract class for defining link transformers."""

    def transform(self, link):
        raise NotImplementedError()

class RelativeLinkTransformer(LinkTransformer):
    """Transforms relative links to absolute links."""
    def transform(self, currentLink, newLink):
        urlparts = urlparse(currentLink.value)

        # absolute link, nothing to touch
        if (newLink.value.lower().startswith("http")):
            return

        if (newLink.value.lower().startswith("mailto:")):
            return

        if (urlparts.path == ""):
            newLink.value = "{}/{}".format(currentLink.value, newLink.value)
            return

        if ((urlparts.netloc == "") and (("/" in urlparts.path) == False)):
            newLink.value = "{}/{}".format(currentLink.value, newLink.value)
            return

        if (urlparts.path.endswith("/")):
            # note that we're not joining the two strings w/ a slash here to
            # prevent a double slash
            newLink.value = "{}{}".format(currentLink.value, newLink.value)
            return

        if (urlparts.path.endswith("/") == False):
            indexOfFinalSlash = currentLink.value.rfind("/")
            newLink.value = "{}/{}".format(currentLink.value[:indexOfFinalSlash], newLink.value)
            return