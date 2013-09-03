import contentRequester
import htmlLinkParserFactory
import link
import linkChecker
import linkFilter
import linkRequester
import resourceGetter
import htmlLinkParser

startLink = link.Link("http://www.markwberryman.com", link.LinkType.ANCHOR)
depth = 2

print("Starting link checking with \"{}\" and depth {}".format(startLink, depth))

linkParserFactory = htmlLinkParserFactory.HtmlLinkParserFactory()
contRequester = contentRequester.ContentRequester()
resourceGetter = resourceGetter.ResourceGetter(contRequester)
requester = linkRequester.LinkRequester(resourceGetter)
linkFilter = linkFilter.LinkFilter()

checker = linkChecker.LinkChecker(linkParserFactory, requester, linkFilter)

checker.check_links(set([startLink]), depth)

checker.print_results()

input('Press Enter to exit')