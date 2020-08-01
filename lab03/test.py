from mySolution import *

import unittest

class TestPostfix(unittest.TestCase):

    def testPostfixCoversion(self):
        #Assert that we can correctly covert an expression to postfix
        self.assertEqual(infixToPostfix("1 * 2 + 3 * 4"), "1 2 * 3 4 * +", "Correct output: 1 2 * 3 4 * +")

    def testPostfixEvaluation(self):
         #Assert that we can correctly evaluate a postfix expression
        self.assertEqual(postfixEval("1 2 * 3 4 * +"), 14, "Correct output is 14")

    def testOperationEvaluation(self):
        #Assert that the doMath() method works as intended
        self.assertEqual(doMath("*", 4, 6), 24, "Correct output is 24")

    def testNestedOperations(self):
        #Test both converting and evaluating a more complex expression.
        self.assertEqual(infixToPostfix("2 * ( 5 - 4 / 2 ) + 1"), "2 5 4 2 / - * 1 +", "Correct output: 2 5 4 2 / - * 1 +")
        self.assertEqual(postfixEval("2 5 4 2 / - * 1 +"), 7, "Correct output is 7")

    def testInfixToPostfixEval(self):
        #Try out infixToPostfixEval() on a few expressions, check if they return the correct output.
        self.assertEqual(infixToPostfixEval("( 6 - 6 ) + ( 6 * 5 ) / 3"), 10, "Correct output is 10")
        #Testing factorials
        self.assertEqual(infixToPostfixEval("8 ! + 3 * 5"), 40335, "Correct output is 40335")
        #Testing nested parenthesis
        self.assertEqual(infixToPostfixEval("5 + ( ( 3 / 5 ) * ( 1 * 5 ) )"), 8, "Correct output is 8")
        self.assertEqual(infixToPostfixEval("4 + ( 5 - ( 9 / 3 ) )"), 6, "Correct output is 6")
        #Testing out a rather long and complex expression
        self.assertEqual(infixToPostfixEval("( 5 / 5 + ( ( 3 / ( 5 + 9 - 0 ) ) * ( 1 * 5 + 6 + 3 ) ) ) !"), 24, "Correct output is 24")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)