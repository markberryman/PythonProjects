import link
import linkTransformersProcessor
import unittest

class MockTransform(object):
    def __init__(self):
        self.transformFnCalled = False

    def transform(self, link):
        self.transformFnCalled = True

class ApplyTransformersUnitTests(unittest.TestCase):
    def test_ReturnsLinksWhenNoTransformersLeftToApply(self):
        dummyTransformers = []
        dummyLinks = [link.Link("a link")]
        sut = linkTransformersProcessor.LinkTransformersProcessor(dummyTransformers)
        
        result = sut.apply_transformers(dummyLinks)

        self.assertEqual(dummyLinks, result)

    def test_AppliesAllTransforms(self):
        dummyTransformA = MockTransform()
        dummyTransformB = MockTransform()
        dummyTransformers = [dummyTransformA, dummyTransformB]
        dummyLinks = [link.Link("a link")]
        sut = linkTransformersProcessor.LinkTransformersProcessor(dummyTransformers)

        sut.apply_transformers(dummyLinks)

        self.assertTrue(dummyTransformA.transformFnCalled)
        self.assertTrue(dummyTransformB.transformFnCalled)


if __name__ == '__main__':
    unittest.main()