import http.client


class LinkRequestResult(object):
    """Represents result of requesting a link."""
    def __init__(self, link_url, status_code, response):
        self.__link_url = link_url
        self.__status_code = status_code
        self.__response = response

    @property
    def value(self):
        return self.__link_url

    @property
    def response(self):
        return self.__response

    @property
    def status_code(self):
        return self.__status_code

    def is_link_broken(self):
        return ((self.__status_code < http.client.OK) or
                (self.__status_code >= http.client.BAD_REQUEST))
