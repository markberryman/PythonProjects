import contentRequester

class PageGetter:
    """Gets a web page and returns its content"""
    def __init__(self, contRequester):
        self.contRequester = contRequester
        
    def get_page(self, url):
        print("Getting url \"{0}\"".format(url))

        res = self.contRequester.request_url(url)
        statusCode = res.status

        print("Response status = {0}".format(statusCode))

        responseBytes = res.read()
                
        return statusCode, responseBytes.decode()