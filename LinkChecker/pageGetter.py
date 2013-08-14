import contentRequester
import http.client

class PageGetter:
    """Gets a web page and returns its content"""
    def __init__(self, requester = None):
        if (requester is None):
            self.requester = contentRequester.ContentRequester()
        else:
            self.requester = requester
        
    def get_page(self, url):
        print("Getting url \"{0}\"".format(url))

        res = self.requester.request_url(url)
        statusCode = res.status

        print("Response status = {0}".format(statusCode))

        if ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST)):
            return None

        # todo - use the correct encoding based on the response headers
        responseBytes = res.read()
        
        return responseBytes.decode("utf-8")