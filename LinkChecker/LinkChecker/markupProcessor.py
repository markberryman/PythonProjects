import htmlLinkParserFactory

class MarkupProcessor(object):
    """Processes markup, applies filters and returns links."""

    def __init__(self, filters, htmlLinkParserFactory):
        self.filters = filters
        self.htmlLinkParserFactory = htmlLinkParserFactory

    def apply_filters(self, links):
        """Applies filters to a set of links."""
        if (len(self.filters) == 0):
            return links

        filter = self.filters.pop()

        linksToFilter = set([link for link in links if filter.should_filter(link.value)])

        return self.apply_filters(links.difference(linksToFilter))

    def get_links_from_markup(self, markup):
        """Processes markup and returns links."""
        if (markup is None):
            return None

        htmlLinkParser = self.htmlLinkParserFactory.create_html_link_parser()

        htmlLinkParser.feed(markup)        

        return htmlLinkParser.links