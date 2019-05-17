# this software copy includes an MIT licence- by using this you will not:
# 1. edit the license or share it
 

from time import *

file = input("please type in the full name and extension of the file you want to create: ")

f = open(file, "x")

print(f.read(10000))
sleep(5)


