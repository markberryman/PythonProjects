class LinkParser:
    def ParseLinks(self, markup):
        links = set()
        # todo - parse the markup for links
        print("Parse links returning {0} links".format(len(links)))
        return links

class PageGetter:
    def GetPage(self, page):
        print("Getting page \"{0}\"".format(page))
        # todo - get the page
        # todo - track if the link is broken or not
        # we can return some special value to indicate the link
        # was broken
        return "page markup"

class LinkChecker:
    def __init__(self, startLink, depth):
        self.startLink = startLink
        self.depth = depth
        self.pageGetter = PageGetter()
        self.linkParser = LinkParser()
        self.numLinksProcessed = 0

    def __repr__(self):
        return "Started with link: {0}. Processed {1} links.".format(
            self.startLink, self.numLinksProcessed)

    def CheckLinks(self):
        links = set()
        links.add(self.startLink)

        while (self.depth >= 0):
            nextSetOfLinks = set()
            
            for link in links:
                markup = self.pageGetter.GetPage(link)
                self.numLinksProcessed += 1
                newLinks = self.linkParser.ParseLinks(markup)
                nextSetOfLinks.union(newLinks)

            # toss out the processed links and get ready
            # to process the next set of links
            links = nextSetOfLinks.copy()
        
            self.depth -= 1;

        return
        

# todo - take input param that's the start page and link depth
startLink = "http://www.markwberryman.com"
depth = 1

print("Starting link checking with \"{0}\" and depth {1}".format(startLink, depth))

linkChecker = LinkChecker(startLink, depth)
linkChecker.CheckLinks()

print(linkChecker)
