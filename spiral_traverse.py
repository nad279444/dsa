"""Traverse a 2D matrix in spiral order: right -> down -> left -> up, layer by layer.

Approach: keep four shrinking boundaries (starting/ending row and column).
Each turn of the while loop walks all four sides of the current outer layer —
across the top row, down the right column, back across the bottom row (skipped
when the top and bottom rows have collapsed into one), then up the left column
(skipped when the left and right columns have collapsed into one) — before
moving every boundary one step inward. The two guards are what stop elements
from being visited twice in single-row, single-column, or odd-centred matrices.
Time: O(rows * cols), every element visited once; Space: O(1) extra
besides the output list.
"""


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
    # 3x3 matrix: outer layer then the centre
    assert spiralTraverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 6, 9, 8, 7, 4, 5,
    ]

    # 4x4 matrix: two full layers
    assert spiralTraverse(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    ) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    # Single row / single column (the guards skip the empty legs)
    assert spiralTraverse([[1, 2, 3]]) == [1, 2, 3]
    assert spiralTraverse([[1], [2], [3]]) == [1, 2, 3]

    # Rectangular matrix
    assert spiralTraverse([[1, 2], [3, 4]]) == [1, 2, 4, 3]

    # Empty input
    assert spiralTraverse([]) == []
    assert spiralTraverse([[]]) == []

    print("All tests passed")
