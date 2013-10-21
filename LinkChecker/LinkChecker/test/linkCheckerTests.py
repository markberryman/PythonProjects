import contentRequester
import htmlLinkParser
import link
import linkChecker
import linkFilter
import linkFilterProcessor
import linkTransform
import linkTransformProcessor
import linkProcessor
import markupProcessor
import pLinkRequester
import queue
import resourceGetter
import unittest


# these are more functional tests rather than unit tests
class LinkChecker_CheckLinksTests(unittest.TestCase):
    def test_FunctionalE2ETest(self):
        baseStartUrl = "http://localhost:35944"
        startLink = link.Link(baseStartUrl + "/index.html")
        depth = 3
        contRequester = contentRequester.ContentRequester()
        resGetter = resourceGetter.ResourceGetter(contRequester)
        linkFilters = set(
            [linkFilter.MailToFilter(),
                linkFilter.DomainCheckFilter(startLink.value)])
        linkTransformers = [linkTransform.RelativeLinkTransform(),
                            linkTransform.LowerCaseTransform()]
        html_link_parser = htmlLinkParser.HTMLLinkParser()
        mp = markupProcessor.MarkupProcessor(html_link_parser)
        lfp = linkFilterProcessor.LinkFilterProcessor(linkFilters)
        lt = linkTransformProcessor.LinkTransformProcessor(linkTransformers)
        lp = linkProcessor.LinkProcessor(mp, lfp, lt)
        plr = pLinkRequester.PLinkRequester(
            3, resGetter.get_resource, queue.Queue(), queue.Queue())
        sut = linkChecker.LinkChecker(resGetter, lp, plr, depth)

        results = sut.check_links(startLink)

        linksRequested = results["linksRequested"]
        self.assertEqual(11, len(linksRequested))
        self.assertEqual(3, len(results["brokenLinks"]))
        self.assertEqual(1, len(results["invalidMarkupLinks"]))
        self.assertTrue(
            baseStartUrl + "/arelativelink.html" in linksRequested)
        self.assertTrue(
            baseStartUrl + "/subdir/arelativelinkinasubdir.html"
            in linksRequested)


if __name__ == '__main__':
    unittest.main()
