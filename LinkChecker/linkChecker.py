class LinkParser:
    def ParseLinks(self, markup):
        links = set()
        # todo - parse the markup for links
        print("Parse links returning {0} links".format(len(links)))
        return links

class PageGetter:
    def __init__(self, page):
        self.page = page

    def GetPage(self):
        print("Getting page \"{0}\"".format(self.page))
        # todo - get the page
        return "page markup"

class LinkChecker:
    def __init__(self, startLink):
        self.startLink = startLink

    def __repr__(self):
        return "Starting link: {0}".format(self.startLink)

    def CheckLinks(self):
        pageGetter = PageGetter(self.startLink)
        markup = pageGetter.GetPage()
        linkParser = LinkParser()
        links = linkParser.ParseLinks(markup)
        
        # todo - add new links to set to parse
        # todo - repeat until no links left
        return
        

# todo - take a single input param that's the page to start with
startLink = "http://www.markwberryman.com"

print("Starting link checking with \"{0}\"".format(startLink))

linkChecker = LinkChecker(startLink)
linkChecker.CheckLinks()

print(linkChecker)
