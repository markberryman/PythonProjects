import http.client
# todo - understand how this "from" keyword works
from urllib.parse import urlparse

class PageGetter:
    """Gets a web page and returns its content"""
    def _parse_url(self, url):
        urlParts = urlparse(url)
        netloc = urlParts.netloc
        path = urlParts.path

        return netloc, path

    def _request_url(self, host, path):
        conn = http.client.HTTPConnection(host)
        conn.request("GET", path)

        return conn.getresponse()
        
    def get_page(self, url):
        print("Getting url \"{0}\"".format(url))

        host, path = self._parse_url(url)
        res = self._request_url(host, path)
        statusCode = res.status

        print("Response status = {0}".format(statusCode))

        if ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST)):
            return None

        # todo - use the correct encoding based on the response headers
        responseBytes = res.read()
        
        return responseBytes.decode("utf-8")