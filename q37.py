# Prompt the user for two 2D matrices (lists of lists) of the same dimensions. Perform matrix addition and print the result.
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

matrix1 = []
matrix2 = []
print("Enter elements of the first matrix:")
for i in range(rows):
    row = [int(input(f"Element {i+1}{j+1}: ")) 
           for j in range(cols)]
    matrix1.append(row)

print("Enter elements of the second matrix:")
for i in range(rows):
    row = [int(input(f"Element {i+1}{j+1}: ")) 
           for j in range(cols)]
    matrix2.append(row)

result = [[matrix1[i][j] + matrix2[i][j] 
           for j in range(cols)] 
                for i in range(rows)]

print("Matrix after addition:")
for row in result:
    print(row)
