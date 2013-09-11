import http.client
from urllib.parse import urlparse


class ContentRequester(object):
    """Requests content from url."""
    def request_url(self, url):
        urlParts = urlparse(url)

        # need to include some user agent value otherwise
        # sites are rejecting the request
        headers = {"User-Agent": "linkChecker"}

        conn = http.client.HTTPConnection(urlParts.netloc)
        conn.request("GET", urlParts.path, body=None, headers=headers)

        return conn.getresponse()
