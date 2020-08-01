from mySolution import *
import unittest

class tests(unittest.TestCase):
	def testPower(self):
		self.assertEqual(power(10, 7), 10000000, "Correct output is 10000000")

	def testPowerH(self):
		self.assertEqual(powerH(10, 7), 10000000, "Correct output is 10000000")

	def testBinomial(self):
		self.assertEqual(binomial(8, 4), 70, "Correct output is 70")
		
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)