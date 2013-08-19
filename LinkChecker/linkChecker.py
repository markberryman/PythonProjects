import htmlLinkParser
import linkRequester
import linkCheckerUtilities
import pageGetter

class LinkChecker:
    def __init__(self, startLink, maxDepth, htmlLinkParser, linkRequester):
        self.startLink = startLink
        self.maxDepth = maxDepth
        self.htmlLinkParser = htmlLinkParser
        self.linkRequester = linkRequester
        self.numLinksProcessed = 0
        self.brokenLinks = set()

    def __repr__(self):
        return "Started with link: {}. Processed {} links.".format(self.startLink, self.numLinksProcessed)

    def print_results(self):
        print("Results:")
        print("Started with link: {}".format(self.startLink))
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

    # todo - add test; won't be unit tests though    
    def __check_links_helper(self, linksToProcess, curDepth):
        """Checks the provided set of links but not beyond the specified depth."""
        if (curDepth <= self.maxDepth):
            for link in linksToProcess:
                # todo - should we block leaving the root domain?
                markup = self.linkRequester.get_link(link)

                if (markup is None):
                    self.brokenLinks.add(link)
        
                newLinks = linkCheckerUtilities.linkCheckerUtilities.get_links_from_markup(markup, self.htmlLinkParser)

                self.__check_links_helper(newLinks, curDepth + 1)

            self.numLinksProcessed += len(linksToProcess)

        return None

    def check_links(self):
        """Loops through the link checking, stopping at the specified depth."""
        # todo - why can't i pass this directly
        linksToProcess = set()
        linksToProcess.add(self.startLink)

        self.__check_links_helper(linksToProcess, 1)
        
        return None