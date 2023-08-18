"""
Based from https://docs.python.org/3/library/unittest.html

Use:
 python -m unittest test_suite_runner.py

"""

import unittest
from test_class_01 import TestClass01
from test_class_02 import TestClass02


def suite_all_cases():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestClass01))
    suite.addTest(unittest.makeSuite(TestClass02))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_all_cases())