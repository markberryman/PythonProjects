import contentRequester

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

        responseBytes = res.read()

        # todo - use the correct encoding based on the response headers        
        return statusCode, responseBytes.decode()