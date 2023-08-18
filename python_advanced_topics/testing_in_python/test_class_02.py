"""
Based from https://docs.python.org/3/library/unittest.html

Use:
 python -m unittest test_class_02.py

"""
import unittest

class TestClass02(unittest.TestCase):

    def setUp(self):
        print("HERE setting parameters for TestClass01(unittest.TestCase) --")
        self.my_variable = "HELLO_CLASS_02!"

    def test_upper(self):
        print(f"Using my internal variale {self.my_variable}")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()