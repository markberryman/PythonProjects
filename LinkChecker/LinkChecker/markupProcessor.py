import htmlLinkParserFactory
import linkCheckerUtilities
import linkFilterProcessor

class MarkupProcessor(object):
    """Processes markup and returns links."""

    def __init__(self, filters, htmlLinkParserFactory):
        self.filters = filters
        self.htmlLinkParserFactory = htmlLinkParserFactory

    def process_markup(self, markup):
        htmlLinkParser = self.htmlLinkParserFactory.create_html_link_parser()

        newLinks = linkCheckerUtilities.linkCheckerUtilities.get_links_from_markup(markup, htmlLinkParser)

        return linkFilterProcessor.LinkFilterProcessor.apply_filters(self.filters, newLinks)