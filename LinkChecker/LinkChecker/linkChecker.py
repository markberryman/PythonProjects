import http.client
import html.parser
import link


class LinkChecker:
    def __init__(
            self, resourceGetter, linkProcessor, pLinkRequester, maxDepth):
        self.resourceGetter = resourceGetter
        self.linkProcessor = linkProcessor
        self.linksRequested = set()
        self.brokenLinks = set()
        self.invalidMarkupLinks = set()
        self.pLinkRequester = pLinkRequester
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

    def __check_links_helper(self, startLink):
        linksToProcess = [startLink]

        # breadth-first search of links
        for depth in range(self.maxDepth):
            # give work
            print("\nProcessing {} link(s) at depth {}."
                  .format(len(linksToProcess), depth + 1))

            while (len(linksToProcess) > 0):
                linkToProcess = linksToProcess.pop()
                self.pLinkRequester.add_work(linkToProcess)

            # get results; blocking until all link processing completed
            print("\nAwaiting results...\n")
            linkProcessingResults = self.pLinkRequester.get_results()

            for processedLink in linkProcessingResults:
                print("[{}] {}\n  --> {}".format(processedLink.statusCode,
                                          http.client.responses[processedLink.statusCode].upper(),
                                          processedLink.value))

                self.linksRequested.add(processedLink.value)

                if (processedLink.is_link_broken() is False):
                    if (processedLink.type == link.LinkType.ANCHOR):
                        try:
                            newLinks = self.linkProcessor.process_link(
                                processedLink)

                            for nl in newLinks:
                                # this check is a lookup in a set object
                                # and a set is implemented as a hashtable so
                                # it should be fast - O(n) on average
                                if (nl.value not in self.linksRequested):
                                    linksToProcess.append(nl)
                        except html.parser.HTMLParseError:
                            self.invalidMarkupLinks.add(processedLink.value)
                else:
                    self.brokenLinks.add(processedLink.value)

    def check_links(self, startLink):
        self.pLinkRequester.start()
        self.__check_links_helper(startLink)

        return {
            "linksRequested": self.linksRequested,
            "brokenLinks": self.brokenLinks,
            "invalidMarkupLinks": self.invalidMarkupLinks
            }
