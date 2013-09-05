import contentRequester
import link

class ResourceGetter:
    def __init__(self, contRequester):
        self.contRequester = contRequester
        
    def get_resource(self, linkToProcess):
        """Gets a web page and returns its content"""
        responseData = None

        print("Getting url \"{0}\"".format(linkToProcess.value))

        res = self.contRequester.request_url(linkToProcess.value)
        statusCode = res.status

        print("Response status = {0}".format(statusCode))

        # only want to fetch the content of anchor links
        if (linkToProcess.type == link.LinkType.ANCHOR):
            responseData = res.read().decode()
            
        return statusCode, responseData