import linkAnalysisUtilityTests
import unittest

linkAnalysisUtilityTestSuite = linkAnalysisUtilityTests.LinkAnalysisUtilityClassTests.suite()

#todo - build a list of test suites and iterate over them
unittest.TextTestRunner(verbosity=2).run(linkAnalysisUtilityTestSuite)
