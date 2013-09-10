from urllib.parse import urlunparse


class LinkConverterUtility:
    @staticmethod
    def convert_relative_link_to_absolute_link(host, link):
        return host + link
