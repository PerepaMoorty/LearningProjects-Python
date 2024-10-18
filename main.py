list = []

listLength = int(input("Enter the List Length: "))
additiveFactor = float(input("Enter Multiple factor: "))

for i in range(listLength):
    list.append(float(input("Enter Value: ")))

for i in range(len(list)):
    list[i] += additiveFactor
    
print(list)