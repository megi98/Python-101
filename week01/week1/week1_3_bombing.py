def matrix_bombing_plan(matrix):

	result = {}
	tuples = ()

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):

			tuples = i, j
			sums = matrix[i][j]

			for h in range(len(matrix)):
				for g in range(len(matrix[0])):


					if h in range(i-1, i+2) and g in range(j-1, j+2):

						if matrix[h][g] - matrix[i][j] > 0:

							sums += (matrix[h][g] - matrix[i][j])

					else:
						sums += matrix[h][g]

			result.update({tuples: sums})
			tuples = ()

	return result

print(matrix_bombing_plan([[1,2,3], [4,5,6], [7,8,9]]))







