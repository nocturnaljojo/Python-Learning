# This is an introductory into functions
#Write your code below this line 👇
import math # by importing math - this will round up a number for eg. 

#math.ceil(1.2) - will round up to 2 and not round down to 1

def paint_calc(height,width,cover):
    number_of_cans = math.ceil(((test_h * test_w))/coverage)
    print("You'll need " + str(number_of_cans) + " cans of paint.")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
