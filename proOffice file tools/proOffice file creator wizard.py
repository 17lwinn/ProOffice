# this software copy includes an Mozilia Public License- see our license file for more info

 from time import *

print("welcome to ProTech file creator")
sleep(2)
file = input("please type in the full name and extension of the file you want to create: ")

f = open(file, "x")

print(f.read(10000))
sleep(5)




