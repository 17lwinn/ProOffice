from time import *


file = input("please enter the name of the file pending deletion: ")

import os
os.remove(file)

sleep(2)
print(file, "was deleted")
sleep(2)
