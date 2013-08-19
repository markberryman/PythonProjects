import contentRequester
import linkChecker
import linkRequester
import pageGetter
import htmlLinkParser

# todo - take input param that's the start page and link depth
startLink = "http://www.markwberryman.com"
depth = 1

print("Starting link checking with \"{0}\" and depth {1}".format(startLink, depth))

linkParser = htmlLinkParser.HTMLLinkParser()
contRequester = contentRequester.ContentRequester()
pageGetter = pageGetter.PageGetter(contRequester)
requester = linkRequester.LinkRequester(pageGetter)

checker = linkChecker.LinkChecker(startLink, depth, linkParser, requester)
checker.check_links()

checker.print_results()

input('Press Enter to exit')