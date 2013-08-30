import linkRequester
import linkCheckerUtilities
import pageGetter

class LinkChecker:
    def __init__(self, htmlLinkParserFactory, linkRequester):
        self.htmlLinkParserFactory = htmlLinkParserFactory
        self.linkRequester = linkRequester
        self.numLinksProcessed = 0
        self.brokenLinks = set()

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

    def check_links(self, linksToProcess, depth):
        """Checks the provided set of links to a specified depth."""
        if (depth != 0):
            for link in linksToProcess:
                # todo - should we block leaving the root domain?
                markup = self.linkRequester.get_link(link)

                if (markup is None):
                    self.brokenLinks.add(link)
        
                htmlLinkParser = self.htmlLinkParserFactory.create_html_link_parser()

                newLinks = linkCheckerUtilities.linkCheckerUtilities.get_links_from_markup(markup, htmlLinkParser)

                self.check_links(newLinks, depth - 1)

            self.numLinksProcessed += len(linksToProcess)

        return None