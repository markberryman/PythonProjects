class MarkupProcessor(object):
    """Processes markup."""

    def __init__(self, html_link_parser):
        self._html_link_parser = html_link_parser

    def get_links_from_markup(self, markup):
        """Returns links from provided markup."""
        if (markup is None):
            return set()

        self._html_link_parser.feed(markup)

        return self._html_link_parser.links
