class LinkFilterProcessor(object):
    """Filters links based on a supplied set of filters."""

    def __init__(self, filters):
        self.filters = filters

    def apply_filters(self, links):
        """Applies filters to links."""
        if (len(self.filters) == 0):
            return links

        filter = self.filters.pop()

        linksToFilter = set([link for link in links if filter.should_filter(link.value)])

        return self.apply_filters(links.difference(linksToFilter))
