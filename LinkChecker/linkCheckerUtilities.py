import html.parser

class linkCheckerUtilities(object):
    """Various utility methods"""

    @staticmethod
    def get_links_from_markup(markup, htmlLinkParser):
        """Returns the new links detected from processing a link."""
        if (markup is None):
            return None

        # todo - convert relative links to absolute links
        try:
            htmlLinkParser.feed(markup)
        except html.parser.HTMLParseError:
            print("Invalid markup!")        
        
        print("Processed markup and found {} links".format(len(htmlLinkParser.links)))
                            
        return htmlLinkParser.links