class LinkTransformProcessor(object):
    """Transforms links based on a supplied set of transformers."""

    def __init__(self, transformers):
        self.transformers = transformers

    def apply_transformers(self, context, newLinks):
        """Applies transformers to newly found links. The provided
        context contains add'l info required by some transforms."""
        if (context is None):
            raise TypeError("context can not be None.")

        if (newLinks is None):
            raise TypeError("newLinks can not be None.")

        for transformer in self.transformers:
            [transformer.transform(context, link) for link in newLinks]
