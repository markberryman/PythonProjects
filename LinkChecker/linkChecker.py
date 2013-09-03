import html.parser
import linkRequester
import linkCheckerUtilities
import pageGetter

class LinkChecker:
    def __init__(self, htmlLinkParserFactory, linkRequester, linkFilter):
        self.htmlLinkParserFactory = htmlLinkParserFactory
        self.linkRequester = linkRequester
        self.linkFilter = linkFilter
        self.numLinksProcessed = 0
        self.brokenLinks = set()
        self.invalidMarkupLinks = set()

    def __repr__(self):
        return "Processed {} links.".format(self.numLinksProcessed)

    def print_results(self):
        print("Results:")
        print("Number of links checked = {}".
              format(self.numLinksProcessed))
        print("Number of broken links = {}".
              format(len(self.brokenLinks)))

        if (len(self.brokenLinks) > 0):
            print("Broken links:")

            for link in self.brokenLinks:
                print(">>> {}".format(link))
        else:
            print("No broken links.")

        print("Number of links with invalid markup = {}".
              format(len(self.invalidMarkupLinks)))

        if (len(self.invalidMarkupLinks) > 0):
            print("Invalid markup links:")

            for link in self.invalidMarkupLinks:
                print(">>> {}".format(link))
        else:
            print("No links with invalid markup.")

    def check_links(self, linksToProcess, depth):
        """Checks the provided set of links to a specified depth."""
        if (depth != 0):
            for link in linksToProcess:                
                markup = self.linkRequester.get_link(link)

                if (markup is not None):
                    htmlLinkParser = self.htmlLinkParserFactory.create_html_link_parser()

                    try:
                        newLinks = linkCheckerUtilities.linkCheckerUtilities.get_links_from_markup(markup, htmlLinkParser)
                        newLinks = self.linkFilter.filter_links(newLinks)
                        self.check_links(newLinks, depth - 1)
                    except html.parser.HTMLParseError:
                        self.invalidMarkupLinks.add(link)
                else:
                    self.brokenLinks.add(link)

            self.numLinksProcessed += len(linksToProcess)

        return None