import string
import random

maxLimit = int(input("Enter the length of the Password: "))
AVAILABLE_CHARACTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits + ".&$@!"

generatedPassword = ""
for i in range(maxLimit + 1): generatedPassword += random.choice(AVAILABLE_CHARACTERS)    

print("The generated password is: " + generatedPassword + "\n")