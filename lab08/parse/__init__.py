#Lab 8
#Owen Goodwin
#500909196
#11/05/19


def precedence(oper):
    if oper in ['+', '-']:
        return 1
    elif oper == "!":#We want this guy to be a little bit more important than + & -
        return 2
    else: 
        return 3


def operatorp(x):
    return x in ['+', '-', '/', '*', '!']

def numberp(x):
    return not operatorp(x)


def parse(expr):
    return parseHelper(expr, [], [])

def parseHelper(expr, operators, operands):
    
    if expr == []:
        if operators == []:
            return operands[0]
        else:
            return handleOp([], operators, operands)

    #Added a check to see if we've got a nested expression. 
    #In this case, we call parse() on the sub-expression in the return call.
    #This allows us to fit the properly formatted sub-expression neatly into place.
    if isinstance(expr[0], list):
        return parseHelper(expr[1:], operators, [parse(expr[0])]+operands)

    if numberp(expr[0]):
        return parseHelper(expr[1:], operators, [[expr[0], [], []]]+operands)
    elif operators == [] or precedence(expr[0]) > precedence(operators[0]):
        return parseHelper(expr[1:], [expr[0]]+operators, operands)
    else:
        return handleOp(expr, operators, operands)

def handleOp(expr, operators, operands):
    #We need to do something special for the factorial operator,
    #since it works differently than the others, taking only 1 operand.
    if operators[0] == "!":
        return parseHelper(expr, operators[1:], [[operators[0], operands[0], []]]+operands[2:])
    return parseHelper(expr, operators[1:], [[operators[0], operands[1], operands[0]]]+operands[2:])

# x=[['2', '+', '2'],'/','6','-', '9']
# x=[['4', '+', '3'], '*', '7']
# x=['2', '!']
# x=['3','/',['6', '!'],'-', '9']
# x=['4', '+', ['3', '!']]
# x=['4', '+', ['3', '!']]
#x=['4', '+', '3', '*', '7']
#x=[['4'], '+', ['3'], '+', '6']
# x="( 4 + 3 * 7 - 5 / ( 3 + 4 ) + 6 )"
# print("--", parse(x))
