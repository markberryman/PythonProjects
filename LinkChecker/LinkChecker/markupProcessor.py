class MarkupProcessor(object):
    """Processes markup."""

    def __init__(self, html_link_parser):
        self._html_link_parser = html_link_parser

    def get_links_from_markup(self, markup):
        """Returns links from provided markup."""
        if (markup is None):
            return set()

        return self._html_link_parser.parse_markup(markup)
