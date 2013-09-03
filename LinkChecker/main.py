import contentRequester
import htmlLinkParserFactory
import link
import linkChecker
import linkFilter
import linkRequester
import pageGetter
import htmlLinkParser

startLink = link.Link("http://www.markwberryman.com", link.LinkType.ANCHOR)
depth = 2

print("Starting link checking with \"{}\" and depth {}".format(startLink, depth))

linkParserFactory = htmlLinkParserFactory.HtmlLinkParserFactory()
contRequester = contentRequester.ContentRequester()
pageGetter = pageGetter.PageGetter(contRequester)
requester = linkRequester.LinkRequester(pageGetter)
linkFilter = linkFilter.LinkFilter()

checker = linkChecker.LinkChecker(linkParserFactory, requester, linkFilter)

checker.check_links(set([startLink]), depth)

checker.print_results()

input('Press Enter to exit')