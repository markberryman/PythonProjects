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
        result = True

        if ((urlparse(link).hostname is not None) and
            (self.baseHostname is not None)):
            linkHostnameSegments = urlparse(link).hostname.split(".")
            baseHostnameSegments = self.baseHostname.split(".")

            # handle the intranet case as well w/ this check
            if (urlparse(link).hostname == self.baseHostname):
                result = False
            else:
                if ((len(linkHostnameSegments) >= 2) and
                    (len(baseHostnameSegments) >= 2)):
                    if ((linkHostnameSegments[len(linkHostnameSegments) - 1] == baseHostnameSegments[len(baseHostnameSegments) - 1]) and
                        (linkHostnameSegments[len(linkHostnameSegments) - 2] == baseHostnameSegments[len(baseHostnameSegments) - 2])):
                        result = False

        return result
