def spiralTraverse(array):
    if not array or not array[0]:
        return []

    result = []
    starting_row, ending_row = 0, len(array) - 1
    starting_column, ending_column = 0, len(array[0]) - 1

    while starting_row <= ending_row and starting_column <= ending_column:
        # 1. Move Right: across starting_row, from starting_column to ending_column
        for col in range(starting_column, ending_column + 1):
            result.append(array[starting_row][col])

        # 2. Move Down: down ending_column, from starting_row + 1 to ending_row
        for row in range(starting_row + 1, ending_row + 1):
            result.append(array[row][ending_column])

        # 3. Move Left: back across ending_row, from ending_column - 1 down to starting_column
        if (
            starting_row < ending_row
        ):  # Prevents duplicate rows in single-row/odd matrices
            for col in reversed(range(starting_column, ending_column)):
                result.append(array[ending_row][col])

        # 4. Move Up: up starting_column, from ending_row - 1 down to starting_row + 1
        if (
            starting_column < ending_column
        ):  # Prevents duplicate columns in single-col/odd matrices
            for row in reversed(range(starting_row + 1, ending_row)):
                result.append(array[row][starting_column])

        # Shrink the boundaries inward
        starting_row += 1
        starting_column += 1
        ending_column -= 1
        ending_row -= 1

    return result


if __name__ == "__main__":
    matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Test 1 (3x3 Matrix):")
    print(spiralTraverse(matrix_3x3))
    # Expected Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
