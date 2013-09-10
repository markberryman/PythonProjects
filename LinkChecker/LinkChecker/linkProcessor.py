import link
import linkFilterProcessor
import linkTransformersProcessor
import markupProcessor

class LinkProcessor(object):
    """Processes the markup returned from requesting a link."""
    def __init__(self, markupProcessor, linkFilterProcessor, linkTransformerProcessor):
        self.markupProcessor = markupProcessor
        self.linkFilterProcessor = linkFilterProcessor
        self.linkTransformerProcessor = linkTransformerProcessor

    def process_link(self, linkToProcess, markup):
        """Parses the links in the provided markup and then applies filters and transformers
        before returning the set of new links."""

        newLinks = self.markupProcessor.get_links_from_markup(markup)
        # we must apply transforms ahead of filtering b/c of the interaction
        # b/w the transform converting relative links to absolute links and the 
        # filter which checks to ensure we're not leaving the root domain
        self.linkTransformerProcessor.apply_transformers(linkToProcess, newLinks)
        newLinks = self.linkFilterProcessor.apply_filters(newLinks)

        return newLinks