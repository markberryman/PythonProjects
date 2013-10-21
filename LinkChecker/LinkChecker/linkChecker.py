import http.client
import html.parser
import link
import linkRequest


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

    @staticmethod
    def _is_link_broken(status_code):
        return ((status_code < http.client.OK) or
                (status_code >= http.client.BAD_REQUEST))

    def __check_links_helper(self, startLink):
        linksToProcess = [startLink]

        # breadth-first search of links
        for depth in range(1, self.maxDepth + 1):
            # give work
            print("\nProcessing {} link(s) at depth {}."
                  .format(len(linksToProcess), depth))

            while (len(linksToProcess) > 0):
                linkToProcess = linksToProcess.pop()
                # don't need to read response for last link depth b/c we're not
                # continuing processing
                shouldReadResponse = ((linkToProcess.type == link.LinkType.ANCHOR) and
                                      (depth < self.maxDepth))
                linkRequestWorkItem = linkRequest.LinkRequest(linkToProcess.value, shouldReadResponse)
                self.pLinkRequester.add_work(linkRequestWorkItem)

            # get results; blocking until all link processing completed
            print("\nAwaiting results...\n")
            linkRequestResults = self.pLinkRequester.get_results()

            for linkRequestResult in linkRequestResults:
                print("[{}] {}\n  --> {}".format(linkRequestResult.status_code,
                                          http.client.responses[linkRequestResult.status_code].upper(),
                                          linkRequestResult.value))

                self.linksRequested.add(linkRequestResult.value)

                if (LinkChecker._is_link_broken(linkRequestResult.status_code) is False):
                    if (linkRequestResult.response is not None):
                        try:
                            newLinks = self.linkProcessor.process_link(
                                linkRequestResult)

                            for nl in newLinks:
                                # this check is a lookup in a set object
                                # and a set is implemented as a hashtable so
                                # it should be fast - O(n) on average
                                if (nl.value not in self.linksRequested):
                                    linksToProcess.append(nl)
                        except html.parser.HTMLParseError:
                            self.invalidMarkupLinks.add(linkRequestResult.value)
                else:
                    self.brokenLinks.add(linkRequestResult.value)

    def check_links(self, startLink):
        self.pLinkRequester.start()
        self.__check_links_helper(startLink)

        return {
            "linksRequested": self.linksRequested,
            "brokenLinks": self.brokenLinks,
            "invalidMarkupLinks": self.invalidMarkupLinks
            }
