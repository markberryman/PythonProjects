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
        return "page markup"

class LinkChecker:
    def __init__(self, startLink, depth):
        self.startLink = startLink
        self.depth = depth
        self.pageGetter = PageGetter()
        self.linkParser = LinkParser()

    def __repr__(self):
        return "Starting link: {0}".format(self.startLink)

    def CheckLinks(self):
        markup = self.pageGetter.GetPage(self.startLink)
        links = self.linkParser.ParseLinks(markup)

        # iterate over the links until max depth reached
        while (self.depth > 0):
            nextSetOfLinks = set()
            
            for link in links:
                markup = self.pageGetter.GetPage(link)
                newLinks = self.linkParser.ParseLinks(markup)
                nextSetOfLinks.union(newLinks)

            links.union(nextSetOfLinks)
        
            self.depth -= 1;

        return
        

# todo - take input param that's the start page and link depth
startLink = "http://www.markwberryman.com"
depth = 1

print("Starting link checking with \"{0}\" and depth {1}".format(startLink, depth))

linkChecker = LinkChecker(startLink, depth)
linkChecker.CheckLinks()

print(linkChecker)
