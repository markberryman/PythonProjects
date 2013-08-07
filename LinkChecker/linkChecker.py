import http.client
# todo - understand how this "from" keyword works
from urllib.parse import urlparse

class LinkParser:
    def parse_links(self, markup):
        links = set()
        # todo - parse the markup for links
        # todo - patch up relative paths to include a host value
        print("Parse links returning {0} links".format(len(links)))
        return links

class PageGetter:
    def _parse_url(self, url):
        urlParts = urlparse(url)
        netloc = urlParts.netloc
        path = urlParts.path

        return netloc, path

    def _request_url(self, host, path):
        conn = http.client.HTTPConnection(host)
        conn.request("GET", path)

        return conn.getresponse()
        
    def get_page(self, url):
        print("Getting url \"{0}\"".format(url))

        host, path = self._parse_url(url)
        res = self._request_url(host, path)
        statusCode = res.status

        print("Response status = {0}".format(statusCode))

        if ((statusCode < 200) and (statusCode >= 400)):
            return None
        
        return res.read()        

class LinkChecker:
    def __init__(self, startLink, depth):
        self.startLink = startLink
        self.depth = depth
        self.pageGetter = PageGetter()
        self.linkParser = LinkParser()
        self.numLinksProcessed = 0
        self.brokenLinks = set()

    def __repr__(self):
        return "Started with link: {0}. Processed {1} links.".format(
            self.startLink, self.numLinksProcessed)

    def check_links(self):
        links = set()
        links.add(self.startLink)

        while (self.depth >= 0):
            nextSetOfLinks = set()
            
            for link in links:
                markup = self.pageGetter.get_page(link)

                if (markup == None):
                    self.brokenLinks.add(link)
                
                self.numLinksProcessed += 1
                newLinks = self.linkParser.parse_links(markup)
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
linkChecker.check_links()

print(linkChecker)
