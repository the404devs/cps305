import unittest
from eval import *

class TestTree(unittest.TestCase):
	def testTrees(self):
		environment1 = [["a", 5], ["b", 10], ["c", 50]]
		environment2 = [["a", 0], ["b", 10], ["c", 50]]
		tree1 = ["+", ["*", "5", "2"], ["/", "26", "2"]]
		tree2 = ["-", "+", ["*", "a", "b"], ["/", "c", "a"], "1"]
		tree3 = ["-", "+", ["*", "a", ["/", "26", "2"]], ["/", ["*", "5", "2"], "a"], "1"]
		self.assertEqual(evalTree(tree1, environment1), 23.0, "Correct answer is 23")
		self.assertEqual(evalTree(tree2, environment1), 59.0, "Correct answer is 59")
		self.assertEqual(evalTree(tree3, environment2), None, "Correct answer is Nones")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)