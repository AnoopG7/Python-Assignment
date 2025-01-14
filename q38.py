# Write a function to find the transpose of a given matrix (list of lists).
def transpose(matrix):
    return [[matrix[j][i] 
             for j in range(len(matrix))] 
             for i in range(len(matrix[0]))]

# Taking matrix input from the user
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

matrix = []
print("Enter elements of the matrix:")
for i in range(rows):
    row = [int(input(f"Element {i+1}{j+1}: ")) 
           for j in range(cols)]
    matrix.append(row)

print("Original matrix:")
for row in matrix:
    print(row)

transposed_matrix = transpose(matrix)
print("Transposed matrix:")
for row in transposed_matrix:
    print(row)
