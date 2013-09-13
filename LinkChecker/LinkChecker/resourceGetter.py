import link


class ResourceGetter:
    def __init__(self, contRequester):
        self.contRequester = contRequester

    def get_resource(self, linkToProcess):
        """Gets a web page and returns its content"""
        responseData = None

        res = self.contRequester.request_url(linkToProcess.value)

        linkToProcess.resultStatusCode = res.status

        # only want to fetch the content of anchor links
        if (linkToProcess.type == link.LinkType.ANCHOR):
            try:
                linkToProcess.responseData = res.read().decode()
            except UnicodeDecodeError:
                # going to hit this when an anchor link refers to a binary
                # resource (e.g. pdf file); instead of trying to filter
                # out all of these extensions, just swallow the exception
                # and move on for now
                pass

        return responseData
