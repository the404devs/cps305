from mySolution import *

import unittest

class TestSquare(unittest.TestCase):

    def test_square(self):
    	# Check if we can correctly calculate the percentage of correct chars in the string
        self.assertEqual(calcScore("fedsuf", "fedora"), 50, "Should be 50%")

    def test_square_aux(self):
    	# Check if we can successfully generate a string, and check the length is correct.
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        teststr = generate(64, len(alphabet), alphabet)
        self.assertIsNotNone(teststr)
        self.assertEqual(len(teststr), 64)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)