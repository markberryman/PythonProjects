import urlRequester
import htmlLinkParser
import link
import linkChecker
import linkFilter
import linkFilterProcessor
import linkProcessor
import linkTransform
import linkTransformProcessor
import linkType
import markupProcessor
import pLinkRequester
import queue
import resourceGetter

startLink = link.Link(
    #"http://www.microsoft.com/en-us/default.aspx", link.LinkType.ANCHOR)
    #"http://www.markwberryman.com/", link.LinkType.ANCHOR)
    "http://apigee.com/about/customers/bechtel-improving-workforce-efficiency-and-productivity-through-apis", linkType.LinkType.ANCHOR)

depth = 2

print("Starting link checking with \"{}\" and depth {}".format(
    startLink.url, depth))

contRequester = urlRequester.UrlRequester()
resourceGetter = resourceGetter.ResourceGetter(contRequester)
linkFilters = set(
    [linkFilter.MailToFilter(), linkFilter.DomainCheckFilter(startLink.url)])
linkTransformers = [linkTransform.RelativeLinkTransform(),
                    linkTransform.LowerCaseTransform()]
html_link_parser = htmlLinkParser.HTMLLinkParser()
linkFilterProcessor = linkFilterProcessor.LinkFilterProcessor(linkFilters)
linkTransformProcessor = linkTransformProcessor.LinkTransformProcessor(
    linkTransformers)
linkProcessor = linkProcessor.LinkProcessor(
    linkFilterProcessor, linkTransformProcessor, html_link_parser)
pLinkRequester = pLinkRequester.PLinkRequester(
    3, resourceGetter.get_resource, queue.Queue(), queue.Queue())

checker = linkChecker.LinkChecker(
    resourceGetter, linkProcessor, pLinkRequester, depth)

results = checker.check_links(startLink)

checker.print_results(results)

input('Press Enter to exit')
