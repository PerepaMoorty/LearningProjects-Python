import string
import os
import time

os.system("cls")
letters = string.ascii_letters + " ,.!"
target = input("Enter the string you want to be displayed: ")
result = ""
for letter in target:
    for l in letters:
        print(result + l)
        if(l == letter):
            result += l
            break
        time.sleep(0.001)

time.sleep(0.5)
os.system("cls")
print(result)