class LinkFilter(object):
    """Filters out links based on the filter_links method."""

    def filter_links(self, links):
        linksToFilterOut = set()

        for link in links:
            if (link.lower().startswith("mailto:")):
                linksToFilterOut.add(link)

        return links.difference(linksToFilterOut)