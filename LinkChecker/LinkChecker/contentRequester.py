import http.client
from urllib.parse import urlparse

class ContentRequester(object):
    """Requests content from url."""
    def request_url(self, url):
        urlParts = urlparse(url)

        conn = http.client.HTTPConnection(urlParts.netloc)
        conn.request("GET", urlParts.path)

        return conn.getresponse()

