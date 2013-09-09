import contentRequester
import htmlLinkParserFactory
import link
import linkChecker
import linkFilter
import linkFilterProcessor
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
        mp = markupProcessor.MarkupProcessor(linkParserFactory)
        lfp = linkFilterProcessor.LinkFilterProcessor(linkFilters)
        lp = linkProcessor.LinkProcessor(mp, lfp)
        sut = linkChecker.LinkChecker(resGetter, lp)

        sut.check_links(set([startLink]), depth)
        results = sut.get_results()
        
        self.assertEqual(8, len(results["linksProcessed"]))
        self.assertEqual(3, len(results["brokenLinks"]))
        self.assertEqual(1, len(results["invalidMarkupLinks"]))

if __name__ == '__main__':
    unittest.main()