class LinkTransformProcessor(object):
    """Transforms links based on a supplied set of transformers."""

    def __init__(self, transformers):
        self.transformers = transformers

    def apply_transformers(self, context, newLinks):
        """Applies transformers to newly found links. The provided
        context contains add'l info required by some trasnforms."""
        if (len(self.transformers) == 0):
            return newLinks

        transformer = self.transformers.pop()

        [transformer.transform(context, link) for link in newLinks]

        return self.apply_transformers(context, newLinks)
