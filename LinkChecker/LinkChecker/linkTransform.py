from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse


class LinkTransform(object):
    """Abstract class for defining link transformers."""

    def transform(self, context, newLink):
        raise NotImplementedError()


class LowerCaseTransform(LinkTransform):
    """Lower cases parts of url that don't alter semantics."""
    def transform(self, context, newLink):
        urlparts = urlparse(newLink.value)
        # have to explicitly create a tuple to pass to urlunparse
        # b/c we can't modify the values on the urlparts obj directly
        newLink.value = urlunparse(
            (urlparts.scheme.lower(), urlparts.netloc.lower(),
             urlparts.path.lower(), urlparts.params,
             urlparts.query, urlparts.fragment))


class RelativeLinkTransform(LinkTransform):
    """Transforms relative links to absolute links."""
    def transform(self, context, newLink):
        currentLink = context["currentLink"]

        newLink.value = urljoin(currentLink.value, newLink.value)