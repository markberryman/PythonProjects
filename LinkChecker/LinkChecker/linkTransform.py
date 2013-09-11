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
        urlparts = urlparse(currentLink.value)

        # absolute link, nothing to touch
        if (newLink.value.lower().startswith("http")):
            return

        if (newLink.value.lower().startswith("mailto:")):
            return

        if (urlparts.path == ""):
            newLink.value = "{}/{}".format(currentLink.value, newLink.value)
            return

        if ((urlparts.netloc == "") and (("/" in urlparts.path) is False)):
            newLink.value = "{}/{}".format(currentLink.value, newLink.value)
            return

        if (urlparts.path.endswith("/")):
            # note that we're not joining the two strings w/ a slash here to
            # prevent a double slash
            newLink.value = "{}{}".format(currentLink.value, newLink.value)
            return

        if (urlparts.path.endswith("/") is False):
            indexOfFinalSlash = currentLink.value.rfind("/")
            newLink.value = "{}/{}".format(
                currentLink.value[:indexOfFinalSlash], newLink.value)
            return
