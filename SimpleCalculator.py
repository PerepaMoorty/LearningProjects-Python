print("This is a Calculator Program\n")
programActive = True
while(programActive):
    #Getting the Operands
    print("Enter the two numbers you want to do calculations on:\n")
    num1 = input()
    num2 = input()

    #Getting the Operators
    operation = input("Enter the Operation Symbol: (+, -, *, /): ")

    #Operator Check
    result = 0
    if(operation == "+"):
        result = float(num1) + float(num2)
    elif(operation == "-"):
        result = float(num1) - float(num2)
    elif(operation == "*"):
        result = float(num1) * float(num2)
    elif(operation == "/"):
        result = float(num1) / float(num2)
    else:
        print("Sorry, That is an invalid input\n")

    print("Result: " +str(result))
    operation = input("Do you want to continue using the program? [Y/N]: ")
    if(operation.lower() == "n"):
        programActive = False
    elif(operation.lower() == "y"):
        continue
    else:
        print("Sorry, That is an Invalid Choice\n")