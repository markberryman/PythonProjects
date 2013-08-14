import htmlLinkParser
import pageGetter
import http.client

class LinkChecker:
    def __init__(self, startLink, depth, pageGetter):
        self.startLink = startLink
        self.depth = depth
        self.pageGetter = pageGetter
        self.numLinksProcessed = 0
        self.brokenLinks = set()

    def __repr__(self):
        return "Started with link: {0}. Processed {1} links.".format(self.startLink, self.numLinksProcessed)

    def print_results(self):
        print("Results:")
        print("Started with link: {0}".format(self.startLink))
        print("Number of links checked = {0}".
              format(self.numLinksProcessed))
        print("Number of broken links = {0}".
              format(len(self.brokenLinks)))

        if (len(self.brokenLinks) > 0):
            print("Broken links:")

            for link in self.brokenLinks:
                print(">>> {0}".format(link))
        else:
            print("No broken links.")

    def process_link(self, link):
        """Returns a boolean indicating if the links is broken and the new links discovered."""
        isLinkBroken = False
        statusCode, markup = self.pageGetter.get_page(link)

        if ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST)):
            isLinkBroken = True
        else:
            # todo - instead of instantiating an HTMLLinkParser each time; re-use one
            parser = htmlLinkParser.HTMLLinkParser()
            parser.feed(markup)
            print("Parse links returning {0} links".format(len(parser.links)))      
        
        return isLinkBroken, parser.links

    def check_links(self):
        links = set()
        links.add(self.startLink)

        while (self.depth >= 0):
            nextSetOfLinks = set()
            
            for link in links:
                self.numLinksProcessed += 1

                # todo - should we block leaving the root domain?
                isLinkBroken, newLinks = self.process_link(link)

                if (isLinkBroken == False):
                    nextSetOfLinks.union(newLinks)
                else:
                    self.brokenLinks.add(link)                  
                
            # toss out the processed links and get ready
            # to process the next set of links
            # todo - add optimization to record links we've
            # previously visited in case they come up again
            links = nextSetOfLinks.copy()

            # todo - convert relative links to absolute links
        
            self.depth -= 1

        return
        

# todo - take input param that's the start page and link depth
startLink = "http://www.markwberryman.com"
depth = 1

print("Starting link checking with \"{0}\" and depth {1}".format(startLink, depth))

linkChecker = LinkChecker(startLink, depth, pageGetter.PageGetter())
linkChecker.check_links()

linkChecker.print_results()

input('Press Enter to exit')