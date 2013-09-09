import link
import linkFilterProcessor
import markupProcessor

class LinkProcessor(object):
    """Processes the markup returned from requesting a link."""
    def __init__(self, markupProcessor, linkFilterProcessor):
        self.markupProcessor = markupProcessor
        self.linkFilterProcessor = linkFilterProcessor

    def process_link(self, linkToProcess, markup):
        newLinks = self.markupProcessor.get_links_from_markup(markup)

        return self.linkFilterProcessor.apply_filters(newLinks)