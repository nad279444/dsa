"""Find the first duplicate value in an array.

Approach: track seen values in a set as we scan from left to right.
Return the first value that is encountered again; if no duplicates exist,
return -1.
Time: O(n) on average; Space: O(n) for the set.
"""


def first_duplicate(arr: list[int]):
    seen = set()
    for value in arr:
        if value in seen:
            return value
        seen.add(value)
    return -1


# Alias for compatibility
duplicate_values = first_duplicate


if __name__ == "__main__":
    # First duplicate encountered is 3
    assert first_duplicate([2, 1, 3, 5, 3, 2, 4]) == 3

    # First duplicate encountered is 1
    assert first_duplicate([1, 2, 3, 4, 5, 1]) == 1

    # Consecutive duplicates
    assert first_duplicate([1, 1, 2, 3]) == 1

    # No duplicates -> -1
    assert first_duplicate([1, 2, 3, 4]) == -1

    # Empty array -> -1
    assert first_duplicate([]) == -1

    # Single element -> -1
    assert first_duplicate([5]) == -1

    print("All tests passed")
