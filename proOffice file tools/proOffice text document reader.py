

from time import *

print("welcome to proTech TXT file reader")
sleep(2)
file = input("please type in the full name and extension of the file you want to read: ")

f = open(file, "r")

print(f.read(10000))
sleep(21)


