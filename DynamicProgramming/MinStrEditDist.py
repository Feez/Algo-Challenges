from collections import deque

def GetMinimumStringEditDistance(a : str, b : str):
    # Number of rows    = len(a) + 1
    # Number of columns = len(b) + 1
    # - The (+ 1) is for the null/empty string
    matrix = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    steps = [[None for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    steps[0][0] = "Empty"

    # String 'a' will be represented on the column
    # Fill out the edit distances from string 'a' to null string
    for i in range(1, len(a) + 1):
        matrix[i][0] = i
        steps[i][0] = f"Extra from text [{a[i - 1]}]"
        
    # String 'b' will be represented on the row
    # Fill out the edit distances from string 'b' to null string
    for i in range(1, len(b) + 1):
        matrix[0][i]  = i
        steps[0][i] = f"Extra from pattern  [{b[i - 1]}]"

    # Fill out rest of matrix
    for row in range(1, len(a) + 1):
        for col in range(1, len(b) + 1):
            is_chars_different = a[row - 1] != b[col - 1]

            add_amount = 1 if is_chars_different else 0

            val, step = min(
                # Diff extending string by this character
                (matrix[row - 1][col - 1] + add_amount, 
                "Diff" if is_chars_different else "Match"),

                # Extra character in text (a)
                (matrix[row - 1][col] + 1, 
                f"Extra from text [{a[row - 1]}]"),

                # Extra character in pattern (b)
                (matrix[row][col - 1] + 1, 
                "Extra from pattern")
            )

            matrix[row][col] = val

            steps[row][col] = step

    return matrix, steps

# Get pretty string matrix representation of solution
def get_matrix_string(matrix, a, b):
    a = f"*{a}"
    b = f"*{b}"

    lengths = [1] * len(matrix[0])

    for col in range(len(matrix[0])):
        largest = max(len(str(matrix[row][col])) for row in range(len(matrix)))

        lengths[col] = largest
        
    rows = [str()] * len(matrix)
    for row in range(len(matrix)):
        for col, x in enumerate(matrix[row]):
            if col == len(matrix[row]) - 1:
                rows[row] += (str(x)).ljust(lengths[col])
            else:
                rows[row] += (str(x) + ', ').ljust(lengths[col] + 2)

        rows[row] = f"[{rows[row].rstrip(',')}]"

    for row in range(len(a)):
        rows[row] = f"{a[row]} {rows[row]}"

    first_row = ['' for i in range(len(b))]
    for col, x in enumerate(b):
        if col == len(first_row) - 1:
            first_row[col] = (str(x)).ljust(lengths[col])
        else:
            first_row[col] = (str(x) + '  ').ljust(lengths[col] + 2)
    first_row = '   ' + ''.join(first_row)

    rows = [first_row] + rows

    return '\n'.join(str(row) for row in rows)

# Gets ** a ** minimum steps path
def get_min_steps_path(matrix, steps):
    best_steps = deque()

    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    best_steps.appendleft(steps[row][col])

    while row >= 1 and col >= 1:
        val, i, j = min(
            (matrix[row - 1][col - 1], row - 1, col - 1),
            (matrix[row - 1][col] + 1, row - 1, col),
            (matrix[row][col - 1] + 1, row, col - 1)
        )

        best_steps.appendleft(steps[i][j])

        row = i
        col = j

    return list(best_steps)


text    = "ItsYaBoiBrian"
pattern = "IshyeBoyBryan"

matrix, steps = GetMinimumStringEditDistance(text, pattern)

print(f"Text = {text}, Pattern = {pattern}")
print(get_matrix_string(matrix, text, pattern))
print()
print(get_min_steps_path(matrix, steps))
