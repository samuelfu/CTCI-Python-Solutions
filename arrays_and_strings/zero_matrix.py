def zero_matrix(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0.
    """

    coor = []
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if matrix[m][n] == 0:
                coor.append((m, n))
    for x, y in coor:
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                if m == x or y == n:
                    matrix[m][n] = 0
    return matrix

print(zero_matrix([[1, 0, 1], [1, 1, 1], [1, 1, 0]]))
