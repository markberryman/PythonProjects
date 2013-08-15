import htmlLinkParser
import pageGetter
import http.client

class LinkChecker:
    def __init__(self, startLink, depth, pageGetter_ = None, htmlLinkParser_ = None):
        self.startLink = startLink
        self.depth = depth

        self.pageGetter = pageGetter.PageGetter() \
            if pageGetter_ is None \
            else pageGetter_
        self.htmlLinkParser = htmlLinkParser.HTMLLinkParser() \
            if htmlLinkParser_ is None \
            else htmlLinkParser_
        
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

    def get_link(self, link):
        """Returns a boolean indicating if the link is broken and the markup returned by the link."""
        isLinkBroken = False
        statusCode, markup = self.pageGetter.get_page(link)

        if ((statusCode < http.client.OK) or (statusCode >= http.client.BAD_REQUEST)):
            isLinkBroken = True

        return isLinkBroken, markup

    def process_link(self, markup):
        """Returns the new links contained in the provided markup."""
        self.htmlLinkParser.feed(markup)
        print("Parse links returning {0} links".format(len(self.htmlLinkParser.links)))      
        
        return self.htmlLinkParser.links

    def check_links(self):
        """Loops through the link checking, stopping at the specified depth."""
        links = set()
        links.add(self.startLink)

        while (self.depth >= 0):
            nextSetOfLinks = set()
            
            for link in links:
                self.numLinksProcessed += 1

                # todo - should we block leaving the root domain?
                isLinkBroken, markup = self.get_link(link)
                
                if (isLinkBroken == False):
                    newLinks = self.process_link(markup)
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