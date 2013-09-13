class LinkProcessor(object):
    """Processes the markup returned from requesting a link."""
    def __init__(
            self, markupProcessor, linkFilterProcessor,
            linkTransformProcessor):
        self.markupProcessor = markupProcessor
        self.linkFilterProcessor = linkFilterProcessor
        self.linkTransformProcessor = linkTransformProcessor

    def process_link(self, linkToProcess):
        """Parses the link's response and then applies filters
        and transformers before returning the set of new links."""

        newLinks = self.markupProcessor.get_links_from_markup(
            linkToProcess.responseData)
        # we must apply transforms ahead of filtering b/c of the interaction
        # b/w the transform converting relative links to absolute links and the
        # filter which checks to ensure we're not leaving the root domain
        context = {
            "currentLink": linkToProcess
            }

        self.linkTransformProcessor.apply_transformers(context, newLinks)
        newLinks = self.linkFilterProcessor.apply_filters(newLinks)

        return newLinks
