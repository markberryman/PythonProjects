from urllib.parse import urlparse

class LinkFilter(object):
    """Abstract class defining for filtering links."""
    def should_filter(self, dataItem):
        raise NotImplementedError()

class MailToFilter(LinkFilter):
    def should_filter(self, link):
        return link.lower().startswith("mailto:")

class DomainCheckFilter(LinkFilter):
    def __init__(self, baseLink):
        self.baseHostname = urlparse(baseLink).hostname

    def should_filter(self, link):
        linkHostname = urlparse(link).hostname

        # no need to convet to lowercase; hostName attribute already does it
        return self.baseHostname != linkHostname