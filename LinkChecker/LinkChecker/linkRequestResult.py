import http.client


class LinkRequestResult(object):
    """Represents result of requesting a link."""
    def __init__(self, link_url, statusCode, responseData):
        self.__link_url = link_url
        self.__statusCode = statusCode
        self.__responseData = responseData

    @property
    def value(self):
        return self.__link_url

    @property
    def responseData(self):
        return self.__responseData

    @property
    def statusCode(self):
        return self.__statusCode

    def is_link_broken(self):
        return ((self.__statusCode < http.client.OK) or
                (self.__statusCode >= http.client.BAD_REQUEST))
