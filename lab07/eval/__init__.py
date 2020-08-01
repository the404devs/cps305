# Owen Goodwin
# 500909196
# 10/29/19
# I actually enjoyed making this. I think it works perfectly, but don't quote me on that.

import re
from pythonds.basic import Stack

# Main function to evaluate a tree
def evalTree(tree, env):
	evalTree.expression = ""
	#Create an empty dictionary.
	#We use this to track the values of variables given in the environment
	envDict = {}
	#We now populate the dictionary, by looking at each pair in the environment
	#and turning those pairs into key-value pairs in the dictionary.
	for pair in env:
		envDict[pair[0]] = pair[1]
	#Begin traversing the tree.
	traverse(tree, envDict)
	return prefixEvaluation(evalTree.expression)

#This function will traverse the given tree,
#use the dictionary to substitute variables for their values
#and creates an expression in prefix form.
#Funnily enough, the prefix thing happened by accident. I just figured I should iterate
#over the tree recursively, and add each element to a string. Upon testing it, I noticed it made a prefix expression,
#and life got 10 times easier.
def traverse(tree, envDict):
	#We begin by iterating over each element within the tree, which is basically a list with mini lists inside it.
	for subtree in tree:
		#First, check if the current element is a mini list.
		if isinstance(subtree, list):
			#If it's a mini-list, begin iterating over the mini-list and it's kids, recursively.
			traverse(subtree, envDict)
		#Otherwise, it's probably a string.
		#Either it's a number, like "5"
		#or a variable, like "x1"t
		#or an operator, like "+"
		elif isinstance(subtree, str):
			#Check if there's an entry in the dictionary...
			if subtree in envDict:
				#...and if so, swap the variable out for it's proper value
				evalTree.expression += str(envDict[subtree]) + " "
			else:
				#Otherwise, it's a number or operator, so just chuck that into our expression.
				evalTree.expression += subtree + " "

#Helper function to test if a string is actually a number.
#We attempt to cast the string to a float, and return a bool based on the result.
#If it doesn't work, it obviously isn't a float
def isFloat(s):
	try:
		int(s)
	except ValueError:
		return False
	return True

#Function to evaluate a prefix expression.
def prefixEvaluation(expr):

	#A quick check to see if the expression contains any letters
	#This would mean that there's a variable in the expression that didn't have its value defined in the environment
	#In this case, don't bother trying to evaluate, and simply return None.
	if re.search('[a-zA-Z]', expr):
		return None

	#We split up our expression into individual tokens, so each operand and operator becomes its own element.
	#Originally, I was iterating over the expression character by character, but obviously this becomes a problem when you have any value with more than 2 digits
	#Then I remembered that I should yeet a space after adding an element when constructing the expression
	tokens = expr.split()
	#Empty stack to chuck values onto as we work with them.
	operandStack = Stack()

	#Begin iterating over our tokens
	#B/c this is prefix, we go backwards, starting from the end and working towards the start.
	for j in range(len(tokens)-1, -1, -1):
		#Check if the token is a float...
		if isFloat(tokens[j]):
			#...and chuck it onto the stack
			operandStack.push(float(tokens[j]))
		#If it's not a float, then it's an operator
		else:
			#Take the top two operands off the stack, these are the numbers we do the operation on.
			op1 = operandStack.pop()
			op2 = operandStack.pop()
			#Figure out which operation we're doing, and then push the result back onto the stack
			if tokens[j] == "+":
				operandStack.push(op1 + op2)
			elif tokens[j] == "-":
				operandStack.push(op1 - op2)
			elif tokens[j] == "*":
				operandStack.push(op1 * op2)
			elif tokens[j] == "/":
				try:
					operandStack.push(op1 / op2)
				#A try-catch in case somebody tries to divide by 0
				except ZeroDivisionError:
					return None


	#When we're done evaluating the expression, pop off the last value. That's our solution.
	return operandStack.pop()
