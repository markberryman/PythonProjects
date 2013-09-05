class linkCheckerUtilities(object):
    """Various utility methods"""

    @staticmethod
    def get_links_from_markup(markup, htmlLinkParser):
        """Returns the new links detected from processing a link."""
        if (markup is None):
            return None
                
        htmlLinkParser.feed(markup)
        
        print("Processed markup and found {} links".format(len(htmlLinkParser.links)))
                            
        return htmlLinkParser.links