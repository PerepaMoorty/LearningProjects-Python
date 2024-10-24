matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

factor = int(input("Factor: "))

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] += factor
        
print(matrix)