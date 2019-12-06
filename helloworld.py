#this is for advent of code 2019

import math

print("hello world")
print("welcome to my program")

F = open("workfile.txt","r")
lines = F.readlines()
total = 0
for x in lines:
    division = int(x) // 3
    subtraction = division - 2
    total = total + subtraction

print "and the answer is"
print total
