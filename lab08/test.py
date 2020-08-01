import unittest
from parse import *

class TestParse(unittest.TestCase):
	def testParse1(self):
		x=['8', '*', ['5', '+', '2']]
		expected = ['*', ['8', [], []], ['+', ['5', [], []], ['2', [], []]]]
		self.assertEqual(parse(x), expected, "['*', ['8', [], []], ['+', ['5', [], []], ['2', [], []]]]")

	def testParse2(self):
		x=['4', '*', ['5', '!']]
		expected = ['*', ['4', [], []], ['!', ['5', [], []], []]]
		self.assertEqual(parse(x), expected, "['*', ['4', [], []], ['!', ['5', [], []], []]]")

	def testParse3(self):
		x=['10', '/', ['80', '/', ['20', '*', '2']]]
		expected = ['/', ['10', [], []], ['/', ['80', [], []], ['*', ['20', [], []], ['2', [], []]]]]
		self.assertEqual(parse(x), expected, "['/', ['10', [], []], ['/', ['80', [], []], ['*', ['20', [], []], ['2', [], []]]]]")


if __name__ == '__main__':
	unittest.main(argv=['first-arg-is-ignored'], exit=False)
