def GetMinimumStringEditDistance(a : str, b : str):
    # Number of rows    = len(a) + 1
    # Number of columns = len(b) + 1
    # - The (+ 1) is for the null/empty string
    matrix = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    # String 'a' will be represented on the column
    # Fill out the edit distances from string 'a' to null string
    for i in range(len(a) + 1):
        matrix[i][0] = i
        
    # String 'b' will be represented on the row
    # Fill out the edit distances from string 'b' to null string
    for i in range(len(b) + 1):
        matrix[0][i]  = i

    # Fill out rest of matrix
    for row in range(1, len(a) + 1):
        for col in range(1, len(b) + 1):
            is_chars_different = a[row - 1] != b[col - 1]

            add_amount = 1 if is_chars_different else 0

            matrix[row][col] = min(
                # Diff extending string by this character
                matrix[row - 1][col - 1] + add_amount,

                # Diff extra character (insertion)
                matrix[row - 1][col] + 1,

                # Diff removed character (deletion)
                matrix[row][col - 1] + 1,
            )

    return matrix

def get_matrix_string(matrix):
    return '\n'.join(str(row) for row in matrix)

def get_steps(matrix, a, b):
    if len(matrix) == 0:
        return ""

    results = []

    for row in reversed(range(len(matrix[0]))):
        for col in reversed(range(len(matrix))):
            pass


print(get_matrix_string(GetMinimumStringEditDistance("FLEA", "BEAR")))
print()
print(get_matrix_string(GetMinimumStringEditDistance("a3ced", "abcdef")))
