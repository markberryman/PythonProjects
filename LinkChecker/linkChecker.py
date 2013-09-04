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
        else:
            print("No broken links.")

        print("Number of links with invalid markup = {}".
              format(len(self.invalidMarkupLinks)))

        if (len(self.invalidMarkupLinks) > 0):
            print("Invalid markup links:")

            self.__print_links(self.invalidMarkupLinks)
        else:
            print("No links with invalid markup.")

    def __print_links(self, links):
        for link in links:
            print(">>> {}".format(link.value))

    def check_links(self, linksToProcess, depth):
        """Checks the provided set of links to a specified depth."""
        if (depth != 0):
            for linkToProcess in linksToProcess:                
                statusCode, markup = self.resourceGetter.get_resource(linkToProcess)

                if (self.__is_link_broken(statusCode) == False):
                    if (linkToProcess.type == link.LinkType.ANCHOR):
                        htmlLinkParser = self.htmlLinkParserFactory.create_html_link_parser()

                        try:
                            newLinks = linkCheckerUtilities.linkCheckerUtilities.get_links_from_markup(markup, htmlLinkParser)
                            filteredLinks = self.linkFilter.filter_links(newLinks)
                            self.check_links(filteredLinks, depth - 1)
                        except html.parser.HTMLParseError:
                            self.invalidMarkupLinks.add(linkToProcess)
                else:
                    self.brokenLinks.add(linkToProcess)

            self.numLinksProcessed += len(linksToProcess)

        return None

    def __is_link_broken(self, statusCode):
        result = False

        if ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST)):
            result = True

        return result