# tests/runner.py
import unittest

# import your test modules
from jenkins_python.test_login import TestLogin
from jenkins_python.test_navigate import TestNavigate

# initialize the test suite
loader = unittest.TestLoader()

# add tests to the test suite
Test1 = loader.loadTestsFromTestCase(TestLogin)
Test2 = loader.loadTestsFromModule(TestNavigate)

# Sanity Test
sanityTestSuite=unittest.TestSuite([Test1,Test2])

# Run your test
unittest.TextTestRunner().run(sanityTestSuite)