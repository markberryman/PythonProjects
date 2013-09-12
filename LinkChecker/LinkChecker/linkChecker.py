import html.parser
import link
import pLinkProcessor


class LinkChecker:
    def __init__(self, resourceGetter, linkProcessor):
        self.resourceGetter = resourceGetter
        self.linkProcessor = linkProcessor
        self.linksRequested = set()
        self.brokenLinks = set()
        self.invalidMarkupLinks = set()
        self.pLinkProcessor = pLinkProcessor.PLinkProcessor(
            20, self.resourceGetter.get_resource)
        self.workItemsSubmitted = 0

    def print_results(self, results):
        print("Results:")
        print("Number of links checked = {}".
              format(len(results["linksRequested"])))

        self.__print_links(results["linksRequested"])

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
        links = sorted(links)

        for l in links:
            print(">>> {}".format(l))

    def __check_links_helper2(self, startLink, depth):
        self.pLinkProcessor.add_work(startLink)
        numActiveWorkItems = 1

        while (numActiveWorkItems > 0):
            # we block here
            statusCode, markup, processedLink = self.pLinkProcessor.get_result()

            self.linksRequested.add(processedLink.value)

            numActiveWorkItems -= 1

            print("{} --> {}".format(statusCode, processedLink.value))

            # todo - consider setting status code inside of get_result
            processedLink.resultStatusCode = statusCode

            if (processedLink.is_link_broken() is False):
                if (processedLink.type == link.LinkType.ANCHOR):
                    if (processedLink.depth <= depth):
                        try:
                            newLinks = self.linkProcessor.process_link(
                                processedLink, markup)

                            for nl in newLinks:
                                # todo - check to see if we've previously
                                # requested this link
                                nl.depth = processedLink.depth + 1
                                self.pLinkProcessor.add_work(nl)
                                numActiveWorkItems += 1
                        except html.parser.HTMLParseError:
                            self.invalidMarkupLinks.add(processedLink.value)
                else:
                    self.brokenLinks.add(processedLink.value)


    #def __check_links_helper(self, linksToProcess, depth):
    #    """Checks the provided set of links to a specified depth."""
    #    if (depth != 0):

    #        for linkToProcess in linksToProcess:
    #            if linkToProcess.value not in self.linksRequested:
    #                self.linksRequested.add(linkToProcess.value)

    #                statusCode, markup = self.resourceGetter.get_resource(
    #                    linkToProcess)

    #                linkToProcess.resultStatusCode = statusCode

    #                if (linkToProcess.is_link_broken() is False):
    #                    if (linkToProcess.type == link.LinkType.ANCHOR):
    #                        try:
    #                            newLinks = self.linkProcessor.process_link(
    #                                linkToProcess, markup)

    #                            print(
    #                                "Processed markup, found {} links".format(
    #                                    len(newLinks)))

    #                            self.__check_links_helper(newLinks, depth - 1)
    #                        except html.parser.HTMLParseError:
    #                            self.invalidMarkupLinks.add(linkToProcess)
    #                else:
    #                    self.brokenLinks.add(linkToProcess)

    #    return None

    def check_links(self, linksToProcess, depth):
        self.pLinkProcessor.start()
        self.__check_links_helper2(linksToProcess.pop(), depth)

        return {
            "linksRequested": self.linksRequested,
            "brokenLinks": self.brokenLinks,
            "invalidMarkupLinks": self.invalidMarkupLinks
            }
