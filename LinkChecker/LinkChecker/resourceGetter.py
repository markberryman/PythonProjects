import http.client
import link
import socket


class ResourceGetter:
    def __init__(self, contRequester):
        self.contRequester = contRequester

    def get_resource(self, linkToProcess):
        """Request link and sets the response status and response
        on the linkToProcess object."""
        if (linkToProcess is None):
            raise TypeError("linkToProcess can not be None.")

        try:
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
        except socket.error as msg:
            # not decoding the msg error code value to a meaningful
            # http status code; since we're primarily hitting timeouts
            # we'll go w/ that
            print("Socket error making request: " + str(msg))
            linkToProcess.resultStatusCode = http.client.GATEWAY_TIMEOUT
