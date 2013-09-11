class MarkupProcessor(object):
    """Processes markup and returns links."""

    def __init__(self, htmlLinkParserFactory):
        self.htmlLinkParserFactory = htmlLinkParserFactory

    def get_links_from_markup(self, markup):
        """Processes markup and returns links."""
        if (markup is None):
            return None

        htmlLinkParser = self.htmlLinkParserFactory.create_html_link_parser()

        htmlLinkParser.feed(markup)

        return htmlLinkParser.links
