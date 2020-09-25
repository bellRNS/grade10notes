""" Using a package called Turtles to visualize our work """

import turtle   #we are loading a module called turtle. it has functions

bob = turtle.Turtle()

bob.fd(100)        #this is called a 'method'.
                # a method is a function that is used on an object. 

bob.rt(90)      #this is the right turn method
bob.fd(100)

#task: make bob finish the square.
# you definitely repeated the same sequence 4 times:
    #bob.fd(100)
    #bob.rt(90)

""" introducing FOR loops """

for i in range(4):
    print('hello')

nancy = turtle.Turtle()

for i in range(4):
    nancy.fd(100)
    nancy.rt(90)

def turt_square(t):         #this GENERALIZES to include any turtle
    for i in range(4):
        t.fd(100)
        t.rt(90)


def turtle_plus_length(t, l): # this was the answer question 2 on exercise. 
        for i in range(4):
            t.fd(l)
            t.rt(90)

def turtle_polygon(t, l, n):
    x = 360/n                   #this line figures out internal angles
    for i in range(n):
            t.fd(l)
            t.rt(x)

    






