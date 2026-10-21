"""Return every triplet in `arr` whose values sum to `target`.

Approach: sort the array first, then fix one element at index i and sweep the
elements after it with two pointers (left starts just after i, right at the
end). If the current sum is below the target the values are too small, so move
left forward; if it is above, move right backward. On a match, record the
triplet and move BOTH pointers in. Sorting keeps equal values together and the
left < right guard keeps the pointers on distinct indices, so each combination
is found exactly once.
Time: O(n^2) on top of the O(n log n) sort; Space: O(1) extra besides output.
"""


def three_number_sum(arr: list[int], target: int):
    arr.sort()
    three_sums = []

    for i in range(len(arr) - 2):
        # can't loop to the end to reserve numbers for left and right
        left = i + 1
        right = len(arr) - 1

        while left < right:
            # left must always be less than right for the pointers not to point at the same value to prevent duplicates
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                three_sums.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

            elif current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1
    return three_sums


if __name__ == "__main__":
    # Classic example -> the three triplets that sum to 0
    assert three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [
        [-8, 2, 6],
        [-8, 3, 5],
        [-6, 1, 5],
    ]

    # Single exact match
    assert three_number_sum([1, 2, 3], 6) == [[1, 2, 3]]

    # Target is the sum of two, not three, values -> no triplet
    assert three_number_sum([1, 2, 3], 6 - 1) == []

    # Empty / too-short input -> no triplets
    assert three_number_sum([], 0) == []
    assert three_number_sum([1, 2], 3) == []

    print("All tests passed")
