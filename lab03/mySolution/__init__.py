from math import factorial
from pythonds.basic import Stack

def infixToPostfix(infixExpr):
    ops = Stack()#To keep track of our various operation chars
    tokens = infixExpr.split()#Take our input string, and split it into a list of chars we can iterate over
    postfixList = list()#An empty list, that we fill with chars as we sort them into the correct order to make the expression postfix
    priority = {}#A list, which we will use to define the priority of different operations
    priority["*"] = 3#Here we define the priorities of these operations. This determines the order they're shown in the output
    priority["/"] = 3
    priority["+"] = 2
    priority["-"] = 2
    priority["("] = 1
    priority["!"] = 4

    nums = "0123456789"#Numbers. Our input will likely have these, so let's use a big string of them so we can easily check if we've found a number when we begin
    
    for t in tokens:#Begin by iterating through all of our input tokens
        if t in nums:
            #If we've got a number, chuck that onto our postfix list,
            postfixList.append(t)
        elif t == "(":
            # Push an opening bracket onto the operation stack
            ops.push(t)
        elif t == ")":
            # We've got a closing bracket. Time to find its matching opening one.
            top = ops.pop() #Grab the element at the top of the operations stack
            while top != '(':
                #first, chuck the old top element onto the postfix list...
                postfixList.append(top)
                #then, get the new top now that we've removed one.
                top = ops.pop()
                #this continues until we've got the matching left brace.
                
        else:
            #Ok, so it's not a digit or bracket. That must mean it's one of the other operations (+, -, *, /)
            while ((not ops.isEmpty()) and (priority[ops.peek()] >= priority[t])):
                #Just spent 10 minutes trying to figure out why this loop wasn't firing.
                #Turns out, I had ops.isEmpty, instead of ops.IsEmpty()
                #Anyways, here we look through our operation stack, and grab any element with a lower priority
                #than the current token. The lower priority elements are then put into our postfix list.
                #Stop when we find a higher priority operation.
                postfixList.append(ops.pop())
                
            #Now that we've finished with that, we can put our current token onto the operations stack
            #It'll be sorted into its place next time we come to an operation in our infix string
            ops.push(t)
            
    while (not ops.isEmpty()):
        #In the case we've sorted all of the operations and digits and whatnot,
        #we take our operations stack, turn it upside-down, and dump whatever's left in there into our postfix list
        #They're already in the correct order, so just pop em' and we're done!
        postfixList.append(ops.pop())
        
        
    return " ".join(postfixList)#Spit out our finished postfix expression.

#The postfix evaluation method, as provided by the textbook.
#Takes a postfix expression, does some magic, and returns the correct answer
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        elif token == "!":
            #Quick addition here to process factorials.
            operandStack.push(factorial(operandStack.pop()))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

#Helper for the postfixEval method. Looks at an operation, then performs it on the given operands.
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

#Wrapper function that'll take an input infix,
#Convert it to postfix with our infixToPostfix(),
#And then evaluate it with the textbook's postfixEval()
def infixToPostfixEval(infix):
    return postfixEval(infixToPostfix(infix))