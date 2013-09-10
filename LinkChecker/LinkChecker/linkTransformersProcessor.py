class LinkTransformersProcessor(object):
    """Transforms links based on a supplied set of transformers."""

    def __init__(self, transformers):
        self.transformers = transformers

    def apply_transformers(self, links):
        """Applies transformers to links."""
        if (len(self.transformers) == 0):
            return links

        transformer = self.transformers.pop()

        transformedLinks = [transformer.transform(link) for link in links]

        return self.apply_transformers(links)