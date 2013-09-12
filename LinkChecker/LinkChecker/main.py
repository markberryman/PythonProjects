import contentRequester
import htmlLinkParserFactory
import link
import linkChecker
import linkFilter
import linkFilterProcessor
import linkProcessor
import linkTransform
import linkTransformProcessor
import markupProcessor
import pLinkRequester
import resourceGetter

startLink = link.Link(
    #"http://www.microsoft.com/en-us/default.aspx", link.LinkType.ANCHOR)
    "http://www.markwberryman.com/", link.LinkType.ANCHOR)
depth = 2

print("Starting link checking with \"{}\" and depth {}".format(
    startLink.value, depth))

linkParserFactory = htmlLinkParserFactory.HtmlLinkParserFactory()
contRequester = contentRequester.ContentRequester()
resourceGetter = resourceGetter.ResourceGetter(contRequester)
linkFilters = set(
    [linkFilter.MailToFilter(), linkFilter.DomainCheckFilter(startLink.value)])
linkTransformers = [linkTransform.RelativeLinkTransform(),
                    linkTransform.LowerCaseTransform()]
markupProcessor = markupProcessor.MarkupProcessor(linkParserFactory)
linkFilterProcessor = linkFilterProcessor.LinkFilterProcessor(linkFilters)
linkTransformProcessor = linkTransformProcessor.LinkTransformProcessor(
    linkTransformers)
linkProcessor = linkProcessor.LinkProcessor(
    markupProcessor, linkFilterProcessor, linkTransformProcessor)
pLinkRequester = pLinkRequester.PLinkRequester(
    3, resourceGetter.get_resource)

checker = linkChecker.LinkChecker(
    resourceGetter, linkProcessor, pLinkRequester, depth)

results = checker.check_links(startLink)

checker.print_results(results)

input('Press Enter to exit')
