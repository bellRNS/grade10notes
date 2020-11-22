"""This is a great way to create a
multi-line comment, by using three quotes"""

# hash tags also comment out the entire line.

initialtime = 6*60 + 4

#inputting our running speeds for the morning jog
slow_speed = 8 + (15/60)
fast_speed = 7 + (12/60)

#distances at each type of pace
slow_distance = 10
fast_distance = 15

#getting times from distances and speeds
slow_time = slow_speed * slow_distance
fast_time = fast_speed * fast_distance

#finally, our total times, and time at home
total_time = slow_time + fast_time
time_at_home = initialtime + total_time

print(total_time)
print(time_at_home)

"""What we learned here:
-variables are assigned with an =
-creating a file/script is important (save recipes!)
-We can re-use a script for different purposes
-It organizes our code, and our thoughts.
-It makes things easier to read for other coders."""


"""Moving on to FUNCTIONS"""
import math
#this is a module made by someone else. It is helpful!

#this has the ability to take the square root
#square rooting is its 'function'
#4 is what's called an 'argument' 
math.sqrt(4)

# we will import more modules later (like math)
#functions package some code (encapsulation)
# to make a function, we use 'def'
#anything indented is part of the function. 

def myfunction():
    print('banana pants')

# we have to CALL the function in order for it to work.

myfunction()

#homework!
#make our time example above, into one single function.

def runtime():
    




    


