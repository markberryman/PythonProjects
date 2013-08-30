import contentRequester
import htmlLinkParserFactory
import linkChecker
import linkRequester
import pageGetter
import htmlLinkParser

# todo - take input param that's the start page and link depth
startLink = "http://www.markwberryman.com"
depth = 1

print("Starting link checking with \"{}\" and depth {}".format(startLink, depth))

linkParserFactory = htmlLinkParserFactory.HtmlLinkParserFactory()
contRequester = contentRequester.ContentRequester()
pageGetter = pageGetter.PageGetter(contRequester)
requester = linkRequester.LinkRequester(pageGetter)

checker = linkChecker.LinkChecker(linkParserFactory, requester)

checker.check_links(set([startLink]), 1)

checker.print_results()

input('Press Enter to exit')