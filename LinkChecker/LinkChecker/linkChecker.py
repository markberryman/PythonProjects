import http.client
import html.parser
import link
import linkCheckerUtilities
import resourceGetter

class LinkChecker:
    def __init__(self, htmlLinkParserFactory, resourceGetter, linkFilters):
        self.htmlLinkParserFactory = htmlLinkParserFactory
        self.resourceGetter = resourceGetter
        self.linkFilters = linkFilters
        self.linksProcessed = set()
        self.brokenLinks = set()
        self.invalidMarkupLinks = set()

    def get_results(self):
        return {
                "linksProcessed": self.linksProcessed,
                "brokenLinks": self.brokenLinks,
                "invalidMarkupLinks": self.invalidMarkupLinks
                }

    def print_results(self):
        results = self.get_results()

        print("Results:")
        print("Number of links checked = {}".
              format(len(results["linksProcessed"])))

        print("Number of broken links = {}".
              format(len(results["brokenLinks"])))

        if (len(results["brokenLinks"]) > 0):
            print("Broken links:")
            self.__print_links(results["brokenLinks"])

        print("Number of links with invalid markup = {}".
              format(len(results["invalidMarkupLinks"])))

        if (len(results["invalidMarkupLinks"]) > 0):
            print("Invalid markup links:")
            self.__print_links(results["invalidMarkupLinks"])

    def __print_links(self, links):
        for link in links:
            print(">>> {}".format(link.value))

    def __is_link_broken(self, statusCode):
        return ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST))

    def check_links(self, linksToProcess, depth):
        """Checks the provided set of links to a specified depth."""
        if (depth != 0):

            for linkToProcess in linksToProcess:
                if linkToProcess.value.lower() not in self.linksProcessed:
                    self.linksProcessed.add(linkToProcess.value.lower())

                    statusCode, markup = self.resourceGetter.get_resource(linkToProcess)

                    if (self.__is_link_broken(statusCode) == False):
                        if (linkToProcess.type == link.LinkType.ANCHOR):
                            htmlLinkParser = self.htmlLinkParserFactory.create_html_link_parser()

                            try:
                                newLinks = linkCheckerUtilities.linkCheckerUtilities.get_links_from_markup(markup, htmlLinkParser)

                                if (self.linkFilters is not None):
                                    linksToFilter = set()

                                    for filter in self.linkFilters:
                                        for newLink in newLinks:
                                            if filter.shouldFilter(newLink.value):
                                                linksToFilter.add(newLink)

                                        newLinks = newLinks.difference(linksToFilter)
        
                                self.check_links(newLinks, depth - 1)
                            except html.parser.HTMLParseError:
                                self.invalidMarkupLinks.add(linkToProcess)
                    else:
                        self.brokenLinks.add(linkToProcess)

        return None    