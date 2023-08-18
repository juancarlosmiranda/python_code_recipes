"""
# Project: Fruit Size Estimation
# Author: Juan Carlos Miranda
# Date: January 2022
# Description:
  Test suite  for project

Usage:

# todo: add usage
"""

import unittest
from test.test_ka_real_time_video_extraction import TestRealTimeVideoExtraction


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRealTimeVideoExtraction('test_video_real_time'))
    #suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())