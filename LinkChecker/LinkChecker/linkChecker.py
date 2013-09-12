import html.parser
import link


class LinkChecker:
    def __init__(self, resourceGetter, linkProcessor, pLinkRequester, maxDepth):
        self.resourceGetter = resourceGetter
        self.linkProcessor = linkProcessor
        self.linksRequested = set()
        self.brokenLinks = set()
        self.invalidMarkupLinks = set()
        self.pLinkRequester = pLinkRequester
        self.workItemsSubmitted = 0
        self.maxDepth = maxDepth

    def print_results(self, results):
        print("")
        print("Results:")
        print("Number of links checked = {}".
              format(len(results["linksRequested"])))

        self.__print_links(results["linksRequested"])

        print("")
        print("Number of broken links = {}".
              format(len(results["brokenLinks"])))

        if (len(results["brokenLinks"]) > 0):
            print("Broken links:")
            self.__print_links(results["brokenLinks"])

        print("")
        print("Number of links with invalid markup = {}".
              format(len(results["invalidMarkupLinks"])))

        if (len(results["invalidMarkupLinks"]) > 0):
            print("Invalid markup links:")
            self.__print_links(results["invalidMarkupLinks"])

    def __print_links(self, links):
        links = sorted(links)

        for l in links:
            print("* {}".format(l))

    def __check_links_helper2(self, startLink):
        self.pLinkRequester.add_work(startLink)
        numActiveWorkItems = 1

        while (numActiveWorkItems > 0):
            # we block here
            markup, processedLink = self.pLinkRequester.get_result()

            self.linksRequested.add(processedLink.value)

            numActiveWorkItems -= 1

            print("{} --> {}".format(processedLink.resultStatusCode, processedLink.value))

            if (processedLink.is_link_broken() is False):
                if (processedLink.type == link.LinkType.ANCHOR):
                    if (processedLink.depth < self.maxDepth):
                        try:
                            newLinks = self.linkProcessor.process_link(
                                processedLink, markup)

                            for nl in newLinks:
                                if (nl.value not in self.linksRequested):
                                    nl.depth = processedLink.depth + 1
                                    self.pLinkRequester.add_work(nl)
                                    numActiveWorkItems += 1
                        except html.parser.HTMLParseError:
                            self.invalidMarkupLinks.add(processedLink.value)
            else:
                self.brokenLinks.add(processedLink.value)

    def check_links(self, startLink):
        self.pLinkRequester.start()
        self.__check_links_helper2(startLink)

        return {
            "linksRequested": self.linksRequested,
            "brokenLinks": self.brokenLinks,
            "invalidMarkupLinks": self.invalidMarkupLinks
            }
