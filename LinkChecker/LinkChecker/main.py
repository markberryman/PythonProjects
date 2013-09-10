import contentRequester
import htmlLinkParserFactory
import link
import linkChecker
import linkFilter
import linkFilterProcessor
import linkProcessor
import linkTransformer
import linkTransformersProcessor
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
linkTransformers = [linkTransformer.RelativeLinkTransform()]
markupProcessor = markupProcessor.MarkupProcessor(linkParserFactory)
linkFilterProcessor = linkFilterProcessor.LinkFilterProcessor(linkFilters)
linkTransformersProcessor = linkTransformersProcessor.LinkTransformersProcessor(linkTransformers)
linkProcessor = linkProcessor.LinkProcessor(markupProcessor, linkFilterProcessor, linkTransformersProcessor)

checker = linkChecker.LinkChecker(resourceGetter, linkProcessor)

results = checker.check_links(set([startLink]), depth)

checker.print_results(results)

input('Press Enter to exit')