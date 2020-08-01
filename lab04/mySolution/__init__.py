import turtle, sys, random

def tree(branchLen, t, pen):
    if pen < 1:
        pen = 1
    t.pensize(pen)
    col = "brown"
    if branchLen < 15:
        col = "green"
    elif branchLen < 35:
        col = "darkgreen"
    t.color(col)
    if branchLen > 5:
        t.forward(branchLen)
        angle = random.randint(15, 45)
        less = random.randint(5, 15)
        t.right(angle)
        tree(branchLen-less, t, pen-1)
        t.left(angle*2)
        tree(branchLen-less, t, pen-1)
        t.right(angle)
        t.backward(branchLen)
        t.color(col)

def main():
    pen = 5
    t = turtle.Turtle()
    myWin = turtle.Screen()
    # turtle.tracer(0) # for instant tree
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    tree(75, t, pen)

def power(x, n, acc=1):
    if n == 0:
        return acc
    return power(x, n - 1, acc * x)

# print(power(5, 64))

def powerH(x, n, acc=1):
    if n == 0:
        return acc
    elif n % 2 != 0:
        return powerH(x * x, n // 2, acc * x)
    else:
        return powerH(x * x, n // 2, acc)
# print(powerH(5, 5))


def binomial(n, k):
    if (n == k) or (k == 0):
        return 1
    else:
        return binomial(n-1, k) + binomial(n-1, k-1)

# print(binomial(10, 3))
# main()