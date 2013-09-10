import contentRequester
import htmlLinkParserFactory
import link
import linkChecker
import linkFilter
import linkFilterProcessor
import linkTransform
import linkTransformProcessor
import linkProcessor
import markupProcessor
import resourceGetter
import unittest

# these are more functional tests rather than unit tests
class CheckLinksTests(unittest.TestCase):
    def test_FunctionalE2ETest(self):
        startLink = link.Link("http://localhost:35944/index.html")
        depth = 2
        linkParserFactory = htmlLinkParserFactory.HtmlLinkParserFactory()
        contRequester = contentRequester.ContentRequester()
        resGetter = resourceGetter.ResourceGetter(contRequester)
        linkFilters = set([linkFilter.MailToFilter(), linkFilter.DomainCheckFilter(startLink.value)])
        linkTransformers = [linkTransform.RelativeLinkTransform()]
        mp = markupProcessor.MarkupProcessor(linkParserFactory)
        lfp = linkFilterProcessor.LinkFilterProcessor(linkFilters)
        lt = linkTransformProcessor.LinkTransformProcessor(linkTransformers)
        lp = linkProcessor.LinkProcessor(mp, lfp, lt)
        sut = linkChecker.LinkChecker(resGetter, lp)

        results = sut.check_links(set([startLink]), depth)
        
        self.assertEqual(10, len(results["linksProcessed"]))
        self.assertEqual(3, len(results["brokenLinks"]))
        self.assertEqual(1, len(results["invalidMarkupLinks"]))
        self.assertTrue("http://localhost:35944/arelativelink.html" in results["linksProcessed"])
        self.assertTrue("http://localhost:35944/subdir/arelativelinkinasubdir.html" in results["linksProcessed"])
        

if __name__ == '__main__':
    unittest.main()