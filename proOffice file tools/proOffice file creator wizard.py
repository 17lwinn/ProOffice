# this software copy includes an Mozilia Public License- see our license file for more info

from time import *
print("to prevent software piracy, we will now search your DOCUMENTS folder for the license.txt file.")
sleep(5)
f = open("LICENSE.txt", "r")

print(f.read(100000000))
sleep(3)
print("____________________________________________________________")
print("welcome to ProTech file creator")
sleep(2)
file = input("please type in the full name and extension of the file you want to create: ")

f = open(file, "x")

print(f.read(10000))
sleep(5)




