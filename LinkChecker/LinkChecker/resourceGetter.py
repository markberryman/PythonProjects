import http.client
import link
import linkRequestResult
import socket


class ResourceGetter:
    def __init__(self, contRequester):
        self.contRequester = contRequester

    def get_resource(self, linkRequest):
        """Process the link request object."""
        if (linkRequest is None):
            raise TypeError("linkRequest can not be None.")

        resultStatusCode = None
        responseData = None
        url = linkRequest.link_url

        try:
            res = self.contRequester.request_url(url)

            resultStatusCode = res.status

            if (linkRequest.read_response):
                try:
                    responseData = res.read().decode()
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
            resultStatusCode = http.client.GATEWAY_TIMEOUT

        result = linkRequestResult.LinkRequestResult(
            url, resultStatusCode, responseData)

        return result
