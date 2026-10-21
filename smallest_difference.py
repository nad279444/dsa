"""Find the pair (one value from each array) with the smallest absolute difference.

Approach: sort both arrays, then walk them with two pointers starting at their
smallest elements. The difference at the two pointers is a candidate; advance
the pointer holding the smaller value, because only that side can shrink the
difference (the other side would only grow it). An exact match ends the search
immediately since 0 is the smallest possible difference.
Time: O(n log n + m log m) for the sorts; Space: O(1) extra.
"""


def smallest_difference(arr1: list[int], arr2: list[int]):
    arr1.sort()
    arr2.sort()

    idx1 = 0
    idx2 = 0
    current = float("inf")
    smallest = float("inf")

    smallestPairs = []

    while idx1 < len(arr1) and idx2 < len(arr2):
        first_num, second_num = arr1[idx1], arr2[idx2]
        if first_num < second_num:
            current = second_num - first_num
            idx1 = idx1 + 1

        elif second_num < first_num:
            current = first_num - second_num
            idx2 = idx2 + 1
        else:
            return [first_num, second_num]
        if current < smallest:
            # condition always overides the other because smallest is initially infinity
            smallest = current
            smallestPairs = [first_num, second_num]
    return smallestPairs


if __name__ == "__main__":
    # Classic example: |28 - 26| = 2 is the closest pair
    assert smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]) == [28, 26]

    # Closest approach at the tails of each array
    assert smallest_difference([1, 2, 3], [10, 20, 30]) == [3, 10]

    # Identical values -> exact match returns immediately
    assert smallest_difference([5, 5], [5, 5]) == [5, 5]

    print("All tests passed")
