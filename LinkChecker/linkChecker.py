import http.client
import html.parser
import link
import linkCheckerUtilities
import resourceGetter

class LinkChecker:
    def __init__(self, htmlLinkParserFactory, resourceGetter, linkFilter):
        self.htmlLinkParserFactory = htmlLinkParserFactory
        self.resourceGetter = resourceGetter
        self.linkFilter = linkFilter
        self.numLinksProcessed = 0
        self.brokenLinks = set()
        self.invalidMarkupLinks = set()

        self.allLinksProcessed = set()

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
            self.__print_links(self.brokenLinks)

        print("Number of links with invalid markup = {}".
              format(len(self.invalidMarkupLinks)))

        if (len(self.invalidMarkupLinks) > 0):
            print("Invalid markup links:")
            self.__print_links(self.invalidMarkupLinks)

    def __print_links(self, links):
        for link in links:
            print(">>> {}".format(link.value))

    def __is_link_broken(self, statusCode):
        return ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST))

    def check_links(self, linksToProcess, depth):
        """Checks the provided set of links to a specified depth."""
        if (depth != 0):

            for linkToProcess in linksToProcess:
                if linkToProcess.value.lower() not in self.allLinksProcessed:
                    self.numLinksProcessed += 1
                    self.allLinksProcessed.add(linkToProcess.value.lower())

                    statusCode, markup = self.resourceGetter.get_resource(linkToProcess)

                    if (self.__is_link_broken(statusCode) == False):
                        if (linkToProcess.type == link.LinkType.ANCHOR):
                            htmlLinkParser = self.htmlLinkParserFactory.create_html_link_parser()

                            try:
                                newLinks = linkCheckerUtilities.linkCheckerUtilities.get_links_from_markup(markup, htmlLinkParser)

                                if (self.linkFilter is not None):
                                    newLinks = self.linkFilter.filter_links(newLinks)

                                self.check_links(newLinks, depth - 1)
                            except html.parser.HTMLParseError:
                                self.invalidMarkupLinks.add(linkToProcess)
                    else:
                        self.brokenLinks.add(linkToProcess)

        return None    