class linkCheckerUtilities(object):
    """Various utility methods"""

    def get_links_from_markup(self, markup, htmlLinkParser):
        """Returns the new links detected from processing a link."""
        if (markup is None):
            return None

        # todo - convert relative links to absolute links
        htmlLinkParser.feed(markup)
        
        print("Processed markup and found {0} links".format(len(htmlLinkParser.links)))
                            
        return htmlLinkParser.links