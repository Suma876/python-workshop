r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

matrix = []

print("Enter the elements row-wise:")

for i in range(r):
	row = []
	for j in range(c):
		row.append(int(input()))
	matrix.append(row)

print("Matrix:")
for row in matrix:
	print(row)
	
if r == c:  
	diagonal_sum = 0
	for i in range(r):
		diagonal_sum += matrix[i][i]
	print("Sum of the main diagonal:", diagonal_sum)
else:
	print("Cannot calculate diagonal sum for a non-square matrix.")

transposed = []
for j in range(c):
	rows = []
	for i in range(r):
		rows.append(matrix[i][j])
	transposed.append(rows)

print("Transposed Matrix:")
for rows in transposed:
	print(rows)