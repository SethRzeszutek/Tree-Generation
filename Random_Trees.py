'''
 Name of file: Chapter10_11_Homework
 Purpose: To satisfy conditions given goals in homework assigned in chapter 10.

 Author: Seth A. Rzeszutek

 Date Created: April 16, 2017

'''
import turtle
import random


def tree(tortoise, length, depth, amount):
    """
    Description: Recursively draw a tree
    :param tortoise: a turtle object
    :param length: length of trunk
    :param depth: desired depth of recursion
    :return:
    """
    tortoise.color("white")
    tortoise.pensize(amount*(length/10))
    branch = randomnumber("branch")
    fraction = randomnumber("fraction")
    #tortoise.forward(amount * length)
    if depth <= 1:
        tortoise.forward(amount * length)
        tortoise.backward(amount*length)
    else:
        tortoise.forward(amount*length)
        tortoise.left(branch)
        tree(tortoise, length*(fraction), depth-1, amount)
        tortoise.right(branch + branch)
        tree(tortoise, length*(fraction), depth-1, amount)
        tortoise.left(branch)
        tortoise.backward(amount* length)



def randomnumber(test):
    '''
    Random Number generator
    :param test: Value for what random to use.
    :return: the random number
    '''
    rnumber = 0
    if test == "branch":
        rnumber=random.randint(10,60)
        #print("Branch angle:", rnumber)
        return rnumber
    elif test == "fraction":
        rnumber=random.uniform(0.5,0.75)
        #print("Fraction multiplier:", rnumber)
        return rnumber
    elif test == "size":
        rnumber=random.uniform(0.20,1.00)
        #print("Fraction multiplier:", rnumber)
        return rnumber
    elif test == "distance":
        rnumber=random.randint(-290,290)

        return rnumber
    elif test == "negativedistance":
        rnumber=random.randint(60,290)
        rnumber = rnumber * (-1)

        return rnumber
    else:
        print("Error.")

def callofthetrees(tortoise):
    '''
    Gives number of trees to be generated
    :param tortoise: Well, its the turtle
    :return: NONE
    '''
    numberOfTrees = 10  #number of trees
    while numberOfTrees != 0:
        amount = randomnumber("size")
        x = randomnumber("distance")
        y = randomnumber("negativedistance")
        tortoise.penup()
        tortoise.setpos(x, y)
        tortoise.pendown()
        tree(tortoise, 100, 6, amount)
        numberOfTrees += -1

def background(george):
    '''
    Draws the background
    :param george: Well, its the turtle
    :return: NONE
    '''
    george.left(90)
    george.forward(360)
    george.color("white")
    george.right(180)
    george.forward(710)
    #Mountain Time
    george.left(135)
    george.forward(70)
    george.left(90)
    george.forward(70)
    george.right(90)
    george.forward(170)
    george.left(90)
    george.forward(90)
    george.right(90)
    george.forward(150)
    george.left(90)
    george.forward(230)
    george.right(90)
    george.forward(110)
    george.left(90)
    george.forward(110)
    george.right(135)



def main():
    '''
    Calls desired functions
    :return: NONE
    '''
    george = turtle.Turtle()
    screen = george.getscreen()
    screen.tracer(0,0)                  #disables animations/tracer
    screen.bgcolor("black")
    george.speed('fastest')
    george.left(90)
    george.forward(85)
    background(george)
    callofthetrees(george)
    screen.exitonclick()

if __name__ == '__main__':
    main()
