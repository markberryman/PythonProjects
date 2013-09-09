import contentRequester
import htmlLinkParserFactory
import link
import linkChecker
import linkFilter
import markupProcessor
import resourceGetter
import htmlLinkParser

startLink = link.Link("http://www.markwberryman.com", link.LinkType.ANCHOR)
depth = 2

print("Starting link checking with \"{}\" and depth {}".format(startLink.value, depth))

linkParserFactory = htmlLinkParserFactory.HtmlLinkParserFactory()
contRequester = contentRequester.ContentRequester()
resourceGetter = resourceGetter.ResourceGetter(contRequester)
linkFilters = set([linkFilter.MailToFilter(), linkFilter.DomainCheckFilter(startLink.value)])
mp = markupProcessor.MarkupProcessor(linkFilters, linkParserFactory)

checker = linkChecker.LinkChecker(resourceGetter, mp)

checker.check_links(set([startLink]), depth)

checker.print_results()

input('Press Enter to exit')