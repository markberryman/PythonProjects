import contentRequester
import link

class ResourceGetter:
    """Gets a web page and returns its content"""
    def __init__(self, contRequester):
        self.contRequester = contRequester
        
    def get_page(self, linkToProcess):
        print("Getting url \"{0}\"".format(linkToProcess.value))

        res = self.contRequester.request_url(linkToProcess.value)
        statusCode = res.status

        print("Response status = {0}".format(statusCode))

        # only want to fetch the content of anchor links
        if (linkToProcess.type == link.LinkType.ANCHOR):
            responseBytes = res.read()
            
            return statusCode, responseBytes.decode()

        return statusCode, None