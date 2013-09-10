import html.parser
import link
import linkProcessor


class LinkChecker:
    def __init__(self, resourceGetter, linkProcessor):
        self.resourceGetter = resourceGetter
        self.linkProcessor = linkProcessor
        self.linksRequested = set()
        self.brokenLinks = set()
        self.invalidMarkupLinks = set()

    def print_results(self, results):
        print("Results:")
        print("Number of links checked = {}".
              format(len(results["linksRequested"])))

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

    def __check_links_helper(self, linksToProcess, depth):
        """Checks the provided set of links to a specified depth."""
        if (depth != 0):

            for linkToProcess in linksToProcess:
                if linkToProcess.value.lower() not in self.linksRequested:
                    self.linksRequested.add(linkToProcess.value.lower())

                    statusCode, markup = self.resourceGetter.get_resource(
                        linkToProcess)

                    linkToProcess.resultStatusCode = statusCode

                    if (linkToProcess.is_link_broken() is False):
                        if (linkToProcess.type == link.LinkType.ANCHOR):
                            try:
                                newLinks = self.linkProcessor.process_link(
                                    linkToProcess, markup)

                                print(
                                    "Processed markup, found {} links".format(
                                        len(newLinks)))

                                self.__check_links_helper(newLinks, depth - 1)
                            except html.parser.HTMLParseError:
                                self.invalidMarkupLinks.add(linkToProcess)
                    else:
                        self.brokenLinks.add(linkToProcess)

        return None

    def check_links(self, linksToProcess, depth):
        self.__check_links_helper(linksToProcess, depth)

        return {
            "linksRequested": self.linksRequested,
            "brokenLinks": self.brokenLinks,
            "invalidMarkupLinks": self.invalidMarkupLinks
            }
