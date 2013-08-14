import htmlLinkParser
import pageGetter

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

    # todo - unit test this by injecting dependencies
    def process_link(self, link):
        result = None
        markup = self.pageGetter.get_page(link)

        if (markup != None):
            # todo - instead of instantiating an HTMLLinkParser each time; re-use one
            parser = htmlLinkParser.HTMLLinkParser()
            parser.feed(markup)
            print("Parse links returning {0} links".format(len(parser.links)))
            result = parser.links
        
        return result

    def check_links(self):
        links = set()
        links.add(self.startLink)

        while (self.depth >= 0):
            nextSetOfLinks = set()
            
            for link in links:
                self.numLinksProcessed += 1

                # todo - should we block leaving the root domain?
                newLinks = self.process_link(link)
                
                # using None as special indicator that the link was broken
                # if the link had no new links to follow, we'd get back
                # an empty set
                if (newLinks == None):
                    self.brokenLinks.add(link)
                                
                nextSetOfLinks.union(newLinks)
                
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