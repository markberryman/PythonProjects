import linkAnalysisUtilityTests
import unittest

linkAnalysisUtilityTestSuite = linkAnalysisUtilityTests.LinkAnalysisUtilityTests.suite()

unittest.TextTestRunner(verbosity=2).run(linkAnalysisUtilityTestSuite)
