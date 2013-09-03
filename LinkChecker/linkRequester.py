import http.client
import resourceGetter

class LinkRequester:
    """Requests a link using the provided page getter."""
    def __init__(self, pageGetter):
        self.pageGetter = pageGetter

    def get_link(self, link):
        """Returns markup from requested link."""
        return self.pageGetter.get_page(link)

        #if ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST)):
        #    # using a return value of None to indicate to calling code
        #    # that the link was broken
        #    markup = None

        #return markup