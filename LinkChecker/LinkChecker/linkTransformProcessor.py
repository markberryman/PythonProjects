class LinkTransformProcessor(object):
    """Transforms links based on a supplied set of transformers."""

    def __init__(self, transformers):
        self.transformers = transformers

    def apply_transformers(self, currentLink, newLinks):
        """Applies transformers to newly found links. Some transforms require knowing
        the "current" link as well so that must be provided."""
        if (len(self.transformers) == 0):
            return newLinks

        transformer = self.transformers.pop()

        transformedLinks = [transformer.transform(currentLink, link) for link in newLinks]

        return self.apply_transformers(currentLink, newLinks)