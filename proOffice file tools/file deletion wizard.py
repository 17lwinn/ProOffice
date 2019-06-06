from time import *
print("to prevent software piracy, we will now search your DOCUMENTS folder for the license.txt file.")
sleep(5)
f = open("LICENSE.txt", "r")

print(f.read(100000000))
sleep(3)
print("____________________________________________________________")

file = input("please enter the name of the file pending deletion: ")

import os
os.remove(file)

sleep(2)
print(file, "was deleted")
sleep(2)
