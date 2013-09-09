class LinkFilterProcessor:
    """Applies filters to a set of Links."""
    @staticmethod
    def apply_filters(filters, links):
        if (len(filters) == 0):
            return links

        filter = filters.pop()

        linksToFilter = set([link for link in links if filter.should_filter(link.value)])

        return LinkFilterProcessor.apply_filters(filters, links.difference(linksToFilter))