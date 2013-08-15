import http.client
import pageGetter

class LinkRequester:
    """Requests a link using the provided page getter."""
    def __init__(self, pageGetter_ = None):
        self.pageGetter = pageGetter.PageGetter() \
            if pageGetter_ is None \
            else pageGetter_

    def get_link(self, link):
        """Returns a boolean indicating if the link is broken and the markup returned by the link."""
        isLinkBroken = False
        statusCode, markup = self.pageGetter.get_page(link)

        if ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST)):
            isLinkBroken = True

        return isLinkBroken, markup